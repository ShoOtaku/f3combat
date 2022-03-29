import string
import json

import pysaintcoinach
import re
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'  # 自行替换
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'  # 自行替换
line_break = re.compile(r'[\r\n\u3000]+')
ui_foreground = re.compile(r"</?UIForeground(\(\d+\))?>")
ui_glow = re.compile(r"</?UIGlow(\(\d+\))?>")
if_job = re.compile(r"<If\(Equal\(PlayerParameter\(68\),(?P<job_id>\d+)\)\)>(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")
if_lv = re.compile(r"<If\(GreaterThanOrEqualTo\(PlayerParameter\(72\),(?P<min_lv>\d+)\)\)>"
                   r"(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")

rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt4')  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')  # 国际服
data_realm = realm_eng
translate_realm = realm_eng
action_sheet = data_realm.game_data.get_sheet('Action')
eng_action_sheet = realm_eng.game_data.get_sheet('Action')
status_sheet = data_realm.game_data.get_sheet('Status')
status_sheet_eng = realm_eng.game_data.get_sheet('Status')
status_sheet_chs = realm_chs.game_data.get_sheet('Status')
action_sheet_chs = realm_chs.game_data.get_sheet('Action')
action_transient_sheet = data_realm.game_data.get_sheet('ActionTransient')
action_transient_translate_sheet = translate_realm.game_data.get_sheet('ActionTransient')
chs_action_transient_sheet = realm_chs.game_data.get_sheet('ActionTransient')
eng_cj_sheet = realm_eng.game_data.get_sheet('ClassJob')
fight_abbrev = [class_job['Abbreviation']
                for class_job in data_realm.game_data.get_sheet('ClassJob')
                if class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31}]
fight_category = []
common_category = []
for class_job_category in data_realm.game_data.get_sheet('ClassJobCategory'):
    if sum(class_job_category[class_job] for class_job in fight_abbrev) == 0: continue
    (fight_category if sum(class_job_category[class_job] for class_job in fight_abbrev) < 3 else common_category).append(class_job_category.key)

_status_by_name = {}
for status in realm_chs.game_data.get_sheet('Status'):
    _status_by_name.setdefault(status['Name'], set()).add(status.key)
for status in realm_eng.game_data.get_sheet('Status'):
    _status_by_name.setdefault(status['Name'].lower(), set()).add(status.key)

if_else_node = re.compile(r'\(.*\?.*:.*\)')

add_effect_regex1 = re.compile(r"附加(.+?)(状态 |\n)")
add_effect_regex2 = re.compile(r"\n(.+?)效果：")
status_black_list = {"止步", "眩晕", "持续伤害", "体力持续恢复", "加重", "麻痹", "石化", "受伤加重", "睡眠"}


def to_under_line(s):
    return re.sub(r'([A-Z]|[_ -][a-z])', lambda m: '_' + m.group(0)[-1].lower(), s).replace(' ', '')


def to_hump(s):
    return re.sub(r'[_ -]([a-zA-Z])',
                  lambda m: m.group(1).upper(), s.capitalize()).replace(' ', '').replace("'", '').replace("-", '_').replace(':', '')


def status_data(status_id):
    if not status_id: return None
    chs_status = status_sheet_chs[status_id]
    eng_status = status_sheet_eng[status_id]
    return {
        'id': status_id,
        'name': {
            'chs': chs_status['Name'],
            'eng': eng_status['Name'],
        },
        'description': {
            'chs': desc_process(chs_status['Description']),
            'eng': desc_process(eng_status['Description']),
        }
    }


def desc_process(desc: str):
    rtn = ui_glow.sub('', ui_foreground.sub('', line_break.sub('\n', desc)))
    while if_job.search(rtn) or if_lv.search(rtn):
        rtn = if_job.sub(r"(job==\1?\2:\3)", rtn)
        rtn = if_lv.sub(r"(level>=\1?\2:\3)", rtn)
    return rtn


job_actions = {}


def chs_effect_parse(chs_desc):
    matching_node = []
    desc = ui_glow.sub('', ui_foreground.sub('', line_break.sub('\n', chs_desc)))

    while if_job.search(desc) or if_lv.search(desc):
        if_job_match = if_job.search(desc)
        if if_job_match:
            matching_node.append({
                'type': 'if_job',
                'job_id': int(if_job_match.group('job_id')),
                'true_statement': if_job_match.group('true_statement'),
                'false_statement': if_job_match.group('false_statement'),
            })
            desc = if_job.sub(f'&{len(matching_node) - 1}&', desc, 1)
        if_lv_match = if_lv.search(desc)
        if if_lv_match:
            matching_node.append({
                'type': 'if_lv',
                'min_lv': int(if_lv_match.group('min_lv')),
                'true_statement': if_lv_match.group('true_statement'),
                'false_statement': if_lv_match.group('false_statement'),
            })
            desc = if_lv.sub(f'&{len(matching_node) - 1}&', desc, 1)

    def _parse_node(match):
        node = matching_node[int(match.group(1))]
        t = parse_node(node['true_statement']).split('\n', 1)[0]
        f = parse_node(node['false_statement']).split('\n', 1)[0]
        if t or f:
            match node['type']:
                case 'if_job':
                    return f"(job=={node['job_id']}?{t}:{f})"
                case 'if_lv':
                    return f"(lv>={node['min_lv']}?{t}:{f})"
            return match.group(0)
        return ''

    def parse_node(node):
        return re.sub(r'&(\d+)&', _parse_node, node)

    effects = {}
    cont = False
    related_status = set()
    for line in desc.split('\n'):
        if '持续' in line:
            cont = True
        if "威力：" in line:
            p, a = line.split('威力：', 1)
            a = parse_node(a.strip())
            if '连击中' in p:
                key = 'combo_dmg'
            else:
                key = 'dmg'
            if '背面' in p:
                key = 'back_' + key
            elif '侧面' in p:
                key = 'side_' + key
            if cont:
                key = key + '_ot'
                cont = False
            if '中' in p:
                req = re.sub(r'[“”"\']', '', p.split('中', 1)[0])
                if req and req != '连击':
                    related_status.add(req)
                    if key in effects:
                        orig = effects[key].pop()
                    else:
                        orig = '-'
                    a = f"({req}?{a}:{orig})"
            effects.setdefault(key, []).append(a)
        line = parse_node(line)
        if "恢复力：" in line:
            if cont:
                cont = False
                k = 'heal_ot'
            else:
                k = 'heal'
            p, a = line.split('恢复力：', 1)
            a = parse_node(a.strip())
            if '中' in p:
                req = re.sub(r'[“”"\']', '', p.split('中', 1)[0])
                if req:
                    if k in effects:
                        orig = effects[k].pop()
                    else:
                        orig = '-'
                    a = f"({req}?{a}:{orig})"
            effects.setdefault(k, []).append(a)

        if "伤害减轻" in line:
            effects.setdefault('taken_dmg_reduce', []).append(parse_node(line.split('伤害减轻', 1)[1].strip()))
        if "伤害降低" in line:
            p, a = line.split('伤害降低', 1)
            if '受' in p:
                effects.setdefault('taken_dmg_reduce', []).append(parse_node(a.strip()))
            else:
                effects.setdefault('dmg_reduce', []).append(parse_node(a.strip()))
        if "伤害提高" in line:
            p, a = line.split('伤害提高', 1)
            if '受' in p:
                effects.setdefault('taken_dmg_increase', []).append(parse_node(a.strip()))
            else:
                effects.setdefault('dmg_increase', []).append(parse_node(a.strip()))
        if "对目标之外的敌人威力降低" in line:
            effects.setdefault('aoe_reduce', []).append(parse_node(line.split('对目标之外的敌人威力降低', 1)[1].strip()))
        shield_match = re.search(r'抵消相当于(.*)的伤害', line)
        if shield_match:
            effects.setdefault('shield', []).append(parse_node(shield_match.group(1)))
        for status_match in re.finditer(r"(.+?)(效果|状态)", line):
            k = re.sub(r'.*(追加|附加|条件：)', '', status_match.group(1)).strip()
            if k: related_status |= {s for s in re.split(r'[和、]', re.sub(r'[“”"\']', '', k)) if s}
        for status_match in re.finditer(r"追加效果：(.+)", line):
            k = status_match.group(1).strip()
            if k: related_status |= {s for s in re.split(r'[和、]', re.sub(r'[“”"\']', '', k)) if s}

    return related_status - status_black_list, {k: set(v) if len(set(v)) > 1 else v[0] for k, v in effects.items()}


def get_status_ids(string):
    for i in range(len(string)):
        s = string[i:]
        if s in status_black_list: return set()
        t = _status_by_name.get(s, set())
        if t: return t
    return set()


def add_actions(abbrev, action):
    names = {'eng': eng_action_sheet[action.key]['Name'], 'chs': action_sheet_chs[action.key]['Name']}

    if action['IsPvP']: names = {l: f"{name}(pvp)" for l, name in names.items()}
    orig_names = names.copy()
    names = {l: f"{name}({abbrev})" for l, name in names.items()}

    if action['AttackType']:
        match action['AttackType'].key:
            case 0:
                attack_type = None
            case 1 | 2 | 3 | 4:
                attack_type = 'Physical'
            case 5:
                attack_type = 'Magical'
            case _:
                attack_type = action['AttackType']['Name']
    else:
        attack_type = 'Physical'

    if action['Status{GainSelf}']:
        status_gain_self = status_data(action['Status{GainSelf}'].key)
    else:
        status_gain_self = None
    desc = {
        'eng': desc_process(action_transient_translate_sheet[action.key]['Description']),
        'chs': desc_process(chs_action_transient_sheet[action.key]['Description']),
    }
    other_status = _status_by_name.get(eng_action_sheet[action.key]['Name'].lower(), set()) | \
                   _status_by_name.get(action_sheet_chs[action.key]['Name'].lower(), set())

    related_status, effects = chs_effect_parse(chs_action_transient_sheet[action.key]['Description'])

    if related_status:
        for s in related_status:
            other_status |= get_status_ids(s.lower())

    if status_gain_self: other_status -= {status_gain_self['id']}

    action_data = {
        'id': action.key,
        'names': names,
        'orig_names': orig_names,
        'combo_action': action['Action{Combo}'].key or None,
        'desc': desc,
        'class': abbrev,
        'attack_type': attack_type,
        'status_gain_self': status_gain_self,
        'other_status': [
            status_data(status_id) for status_id in other_status
        ],
        'effects': effects,
        # 'data_row':action
    }
    job_actions[abbrev][action.key] = action_data


for class_job in data_realm.game_data.get_sheet('ClassJob'):
    if class_job.key and class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31} and not class_job['StartingTown'].key:
        abbrev = class_job['Abbreviation']
        if abbrev == 'ROG': continue
        job_actions[abbrev] = {}
        print(f"Processing {abbrev}...")
        for action in action_sheet:
            if (
                    action['Name'] and action['ClassJobCategory'] and
                    action['ClassJobCategory'][abbrev] and
                    action['ClassJobCategory'].key in fight_category and
                    action_transient_sheet[action.key]['Description']
            ):
                add_actions(abbrev, action)
print(f"Processing CMN...")
job_actions['CMN'] = {}
for action in action_sheet:
    if (
            action['Name'] and action['ClassJobCategory'] and
            action['ClassJobCategory'].key in common_category and
            action_transient_sheet[action.key]['Description']
    ):
        add_actions('CMN', action)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


json.dump(job_actions, open(f"job_actions.json", 'w', encoding='utf-8'), ensure_ascii=False, indent=4, cls=SetEncoder)
