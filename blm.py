from functools import cache
from math import radians
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle


class BlackMageStrategy(Strategy):
    name = 'ot/blm'
    job = 'BlackMage'