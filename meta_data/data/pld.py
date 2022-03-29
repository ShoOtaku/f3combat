from ._base import *


class Status74(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [预警(PLD)](Action17), [干预(PLD)](Action7382),
    id = 74
    names = ['预警', 'Sentinel']


class Status1370(Status):
    # 发动攻击所造成的伤害及自身发动的体力恢复效果降低
    # Damage dealt and potency of all HP restoration actions are reduced.
    # related: [战女神之怒(PLD)](Action21),
    id = 1370
    names = ['战女神之怒', 'Rage of Halone']


class Status248(Status):
    # 体力逐渐减少
    # Wounds are bleeding, causing damage over time.
    # related: [厄运流转(PLD)](Action23),
    id = 248
    names = ['厄运流转', 'Circle of Scorn']


class Status80(Status):
    # 正在保护特定的队员
    # Protecting a party member.
    # related: [保护(PLD)](Action27),
    id = 80
    names = ['保护(0)', 'Cover(0)']


class Status1300(Status):
    # 正在保护特定的队员，效果中受到的伤害增加
    # Protecting a party member. Damage taken is increased.
    # related: [保护(PLD)](Action27),
    id = 1300
    names = ['保护(1)', 'Cover(1)']


class Status2412(Status):
    # 正在保护特定的对象
    # Protecting an ally.
    # related: [保护(PLD)](Action27),
    id = 2412
    names = ['保护(2)', 'Cover(2)']


class Status393(Status):
    # 自身仇恨提高
    # Enmity is increased.
    # related: [钢铁信念(PLD)](Action28),
    id = 393
    names = ['钢铁信念(0)', 'Iron Will(0)']


class Status2843(Status):
    # 自身仇恨提高
    # Enmity is increased.
    # related: [钢铁信念(PLD)](Action28),
    id = 2843
    names = ['钢铁信念(1)', 'Iron Will(1)']


class Status82(Status):
    # 除特定攻击之外其他所有攻击均无效化
    # Impervious to most attacks.
    # related: [神圣领域(PLD)](Action30), [神圣领域(pvp)(PLD)](Action8755),
    id = 82
    names = ['神圣领域(0)', 'Hallowed Ground(0)']


class Status1302(Status):
    # 除特定攻击之外其他所有攻击均无效化
    # Impervious to most attacks.
    # related: [神圣领域(PLD)](Action30), [神圣领域(pvp)(PLD)](Action8755),
    id = 1302
    names = ['神圣领域(1)', 'Hallowed Ground(1)']


class Status725(Status):
    # 体力逐渐减少
    # Wounds are bleeding, causing damage over time.
    # related: [沥血剑(PLD)](Action3538),
    id = 725
    names = ['沥血剑', 'Goring Blade']


class Status726(Status):
    # 受到治疗魔法时为周围队员附加能够抵消一定伤害的防护罩
    # Upon HP recovery via healing magic, a damage-reducing barrier is created.
    # related: [圣光幕帘(PLD)](Action3540),
    id = 726
    names = ['圣光幕帘(0)', 'Divine Veil(0)']


class Status727(Status):
    # 抵消一定伤害
    # A holy barrier is nullifying damage.
    # related: [圣光幕帘(PLD)](Action3540),
    id = 727
    names = ['圣光幕帘(1)', 'Divine Veil(1)']


class Status2168(Status):
    # 身附能够抵消一定伤害的防护罩，当防护罩因吸收足量伤害而消失时，会为周围队员附加能够抵消一定伤害的防护罩
    # A holy barrier is nullifying damage. When barrier is completely absorbed, creates a barrier around all nearby party members.
    # related: [圣光幕帘(PLD)](Action3540),
    id = 2168
    names = ['圣光幕帘(2)', 'Divine Veil(2)']


class Status2169(Status):
    # 抵消一定伤害
    # A holy barrier is nullifying damage.
    # related: [圣光幕帘(PLD)](Action3540),
    id = 2169
    names = ['圣光幕帘(3)', 'Divine Veil(3)']


class Status728(Status):
    # 下次受到攻击时必定发动格挡
    # Next attack will be blocked.
    # related: [盾阵(PLD)](Action3542),
    id = 728
    names = ['盾阵(0)', 'Sheltron(0)']


class Status1856(Status):
    # 受到攻击时必定发动格挡
    # Blocking incoming attacks.
    # related: [盾阵(PLD)](Action3542),
    id = 1856
    names = ['盾阵(1)', 'Sheltron(1)']


class Status2020(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [干预(pvp)(PLD)](Action19085),
    id = 2020
    names = ['干预(0)', 'Intervention(0)']


class Status2675(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [圣盾阵(PLD)](Action25746),
    id = 2675
    names = ['骑士的坚守', "Knight's Resolve"]


class Status1174(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [干预(pvp)(PLD)](Action19085),
    id = 1174
    names = ['干预(1)', 'Intervention(1)']


class Status1368(Status):
    # 咏唱魔法时没有任何咏唱时间,圣灵和圣环威力提高
    # Potency of Holy Spirit and Holy Circle is increased and spells require no time to cast.
    # related: [安魂祈祷(PLD)](Action7383), [安魂祈祷(pvp)(PLD)](Action8754), [圣环(PLD)](Action16458), [悔罪(PLD)](Action16459),
    id = 1368
    names = ['安魂祈祷', 'Requiescat']


# class Status1369(Status):
#     # 咏唱魔法时没有任何咏唱时间，并且不会消耗魔力
#     # Spells require no time to cast and consume no MP.
#     # related: [安魂祈祷(PLD)](Action7383), [安魂祈祷(pvp)(PLD)](Action8754), [圣环(PLD)](Action16458), [悔罪(PLD)](Action16459),
#     id = 1369
#     names = ['安魂祈祷(1)', 'Requiescat(1)']


class Status1175(Status):
    # 产生减轻伤害的防护区域
    # An area of land has been granted protection, reducing damage taken for all who enter.
    # related: [武装戍卫(PLD)](Action7385),
    id = 1175
    names = ['武装戍卫', 'Passage of Arms']


class Status2076(Status):
    # 发动攻击所造成的伤害及自身发动的体力恢复效果降低
    # Damage dealt and potency of all HP restoration actions are reduced.
    # related: [悔罪(PLD)](Action16459), [悔罪(pvp)(PLD)](Action17692),
    id = 2076
    names = ['悔罪', 'Confiteor']


class Status1902(Status):
    # 可以发动赎罪剑
    # Able to execute Atonement.
    # related: [赎罪剑(pvp)(PLD)](Action17691), [调停(pvp)(PLD)](Action17694),
    id = 1902
    names = ['忠义之剑', 'Sword Oath']


# class Status381(Status):
#     # 对自动攻击附加追加伤害
#     # Auto-attacks are enhanced.
#     # related: [赎罪剑(pvp)(PLD)](Action17691), [调停(pvp)(PLD)](Action17694),
#     id = 381
#     names = ['忠义之剑(1)', 'Sword Oath(1)']
#
#
# class Status78(Status):
#     # 对自动攻击附加追加伤害
#     # Auto-attacks are enhanced.
#     # related: [赎罪剑(pvp)(PLD)](Action17691), [调停(pvp)(PLD)](Action17694),
#     id = 78
#     names = ['忠义之剑(2)', 'Sword Oath(2)']
#
#
# class Status1991(Status):
#     # 可以发动赎罪剑与荣耀斩
#     # Able to execute Atonement and Glory Slash.
#     # related: [赎罪剑(pvp)(PLD)](Action17691), [调停(pvp)(PLD)](Action17694),
#     id = 1991
#     names = ['忠义之剑(3)', 'Sword Oath(3)']


class Status2179(Status):
    # 抵消一定伤害
    # A highly effective defensive maneuver is nullifying damage.
    # related: [掩护盾(pvp)(PLD)](Action19086),
    id = 2179
    names = ['掩护盾', 'Testudo']


class Status2674(Status):
    # 受到攻击时必定发动格挡
    # Blocking incoming attacks.
    # related: [圣盾阵(PLD)](Action25746),
    id = 2674
    names = ['圣盾阵', 'Holy Sheltron']


class Status2676(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [圣盾阵(PLD)](Action25746),
    id = 2676
    names = ['骑士的加护', "Knight's Benediction"]


class Status2721(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [英勇之剑(PLD)](Action25750),
    id = 2721
    names = ['英勇之剑', 'Blade of Valor']


class Action9(Action):
    # 对目标发动物理攻击
    # 威力：(job==19?(level>=84?200:150):150)
    # Delivers an attack with a potency of (job==19?(level>=84?200:150):150).
    id = 9
    names = ['Fast Blade(PLD)', '先锋剑(PLD)']
    _orig_names = ['先锋剑', 'Fast Blade']
    damage = "(job==19?(lv>=84?200:150):150)"


class Action15(Action):
    # 对目标发动物理攻击
    # 威力：(job==19?(level>=84?170:100):100)
    # 连击条件：先锋剑
    # 连击中威力：(job==19?(level>=84?300:230):230)(job==19?(level>=58?
    # 连击成功：恢复自身魔力:):)
    # Delivers an attack with a potency of (job==19?(level>=84?170:100):100).
    # Combo Action: Fast Blade
    # Combo Potency: (job==19?(level>=84?300:230):230)(job==19?(level>=58?
    # Combo Bonus: Restores MP:):)
    id = 15
    names = ['暴乱剑(PLD)', 'Riot Blade(PLD)']
    _orig_names = ['暴乱剑', 'Riot Blade']
    combo_action = 9
    damage = "(job==19?(lv>=84?170:100):100)"
    combo_damage = "(job==19?(lv>=84?300:230):230)"


class Action16(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：眩晕
    # 持续时间：6秒
    # Delivers an attack with a potency of 100.
    # Additional Effect: Stun
    # Duration: 6s
    id = 16
    names = ['Shield Bash(PLD)', '盾牌猛击(PLD)']
    _orig_names = ['Shield Bash', '盾牌猛击']
    damage = 100


class Action17(Action):
    # 一定时间内，将自身所受的伤害减轻30%
    # 持续时间：15秒
    # Reduces damage taken by 30%.
    # Duration: 15s
    # related: [预警](Status74),
    id = 17
    names = ['预警(PLD)', 'Sentinel(PLD)']
    _orig_names = ['Sentinel', '预警']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action20(Action):
    # 一定时间内，自身发动物理攻击造成的伤害提高25%
    # 持续时间：25秒
    # Increases physical damage dealt by 25%.
    # Duration: 25s
    # related: [战逃反应](Status76),
    id = 20
    names = ['战逃反应(PLD)', 'Fight or Flight(PLD)']
    _orig_names = ['战逃反应', 'Fight or Flight']
    # remain metas: {'dmg_increase': '25%'}


class Action21(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：暴乱剑
    # 连击中威力：330
    # Delivers an attack with a potency of 100.
    # Combo Action: Riot Blade
    # Combo Potency: 330
    # related: [战女神之怒](Status1370),
    id = 21
    names = ['战女神之怒(PLD)', 'Rage of Halone(PLD)']
    _orig_names = ['战女神之怒', 'Rage of Halone']
    combo_action = 15
    damage = 100
    combo_damage = 330


class Action23(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 追加效果：持续伤害
    # 威力：30
    # 持续时间：15秒
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Additional Effect: Damage over time
    # Potency: 30
    # Duration: 15s
    # related: [厄运流转](Status248),
    id = 23
    names = ['Circle of Scorn(PLD)', '厄运流转(PLD)']
    _orig_names = ['Circle of Scorn', '厄运流转']
    damage = 100
    # remain metas: {'dmg_ot': '30'}


class Action24(Action):
    # 对目标发动远距离物理攻击
    # 威力：100
    # 追加效果：提升仇恨
    # Delivers a ranged attack with a potency of 100.
    # Additional Effect: Increased enmity
    id = 24
    names = ['Shield Lob(PLD)', '投盾(PLD)']
    _orig_names = ['Shield Lob', '投盾']
    damage = 100


class Action27(Action):
    # 替目标队员承受来自敌人的攻击
    # 但对部分攻击无效
    # 持续时间：12秒
    # 与目标的距离不能超过10米
    # 效果发动条件：忠义50点
    # Take all damage intended for another party member as long as said member remains within 10 yalms.
    # Does not activate with certain attacks.
    # Duration: 12s
    # Oath Gauge Cost: 50
    # related: [保护(0)](Status80), [保护(1)](Status1300), [保护(2)](Status2412),
    id = 27
    names = ['保护(PLD)', 'Cover(PLD)']
    _orig_names = ['保护', 'Cover']


class Action28(Action):
    # 极大幅度增加战斗时获得的仇恨量
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Significantly increases enmity generation.
    # Effect ends upon reuse.
    # related: [钢铁信念(0)](Status393), [钢铁信念(1)](Status2843),
    id = 28
    names = ['钢铁信念(PLD)', 'Iron Will(PLD)']
    _orig_names = ['Iron Will', '钢铁信念']


class Action29(Action):
    # 对目标发动物理攻击
    # 威力：270(job==19?(level>=58?
    # 追加效果：恢复自身魔力:):)
    # Delivers an attack with a potency of 270.(job==19?(level>=58?
    # Additional Effect: Restores MP:):)
    id = 29
    names = ['Spirits Within(PLD)', '深奥之灵(PLD)']
    _orig_names = ['Spirits Within', '深奥之灵']
    damage = 270


class Action30(Action):
    # 一定时间内，除特定攻击之外其他所有对自身发动的攻击均无效
    # 持续时间：10秒
    # Renders you impervious to most attacks.
    # Duration: 10s
    # related: [神圣领域(0)](Status82), [神圣领域(1)](Status1302),
    id = 30
    names = ['神圣领域(PLD)', 'Hallowed Ground(PLD)']
    _orig_names = ['Hallowed Ground', '神圣领域']


class Action3538(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：暴乱剑
    # 连击中威力：250
    # 连击成功：持续伤害
    # 威力：65
    # 持续时间：21秒
    # 无法与英勇之剑的持续伤害叠加
    # Delivers an attack with a potency of 100.
    # Combo Action: Riot Blade
    # Combo Potency: 250
    # Combo Bonus: Damage over time
    # Potency: 65
    # Duration: 21s
    # Damage over time effect cannot be stacked with that of Blade of Valor.
    # related: [沥血剑](Status725),
    id = 3538
    names = ['沥血剑(PLD)', 'Goring Blade(PLD)']
    _orig_names = ['沥血剑', 'Goring Blade']
    combo_action = 15
    damage = 100
    combo_damage = 250
    # remain metas: {'dmg_ot': '65'}


class Action3539(Action):
    # 对目标发动物理攻击
    # 威力：(job==19?(level>=84?130:100):100)
    # 连击条件：暴乱剑
    # 连击中威力：(job==19?(level>=84?420:390):390)(job==19?(level>=76?
    # 连击成功：3档忠义之剑
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of (job==19?(level>=84?130:100):100).
    # Combo Action: Riot Blade
    # Combo Potency: (job==19?(level>=84?420:390):390)(job==19?(level>=76?
    # Combo Bonus: Grants 3 stacks of Sword Oath
    # Duration: 30s:):)
    id = 3539
    names = ['王权剑(PLD)', 'Royal Authority(PLD)']
    _orig_names = ['Royal Authority', '王权剑']
    combo_action = 15
    damage = "(job==19?(lv>=84?130:100):100)"
    combo_damage = "(job==19?(lv>=84?420:390):390)"


class Action3540(Action):
    # 自身受到自身或队员的治疗魔法时，为周围15米内的队员张开防护罩
    # 持续时间：30秒
    # (job==19?(level>=88?追加效果：恢复目标的体力
    # 恢复力：400
    # :):)防护罩效果（受到攻击时）：抵消相当于骑士自身最大体力10%的伤害量
    # 持续时间：30秒
    # 防护罩效果发动后，该技能效果消失
    # Upon HP recovery via healing magic cast by self or a party member, a protective barrier is cast on all party members within a radius of 15 yalms.
    # Duration: 30s
    # Barrier Effect: Prevents damage up to 10% of your maximum HP
    # Duration: 30s
    # (job==19?(level>=88?Additional Effect: Restore target's HP
    # Cure Potency: 400
    # :):)Effect ends upon casting barrier on self and nearby party members.
    # related: [圣光幕帘(0)](Status726), [圣光幕帘(1)](Status727), [圣光幕帘(2)](Status2168), [圣光幕帘(3)](Status2169),
    id = 3540
    names = ['Divine Veil(PLD)', '圣光幕帘(PLD)']
    _orig_names = ['圣光幕帘', 'Divine Veil']
    # remain metas: {'shield': '骑士自身最大体力10%'}


class Action3541(Action):
    # 恢复目标的体力
    # 恢复力：1000
    # 追加效果：对小队队员发动该技能时，自身恢复目标所恢复体力的一半
    # Restores target's HP.
    # Cure Potency: 1,000
    # Additional Effect: Restores to self 50% of HP restored to target if target is a party member
    id = 3541
    names = ['深仁厚泽(PLD)', 'Clemency(PLD)']
    _orig_names = ['Clemency', '深仁厚泽']
    heal = 1000


class Action3542(Action):
    # 一定时间内，受到攻击必定发动格挡
    # 持续时间：(job==19?(level>=74?6:4):4)秒
    # 发动条件：忠义50点
    # Block incoming attacks.
    # Duration: (job==19?(level>=74?6:4):4)s
    # Oath Gauge Cost: 50
    # related: [盾阵(0)](Status728), [盾阵(1)](Status1856),
    id = 3542
    names = ['盾阵(PLD)', 'Sheltron(PLD)']
    _orig_names = ['盾阵', 'Sheltron']


class Action7381(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # Delivers an attack with a potency of 100 to all nearby enemies.
    id = 7381
    names = ['Total Eclipse(PLD)', '全蚀斩(PLD)']
    _orig_names = ['全蚀斩', 'Total Eclipse']
    damage = 100


class Action7382(Action):
    # 指定一名队员，令其受到的伤害减轻10%
    # 持续时间：(job==19?(level>=82?8:6):6)秒
    # 追加效果：自身处于铁壁、预警状态时，效果提高10%
    # (job==19?(level>=82?追加效果：为目标附加骑士的坚守状态
    # 持续时间：4秒
    # 骑士的坚守效果：令目标受到的伤害减轻10%
    # 追加效果：为目标附加骑士的加护状态
    # 持续时间：12秒
    # 骑士的加护效果：令目标体力持续恢复
    # 恢复力：250
    # :):)发动条件：忠义50点
    # Reduces target party member's damage taken by 10%.
    # Duration: (job==19?(level>=82?8:6):6)s
    # Additional Effect: Increases damage reduction by an additional 10% if Rampart or Sentinel are active
    # (job==19?(level>=82?Additional Effect: Grants Knight's Resolve to target
    # Knight's Resolve Effect: Reduces damage taken by 10%
    # Duration: 4s
    # Additional Effect: Grants Knight's Benediction to target
    # Knight's Benediction Effect: Gradually restores HP
    # Cure Potency: 250
    # Duration: 12s
    # :):)Oath Gauge Cost: 50
    # related: [干预(0)](Status2020), [铁壁(0)](Status1191), [铁壁(1)](Status71), [预警](Status74), [骑士的坚守](Status2675), [干预(1)](Status1174), [铁壁(2)](Status1978),
    id = 7382
    names = ['Intervention(PLD)', '干预(PLD)']
    _orig_names = ['干预', 'Intervention']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action7383(Action):
    # 对目标发动无属性魔法攻击
    # 威力：400
    # 追加效果：为自身附加5档安魂祈祷状态
    # 持续时间：30秒
    # 安魂祈祷效果：咏唱魔法不需要咏唱时间，同时圣灵和圣环威力提高
    # Deals unaspected damage with a potency of 400.
    # Additional Effect: Grants 5 stacks of Requiescat
    # Requiescat Effect: Increases the potency of Holy Spirit and Holy Circle and spells will require no cast time
    # Duration: 30s
    # related: [安魂祈祷(0)](Status1368), [安魂祈祷(1)](Status1369),
    id = 7383
    names = ['Requiescat(PLD)', '安魂祈祷(PLD)']
    _orig_names = ['Requiescat', '安魂祈祷']
    damage = 400


class Action7384(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==19?(level>=84?270:250):250)(job==19?(level>=68?
    # 安魂祈祷状态中威力：(job==19?(level>=84?540:500):500):):)(job==19?(level>=84?
    # 追加效果：恢复自身体力
    # 恢复力：400:):)
    # Deals unaspected damage with a potency of (job==19?(level>=84?270:250):250).(job==19?(level>=68?
    # Requiescat Potency: (job==19?(level>=84?540:500):500):):)(job==19?(level>=84?
    # Additional Effect: Restores own HP
    # Cure Potency: 400:):)
    id = 7384
    names = ['圣灵(PLD)', 'Holy Spirit(PLD)']
    _orig_names = ['圣灵', 'Holy Spirit']
    damage = "(job==19?(lv>=84?270:250):250)"


class Action7385(Action):
    # 向自身后方扇形范围展开减轻伤害的防护区域
    # 效果时间内自身的格挡发动率变为100%，范围内的队员受到的伤害减轻15%
    # 持续时间：18秒
    # 效果时间内发动技能或进行移动、转身都会立即解除武装戍卫
    # 发动之后会停止自动攻击
    # Increases block rate to 100% and creates a designated area in a cone behind you in which party members will only suffer 85% of all damage inflicted.
    # Duration: 18s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # related: [武装戍卫](Status1175),
    id = 7385
    names = ['Passage of Arms(PLD)', '武装戍卫(PLD)']
    _orig_names = ['武装戍卫', 'Passage of Arms']
    # remain metas: {'taken_dmg_reduce': '15%'}


class Action8746(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：获得5点忠义
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Increases Oath Gauge by 5
    # ※This action cannot be assigned to a hotbar.
    id = 8746
    names = ['先锋剑(pvp)(PLD)', 'Fast Blade(pvp)(PLD)']
    _orig_names = ['Fast Blade(pvp)', '先锋剑(pvp)']
    damage = 1000


class Action8749(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：先锋剑
    # 连击成功：恢复500点魔力
    # 连击成功：获得5点忠义
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Fast Blade
    # Combo Potency: 1,200
    # Combo Bonus: Restores 500 MP
    # Combo Bonus: Increases Oath Gauge by 5
    # ※This action cannot be assigned to a hotbar.
    id = 8749
    names = ['暴乱剑(pvp)(PLD)', 'Riot Blade(pvp)(PLD)']
    _orig_names = ['Riot Blade(pvp)', '暴乱剑(pvp)']
    combo_action = 8746
    combo_damage = 1200


class Action8750(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：暴乱剑
    # 连击成功：获得5点忠义
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Riot Blade
    # Combo Potency: 1,400
    # Combo Bonus: Increases Oath Gauge by 5
    # ※This action cannot be assigned to a hotbar.
    id = 8750
    names = ['Royal Authority(pvp)(PLD)', '王权剑(pvp)(PLD)']
    _orig_names = ['Royal Authority(pvp)', '王权剑(pvp)']
    combo_action = 8749
    combo_damage = 1400


class Action8752(Action):
    # 对目标发动魔法攻击
    # 威力：1800
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：获得10点忠义
    # Deals unaspected damage with a potency of 1,800.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Increases Oath Gauge by 10
    id = 8752
    names = ['圣灵(pvp)(PLD)', 'Holy Spirit(pvp)(PLD)']
    _orig_names = ['圣灵(pvp)', 'Holy Spirit(pvp)']
    damage = 1800


class Action8754(Action):
    # 对目标发动物理攻击
    # 威力：1000～2000
    # 自身剩余魔力越少威力越大
    # 追加效果：咏唱魔法不消耗魔力且不需要咏唱时间
    # 持续时间：6秒
    # Delivers an attack with a potency of 1,000.
    # Potency increases up to a maximum of 2,000 as MP decreases.
    # Additional Effect: Reduces MP cost of all spells to 0 and allows spells to be cast immediately
    # Duration: 6s
    # related: [安魂祈祷(0)](Status1368), [安魂祈祷(1)](Status1369),
    id = 8754
    names = ['安魂祈祷(pvp)(PLD)', 'Requiescat(pvp)(PLD)']
    _orig_names = ['安魂祈祷(pvp)', 'Requiescat(pvp)']
    damage = [1000, 2000]


class Action8755(Action):
    # 对自身张开除特定攻击之外所有攻击均无效的防护罩
    # 持续时间：5秒
    # Erects a magicked barrier rendering you impervious to most attacks.
    # Duration: 5s
    # related: [神圣领域(0)](Status82), [神圣领域(1)](Status1302),
    id = 8755
    names = ['神圣领域(pvp)(PLD)', 'Hallowed Ground(pvp)(PLD)']
    _orig_names = ['神圣领域(pvp)', 'Hallowed Ground(pvp)']


class Action16457(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：全蚀斩
    # 连击中威力：170(job==19?(level>=66?
    # 连击成功：恢复自身魔力:):)
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: Total Eclipse
    # Combo Potency: 170(job==19?(level>=66?
    # Combo Bonus: Restores MP:):)
    id = 16457
    names = ['Prominence(PLD)', '日珥斩(PLD)']
    _orig_names = ['Prominence', '日珥斩']
    combo_action = 7381
    damage = 100
    combo_damage = 170


class Action16458(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：130
    # 安魂祈祷状态中威力：300(job==19?(level>=84?
    # 追加效果：恢复自身体力
    # 恢复力：400:):)
    # Deals unaspected damage with a potency of 130 to all nearby enemies.
    # Requiescat Potency: 300(job==19?(level>=84?
    # Additional Effect: Restores own HP
    # Cure Potency: 400:):)
    # related: [安魂祈祷(0)](Status1368), [安魂祈祷(1)](Status1369),
    id = 16458
    names = ['Holy Circle(PLD)', '圣环(PLD)']
    _orig_names = ['Holy Circle', '圣环']
    damage = "(安魂祈祷状态?300:130)"


class Action16459(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：900
    # 发动后会取消安魂祈祷状态
    # 发动条件：安魂祈祷状态中(job==19?(level>=90?
    # 发动后该技能变为信念之剑:):)
    # Deals unaspected damage with a potency of 900 to target and all enemies nearby it.
    # Can only be executed while under the effect of Requiescat. Effect fades upon execution.(job==19?(level>=90?
    # ※Action changes to Blade of Faith upon execution.:):)
    # related: [安魂祈祷(0)](Status1368), [安魂祈祷(1)](Status1369), [悔罪](Status2076),
    id = 16459
    names = ['悔罪(PLD)', 'Confiteor(PLD)']
    _orig_names = ['悔罪', 'Confiteor']
    damage = 900


class Action16460(Action):
    # 对目标发动物理攻击
    # 威力：(job==19?(level>=84?420:390):390)
    # 追加效果：恢复自身魔力
    # 发动条件：忠义之剑
    # Delivers an attack with a potency of (job==19?(level>=84?420:390):390).
    # Additional Effect: Restores MP
    # Can only be executed while under the effect of Sword Oath.
    id = 16460
    names = ['赎罪剑(PLD)', 'Atonement(PLD)']
    _orig_names = ['赎罪剑', 'Atonement']
    damage = "(job==19?(lv>=84?420:390):390)"


class Action16461(Action):
    # 冲向目标并发动物理攻击
    # 威力：150
    # 积蓄次数：2
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 150.
    # Maximum Charges: 2
    # Cannot be executed while bound.
    id = 16461
    names = ['Intervene(PLD)', '调停(PLD)']
    _orig_names = ['调停', 'Intervene']
    damage = 150


class Action17691(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 追加效果：恢复自身500点魔力
    # 追加效果：获得10点忠义
    # 发动条件：忠义之剑状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 2,000.
    # Additional Effect: Restores 500 MP
    # Additional Effect: Increases Oath Gauge by 10
    # Can only be executed while under the effect of Sword Oath.
    # ※This action cannot be assigned to a hotbar.
    # related: [忠义之剑(0)](Status1902), [忠义之剑(1)](Status381), [忠义之剑(2)](Status78), [忠义之剑(3)](Status1991),
    id = 17691
    names = ['赎罪剑(pvp)(PLD)', 'Atonement(pvp)(PLD)']
    _orig_names = ['Atonement(pvp)', '赎罪剑(pvp)']
    damage = 2000


class Action17692(Action):
    # 对目标及其周围的敌人发动魔法攻击
    # 威力：2000
    # 追加效果：令目标攻击造成的伤害、恢复效果降低10%
    # 持续时间：10秒
    # 发动条件：忠义50点
    # Deals unaspected damage with a potency of 2,000 to target and all enemies nearby it.
    # Additional Effect: Lowers target's damage dealt and healing potency by 10%
    # Duration: 10s
    # Oath Gauge Cost: 50
    # related: [悔罪](Status2076),
    id = 17692
    names = ['Confiteor(pvp)(PLD)', '悔罪(pvp)(PLD)']
    _orig_names = ['悔罪(pvp)', 'Confiteor(pvp)']
    damage = 2000


class Action17693(Action):
    # 对自身周围的敌人发动魔法攻击
    # 威力：1000
    # 追加效果：将攻击所造成伤害的100%转化为自身的体力
    # 追加效果：获得10点忠义
    # Deals unaspected damage with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Increases Oath Gauge by 10
    id = 17693
    names = ['Holy Circle(pvp)(PLD)', '圣环(pvp)(PLD)']
    _orig_names = ['圣环(pvp)', 'Holy Circle(pvp)']
    damage = 1000


class Action17694(Action):
    # 冲向目标并发动物理攻击
    # 威力：600
    # 追加效果：3档忠义之剑
    # 持续时间：10秒
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 600.
    # Additional Effect: Grants 3 stacks of Sword Oath
    # Duration: 10s
    # Cannot be executed while bound.
    # related: [忠义之剑(0)](Status1902), [忠义之剑(1)](Status381), [忠义之剑(2)](Status78), [忠义之剑(3)](Status1991),
    id = 17694
    names = ['Intervene(pvp)(PLD)', '调停(pvp)(PLD)']
    _orig_names = ['调停(pvp)', 'Intervene(pvp)']
    damage = 600


class Action18899(Action):
    # 向自身前方发出扇形范围物理攻击
    # 威力：1200
    # 追加效果：每命中一个目标恢复自身魔力250点
    # 追加效果：获得10点忠义
    # 发动条件：忠义之剑
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200 to all enemies in a cone before you.
    # Additional Effect: Restores 250 MP for each enemy hit
    # Additional Effect: Increases Oath Gauge by 10
    # Can only be executed while under the effect of Sword Oath.
    # ※This action cannot be assigned to a hotbar.
    id = 18899
    names = ['荣耀斩(pvp)(PLD)', 'Glory Slash(pvp)(PLD)']
    _orig_names = ['Glory Slash(pvp)', '荣耀斩(pvp)']
    damage = 1200


class Action18900(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：600
    # 追加效果：获得5点忠义
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Increases Oath Gauge by 5
    # ※This action cannot be assigned to a hotbar.
    id = 18900
    names = ['全蚀斩(pvp)(PLD)', 'Total Eclipse(pvp)(PLD)']
    _orig_names = ['全蚀斩(pvp)', 'Total Eclipse(pvp)']
    damage = 600


class Action18901(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 连击中威力：800
    # 连击条件：全蚀斩
    # 连击成功：每命中一个目标恢复自身魔力250点
    # 连击成功：获得5点忠义
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Total Eclipse
    # Combo Potency: 800
    # Combo Bonus: Restores 250 MP for each enemy hit
    # Combo Bonus: Increases Oath Gauge by 5
    # ※This action cannot be assigned to a hotbar.
    id = 18901
    names = ['Prominence(pvp)(PLD)', '日珥斩(pvp)(PLD)']
    _orig_names = ['Prominence(pvp)', '日珥斩(pvp)']
    combo_action = 18900
    combo_damage = 800


class Action18902(Action):
    # 对目标发动远距离物理攻击
    # 威力：800
    # 追加效果：获得5点忠义
    # Delivers a ranged attack with a potency of 800.
    # Additional Effect: Increases Oath Gauge by 5
    id = 18902
    names = ['投盾(pvp)(PLD)', 'Shield Lob(pvp)(PLD)']
    _orig_names = ['投盾(pvp)', 'Shield Lob(pvp)']
    damage = 800


class Action19085(Action):
    # 指定一名队员，令其受到的伤害减轻20%
    # 持续时间：6秒
    # 自身处于铁壁状态中发动本技能时，可令目标所受伤害减轻效果提高到30%
    # Reduces target party member's damage taken by 20%.
    # Duration: 6s
    # Additional Effect: Increases target's damage reduction to 30% when executed while under the effect of Rampart
    # related: [干预(0)](Status2020), [干预(1)](Status1174), [铁壁(0)](Status1191), [铁壁(1)](Status71), [铁壁(2)](Status1978),
    id = 19085
    names = ['Intervention(pvp)(PLD)', '干预(pvp)(PLD)']
    _orig_names = ['干预(pvp)', 'Intervention(pvp)']
    # remain metas: {'taken_dmg_reduce': ['效果提高到30%', '20%']}


class Action19086(Action):
    # 为自身与周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力3000的伤害量
    # 持续时间：10秒
    # Creates a barrier around self and all party members near you that absorbs damage equivalent to a heal of 3,000 potency.
    # Duration: 10s
    # related: [掩护盾](Status2179),
    id = 19086
    names = ['掩护盾(pvp)(PLD)', 'Testudo(pvp)(PLD)']
    _orig_names = ['Testudo(pvp)', '掩护盾(pvp)']
    # remain metas: {'shield': '恢复力3000'}


class Action25746(Action):
    # 一定时间内，受到攻击必定发动格挡
    # 持续时间：8秒
    # 追加效果：骑士的坚守
    # 持续时间：4秒
    # 骑士的坚守效果：令目标受到的伤害减轻15%
    # 追加效果：骑士的加护
    # 持续时间：12秒
    # 骑士的加护效果：令目标体力持续恢复
    # 恢复力：250
    # 发动条件：忠义50点
    # Block incoming attacks.
    # Duration: 8s
    # Additional Effect: Grants Knight's Resolve
    # Knight's Resolve Effect: Reduces damage taken by 15%
    # Duration: 4s
    # Additional Effect: Grants Knight's Benediction
    # Knight's Benediction Effect: Gradually restores HP
    # Cure Potency: 250
    # Duration: 12s
    # Oath Gauge Cost: 50
    # related: [圣盾阵](Status2674), [骑士的坚守](Status2675), [骑士的加护](Status2676),
    id = 25746
    names = ['圣盾阵(PLD)', 'Holy Sheltron(PLD)']
    _orig_names = ['Holy Sheltron', '圣盾阵']
    # remain metas: {'taken_dmg_reduce': '15%', 'heal_ot': '250'}


class Action25747(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：340
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：恢复自身魔力
    # Delivers an attack to target and all enemies nearby it with a potency of 340 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Restores MP
    id = 25747
    names = ['偿赎剑(PLD)', 'Expiacion(PLD)']
    _orig_names = ['Expiacion', '偿赎剑']
    damage = 340
    # remain metas: {'aoe_reduce': '50%'}


class Action25748(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：420
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 连击条件：悔罪
    # 追加效果：恢复自身魔力
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 420 for the first enemy, and 50% less for all remaining enemies.
    # Combo Action: Confiteor
    # Combo Bonus: Restores MP
    # ※This action cannot be assigned to a hotbar.
    id = 25748
    names = ['信念之剑(PLD)', 'Blade of Faith(PLD)']
    _orig_names = ['Blade of Faith', '信念之剑']
    combo_action = 16459
    damage = 420
    # remain metas: {'aoe_reduce': '50%'}


class Action25749(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：500
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 连击条件：信念之剑
    # 追加效果：恢复自身魔力
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
    # Combo Action: Blade of Faith
    # Combo Bonus: Restores MP
    # ※This action cannot be assigned to a hotbar.
    id = 25749
    names = ['Blade of Truth(PLD)', '真理之剑(PLD)']
    _orig_names = ['Blade of Truth', '真理之剑']
    combo_action = 25748
    damage = 500
    # remain metas: {'aoe_reduce': '50%'}


class Action25750(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：580
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 连击条件：真理之剑
    # 追加效果：恢复自身魔力
    # 连击成功：持续伤害
    # 威力：80
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 持续时间：21秒
    # 无法与沥血剑的持续伤害叠加
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 580 for the first enemy, and 50% less for all remaining enemies.
    # Combo Action: Blade of Truth
    # Combo Bonus: Restores MP
    # Combo Bonus: Damage over time
    # Potency: 80 for the first enemy, and 50% less for all remaining enemies
    # Duration: 21s
    # Damage over time effect cannot be stacked with that of Goring Blade.
    # ※This action cannot be assigned to a hotbar.
    # related: [英勇之剑](Status2721),
    id = 25750
    names = ['英勇之剑(PLD)', 'Blade of Valor(PLD)']
    _orig_names = ['Blade of Valor', '英勇之剑']
    combo_action = 25749
    damage = 580
    # remain metas: {'aoe_reduce': '50%', 'dmg_ot': '80'}


