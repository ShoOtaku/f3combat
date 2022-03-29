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

status_sheet_eng = realm_eng.game_data.get_sheet('Status')
status_sheet_chs = realm_chs.game_data.get_sheet('Status')

def desc_process(desc: str):
    rtn = ui_glow.sub('', ui_foreground.sub('', line_break.sub('\n', desc)))
    while if_job.search(rtn) or if_lv.search(rtn):
        rtn = if_job.sub(r"(job==\1?\2:\3)", rtn)
        rtn = if_lv.sub(r"(level>=\1?\2:\3)", rtn)
    return rtn

def get_status(status_id: int):
    status_chs = status_sheet_chs[status_id]
    status_eng = status_sheet_eng[status_id]
    print(f'class Status{status_id}(Status):')
    for line in desc_process(status_chs['Description']).split('\n'):
        print(f'    # {line}')
    for line in desc_process(status_eng['Description']).split('\n'):
        print(f'    # {line}')
    print(f'    id = {status_id}')
    names = set()
    names.add(status_chs['Name'])
    names.add(status_eng['Name'])
    print(f'    names = {list(names)}')

get_status(148)
