
from functools import cache
from math import radians
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import Rectangle, NearCircle, circle, FarCircle

'''
    chakra_stacks: int
    BeastChakra1: int
    BeastChakra2: int
    BeastChakra3: int
    Nadi: int
    CoeurlChakra = 1, RaptorChakra = 2, OpoopoChakra = 3
    Nadi = 2 阴
    Nadi = 4 阳
    Nadi = 6 阴阳
'''

#基础军体拳循环
'''            
        if s('盗龙形') in data.effects and data.me.level >= 4:
            if aoe_cnt > 2 and data.me.level >= 45 :
                return UseAbility(a('四面脚(MNK)'), data.me.id)
            if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                return UseAbility(a('双掌打(MNK)'),single_target.id)
            return UseAbility(a('正拳(MNK)'),single_target.id)               
        if s('猛豹形') in data.effects and data.me.level >= 6:
            if aoe_cnt > 2 and data.me.level >= 30:
                return UseAbility(a('地烈劲(MNK)'),data.me.id)
            t_effect = data.target.effects.get_dict(source=data.me.id)
            if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                return UseAbility(a('破碎拳(MNK)'), single_target.id)
            return UseAbility(a('崩拳(MNK)'), single_target.id)
        if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
            return UseAbility(a('破坏神冲(MNK)'), data.me.id)
        if aoe_cnt > 2 and data.me.level >= 82:
            return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
        if data.me.level >= 50 and s('连击效果提高') not in data.effects:
            return UseAbility(a('双龙脚(MNK)'), single_target.id)
        return UseAbility(a('连击(MNK)'), single_target.id)        
'''
aoe = NearCircle(5.)
chakra = Rectangle(10,2)


class MonkStrategy(Strategy):
    name = 'ot/mnk'
    job = 'Monk'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        else:
            return None
        #AOE敌人数量
        if data.me.level >= 26:
            aoe_target, aoe_cnt = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_cnt = data.me, 0
#3印与阴阳大招
        #必杀技检查
        if data.gauge.Nadi == 6 and data.gauge.BeastChakra1 != 0 and data.gauge.BeastChakra2 != 0 and data.gauge.BeastChakra3 != 0 :
            if data.me.level >= 90:
                return UseAbility(a('梦幻斗舞(MNK)'))
            else:
                return UseAbility(a('斗魂旋风脚(MNK)'))
        #阴
        if data.gauge.Nadi != 6 and data.gauge.BeastChakra1 == data.gauge.BeastChakra2 and data.gauge.BeastChakra2 == data.gauge.BeastChakra3 and data.gauge.BeastChakra1 != 0:
            return UseAbility(a('苍气炮(MNK)'))
        #阳
        if data.gauge.Nadi != 6 and data.gauge.BeastChakra1 != data.gauge.BeastChakra2 and data.gauge.BeastChakra2 != data.gauge.BeastChakra3 and data.gauge.BeastChakra1 != data.gauge.BeastChakra3 and data.gauge.BeastChakra1 != 0 and data.gauge.BeastChakra2 != 0 and data.gauge.BeastChakra3 != 0:
            if data.me.level >= 86:
                return UseAbility(a('凤凰舞(MNK)'))
            else:
                return UseAbility(a('爆裂脚(MNK)'))
        #不阴不阳        
        if data.gauge.Nadi !=6 and data.gauge.BeastChakra1 != 0 and data.gauge.BeastChakra2 != 0 and data.gauge.BeastChakra3 != 0:
            return UseAbility(a('翻天脚(MNK)'))

        if data.gauge.Nadi == 0 :
            if s('震脚') in data.effects:
                #第一个印
                if data.gauge.BeastChakra1 == 0 and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)
                #第二个印               
                if data.gauge.BeastChakra2 == 0  and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                #第三个印
                if data.gauge.BeastChakra3 == 0:
                    if aoe_cnt > 2 and data.me.level >= 26 and data.me.level < 82:
                        return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                    if aoe_cnt > 2 and data.me.level >= 82:
                        return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                    if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                        return UseAbility(a('双龙脚(MNK)'), single_target.id)
                    return UseAbility(a('连击(MNK)'), single_target.id)
            else:
                if s('盗龙形') in data.effects and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)               
                if s('猛豹形') in data.effects and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                    return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                if aoe_cnt > 2 and data.me.level >= 82:
                    return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                    return UseAbility(a('双龙脚(MNK)'), single_target.id)
                return UseAbility(a('连击(MNK)'), single_target.id)
        #只有阴，则打阳   
        if data.gauge.Nadi == 2 :
            if s('震脚') in data.effects:
                #第一个印
                if data.gauge.BeastChakra1 == 0 and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)
                #第二个印               
                if data.gauge.BeastChakra2 == 0  and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                #第三个印
                if data.gauge.BeastChakra3 == 0:
                    if aoe_cnt > 2 and data.me.level >= 26 and data.me.level < 82:
                        return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                    if aoe_cnt > 2 and data.me.level >= 82:
                        return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                    if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                        return UseAbility(a('双龙脚(MNK)'), single_target.id)
                    return UseAbility(a('连击(MNK)'), single_target.id)
            else:
                if s('盗龙形') in data.effects and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)               
                if s('猛豹形') in data.effects and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                    return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                if aoe_cnt > 2 and data.me.level >= 82:
                    return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                    return UseAbility(a('双龙脚(MNK)'), single_target.id)
                return UseAbility(a('连击(MNK)'), single_target.id)
        #只有阳，则打阴
        if data.gauge.Nadi == 4 :
            if s('震脚') in data.effects:
                if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                    return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                if aoe_cnt > 2 and data.me.level >= 82:
                    return UseAbility(a('破坏神脚(MNK)'), data.me.id)                  
                if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                    return UseAbility(a('双龙脚(MNK)'), single_target.id)
                return UseAbility(a('连击(MNK)'), single_target.id)
            else:
                if s('盗龙形') in data.effects and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)               
                if s('猛豹形') in data.effects and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                    return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                if aoe_cnt > 2 and data.me.level >= 82:
                    return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                    return UseAbility(a('双龙脚(MNK)'), single_target.id)
                return UseAbility(a('连击(MNK)'), single_target.id)                
        #有阴阳
        if data.gauge.Nadi == 6 :
            if s('震脚') in data.effects:
                #第一个印
                if data.gauge.BeastChakra1 == 0 and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)
                #第二个印               
                if data.gauge.BeastChakra2 == 0  and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                #第三个印
                if data.gauge.BeastChakra3 == 0:
                    if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                        return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                    if aoe_cnt > 2 and data.me.level >= 82:
                        return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                    if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                        return UseAbility(a('双龙脚(MNK)'), single_target.id)
                    return UseAbility(a('连击(MNK)'), single_target.id)
            else:
                if s('盗龙形') in data.effects and data.me.level >= 4:
                    if aoe_cnt > 2 and data.me.level >= 45 :
                        return UseAbility(a('四面脚(MNK)'), data.me.id)
                    if data.me.level >= 18 and (s('功力') not in data.effects or data.effect_time(s('功力')) <= 4):
                        return UseAbility(a('双掌打(MNK)'),single_target.id)
                    return UseAbility(a('正拳(MNK)'),single_target.id)               
                if s('猛豹形') in data.effects and data.me.level >= 6:
                    if aoe_cnt > 2 and data.me.level >= 30:
                        return UseAbility(a('地烈劲(MNK)'),data.me.id)
                    t_effect = data.target.effects.get_dict(source=data.me.id)
                    if data.me.level >= 30 and s('破碎拳(1)') not in t_effect or t_effect[s('破碎拳(1)')].timer <=6:
                        return UseAbility(a('破碎拳(MNK)'), single_target.id)
                    return UseAbility(a('崩拳(MNK)'), single_target.id)
                if aoe_cnt > 2 and data.me.level >= 26 and data.me.level <82:
                    return UseAbility(a('破坏神冲(MNK)'), data.me.id)
                if aoe_cnt > 2 and data.me.level >= 82:
                    return UseAbility(a('破坏神脚(MNK)'), data.me.id)            
                if data.me.level >= 50 and s('连击效果提高') not in data.effects:
                    return UseAbility(a('双龙脚(MNK)'), single_target.id)
                return UseAbility(a('连击(MNK)'), single_target.id)







    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 3:
            single_target = data.target
        elif data.gauge.chakra_stacks < 5 :
            return UseAbility(a('斗气(MNK)'))
        else:
            return None
        if data.gauge.chakra_stacks == 5:
            chakra_target, chakra_cnt = cnt_enemy(data, chakra)
            if chakra_cnt > 1 and data.me.level >= 40 and data.me.level < 74:
                return UseAbility(a('空鸣拳(MNK)'), chakra_target.id)
            elif chakra_cnt > 1 and data.me.level >= 74:
                return UseAbility(a('万象斗气圈(MNK)'), chakra_target.id)
            elif chakra_cnt <= 1 and data.me.level >= 54:
                return UseAbility(a('阴阳斗气斩(MNK)'), single_target.id)
            return UseAbility(a('铁山靠(MNK)'), single_target.id)

        if not data[a('红莲极意(MNK)')]:
            return UseAbility(a('红莲极意(MNK)'), data.me.id)
        if not data[a('疾风极意(MNK)')]:
            return UseAbility(a('疾风极意(MNK)'), data.me.id)
        if not data[a('义结金兰(MNK)')]:
            return UseAbility(a('义结金兰(MNK)'), data.me.id)
        if data.me.level >= 50 and s('震脚') not in data.effects :
            if data.gauge.BeastChakra1 == 0 and s('红莲极意(0)') in data.effects or data[a('红莲极意(MNK)')] < 2 or data[a('震脚(MNK)')] < 2 :
                return UseAbility(a('震脚(MNK)'), data.me.id, wait_until=lambda: s('震脚') in data.refresh_cache('effects'))


