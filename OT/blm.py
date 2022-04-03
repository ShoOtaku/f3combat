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
data.gauge.polygot_active  悖论标记
'''
blm_dot = {s('闪雷(0)'), s('震雷(0)'), s('暴雷'), s('霹雷(0)')}
def target_has_dots(data, actor, dots):
    effects = actor.effects.get_dict(source=data.me.id)
    for dot in dots:
        if dot in effects:
            return effects[dot].timer
    return 0
class BlackMageStrategy(Strategy):
    name = 'ot/blm'
    fight_only = False  #非战斗也执行策略，目的是为了保持冰火状态（76级以上在战斗外使用灵极魂）
    job = 'BlackMage'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        #没有目标或者目标大于25米且在冰状态且时间小于7s时，使用灵极魂
        if data.gauge.umbral_stacks < 0 and data.gauge.umbral_ms < 7*1000 and data.me.level >= 76 and (not data.target or data.target_distance >= 25) :
            return UseAbility(a('灵极魂(BLM)'))
        #若没有有效敌人（不在战斗中），则不执行下面的语句    
        if not data.valid_enemies:  
            return
        if data.target and data.target_distance <= 25:
            single_target = data.target
            single_distance = data.target_distance
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('冰冻(BLM)')))
            if not single_target or data.actor_distance_effective(single_target) > 25: 
                return
            single_distance = data.actor_distance_effective(single_target)
        if data.me.level >= 12 :
            aoe_target, aoe_cnt = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_cnt = single_target, 0
        need_fire = data.gauge.umbral_ms < 6*1000
        need_use_foul = data.gauge.next_polyglot_ms < 10*1000
        #移动中用瞬发        
        if data.is_moving and s('三连咏唱') not in data.effects:
            if data.gauge.foul_count > 0 and data.me.level >= 80:
                if aoe_cnt > 2:
                    return UseAbility(a('秽浊(BLM)'), aoe_target.id)
                return UseAbility(a('异言(BLM)'))
            if s('火苗') in data.effects and data.gauge.umbral_stacks > 0:
                return UseAbility(a('爆炎(BLM)'))
            if s('雷云(0)') in data.effects:
                if aoe_cnt > 2:
                    if data.me.level >= 64:
                        return UseAbility(a('霹雷(BLM)'), aoe_target.id)
                    return UseAbility(a('震雷(BLM)'), aoe_target.id)
                if data.me.level >= 45:
                    return UseAbility(a('暴雷(BLM)'))
                return UseAbility(a('闪雷(BLM)'))
            if data.gauge.polygot_active > 0 and data.gauge.umbral_stacks < 0:
                return UseAbility(a('悖论(BLM)'))


        #火状态
        if data.gauge.umbral_stacks > 0 and (not data.is_moving or s('三连咏唱') in data.effects):      
            if data.me.current_mp >= 1600:
                if aoe_cnt > 2 and data.me.level > 18 and data.me.current_mp >= 3000:
                    if data.gauge.foul_count > 0:
                        return UseAbility(a('秽浊(BLM)'), aoe_target.id)
                    if data.ttk(aoe_target) > 15 and target_has_dots(data, aoe_target, blm_dot) < 5 and data.last_action != (a('霹雷(BLM)') or a('震雷(BLM)')):
                        if data.me.level >= 64:
                            return UseAbility(a('霹雷(BLM)'), aoe_target.id)
                        if data.me.level >= 26:
                            return UseAbility(a('震雷(BLM)'), aoe_target.id)
                    if s('核爆效果提高') in data.effects:
                        return UseAbility(a('核爆(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                    if data.me.level >= 82:
                        return UseAbility(a('高烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                if data.ttk(single_target) > 9 and target_has_dots(data, single_target, blm_dot) < 5 and data.last_action != (a('暴雷(BLM)') or a('闪雷(BLM)')):
                    if data.me.level >= 45:
                        return UseAbility(a('暴雷(BLM)'))
                    if data.me.level >= 6:
                        return UseAbility(a('闪雷(BLM)'))
                if data.gauge.foul_count > 0 and need_use_foul:
                    if data.me.level >= 80:
                        return UseAbility(a('异言(BLM)'))
                    return UseAbility(a('秽浊(BLM)'))
                if data.me.level >= 60:
                    if need_fire or data.gauge.umbral_stacks < 3:
                        if data.gauge.polygot_active > 0:
                            return UseAbility(a('悖论(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                        if s('火苗') in data.effects:
                            return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)                        
                        return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                    elif data.gauge.umbral_stacks == 3:
                        return UseAbility(a('炽炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                if s('火苗') in data.effects:
                    return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
                return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
            elif data.me.current_mp >= 800 and data.me.level >= 72:
                return UseAbility(a('绝望(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
            else:
                if aoe_cnt > 2:
                    if data.me.level >= 82:
                        return UseAbility(a('高冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)
                    return UseAbility(a('冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)
                elif data.me.level >= 35:
                    return UseAbility(a('冰封(BLM)'), wait_until = lambda: data.gauge.umbral_stacks < 0)
        #冰状态                    
        if data.gauge.umbral_stacks < 0 and (not data.is_moving or s('三连咏唱') in data.effects):
            if data.me.current_mp < 8000:
                if data.gauge.umbral_hearts == 0:
                    if aoe_cnt > 2:
                        if data.gauge.foul_count > 0:
                            return UseAbility(a('秽浊(BLM)'), aoe_target.id)                        
                        if data.ttk(aoe_target) > 15 and target_has_dots(data, aoe_target, blm_dot) < 5 and data.last_action != (a('霹雷(BLM)') or a('震雷(BLM)')):
                            if data.me.level >= 64:
                                return UseAbility(a('霹雷(BLM)'), aoe_target.id)
                            if data.me.level >= 26:
                                return UseAbility(a('震雷(BLM)'), aoe_target.id)
                        if data.me.level >= 40:
                            return UseAbility(a('玄冰(BLM)'), aoe_target.id)
                        if data.me.level >= 82:
                            return UseAbility(a('高冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)                    
                        return UseAbility(a('冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)                            
                    if data.gauge.foul_count > 0 and need_use_foul:
                        if data.me.level >= 80:
                            return UseAbility(a('异言(BLM)'))
                        return UseAbility(a('秽浊(BLM)'))
                    if data.ttk(single_target) > 9 and target_has_dots(data, single_target, blm_dot) < 5 and data.last_action != (a('暴雷(BLM)') or a('闪雷(BLM)')):
                        if data.me.level >= 45:
                            return UseAbility(a('暴雷(BLM)'))
                        if data.me.level >= 6:
                            return UseAbility(a('闪雷(BLM)'))
                    if data.me.level >= 58:
                        return UseAbility(a('冰澈(BLM)'))
                    if data.gauge.polygot_active > 0:
                        return UseAbility(a('悖论(BLM)'))
                    if data.last_action == a('悖论(BLM)'):
                        return UseAbility(a('爆炎(BLM)'))                                          
                    return UseAbility(a('冰结(BLM)'))
                else:
                    if aoe_cnt > 2 and data.me.level >= 12:
                        return UseAbility(a('冰冻(BLM)'), aoe_target.id)
                    if data.gauge.polygot_active > 0:
                        return UseAbility(a('悖论(BLM)'))
                    if data.last_action == a('悖论(BLM)'):
                        return UseAbility(a('爆炎(BLM)'))                          
                    return UseAbility(a('冰结(BLM)'))
            else:
                if aoe_cnt > 2 and data.me.level >= 18:
                    if data.me.level >= 82:
                        return UseAbility(a('高烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)                    
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)
                elif data.me.level >= 35:
                    return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks > 0)
        #初始状态（无冰无火）
        if data.gauge.umbral_stacks == 0 and (not data.is_moving or s('三连咏唱') in data.effects):
            if aoe_cnt > 2:
                if data.me.level >= 18:
                    if data.me.level >= 82:
                        return UseAbility(a('高烈炎(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks > 0)                    
                    return UseAbility(a('烈炎(BLM)'), aoe_target.id)
                elif data.me.level >= 12:
                    if data.me.level >= 82:
                        return UseAbility(a('高冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)                    
                    return UseAbility(a('冰冻(BLM)'), aoe_target.id, wait_until = lambda: data.gauge.umbral_stacks < 0)
            if data.me.level >= 35 and data.last_action != a('爆炎(BLM)'):
                return UseAbility(a('爆炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks != 0)
            else:
                return UseAbility(a('火炎(BLM)'), wait_until = lambda: data.gauge.umbral_stacks != 0)


    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if data.gauge.umbral_ms < 0.6*1000 and data.gauge.umbral_stacks != 0 :
            if data.me.level >= 4:
                return UseAbility(a('星灵移位(BLM)'))
        #若没有有效敌人（不在战斗中），则不执行下面的语句
        if not data.valid_enemies:
            return        
        if data.is_moving and data.me.level >= 66 and data[a('三连咏唱(BLM)')] < 60 and s('三连咏唱') not in data.effects:
            return UseAbility(a('三连咏唱(BLM)'), wait_until=lambda: s('三连咏唱') in data.refresh_cache('effects'))
        if data.is_moving and not data[a('即刻咏唱')] and s('三连咏唱') not in data.effects:
            return UseAbility(a('即刻咏唱'))
        if not data[a('详述(BLM)')]:
            return UseAbility(a('详述(BLM)'))
        if data[a('激情咏唱(BLM)')] < 60 and s('激情咏唱') not in data.effects:
            return UseAbility(a('激情咏唱(BLM)'), wait_until=lambda: s('激情咏唱') in data.refresh_cache('effects')) 
        if not data.is_moving and data[a('黑魔纹(BLM)')]:
            return UseAbility(a('黑魔纹(BLM)'), data.me.id)
        if data.gauge.umbral_stacks == 0 and data.me.current_mp < 5000:
            return UseAbility(a('醒梦'), data.me.id)
