from ._base import *


class Status116(Status):
    # 下次发动的战技必定打出暴击，并且附带吸收体力的效果
    # Next weaponskill will result in a critical hit with a portion of the resulting damage being absorbed as HP.
    # related: [龙剑(DRG)](Action83), [龙剑(pvp)(DRG)](Action18920),
    id = 116
    names = ['龙剑', 'Life Surge']


class Status2175(Status):
    # 下次发动的战技造成的伤害提高
    # Next weaponskill will deal increased damage.
    # related: [龙剑(DRG)](Action83), [龙剑(pvp)(DRG)](Action18920),
    id = 2175
    names = ['龙剑(pvp)', 'Life Surge(pvp)']


class Status1864(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [猛枪(DRG)](Action85),
    id = 1864
    names = ['猛枪', 'Lance Charge']


class Status120(Status):
    # 下次发动跳跃或破碎冲的伤害提高
    # Damage is increased for next Jump or Spineshatter Dive.
    # related: [开膛枪(DRG)](Action87), [音速刺(DRG)](Action7397),
    id = 120
    names = ['龙枪(0)', 'Power Surge(0)']


class Status121(Status):
    # 突刺耐性降低
    # Piercing resistance is reduced.
    # related: [开膛枪(DRG)](Action87),
    id = 121
    names = ['开膛枪(0)', 'Disembowel(0)']


class Status1914(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [开膛枪(DRG)](Action87),
    id = 1914
    names = ['开膛枪(1)', 'Disembowel(1)']


class Status2720(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [开膛枪(DRG)](Action87), [音速刺(DRG)](Action7397),
    id = 2720
    names = ['龙枪(1)', 'Power Surge(1)']


class Status1312(Status):
    # 受到持续伤害，持续时间中受到为自己附加此状态的玩家的攻击时伤害增加
    # Sustaining damage over time, as well as increased damage from target who executed Chaos Thrust.
    # related: [樱花怒放(DRG)](Action88),
    id = 1312
    names = ['樱花怒放(0)', 'Chaos Thrust(0)']


class Status118(Status):
    # 体力逐渐减少
    # Wounds are bleeding, causing damage over time.
    # related: [樱花怒放(DRG)](Action88),
    id = 118
    names = ['樱花怒放(1)', 'Chaos Thrust(1)']


class Status802(Status):
    # 可以发动龙牙龙爪
    # Able to execute Fang and Claw.
    # related: [龙牙龙爪(DRG)](Action3554),
    id = 802
    names = ['龙牙龙爪预备', 'Sharper Fang and Claw']


class Status803(Status):
    # 可以发动龙尾大回旋
    # Able to execute Wheeling Thrust.
    # related: [龙尾大回旋(DRG)](Action3556),
    id = 803
    names = ['龙尾大回旋预备', 'Enhanced Wheeling Thrust']


class Status786(Status):
    # 暴击发动率提高
    # Critical hit rate is increased.
    # related: [战斗连祷(DRG)](Action3557),
    id = 786
    names = ['战斗连祷(0)', 'Battle Litany(0)']


class Status1414(Status):
    # 造成的伤害提高
    # Damage dealt is increased.
    # related: [战斗连祷(DRG)](Action3557),
    id = 1414
    names = ['战斗连祷(1)', 'Battle Litany(1)']


class Status1184(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [巨龙视线(DRG)](Action7398), [巨龙视线(pvp)(DRG)](Action10032),
    id = 1184
    names = ['巨龙左眼(0)', 'Left Eye(0)']


class Status1910(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [巨龙视线(DRG)](Action7398), [巨龙视线(pvp)(DRG)](Action10032),
    id = 1910
    names = ['巨龙右眼(0)', 'Right Eye(0)']


class Status1453(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [巨龙视线(DRG)](Action7398), [巨龙视线(pvp)(DRG)](Action10032),
    id = 1453
    names = ['巨龙右眼(1)', 'Right Eye(1)']


class Status1454(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [巨龙视线(DRG)](Action7398), [巨龙视线(pvp)(DRG)](Action10032),
    id = 1454
    names = ['巨龙左眼(1)', 'Left Eye(1)']


class Status1183(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [巨龙视线(DRG)](Action7398), [巨龙视线(pvp)(DRG)](Action10032),
    id = 1183
    names = ['巨龙右眼(2)', 'Right Eye(2)']


class Status1243(Status):
    # 可以发动幻象冲
    # Able to execute Mirage Dive.
    # related: [幻象冲(DRG)](Action7399), [高跳(DRG)](Action16478),
    id = 1243
    names = ['幻象冲预备', 'Dive Ready']


class Status736(Status):
    # 跳跃和破碎冲的威力提高
    # Potency of Jump and Spineshatter Dive are increased.
    # related: [死者之岸(pvp)(DRG)](Action8806), [龙眼雷电(pvp)(DRG)](Action18916), [死天枪(pvp)(DRG)](Action18917),
    id = 736
    names = ['苍天龙血', 'Blood of the Dragon']


class Status1863(Status):
    # 可以发动龙眼雷电(job==22?(level>=82?或龙眼苍穹:):)
    # Able to execute Raiden Thrust(job==22?(level>=82? and Draconian Fury:):).
    # related: [龙眼雷电(DRG)](Action16479), [龙眼苍穹(DRG)](Action25770),
    id = 1863
    names = ['龙眼', 'Draconian Fire']


class Status2719(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [樱花缭乱(DRG)](Action25772),
    id = 2719
    names = ['樱花缭乱', 'Chaotic Spring']


class Action75(Action):
    # 对目标发动物理攻击
    # 威力：(job==22?(level>=76?230:170):170)
    # Delivers an attack with a potency of (job==22?(level>=76?230:170):170).(job==22?(level>=76?
    # ※Action changes to Raiden Thrust while under the effect of Draconian Fire.:):)
    id = 75
    names = ['True Thrust(DRG)', '精准刺(DRG)']
    _orig_names = ['True Thrust', '精准刺']
    damage = "(job==22?(lv>=76?230:170):170)"


class Action78(Action):
    # 对目标发动物理攻击
    # 威力：(job==22?(level>=76?130:100):100)
    # 连击条件：精准刺
    # 连击中威力：(job==22?(level>=76?280:250):250)
    # Delivers an attack with a potency of (job==22?(level>=76?130:100):100).
    # Combo Action: True Thrust
    # Combo Potency: (job==22?(level>=76?280:250):250)
    id = 78
    names = ['贯通刺(DRG)', 'Vorpal Thrust(DRG)']
    _orig_names = ['贯通刺', 'Vorpal Thrust']
    combo_action = 75
    damage = "(job==22?(lv>=76?130:100):100)"
    combo_damage = "(job==22?(lv>=76?280:250):250)"


class Action83(Action):
    # 效果时间内，自身发动的1次战技必定打出暴击，并且恢复自身体力
    # 该效果不适用于持续伤害等状态
    # 持续时间：5秒(job==22?(level>=88?
    # 积蓄次数：2:):)
    # Ensures critical damage for first weaponskill used while Life Surge is active.
    # Duration: 5s
    # Effect cannot be applied to damage over time.
    # Additional Effect: Absorbs a portion of damage dealt as HP(job==22?(level>=88?
    # Maximum Charges: 2:):)
    # related: [龙剑(0)](Status116), [龙剑(1)](Status2175),
    id = 83
    names = ['龙剑(DRG)', 'Life Surge(DRG)']
    _orig_names = ['龙剑', 'Life Surge']


class Action84(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：贯通刺
    # 连击中威力：400(level>=56?(job==22?
    # 连击成功：龙牙龙爪预备
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失:):)
    # Delivers an attack with a potency of 100.
    # Combo Action: Vorpal Thrust
    # Combo Potency: 400(level>=56?(job==22?
    # Combo Bonus: Grants Sharper Fang and Claw
    # Duration: 30s
    # Effect of Sharper Fang and Claw ends upon execution of any melee weaponskill.:):)
    id = 84
    names = ['Full Thrust(DRG)', '直刺(DRG)']
    _orig_names = ['Full Thrust', '直刺']
    combo_action = 78
    damage = 100
    combo_damage = 400


class Action85(Action):
    # 一定时间内，自身发动攻击造成的伤害提高10%
    # 持续时间：20秒
    # Increases damage dealt by 10%.
    # Duration: 20s
    # related: [猛枪](Status1864),
    id = 85
    names = ['猛枪(DRG)', 'Lance Charge(DRG)']
    _orig_names = ['猛枪', 'Lance Charge']
    # remain metas: {'dmg_increase': '10%'}


class Action86(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：110
    # Delivers an attack with a potency of 110 to all enemies in a straight line before you.(job==22?(level>=82?
    # ※Action changes to Draconian Fury when under the effect of Draconian Fire.:):)
    id = 86
    names = ['Doom Spike(DRG)', '死天枪(DRG)']
    _orig_names = ['死天枪', 'Doom Spike']
    damage = 110


class Action87(Action):
    # 对目标发动物理攻击
    # 威力：(job==22?(level>=76?140:100):100)
    # 连击条件：精准刺
    # 连击中威力：(job==22?(level>=76?250:210):210)
    # 连击成功：龙枪
    # 持续时间：30秒
    # 龙枪效果：自身发动攻击造成的伤害提高10%
    # Delivers an attack with a potency of (job==22?(level>=76?140:100):100).
    # Combo Action: True Thrust
    # Combo Potency: (job==22?(level>=76?250:210):210)
    # Combo Bonus: Grants Power Surge
    # Power Surge Effect: Increases damage dealt by 10%
    # Duration: 30s
    # related: [龙枪(0)](Status120), [开膛枪(0)](Status121), [开膛枪(1)](Status1914), [龙枪(1)](Status2720),
    id = 87
    names = ['Disembowel(DRG)', '开膛枪(DRG)']
    _orig_names = ['开膛枪', 'Disembowel']
    combo_action = 75
    damage = "(job==22?(lv>=76?140:100):100)"
    combo_damage = "(job==22?(lv>=76?250:210):210)"
    # remain metas: {'dmg_increase': '10%'}


class Action88(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 背面攻击威力：140
    # 连击条件：开膛枪
    # 连击中威力：220
    # 连击中背面攻击威力：260
    # 连击成功：持续伤害
    # 威力：40
    # 持续时间：24秒(level>=58?(job==22?
    # 连击成功：龙尾大回旋预备
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失:):)
    # Delivers an attack with a potency of 100.
    # 140 when executed from a target's rear.
    # Combo Action: Disembowel
    # Combo Potency: 220
    # Rear Combo Potency: 260
    # Combo Bonus: Damage over time
    # Potency: 40
    # Duration: 24s(level>=58?(job==22?
    # Combo Bonus: Grants Enhanced Wheeling Thrust
    # Duration: 30s
    # Effect of Enhanced Wheeling Thrust ends upon execution of any melee weaponskill.:):)
    # related: [樱花怒放(0)](Status1312), [樱花怒放(1)](Status118),
    id = 88
    names = ['樱花怒放(DRG)', 'Chaos Thrust(DRG)']
    _orig_names = ['樱花怒放', 'Chaos Thrust']
    combo_action = 87
    damage = 100
    combo_damage = 220
    back_damage = 140
    back_combo_damage = 260
    # remain metas: {'dmg_ot': '40'}


class Action90(Action):
    # 对目标发动远程物理攻击
    # 威力：150
    # Delivers a ranged attack with a potency of 150.
    id = 90
    names = ['贯穿尖(DRG)', 'Piercing Talon(DRG)']
    _orig_names = ['贯穿尖', 'Piercing Talon']
    damage = 150


class Action92(Action):
    # 跳起接近目标并发动物理攻击
    # 威力：(job==22?(level>=54?320:250):250)
    # 攻击之后回到原位
    # (level>=68?(job==22?追加效果：幻象冲预备
    # 持续时间：15秒
    # :):)止步状态下无法发动
    # Delivers a jumping attack with a potency of (job==22?(level>=54?320:250):250). Returns you to your original position after the attack is made.
    # (level>=68?(job==22?Additional Effect: Grants Dive Ready
    # Duration: 15s
    # :):)Cannot be executed while bound.
    id = 92
    names = ['跳跃(DRG)', 'Jump(DRG)']
    _orig_names = ['Jump', '跳跃']
    damage = "(job==22?(lv>=54?320:250):250)"


class Action94(Action):
    # 向身后跳出15米距离
    # 止步状态下无法发动
    # Executes a jump to a location 15 yalms behind you.
    # Cannot be executed while bound.
    id = 94
    names = ['Elusive Jump(DRG)', '回避跳跃(DRG)']
    _orig_names = ['回避跳跃', 'Elusive Jump']


class Action95(Action):
    # 跳起接近目标并发动物理攻击
    # 威力：(job==22?(level>=54?250:190):190)
    # (job==22?(level>=84?积蓄次数：2
    # :):)止步状态下无法发动
    # Delivers a jumping attack with a potency of (job==22?(level>=54?250:190):190).
    # (job==22?(level>=84?Maximum Charges: 2
    # :):)Cannot be executed while bound.
    id = 95
    names = ['Spineshatter Dive(DRG)', '破碎冲(DRG)']
    _orig_names = ['Spineshatter Dive', '破碎冲']
    damage = "(job==22?(lv>=54?250:190):190)"


class Action96(Action):
    # 跳起接近目标并发动火属性范围攻击
    # 威力：300
    # 止步状态下无法发动
    # Delivers a jumping fire-based attack with a potency of 300 to target and all enemies nearby it.
    # Cannot be executed while bound.
    id = 96
    names = ['Dragonfire Dive(DRG)', '龙炎冲(DRG)']
    _orig_names = ['Dragonfire Dive', '龙炎冲']
    damage = 300


class Action3554(Action):
    # 对目标发动物理攻击
    # 威力：260
    # 侧面攻击威力：300
    # 发动条件：发动(job==22?(level>=86?苍穹刺:直刺):直刺)后为自身附加的龙牙龙爪预备状态中
    # Delivers an attack with a potency of 260.
    # 300 when executed from a target's flank.
    # Can only be executed while under the effect of Sharper Fang and Claw.
    # related: [龙牙龙爪预备](Status802),
    id = 3554
    names = ['龙牙龙爪(DRG)', 'Fang and Claw(DRG)']
    _orig_names = ['Fang and Claw', '龙牙龙爪']
    damage = 260
    side_damage = 300


class Action3555(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：(job==22?(level>=90?260:200):200)
    # 攻击复数敌人时，对目标之外的敌人威力降低30%(level>=70?(job==22?
    # 追加效果：红莲龙血
    # 发动条件：巨龙怒目2档:):)
    # Delivers an attack to all enemies in a straight line before you with a potency of (job==22?(level>=90?260:200):200) for the first enemy, and 30% less for all remaining enemies.(level>=70?(job==22?
    # Additional Effect: Grants Life of the Dragon while under the full gaze of the first brood
    # ※Action changes to Nastrond while under the effect of Life of the Dragon.:):)
    id = 3555
    names = ['武神枪(DRG)', 'Geirskogul(DRG)']
    _orig_names = ['武神枪', 'Geirskogul']
    damage = "(job==22?(lv>=90?260:200):200)"
    # remain metas: {'aoe_reduce': '30%'}


class Action3556(Action):
    # 对目标发动物理攻击
    # 威力：260
    # 背面攻击威力：300
    # 发动条件：发动(job==22?(level>=86?樱花缭乱:樱花怒放):樱花怒放)后为自身附加的龙尾大回旋预备状态中
    # Delivers an attack with a potency of 260.
    # 300 when executed from a target's rear.
    # Can only be executed while under the effect of Enhanced Wheeling Thrust.
    # related: [龙尾大回旋预备](Status803),
    id = 3556
    names = ['Wheeling Thrust(DRG)', '龙尾大回旋(DRG)']
    _orig_names = ['龙尾大回旋', 'Wheeling Thrust']
    damage = 260
    back_damage = 300


class Action3557(Action):
    # 一定时间内，自身与周围队员的暴击发动率提高10%
    # 持续时间：15秒
    # Increases critical hit rate of self and nearby party members by 10%.
    # Duration: 15s
    # related: [战斗连祷(0)](Status786), [战斗连祷(1)](Status1414),
    id = 3557
    names = ['Battle Litany(DRG)', '战斗连祷(DRG)']
    _orig_names = ['战斗连祷', 'Battle Litany']


class Action7397(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：100
    # 连击条件：死天枪
    # 连击中威力：120
    # 连击成功：龙枪
    # 持续时间：30秒
    # 龙枪效果：自身发动攻击造成的伤害提高10%
    # Delivers an attack with a potency of 100 to all enemies in a straight line before you.
    # Combo Action: Doom Spike
    # Combo Potency: 120
    # Combo Bonus: Grants Power Surge
    # Power Surge Effect: Increases damage dealt by 10%
    # Duration: 30s
    # related: [龙枪(0)](Status120), [龙枪(1)](Status2720),
    id = 7397
    names = ['Sonic Thrust(DRG)', '音速刺(DRG)']
    _orig_names = ['Sonic Thrust', '音速刺']
    combo_action = 86
    damage = 100
    combo_damage = 120
    # remain metas: {'dmg_increase': '10%'}


class Action7398(Action):
    # 为自身附加巨龙右眼状态
    # 当指定一名队员为目标时，为自身附加巨龙右眼状态，为目标附加巨龙左眼状态
    # 巨龙右眼效果：攻击伤害提高10%
    # 巨龙左眼效果：攻击伤害提高5%
    # 持续时间：20秒
    # Grants Right Eye to self, increasing damage dealt by 10%. Also grants target party member Left Eye, increasing damage dealt by 5%.
    # Duration: 20s
    # related: [巨龙左眼(0)](Status1184), [巨龙右眼(0)](Status1910), [巨龙右眼(1)](Status1453), [巨龙左眼(1)](Status1454), [巨龙右眼(2)](Status1183),
    id = 7398
    names = ['Dragon Sight(DRG)', '巨龙视线(DRG)']
    _orig_names = ['巨龙视线', 'Dragon Sight']
    # remain metas: {'dmg_increase': ['5%', '10%']}


class Action7399(Action):
    # 对目标发动物理攻击
    # 威力：200
    # (level>=70?(job==22?追加效果：巨龙怒目
    # :):)发动条件：发动(job==22?(level>=74?跳跃、高跳:跳跃):跳跃)后对自身附加的幻象冲预备状态中
    # Delivers an attack with a potency of 200.
    # (level>=70?(job==22?Additional Effect: Strengthens the gaze of your Dragon Gauge by 1
    # :):)Can only be executed when Dive Ready.
    # related: [幻象冲预备](Status1243),
    id = 7399
    names = ['Mirage Dive(DRG)', '幻象冲(DRG)']
    _orig_names = ['Mirage Dive', '幻象冲']
    damage = 200


class Action7400(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：(job==22?(level>=90?360:300):300)
    # 攻击复数敌人时，对目标之外的敌人威力降低30%
    # 发动条件：红莲龙血状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack to all enemies in a straight line before you with a potency of (job==22?(level>=90?360:300):300) for the first enemy, and 30% less for all remaining enemies.
    # Can only be executed while under the effect of Life of the Dragon.
    # ※This action cannot be assigned to a hotbar.
    id = 7400
    names = ['死者之岸(DRG)', 'Nastrond(DRG)']
    _orig_names = ['Nastrond', '死者之岸']
    damage = "(job==22?(lv>=90?360:300):300)"
    # remain metas: {'aoe_reduce': '30%'}


class Action8793(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：龙眼雷电
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Raiden Thrust
    # Combo Potency: 1,400
    # ※This action cannot be assigned to a hotbar.
    id = 8793
    names = ['直刺(pvp)(DRG)', 'Full Thrust(pvp)(DRG)']
    _orig_names = ['直刺(pvp)', 'Full Thrust(pvp)']
    combo_action = 18916
    combo_damage = 1400


class Action8794(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：直刺
    # “苍天龙血”及“红莲龙血”中连击成功：苍天龙血及红莲龙血的持续时间延长10秒，最多可延长至30秒
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Full Thrust
    # Combo Potency: 1,600
    # Combo Bonus: Extends Blood of the Dragon or Life of the Dragon duration by 10s to a maximum of 30s
    # ※This action cannot be assigned to a hotbar.
    id = 8794
    names = ['龙牙龙爪(pvp)(DRG)', 'Fang and Claw(pvp)(DRG)']
    _orig_names = ['Fang and Claw(pvp)', '龙牙龙爪(pvp)']
    combo_action = 8793
    combo_damage = 1600


class Action8798(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：龙牙龙爪
    # “苍天龙血”及“红莲龙血”中连击成功：苍天龙血及红莲龙血的持续时间延长10秒，最多可延长至30秒
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Fang and Claw
    # Combo Potency: 1,600
    # Combo Bonus: Extends Blood of the Dragon or Life of the Dragon duration by 10s, to a maximum of 30s
    # ※This action cannot be assigned to a hotbar.
    id = 8798
    names = ['龙尾大回旋(pvp)(DRG)', 'Wheeling Thrust(pvp)(DRG)']
    _orig_names = ['Wheeling Thrust(pvp)', '龙尾大回旋(pvp)']
    combo_action = 8794
    combo_damage = 1600


class Action8799(Action):
    # 对目标发动远距离物理攻击
    # 威力：800～1600
    # 自身距离目标越远威力越大
    # “苍天龙血”及“红莲龙血”中连击成功：苍天龙血及红莲龙血的持续时间延长10秒，最多可延长至30秒
    # Delivers a ranged attack with a potency of 800. Potency increases up to 1,600 the farther away you are from the target.
    # Additional Effect: Extends Blood of the Dragon or Life of the Dragon duration by 10s, to a maximum of 30s
    id = 8799
    names = ['Piercing Talon(pvp)(DRG)', '贯穿尖(pvp)(DRG)']
    _orig_names = ['贯穿尖(pvp)', 'Piercing Talon(pvp)']
    damage = [800, 1600]


class Action8802(Action):
    # 跳起接近目标并发动物理攻击
    # 威力：800
    # 追加效果：幻象冲的复唱时间缩短15秒
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 800.
    # Additional Effect: Reduces the recast time of Mirage Dive by 15 seconds
    # Cannot be executed while bound.
    id = 8802
    names = ['破碎冲(pvp)(DRG)', 'Spineshatter Dive(pvp)(DRG)']
    _orig_names = ['破碎冲(pvp)', 'Spineshatter Dive(pvp)']
    damage = 800


class Action8803(Action):
    # 向身后跳出15米距离
    # 追加效果：加重、止步和死斗状态下会同时解除上述状态
    # Executes a jump to a location 15 yalms behind you, while removing any Heavy, Bind, or Holmgang effects.
    # related: [死斗(2)](Status88), [死斗(3)](Status409), [死斗(1)](Status1305), [死斗(0)](Status1304),
    id = 8803
    names = ['Elusive Jump(pvp)(DRG)', '回避跳跃(pvp)(DRG)']
    _orig_names = ['回避跳跃(pvp)', 'Elusive Jump(pvp)']


class Action8805(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：1600
    # 追加效果：发动后解除苍天龙血与巨龙怒目状态，为自身附加红莲龙血
    # 持续时间：15秒
    # 发动条件：苍天龙血加巨龙怒目2档
    # ※该技能在“红莲龙血”状态中会变为“死者之岸”
    # Delivers an attack with a potency of 1,600 to all enemies in a straight line before you. Removes Blood of the Dragon status.
    # Additional Effect: Grants Life of the Dragon
    # Duration: Time remaining on original effect, down to a minimum of 15 seconds
    # Can only be executed while under the effect of Blood of the Dragon.
    # Dragon Gauge Cost: 2
    # ※Action changes to Nastrond while under the effect of Life of the Dragon.
    id = 8805
    names = ['武神枪(pvp)(DRG)', 'Geirskogul(pvp)(DRG)']
    _orig_names = ['Geirskogul(pvp)', '武神枪(pvp)']
    damage = 1600


class Action8806(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：2000
    # 追加效果：发动后解除红莲龙血与巨龙怒目状态，为自身附加苍天龙血
    # 发动条件：红莲龙血加巨龙怒目2档
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 2,000 to all enemies in a straight line before you. Removes Life of the Dragon status.
    # Additional Effect: Grants Blood of the Dragon
    # Duration: Time remaining on original effect, down to a minimum of 15 seconds
    # Can only be executed while under the effect of Life of the Dragon.
    # Dragon Gauge Cost: 2
    # ※This action cannot be assigned to a hotbar.
    # related: [苍天龙血](Status736),
    id = 8806
    names = ['Nastrond(pvp)(DRG)', '死者之岸(pvp)(DRG)']
    _orig_names = ['死者之岸(pvp)', 'Nastrond(pvp)']
    damage = 2000


class Action10032(Action):
    # 指定一名队员为目标，为自身附加巨龙右眼状态，为目标附加巨龙左眼状态
    # 巨龙右眼效果：攻击伤害提高10%
    # 巨龙左眼效果：攻击伤害提高10%
    # 持续时间：10秒
    # Grants Right Eye to self and Left Eye to target party member, increasing your damage dealt by 10% and the target party member's damage dealt by 10%.
    # Duration: 10s
    # related: [巨龙左眼(0)](Status1184), [巨龙右眼(0)](Status1910), [巨龙右眼(1)](Status1453), [巨龙左眼(1)](Status1454), [巨龙右眼(2)](Status1183),
    id = 10032
    names = ['巨龙视线(pvp)(DRG)', 'Dragon Sight(pvp)(DRG)']
    _orig_names = ['巨龙视线(pvp)', 'Dragon Sight(pvp)']
    # remain metas: {'dmg_increase': '10%'}


class Action16477(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：100
    # 连击条件：音速刺
    # 连击中威力：150(job==22?(level>=82?
    # 连击成功：龙眼
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of 100 to all enemies in a straight line before you.
    # Combo Action: Sonic Thrust
    # Combo Potency: 150(job==22?(level>=82?
    # Combo Bonus: Grants Draconian Fire
    # Duration: 30s:):)
    id = 16477
    names = ['Coerthan Torment(DRG)', '山境酷刑(DRG)']
    _orig_names = ['山境酷刑', 'Coerthan Torment']
    combo_action = 7397
    damage = 100
    combo_damage = 150


class Action16478(Action):
    # 跳起接近目标并发动物理攻击
    # 威力：400
    # 攻击之后回到原位
    # 追加效果：幻象冲预备
    # 持续时间：15秒
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 400. Returns you to your original position after the attack is made.
    # Additional Effect: Grants Dive Ready
    # Duration: 15s
    # Cannot be executed while bound.
    # related: [幻象冲预备](Status1243),
    id = 16478
    names = ['高跳(DRG)', 'High Jump(DRG)']
    _orig_names = ['High Jump', '高跳']
    damage = 400


class Action16479(Action):
    # 对目标发动物理攻击
    # 威力：280
    # (job==22?(level>=90?追加效果：天龙眼
    # :):)发动条件：龙眼状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 280.
    # (job==22?(level>=90?Additional Effect: Sharpens the Firstminds' Focus by 1
    # :):)Can only be executed while under the effect of Draconian Fire.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙眼](Status1863),
    id = 16479
    names = ['Raiden Thrust(DRG)', '龙眼雷电(DRG)']
    _orig_names = ['Raiden Thrust', '龙眼雷电']
    damage = 280


class Action16480(Action):
    # 跳起接近目标并发动火属性范围物理攻击
    # 威力：620
    # 攻击复数敌人时，对目标之外的敌人威力降低30%
    # 发动条件：红莲龙血状态中
    # 止步状态下无法发动
    # Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 620 for the first enemy, and 30% less for all remaining enemies.
    # Can only be executed while under the effect of Life of the Dragon.
    # Cannot be executed while bound.
    id = 16480
    names = ['Stardiver(DRG)', '坠星冲(DRG)']
    _orig_names = ['Stardiver', '坠星冲']
    damage = 620
    # remain metas: {'aoe_reduce': '30%'}


class Action17728(Action):
    # 跳起接近目标并发动物理攻击
    # 威力：2000
    # 攻击之后回到原位
    # 追加效果：幻象冲的复唱时间缩短15秒
    # 止步状态下无法发动
    #
    # Delivers a jumping attack with a potency of 2,000. Returns you to your original position after the attack is made.
    # Additional Effect: Reduces the recast time of Mirage Dive by 15 seconds
    # Cannot be executed while bound.
    id = 17728
    names = ['High Jump(pvp)(DRG)', '高跳(pvp)(DRG)']
    _orig_names = ['High Jump(pvp)', '高跳(pvp)']
    damage = 2000


class Action17729(Action):
    # 跳起接近目标并发动范围物理攻击
    # 威力：2400
    # 发动条件：苍天龙血或红莲龙血
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 2,400 to target and all enemies nearby it.
    # Can only be executed while under the effect of Blood of the Dragon or Life of the Dragon.
    # Cannot be executed while bound.
    id = 17729
    names = ['坠星冲(pvp)(DRG)', 'Stardiver(pvp)(DRG)']
    _orig_names = ['坠星冲(pvp)', 'Stardiver(pvp)']
    damage = 2400


class Action17730(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：巨龙怒目
    # 发动条件：苍天龙血或红莲龙血
    # 积蓄次数：2
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Strengthens the gaze on your Dragon Gauge by 1
    # Can only be executed while under the effect of Blood of the Dragon or Life of the Dragon.
    # Maximum Charges: 2
    id = 17730
    names = ['幻象冲(pvp)(DRG)', 'Mirage Dive(pvp)(DRG)']
    _orig_names = ['Mirage Dive(pvp)', '幻象冲(pvp)']
    damage = 1000


class Action18916(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 追加效果：苍天龙血
    # 持续时间：15秒
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Grants Blood of the Dragon if not currently under the effect of Life of the Dragon
    # Duration: 15s
    # ※This action cannot be assigned to a hotbar.
    # related: [苍天龙血](Status736),
    id = 18916
    names = ['Raiden Thrust(pvp)(DRG)', '龙眼雷电(pvp)(DRG)']
    _orig_names = ['龙眼雷电(pvp)', 'Raiden Thrust(pvp)']
    damage = 1200


class Action18917(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：800
    # 追加效果：苍天龙血
    # 持续时间：15秒
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 800 to all enemies in a straight line before you.
    # Additional Effect: Grants Blood of the Dragon if not currently under the effect of Life of the Dragon
    # Duration: 15s
    # ※This action cannot be assigned to a hotbar.
    # related: [苍天龙血](Status736),
    id = 18917
    names = ['Doom Spike(pvp)(DRG)', '死天枪(pvp)(DRG)']
    _orig_names = ['Doom Spike(pvp)', '死天枪(pvp)']
    damage = 800


class Action18918(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 连击中威力：1000
    # 连击条件：死天枪
    # “苍天龙血”及“红莲龙血”中连击成功：苍天龙血及红莲龙血的持续时间延长10秒，最多可延长至30秒
    # ※该技能无法设置到热键栏
    # Delivers an attack to all enemies in a straight line before you.
    # Combo Action: Doom Spike
    # Combo Potency: 1,000
    # Combo Bonus: Extends Blood of the Dragon or Life of the Dragon duration by 10s, to a maximum of 30s
    # ※This action cannot be assigned to a hotbar.
    id = 18918
    names = ['音速刺(pvp)(DRG)', 'Sonic Thrust(pvp)(DRG)']
    _orig_names = ['音速刺(pvp)', 'Sonic Thrust(pvp)']
    combo_action = 18917
    combo_damage = 1000


class Action18919(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：1200
    # 连击条件：音速刺
    # “苍天龙血”及“红莲龙血”中连击成功：苍天龙血及红莲龙血的持续时间延长10秒，最多可延长至30秒
    # ※该技能无法设置到热键栏
    # Delivers an attack to all enemies in a straight line before you.
    # Combo Action: Sonic Thrust
    # Combo Potency: 1,200
    # Combo Bonus: Extends Blood of the Dragon or Life of the Dragon duration by 10s, to a maximum of 30s
    # ※This action cannot be assigned to a hotbar.
    id = 18919
    names = ['山境酷刑(pvp)(DRG)', 'Coerthan Torment(pvp)(DRG)']
    _orig_names = ['山境酷刑(pvp)', 'Coerthan Torment(pvp)']
    combo_action = 18918
    damage = 1200


class Action18920(Action):
    # 效果时间内，自身发动的1次战技造成的伤害提升50%
    # 持续时间：5秒
    # 积蓄次数：2
    # Increases potency of next weaponskill by 50%.
    # Duration: 5s
    # Maximum Charges: 2
    # related: [龙剑(0)](Status116), [龙剑(1)](Status2175),
    id = 18920
    names = ['龙剑(pvp)(DRG)', 'Life Surge(pvp)(DRG)']
    _orig_names = ['Life Surge(pvp)', '龙剑(pvp)']


class Action25770(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：130
    # (job==22?(level>=90?追加效果：天龙眼
    # :):)发动条件：龙眼状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 130 to all enemies in a straight line before you.
    # (job==22?(level>=90?Additional Effect: Sharpens the Firstminds' Focus by 1
    # :):)Can only be executed while under the effect of Draconian Fire.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙眼](Status1863),
    id = 25770
    names = ['Draconian Fury(DRG)', '龙眼苍穹(DRG)']
    _orig_names = ['龙眼苍穹', 'Draconian Fury']
    damage = 130


class Action25771(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：贯通刺
    # 连击中威力：480
    # 连击成功：龙牙龙爪预备
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失
    # Delivers an attack with a potency of 100.
    # Combo Action: Vorpal Thrust
    # Combo Potency: 480
    # Combo Bonus: Grants Sharper Fang and Claw
    # Duration: 30s
    # Effect of Sharper Fang and Claw ends upon execution of any melee weaponskill.
    id = 25771
    names = ['苍穹刺(DRG)', "Heavens' Thrust(DRG)"]
    _orig_names = ['苍穹刺', "Heavens' Thrust"]
    combo_action = 78
    damage = 100
    combo_damage = 480


class Action25772(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 背面攻击威力：140
    # 连击条件：开膛枪
    # 连击中威力：260
    # 连击中背面攻击威力：300
    # 连击成功：持续伤害
    # 威力：45
    # 持续时间：24秒
    # 连击成功：龙尾大回旋预备
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失
    # Delivers an attack with a potency of 100.
    # 140 when executed from a target's rear.
    # Combo Action: Disembowel
    # Combo Potency: 260
    # Rear Combo Potency: 300
    # Combo Bonus: Damage over time
    # Potency: 45
    # Duration: 24s
    # Combo Bonus: Grants Enhanced Wheeling Thrust
    # Duration: 30s
    # Effect of Enhanced Wheeling Thrust ends upon execution of any melee weaponskill.
    # related: [樱花缭乱](Status2719),
    id = 25772
    names = ['樱花缭乱(DRG)', 'Chaotic Spring(DRG)']
    _orig_names = ['樱花缭乱', 'Chaotic Spring']
    combo_action = 87
    damage = 100
    combo_damage = 260
    back_damage = 140
    back_combo_damage = 300
    # remain metas: {'dmg_ot': '45'}


class Action25773(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：420
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：天龙眼2档
    # Delivers an attack to all enemies in a straight line before you with a potency of 420 for the first enemy, and 50% less for all remaining enemies.
    # Firstminds' Focus Cost: 2
    id = 25773
    names = ['Wyrmwind Thrust(DRG)', '天龙点睛(DRG)']
    _orig_names = ['天龙点睛', 'Wyrmwind Thrust']
    damage = 420
    # remain metas: {'aoe_reduce': '50%'}


