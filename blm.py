from functools import cache
from math import radians
import re
from tokenize import single_quoted
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle

aoe = FarCircle(25, 5)
'''
data.me.current_mp
data.gauge.umbral_stacks  3 火3   -3 冰3
data.gauge.umbral_hearts  冰针
data.gauge.umbral_ms
data.gauge.foul_count
data.gauge.polygot_active
'''


class BlackMageStrategy(Strategy):
    name = 'ot/blm'
    job = 'BlackMage'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target and data.target_distance <= 25:
            single_target = data.target
            single_distance = data.target_distance
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('冰冻(BLM)')))
            if not single_target or data.actor_distance_effective(single_target) > 25: 
                return
            single_distance = data.actor_distance_effective(single_target)
        t_effect = data.target.effects.get_dict(source=data.me.id)
        need_singledot1 = (data.me.level >= 6 and data.me.level < 45) and (s('闪雷(0)') not in t_effect or t_effect[s('闪雷(0)')].timer <= 3)
        need_aoedot1 = (data.me.level >= 26 and data.me.level < 64) and (s('震雷(0)') not in t_effect or t_effect[s('震雷(0)')].timer <= 3)
        need_singledot2 = data.me.level >= 45 and (s('暴雷') not in t_effect or t_effect[s('暴雷')].timer <= 3)
        need_aoedot2 = data.me.level >= 64 and (s('霹雷(0)') not in t_effect or t_effect[s('霹雷(0)')].timer <= 3)
        need_fire = data.gauge.umbral_ms < 5.5*1000
        if data.me.level >= 12 :
            aoe_target, aoe_cnt = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_cnt = single_target, 0
        
#火状态
        if data.gauge.umbral_stacks > 0 and (not data.is_moving or s('三连咏唱') in data.effects):      
            if data.me.current_mp > 1600:
                if aoe_cnt > 2 and data.me.level > 18 and data.me.current_mp >= 3000:
                    if need_aoedot2:
                        return UseAbility(a('霹雷(BLM)'), aoe_target.id, wait_until=lambda: s('霹雷(0)') in data.refresh_cache('t_effect'))
                    if need_aoedot1:
                        return UseAbility(a('震雷(BLM)'), aoe_target.id, wait_until=lambda: s('震雷(0)') in data.refresh_cache('t_effect'))
                    if s('核爆效果提高') in data.effects:
                        return UseAbility(a('核爆(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                if need_singledot2:
                    return UseAbility(a('暴雷(BLM)'), wait_until=lambda: s('暴雷') in data.refresh_cache('t_effect'))
                if need_singledot1:
                    return UseAbility(a('闪雷(BLM)'), wait_until=lambda: s('闪雷(0)') in data.refresh_cache('t_effect'))
                if data.me.level >= 60:
                    if need_fire or data.gauge.umbral_stacks < 3:
                        return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                    elif data.gauge.umbral_stacks == 3:
                        return UseAbility(a('炽炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                if s('火苗') in data.effects:
                    return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
            elif data.me.current_mp > 800 and not need_fire and data.me.level >= 72:
                return UseAbility(a('绝望(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
            else:
                if aoe_cnt > 2:
                    return UseAbility(a('冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)
                elif data.me.level >= 35:
                    return UseAbility(a('冰封(BLM)'), wait_until = lambda: data.gauge.umbral_stacks < 0)
#冰状态                    
        if data.gauge.umbral_stacks < 0 and (not data.is_moving or s('三连咏唱') in data.effects):
            if data.me.current_mp < 8000:
                if data.gauge.umbral_hearts == 0:
                    if aoe_cnt > 2:
                        if need_aoedot2:
                            return UseAbility(a('霹雷(BLM)'), aoe_target.id, wait_until=lambda: s('霹雷(0)') in data.refresh_cache('t_effect'))
                        if need_aoedot1:
                            return UseAbility(a('震雷(BLM)'), aoe_target.id, wait_until=lambda: s('震雷(0)') in data.refresh_cache('t_effect'))
                        if data.me.level >= 40:
                            return UseAbility(a('玄冰(BLM)'), aoe_target.id)
                    if need_singledot2:
                        return UseAbility(a('暴雷(BLM)'), wait_until=lambda: s('暴雷') in data.refresh_cache('t_effect'))
                    if need_singledot1:
                        return UseAbility(a('闪雷(BLM)'), wait_until=lambda: s('闪雷(0)') in data.refresh_cache('t_effect'))  
                    if data.me.level >= 58:
                        return UseAbility(a('冰澈(BLM)'))                                          
                    return UseAbility(a('冰结(BLM)'))
                else:
                    if aoe_cnt > 2 and data.me.level >= 12:
                        return UseAbility(a('冰结(BLM)'), aoe_target.id)
                    return UseAbility(a('冰结(BLM)'))
            else:
                if aoe_cnt > 2 and data.me.level >= 18:
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                elif data.me.level >= 35:
                    return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
        
        if data.gauge.umbral_stacks == 0 and (not data.is_moving or s('三连咏唱') in data.effects):
            if aoe_cnt > 2:
                if data.me.level >= 18:
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id)
                elif data.me.level >= 12:
                    return UseAbility(a('冰冻(BLM)'), aoe_target.id)
            if data.me.level >= 35:
                return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks != 0)
            else:
                return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks != 0)


    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if data.gauge.umbral_ms < 0.6*1000 and data.gauge.umbral_stacks != 0 :
            if data.me.level >= 4:
                return UseAbility(a('星灵移位(BLM)'))
        if data.is_moving and data.me.level >= 66 and data[a('三连咏唱(BLM)')] < 60:
            return UseAbility(a('三连咏唱(BLM)'), wait_until=lambda: s('三连咏唱') in data.refresh_cache('effects'))

