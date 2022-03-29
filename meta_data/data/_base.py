physical = 1
magical = 2


class Action:
    id: int = 0
    names = []
    _orig_names = []
    combo_action: int = 0
    attack_type = 0
    status_gain_self = 0
    damage = 0
    combo_damage = 0
    back_damage = 0
    side_damage = 0
    back_combo_damage = 0
    side_combo_damage = 0
    heal = 0


class Status:
    id: int = 0
    names: list = []
