from XivCombat.utils import a, s
from XivCombat.strategies import *
from XivCombat.define import *

provoke_and_shirk = {a('挑衅'), a('退避'), a('插言'), a('下踢')}


def mo_provoke_and_shirk(func):
    def process_ability_use(cls, data: 'LogicData', action_id: int, target_id: int) -> None | Tuple[int, int] | UseAbility:
        if action_id in provoke_and_shirk:
            mo_entity = api.get_mo_target()
            if mo_entity and api.action_type_check(action_id, mo_entity):
                return UseAbility(action_id, mo_entity.id)
        return func(cls, data, action_id, target_id)

    return process_ability_use


def get_pos(data: 'LogicData', target) -> int:
    if not target.is_positional or s('真北') in data.effects:
        return REQUIRE_BACK | REQUIRE_FRONT | REQUIRE_SIDE
    match target.target_position(data.me):
        case "BACK":
            return REQUIRE_BACK
        case "SIDE":
            return REQUIRE_SIDE
        case "FRONT":
            return REQUIRE_FRONT
        case _:
            return 0
