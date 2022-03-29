import json
import re


def _process_exp(exp: str):
    is_num = re.match(r'^\d+$', exp)
    if is_num:
        return int(exp)
    is_range = re.match(r'^\d+～\d+$', exp)
    if is_range:
        return [int(exp.split('～')[0]), int(exp.split('～')[1])]

    return json.dumps(exp, ensure_ascii=False)


def process_exp(exp):
    if isinstance(exp, list):
        res = [_process_exp(e) for e in exp]
        return f'{res[0]} # TODO: {res}'
    return _process_exp(exp)


def main():
    raw_data = json.load(open('job_actions.json', encoding='utf-8'))

    all_status = {}
    all_status_with_names_chs = {}
    all_status_with_names_eng = {}
    all_actions = {}
    all_actions_with_names_chs = {}
    all_actions_with_names_eng = {}
    for job, data in raw_data.items():
        for _action_id, action in data.items():
            for _status in action['other_status']:
                s_id = _status['id']
                if s_id not in all_status:
                    all_status[s_id] = _status.copy()
                    all_status_with_names_chs.setdefault(_status['name']['chs'], []).append(all_status[s_id])
                    all_status_with_names_eng.setdefault(_status['name']['eng'], []).append(all_status[s_id])
                all_status[s_id].setdefault('related_action', []).append(action)
                all_status[s_id].setdefault('ref', set()).add(job)
            action_id = action['id']
            all_actions[action_id] = action.copy()
            all_actions_with_names_chs.setdefault(action['names']['chs'], []).append(all_actions[action_id])
            all_actions_with_names_eng.setdefault(action['names']['eng'], []).append(all_actions[action_id])

    for name, status in all_status_with_names_chs.items():
        if len(status) > 1:
            for i, _status in enumerate(status):
                _status['name']['chs'] = f"{name}({i})"

    for name, status in all_status_with_names_eng.items():
        if len(status) > 1:
            for i, _status in enumerate(status):
                _status['name']['eng'] = f"{name}({i})"

    for name, actions in all_actions_with_names_chs.items():
        if len(actions) > 1:
            for i, action in enumerate(actions):
                action['names']['chs'] = f"{name}({i})"

    for name, actions in all_actions_with_names_eng.items():
        if len(actions) > 1:
            for i, action in enumerate(actions):
                action['names']['eng'] = f"{name}({i})"

    job_status = {}
    for s_id, status in all_status.items():
        job_status.setdefault('CMN' if len(status['ref']) > 1 or 'CMN' in status['ref'] else next(iter(status['ref'])), []).append(status)

    for job, data in raw_data.items():

        with open(f'data/{job.lower()}.py', 'w+', encoding='utf-8') as f:
            f.write('from ._base import *\n\n\n')
            for _status in job_status[job]:
                f.write(f"class Status{_status['id']}(Status):\n")
                for line in _status['description']['chs'].split('\n'):
                    f.write(f"    # {line}\n")
                for line in _status['description']['eng'].split('\n'):
                    f.write(f"    # {line}\n")
                f.write(f"    # related: ")
                for action in _status['related_action']:
                    a_id = action['id']
                    f.write(f"[{all_actions[a_id]['names']['chs']}](Action{a_id}), ")
                f.write(f'\n    id = {_status["id"]}\n    names = {list(_status["name"].values())}\n')
                f.write('\n\n')

            for _action_id in data.keys():
                action = all_actions[int(_action_id)]
                f.write(f"class Action{action['id']}(Action):\n")
                for line in action['desc']['chs'].split('\n'):
                    f.write(f"    # {line}\n")
                for line in action['desc']['eng'].split('\n'):
                    f.write(f"    # {line}\n")
                if action['other_status']:
                    f.write(f"    # related: ")
                    for _status in action['other_status']:
                        f.write(f"[{all_status[_status['id']]['name']['chs']}](Status{_status['id']}), ")
                    f.write('\n')
                f.write(f"    id = {action['id']}\n    names = {list(set(action['names'].values()))}\n    _orig_names = {list(set(action['orig_names'].values()))}\n")
                if action['combo_action']:
                    f.write(f"    combo_action = {action['combo_action']}\n")
                effects = action['effects']

                if 'dmg' in effects:
                    f.write(f"    damage = {process_exp(effects['dmg'])}\n")
                    del effects['dmg']
                if 'combo_dmg' in effects:
                    f.write(f"    combo_damage = {process_exp(effects['combo_dmg'])}\n")
                    del effects['combo_dmg']
                if 'back_dmg' in effects:
                    f.write(f"    back_damage = {process_exp(effects['back_dmg'])}\n")
                    del effects['back_dmg']
                if 'back_combo_dmg' in effects:
                    f.write(f"    back_combo_damage = {process_exp(effects['back_combo_dmg'])}\n")
                    del effects['back_combo_dmg']
                if 'side_dmg' in effects:
                    f.write(f"    side_damage = {process_exp(effects['side_dmg'])}\n")
                    del effects['side_dmg']
                if 'side_combo_dmg' in effects:
                    f.write(f"    side_combo_damage = {process_exp(effects['side_combo_dmg'])}\n")
                    del effects['side_combo_dmg']

                if 'heal' in effects:
                    f.write(f"    heal = {process_exp(effects['heal'])}\n")
                    del effects['heal']

                if effects:
                    f.write(f"    # remain metas: {effects}\n")

                f.write('\n\n')


if __name__ == '__main__':
    main()
