import time
from functools import cache
from math import radians
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle

aoe = NearCircle(5.)
fire_aoe = FarCircle(20, 5)

TEN = 3 # 天
CHI = 2 # 地
JIN = 1 # 人

def get_mudra(effects: dict):
    if s('结印') not in effects:
        return ""
    p = effects[s('结印')].param
    s = ''
    for i in range(4):
        m = ( p >> (i * 2)) & 0b11
        if m:
            s += str(m)
        else:
            break
    return s

m2s = {
    TEN: 2259,
    CHI: 2261,
    JIN: 2263,
}

def c(*mudras: int):
    return [m2s[m] for m in mudras]

combos = {
    'normal': c(TEN),
    'fire': c(CHI, TEN),
    'thunder': c(TEN, CHI),
    'ice': c(TEN, JIN),
    'wind': c(JIN, CHI, TEN),
    'ground': c(JIN, TEN, CHI),
    'water': c(TEN, CHI, JIN),
    'water_multi': c(CHI, TEN, JIN),
}

class NinjaStrategy(Strategy):
    name = 'ot/nin'
    job = 'Ninja'

    def __init__(self):
        self.effects_temp = dict()
        self.combo = []
    def have_effect(self, data: 'LogicData', effect_id: int, allow_time=2):
        return effect_id in data.effects or self.effects_temp.setdefault(effect_id, 0) > time.time() - allow_time

    def set_effect(self, effect_id: int):
        self.effects_temp[effect_id] = time.time()

    def can_ground(self, data: 'LogicData'):
        return not self.have_effect(data, s('土遁之术'), 5)

    def get_ground(self):
        self.set_effect(s('土遁之术'))
        return combos['ground'].copy()

    def common(self, data: 'LogicData') -> UseAbility| UseItem| UseCommon| None:
        if data.gcd < 0.3 and not self.combo:
            combo_use = data.config.custom_settings.setdefault('ninja_combo', '')
            if combo_use in combos:
                if combo_use == "ground": self.set_effect(s('土遁之术'))
                data.config.custom_settings['ninja_combo'] = ''
                self.combo = combos[combo_use].copy()
        if self.combo:
            return UseAbility(self.combo.pop(0))
        elif s('结印') in data.effects:
            return UseAbility(a('忍术(NIN)'))



    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        must_huton = data.gauge.huton_ms < 10*1000 and data.gauge.huton_ms and data.max_ttk > data.gauge.huton_ms/1000
        if data.target_distance <= 3:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('飞刀(NIN)')))
            if not single_target:
                return
            if data.actor_distance_effective(single_target) > 5:
                if not data.gcd and data.me.level >= 15:
                    return UseAbility(a('飞刀(NIN)'), single_target.id)
                else:
                    None
        if data.me.level >= 35:
            fire_aoe_target, fire_aoe_cnt = cnt_enemy(data, fire_aoe)
        else:
            fire_aoe_target, fire_aoe_cnt = data.target, 0
        if data.me.level >= 38:
            aoe_target, aoe_cnt = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_cnt = data.me, 0
        if s('生杀予夺') in data.effects:
            if data.me.level >= 76:
                if aoe_cnt > 2:
                    self.combo = combos['fire'].copy()
                else:
                    self.combo = combos['ice'].copy()
            elif aoe_cnt > 2:
                if data.max_ttk > 15 and self.can_groun(data):
                    self.combo = self.get_ground()
                else:
                    self.combo = combos['fire'].copy()
            else:
                self.combo = combos['thunder'].copy()
        elif s('天地人') in data.effects:
            if aoe_cnt < 3:
                self.combo = combos['water'].copy()
            else:
                if self.can_ground(data):
                    self.combo = self.get_ground()
                else:
                    self.combo = combos['water_multi'].copy()
        elif data[a('天之印(NIN)(0)')] <= 20 and data.skill_unlocked(a('天之印(NIN)(0)')):
            if data.me.level >= 45 and data.skill_unlocked(a('人之印(NIN)(0)')):
                if not data.gauge.huton_ms:
                    self.combo = combos['wind'].copy()
                else:
                    if (data[a('天之印(NIN)(0)')] < 20 or not data[a('命水(NIN)')]) and s('水遁之术') not in data.effects and (data[a('天之印(NIN)')] < 5 or data[a('攻其不备(NIN)')] < 5 or data.target_distance > 6):
                        self.combo = combos['water'].copy()
                    elif aoe_cnt > 2 and data.max_ttk > 15 and self.can_ground(data):
                        self.combo = self.get_ground()
            if not self.combo and (data[a('天之印(NIN)(0)')] < 5 or data.target_distance > 6):
                if data.me.level >= 35:
                    if fire_aoe_cnt > 2:
                        self.combo = combos['fire'].copy()
                    else:
                        self.combo = combos['thunder'].copy()  
                else:
                    self.combo = combos['normal'].copy()
        if self.combo:
            return UseAbility(self.combo.pop(0))     
        if data.combo_id == a('血雨飞花(NIN)') and data.skill_unlocked(a('八卦无刃杀(NIN)')) and aoe_cnt:
            return UseAbility(a('八卦无刃杀(NIN)'), data.me.id)
        if aoe_cnt > 2:
            return UseAbility(a('血雨飞花(NIN)'), data.me.id)
        if data.actor_distance_effective(single_target) > 3:
             return
        if data.me.level >= 54 and data.combo_id == a('绝风(NIN)') and data.skill_unlocked(a('强甲破点突(NIN)')):
            if must_huton:
                UseAbility(a('强甲破点突(NIN)'), single_target.id)
        if data.me.level >= 26 and data.combo_id == a('绝风(NIN)'):
            return UseAbility(a('旋风刃(NIN)'), single_target.id)
        if data.me.level >= 4 and data.combo_id == a('双刃旋(NIN)'):
            return UseAbility(a('绝风(NIN)'), single_target.id)
        return UseAbility(a('双刃旋(NIN)'), single_target.id)

#    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
