from functools import cache
from math import radians
from time import perf_counter
from XivCombat.utils import a, s, cnt_enemy, res_lv, find_area_belongs_to_me
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import NearCircle, circle, Sector
from .utils import mo_provoke_and_shirk

aoe2 = NearCircle(5)
aoe1 = Sector(8, radians(120))

class WarriorStrategy(Strategy):
    name = 'ot/war'
    job = 'Warrior'


    @mo_provoke_and_shirk
    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        if action_id == a('原初的勇猛'):
            mo_entity = api.get_mo_target()
            if mo_entity and api.action_type_check(action_id, mo_entity):
                return UseAbility(action_id, mo_entity.id)


    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        need_red = data.me.level >= 50 and (s('战场风暴') not in data.effects or data.effects[s('战场风暴')].timer < 10)
        use_green = data.combo_id == a('凶残裂') and (data.me.level < 50 or s('战场风暴') in data.effects and data.effects[s('战场风暴')].timer > 30)
        sta = a('原初的解放') if data.me.level >= 70 else a('狂暴')
        aoe_target, aoe_cnt = cnt_enemy(data, aoe2)  # 获取aoe攻击目标和数量        
        if data.target_distance <= 3:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('飞斧')))
            if not single_target: return
            if data.actor_distance_effective(single_target) > 5 and data.skill_unlocked(a('飞斧')):
                return UseAbility(a('飞斧'), single_target.id) if not data.gcd and data.me.level >= 15 else None
        if s('蛮荒崩裂预备') in data.effects:
            return UseAbility(a('蛮荒崩裂'))
        if data.skill_unlocked(a('原初之魂')) and s('原初的解放(0)') in data.effects or not need_red and data.gauge.beast >= 50 and (
                {s('狂暴'), s('原初的解放(0)'), s('原初的勇猛(0)'), s('原初的混沌(1)'), s('原初的直觉'), s('原初的血气')}.intersection(data.me.effects.get_set()) or
                data.gauge.beast > (80 if use_green else 90) or data[a('战嚎')] < (60 if data[sta] < 10 else 10)
        ):
            if data.me.level < 45:
                return UseAbility(a('原初之魂'))
            return UseAbility(a('钢铁旋风') if aoe_cnt > 2 and data.skill_unlocked(a('钢铁旋风')) else a('原初之魂'))

        if data.combo_id == a('超压斧') and data.me.level >= 40:
            return UseAbility(a('秘银暴风')) if aoe_cnt else None
        if data.combo_id == a('凶残裂') and data.me.level >= 26:
            return UseAbility(a('暴风斩') if use_green else a('暴风碎'))
        if data.me.level >= 10:
            aoe_target, aoe_cnt = cnt_enemy(data, aoe1)
            if aoe_cnt >= 2: return UseAbility(a('超压斧'), aoe_target.id)
        if data.combo_id == a('重劈') and data.me.level >= 4:
            return UseAbility(a('凶残裂'))
        return UseAbility(a('重劈'))
    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        aoe_target, aoe_cnt = cnt_enemy(data, aoe2)
        sta = a('原初的解放') if data.me.level >= 70 else a('狂暴')
        if not data[sta] and data[a('战嚎')] > 60 and s('原初的混沌(1)') not in data.effects:
            return UseAbility(sta)
        if not data[a('动乱')] and data.gauge.beast >= 20 and data[sta] > 10:
            if aoe_cnt > 2 and data.me.level >= 86:
                return UseAbility(a('群山隆起'))
            else:
                return UseAbility(a('动乱'))
        if (data[a('战嚎')] < 60 and
                not {s('狂暴'), s('原初的解放(0)'), s('原初的混沌(1)')}.intersection(data.me.effects.get_set()) and
                data.gauge.beast <= 50 and (data[a('战嚎')] < 5 or data[sta] < 10)):
            return UseAbility(a('战嚎'), wait_until=lambda: s('原初的混沌(1)') in data.refresh_cache('effects'))
    