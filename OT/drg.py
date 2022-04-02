from functools import cache
from math import radians
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle

aoe = Rectangle(10, 2)
class DragoonStrategy(Strategy):
    name = 'ot/drg'
    job = 'Dragoon'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        else:
            if data.target_distance <= 10 and data.me.level >= 62 and data.combo_id == a('死天枪(DRG)'):
                return UseAbility(a('音速刺(DRG)'))
            elif data.target_distance <= 10 and data.me.level >= 72 and data.combo_id == a('音速刺(DRG)'):
                return UseAbility(a('山境酷刑(DRG)'))
            elif data.target_distance <= 10 and data.me.level >= 82 and s('龙眼') in data.effects:
                return UseAbility(a('龙眼苍穹(DRG)'))
            elif data.target_distance <= 10 and data.me.level >= 40:
                return UseAbility(a('死天枪(DRG)'))
            elif data.target_distance >=5 and data.target_distance <= 20 and data.me.level >= 15:
                return UseAbility(a('贯穿尖(DRG)'))
            else:
                return None

        t_effect = data.target.effects.get_dict(source=data.me.id)
        need_dot1 = (data.me.level >= 50 and data.me.level < 86) and (s('樱花怒放(1)') not in t_effect or t_effect[s('樱花怒放(1)')].timer <= 6) 
        need_dot2 = data.me.level >= 86 and (s('樱花缭乱') not in t_effect or t_effect[s('樱花缭乱')].timer <= 6)
        can_drg4 = s('龙牙龙爪预备') in data.effects
        can_drg5 = s('龙尾大回旋预备') in data.effects

        if data.me.level >= 40:
            aoe_target, aoe_cnt = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_cnt = single_target, 0

        if data.me.level >= 82 and s('龙眼') in data.effects and aoe_cnt > 2:
            return UseAbility(a('龙眼苍穹(DRG)'), aoe_target.id)
        if data.me.level >= 72 and data.combo_id == a('音速刺(DRG)'):
            return UseAbility(a('山境酷刑(DRG)'), aoe_target.id)
        if data.me.level >= 62 and data.combo_id == a('死天枪(DRG)'):
            return UseAbility(a('音速刺(DRG)'), aoe_target.id)
        if aoe_cnt > 2 and data.me.level >= 40:
            return UseAbility(a('死天枪(DRG)'), aoe_target.id)
        if data.me.level >= 56 and can_drg4:
            return UseAbility(a('龙牙龙爪(DRG)'), single_target.id)
        if data.me.level >= 58 and can_drg5:
            return UseAbility(a('龙尾大回旋(DRG)'), single_target.id)
        if data.me.level >= 50 and data.combo_id == a('开膛枪'):
            if data.me.level >= 86:
                return UseAbility(a('樱花缭乱(DRG)'), single_target.id)
            else:
                return UseAbility(a('樱花怒放(DRG)'), single_target.id)
        if need_dot1 and data.combo_id == a('精准刺(DRG)'):
            return UseAbility(a('开膛枪(DRG)'), single_target.id)
        if need_dot2 and data.combo_id == a('精准刺(DRG)'):
            return UseAbility(a('开膛枪(DRG)'), single_target.id)
        if data.me.level >= 4 and data.combo_id == a('精准刺'):
            return UseAbility(a('贯通刺(DRG)'), single_target.id)
        if data.me.level >= 26 and data.combo_id == a('贯通刺'):
            if data.me.level >= 86:
                return UseAbility(a('苍穹刺(DRG)'), single_target.id)
            else:
                return UseAbility(a('直刺(DRG)'), single_target.id)
        return UseAbility(a('精准刺(DRG)'), single_target.id)
    
    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        red_dragoon = data.gauge.stance == 2    
        if not data[a('猛枪(DRG)')]:
            return UseAbility(a('猛枪(DRG)'))
        if not data[a('战斗连祷(DRG)')]:
            return UseAbility(a('战斗连祷(DRG)'))
        if not data[a('破碎冲(DRG)')] or data[a('破碎冲(DRG)')] < 60:
            return UseAbility(a('破碎冲(DRG)'))
        if not data[a('龙炎冲(DRG)')]:
            return UseAbility(a('龙炎冲(DRG)'))
        if data.me.level >= 30:
            if data.me.level >= 74:
                if not data[a('高跳(DRG)')] :
                    return UseAbility(a('高跳(DRG)'))
            else:
                if not data[a('跳跃(DRG)')]:
                    return UseAbility(a('跳跃(DRG)'))
        if s('幻象冲预备') in data.effects:
            return UseAbility(a('幻象冲(DRG)'))
        if not data[a('武神枪(DRG)')]:
            return UseAbility(a('武神枪(DRG)')) 
        if red_dragoon :
            if not data[a('死者之岸(DRG)')]:
                return UseAbility(a('死者之岸(DRG)'))
            if data.me.level >= 80 and not data[a('坠星冲(DRG)')]:
                return UseAbility(a('坠星冲(DRG)'))