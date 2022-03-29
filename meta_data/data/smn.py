from ._base import *


class Status808(Status):
    # 得到了龙神巴哈姆特之力，魔法所造成的伤害提高
    # Drawing on the power of Bahamut, increasing magic damage dealt.
    # related: [龙神附体(SMN)](Action3581), [死星核爆(SMN)](Action3582), [龙神召唤(SMN)](Action7427), [龙神附体(pvp)(SMN)](Action9013), [死星核爆(pvp)(SMN)](Action9014), [不死鸟附体(pvp)(SMN)](Action17781), [星极脉冲(SMN)](Action25820), [星极核爆(SMN)](Action25821),
    id = 808
    names = ['龙神附体', 'Dreadwyrm Trance']


class Status2701(Status):
    # 可以发动毁绝
    # Able to execute Ruin IV.
    # related: [毁绝(SMN)](Action7426),
    id = 2701
    names = ['毁绝预备', 'Further Ruin']


class Status1326(Status):
    # 受到持续伤害
    # Contagions are spreading, causing damage over time.
    # related: [剧毒菌(pvp)(SMN)](Action8873), [溃烂爆发(pvp)(SMN)](Action8877), [灾祸(pvp)(SMN)](Action18939), [三重灾祸(pvp)(SMN)](Action18953),
    id = 1326
    names = ['剧毒菌(0)', 'Bio III(0)']


class Status1214(Status):
    # 体力逐渐减少
    # Contagions are spreading, causing damage over time.
    # related: [剧毒菌(pvp)(SMN)](Action8873), [溃烂爆发(pvp)(SMN)](Action8877), [灾祸(pvp)(SMN)](Action18939), [三重灾祸(pvp)(SMN)](Action18953),
    id = 1214
    names = ['剧毒菌(1)', 'Bio III(1)']


class Status2928(Status):
    #
    # Flames are enhancing target capabilities. Damage dealt and healing potency are increased.
    # related: [灵泉之炎(SMN)](Action16514), [灵泉之炎(pvp)(SMN)](Action17778),
    id = 2928
    names = ['(0)', 'Fountain of Fire(0)']


class Status2029(Status):
    # 受到持续伤害
    # Sustaining fire damage over time.
    # related: [灵泉之炎(SMN)](Action16514), [灵泉之炎(pvp)(SMN)](Action17778),
    id = 2029
    names = ['灵泉之炎', 'Fountain of Fire(1)']


class Status1868(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [不死鸟之翼(SMN)](Action16517),
    id = 1868
    names = ['不死鸟之翼(0)', 'Everlasting Flight(0)']


class Status2030(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [不死鸟之翼(SMN)](Action16517),
    id = 2030
    names = ['不死鸟之翼(1)', 'Everlasting Flight(1)']


class Status1329(Status):
    # 自身所受的体力恢复效果降低
    # HP recovery via healing actions is reduced.
    # related: [凋零(pvp)(SMN)](Action17780),
    id = 1329
    names = ['凋零', 'Withering']


class Status2702(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [守护之光(SMN)(0)](Action25799), [守护之光(SMN)(1)](Action25841),
    id = 2702
    names = ['守护之光', 'Radiant Aegis']


class Status2703(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [灼热之光(SMN)(0)](Action25801), [灼热之光(SMN)(1)](Action25842),
    id = 2703
    names = ['灼热之光', 'Searing Light']


class Status2704(Status):
    # 体力降低到一定比例或持续时间结束后便会发动苏生之炎
    # Undying Flame will be triggered upon HP falling below a certain level or expiration of effect duration.
    # related: [苏生之炎(SMN)](Action25830),
    id = 2704
    names = ['苏生之炎(0)', 'Rekindle']


class Status2705(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [苏生之炎(SMN)](Action25830),
    id = 2705
    names = ['苏生之炎(1)', 'Undying Flame']


class Status2724(Status):
    # 可以发动深红旋风
    # Able to execute Crimson Cyclone.
    # related: [深红旋风(SMN)](Action25835), [火神召唤II(SMN)](Action25838),
    id = 2724
    names = ['深红旋风预备', "Ifrit's Favor"]


class Status2853(Status):
    # 可以发动山崩
    # Able to execute Mountain Buster.
    # related: [山崩(SMN)](Action25836),
    id = 2853
    names = ['山崩预备', "Titan's Favor"]


class Status2706(Status):
    # 产生风属性攻击区域
    # Maintaining a localized windstorm.
    # related: [螺旋气流(SMN)](Action25837),
    id = 2706
    names = ['螺旋气流(0)', 'Slipstream']


class Status1869(Status):
    # 产生风属性攻击区域
    # Maintaining a localized windstorm.
    # related: [螺旋气流(SMN)](Action25837),
    id = 1869
    names = ['螺旋气流(1)', 'Gale Enforcer']


class Status2725(Status):
    # 可以发动螺旋气流
    # Able to execute Slipstream.
    # related: [螺旋气流(SMN)](Action25837), [风神召唤II(SMN)](Action25840),
    id = 2725
    names = ['螺旋气流预备', "Garuda's Favor"]


class Action163(Action):
    # 对目标发动无属性魔法攻击
    # 威力：240
    # Deals unaspected damage with a potency of 240.
    id = 163
    names = ['毁灭(SMN)', 'Ruin(SMN)']
    _orig_names = ['毁灭', 'Ruin']
    damage = 240


class Action172(Action):
    # 对目标发动无属性魔法攻击
    # 威力：270
    # Deals unaspected damage with a potency of 270.
    id = 172
    names = ['Ruin II(SMN)', '毁坏(SMN)']
    _orig_names = ['毁坏', 'Ruin II']
    damage = 270


class Action181(Action):
    # 对目标发动无属性魔法攻击
    # 威力：300
    # 发动条件：以太超流
    # Deals unaspected damage with a potency of 300.
    # Aetherflow Gauge Cost: 1
    id = 181
    names = ['溃烂爆发(SMN)', 'Fester(SMN)']
    _orig_names = ['Fester', '溃烂爆发']
    damage = 300


class Action3578(Action):
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：150
    # 发动条件：以太超流
    # Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
    # Aetherflow Gauge Cost: 1
    id = 3578
    names = ['Painflare(SMN)', '痛苦核爆(SMN)']
    _orig_names = ['痛苦核爆', 'Painflare']
    damage = 150


class Action3579(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==27?(level>=84?310:300):300)
    # Deals unaspected damage with a potency of (job==27?(level>=84?310:300):300).
    id = 3579
    names = ['毁荡(SMN)', 'Ruin III(SMN)']
    _orig_names = ['毁荡', 'Ruin III']
    damage = "(job==27?(lv>=84?310:300):300)"


class Action3581(Action):
    # 为自身附加龙神附体状态
    # 持续时间：15秒
    # 追加效果：毁荡变为星极脉冲，迸裂变为星极核爆
    # 追加效果：为自身附加红宝石的奥秘、黄宝石的奥秘、绿宝石的奥秘状态
    # 发动条件：自身处于战斗状态且宝石兽处于同行状态
    # Enters Dreadwyrm Trance.
    # Duration: 15s
    # Additional Effect: Changes Ruin III to Astral Impulse and Outburst to Astral Flare
    # Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
    # Can only be executed in combat and while Carbuncle is summoned.
    # related: [龙神附体](Status808),
    id = 3581
    names = ['龙神附体(SMN)', 'Dreadwyrm Trance(SMN)']
    _orig_names = ['龙神附体', 'Dreadwyrm Trance']


class Action3582(Action):
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：500
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：龙神附体状态中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 60% less for all remaining enemies.
    # Can only be executed while in Dreadwyrm Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙神附体](Status808),
    id = 3582
    names = ['死星核爆(SMN)', 'Deathflare(SMN)']
    _orig_names = ['Deathflare', '死星核爆']
    damage = 500
    # remain metas: {'aoe_reduce': '60%'}


class Action7426(Action):
    # 对目标发动无属性魔法攻击
    # 威力：430
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：毁绝预备状态中
    # Deals unaspected damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 60% less for all remaining enemies.
    # Can only be executed while under the effect of Further Ruin.
    # related: [毁绝预备](Status2701),
    id = 7426
    names = ['Ruin IV(SMN)', '毁绝(SMN)']
    _orig_names = ['毁绝', 'Ruin IV']
    damage = 430
    # remain metas: {'aoe_reduce': '60%'}


class Action7427(Action):
    # 以一名敌人为目标
    # 为自身附加龙神附体状态，令亚灵神巴哈姆特显现
    # 显现时间：15秒
    # 亚灵神巴哈姆特会对召唤师的攻击目标发动真龙波
    # 追加效果：毁荡变为星极脉冲，(job==27?(level>=74?三重灾祸:迸裂):迸裂)变为星极核爆
    # 追加效果：为自身附加红宝石的奥秘、黄宝石的奥秘、绿宝石的奥秘状态
    # 该技能发动后，令目标对自身仇恨提高
    # 发动条件：宝石兽处于同行状态
    # 亚灵神巴哈姆特显现时，之前召唤出的宝石兽会被暂时回收，并在显现时间结束后再次出现
    # Enters Dreadwyrm Trance and summons Demi-Bahamut to fight your target.
    # Demi-Bahamut will execute Wyrmwave automatically on the targets attacked by you after summoning.
    # Increases enmity in target when Demi-Bahamut is summoned.
    # Duration: 15s
    # Additional Effect: Changes Ruin III to Astral Impulse and (job==27?(level>=74?Tri-disaster:Outburst):Outburst) to Astral Flare
    # Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
    # Can only be executed in combat and while Carbuncle is summoned.
    # related: [龙神附体](Status808),
    id = 7427
    names = ['龙神召唤(SMN)', 'Summon Bahamut(SMN)']
    _orig_names = ['Summon Bahamut', '龙神召唤']


class Action7428(Action):
    # 对目标发动无属性魔法攻击
    # 威力：150
    # 发动条件：亚灵神巴哈姆特显现中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 150.
    # Will only execute while Demi-Bahamut is summoned.
    # ※This action cannot be assigned to a hotbar.
    id = 7428
    names = ['真龙波(SMN)', 'Wyrmwave(SMN)']
    _orig_names = ['Wyrmwave', '真龙波']
    damage = 150


class Action7429(Action):
    # 命令显现的亚灵神巴哈姆特发动死亡轮回
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：1300
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：亚灵神巴哈姆特显现中
    # Orders Demi-Bahamut to execute Akh Morn.
    # Akh Morn Effect: Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies
    id = 7429
    names = ['龙神迸发(SMN)', 'Enkindle Bahamut(SMN)']
    _orig_names = ['Enkindle Bahamut', '龙神迸发']
    damage = 1300
    # remain metas: {'aoe_reduce': '60%'}


class Action7449(Action):
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：1300
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：亚灵神巴哈姆特显现中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies.
    # Can only be executed while Demi-Bahamut is summoned.
    # ※This action cannot be assigned to a hotbar.
    id = 7449
    names = ['Akh Morn(SMN)', '死亡轮回(SMN)']
    _orig_names = ['Akh Morn', '死亡轮回']
    damage = 1300
    # remain metas: {'aoe_reduce': '60%'}


class Action8872(Action):
    # 对目标发动魔法攻击
    # 威力：1600
    # ※亚灵神不死鸟显现中，该技能变为“灵泉之炎”
    # Deals unaspected damage with a potency of 1,600.
    # ※Action changes to Fountain of Fire while under the effect of Firebird Trance.
    id = 8872
    names = ['Ruin III(pvp)(SMN)', '毁荡(pvp)(SMN)']
    _orig_names = ['毁荡(pvp)', 'Ruin III(pvp)']
    damage = 1600


class Action8873(Action):
    # 对目标附加持续伤害状态
    # 威力：600
    # 持续时间：18秒
    # Deals unaspected damage over time.
    # Potency: 600
    # Duration: 18s
    # related: [剧毒菌(0)](Status1326), [剧毒菌(1)](Status1214),
    id = 8873
    names = ['剧毒菌(pvp)(SMN)', 'Bio III(pvp)(SMN)']
    _orig_names = ['Bio III(pvp)', '剧毒菌(pvp)']
    # remain metas: {'dmg_ot': '600'}


class Action8877(Action):
    # 对目标发动魔法攻击
    # 威力：1000
    # 目标身上有自身附加的剧毒菌状态时威力变为2倍
    # 发动条件：以太超流
    # Deals unaspected damage with a potency of 1,000.
    # Additional Effect: If target is suffering from a Bio effect inflicted by you, Fester potency is doubled
    # Aetherflow Gauge Cost: 1
    # related: [剧毒菌(0)](Status1326), [剧毒菌(1)](Status1214),
    id = 8877
    names = ['Fester(pvp)(SMN)', '溃烂爆发(pvp)(SMN)']
    _orig_names = ['Fester(pvp)', '溃烂爆发(pvp)']
    damage = 1000


class Action9013(Action):
    # 进入龙神附体状态
    # 持续时间：15秒
    # 追加效果：重置三重灾祸的复唱时间
    # 发动条件：以太超流2档
    # ※“龙神附体”结束后该技能变为“不死鸟附体”
    # Enters Dreadwyrm Trance.
    # Duration: 15s
    # Additional Effect: Resets Tri-disaster recast timer
    # Aetherflow Gauge Cost: 2
    # ※Action changes to Firebird Trance when effect ends.
    # related: [龙神附体](Status808),
    id = 9013
    names = ['龙神附体(pvp)(SMN)', 'Dreadwyrm Trance(pvp)(SMN)']
    _orig_names = ['Dreadwyrm Trance(pvp)', '龙神附体(pvp)']


class Action9014(Action):
    # 对目标及其周围敌人发动范围魔法攻击
    # 威力：2400
    # 发动条件：龙神附体状态中
    # Deals unaspected damage with a potency of 2,400 to target and all enemies nearby it.
    # Can only be executed while under the effect of Dreadwyrm Trance.
    # related: [龙神附体](Status808),
    id = 9014
    names = ['死星核爆(pvp)(SMN)', 'Deathflare(pvp)(SMN)']
    _orig_names = ['Deathflare(pvp)', '死星核爆(pvp)']
    damage = 2400


class Action16230(Action):
    # 恢复目标的体力
    # 恢复力：400
    # Restores target's HP.
    # Cure Potency: 400
    id = 16230
    names = ['医术(SMN)', 'Physick(SMN)']
    _orig_names = ['Physick', '医术']
    heal = 400


class Action16508(Action):
    # 对目标发动无属性魔法攻击
    # 威力：200
    # 追加效果：2档以太超流(job==27?(level>=62?
    # 追加效果：毁绝预备
    # 持续时间：60秒:):)(job==27?(level>=52?
    # 与能量抽取共享复唱时间:):)
    # Deals unaspected damage with a potency of 200.
    # Additional Effect: Aetherflow II(job==27?(level>=62?
    # Additional Effect: Grants Further Ruin
    # Duration: 60s:):)(job==27?(level>=52?
    # Shares a recast timer with Energy Siphon.:):)
    # related: [以太超流](Status304),
    id = 16508
    names = ['Energy Drain(SMN)', '能量吸收(SMN)']
    _orig_names = ['Energy Drain', '能量吸收']
    damage = 200


class Action16510(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：100
    # 追加效果：2档以太超流
    # (job==27?(level>=62?追加效果：毁绝预备
    # 持续时间：60秒
    # :):)与能量吸收共享复唱时间
    # Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
    # Additional Effect: Aetherflow II
    # (job==27?(level>=62?Additional Effect: Grants Further Ruin
    # Duration: 60s
    # :):)Shares a recast timer with Energy Drain.
    # related: [以太超流](Status304),
    id = 16510
    names = ['能量抽取(SMN)', 'Energy Siphon(SMN)']
    _orig_names = ['Energy Siphon', '能量抽取']
    damage = 100


class Action16511(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：100
    # Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
    id = 16511
    names = ['Outburst(SMN)', '迸裂(SMN)']
    _orig_names = ['迸裂', 'Outburst']
    damage = 100


class Action16514(Action):
    # 对目标发动火属性魔法攻击
    # 威力：540
    # 发动条件：不死鸟附体状态中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 540.
    # Can only be executed while under the effect of Firebird Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [(0)](Status2928), [灵泉之炎](Status2029),
    id = 16514
    names = ['灵泉之炎(SMN)', 'Fountain of Fire(SMN)']
    _orig_names = ['灵泉之炎', 'Fountain of Fire']
    damage = 540


class Action16515(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：240
    # 发动条件：不死鸟附体状态中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 240 to target and all enemies nearby it.
    # Can only be executed while under the effect of Firebird Trance.
    # ※This action cannot be assigned to a hotbar.
    id = 16515
    names = ['炼狱之炎(SMN)', 'Brand of Purgatory(SMN)']
    _orig_names = ['Brand of Purgatory', '炼狱之炎']
    damage = 240


class Action16516(Action):
    # 命令显现的亚灵神不死鸟发动天启
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：1300
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：亚灵神不死鸟显现中
    # 满足发动条件后，龙神迸发变为不死鸟迸发
    # ※该技能无法设置到热键栏
    # Orders Demi-Phoenix to execute Revelation.
    # Revelation Effect: Deals fire damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies
    # Action replaces Enkindle Bahamut while Demi-Phoenix is summoned.
    # ※This action cannot be assigned to a hotbar.
    id = 16516
    names = ['不死鸟迸发(SMN)', 'Enkindle Phoenix(SMN)']
    _orig_names = ['不死鸟迸发', 'Enkindle Phoenix']
    damage = 1300
    # remain metas: {'aoe_reduce': '60%'}


class Action16517(Action):
    # 持续恢复周围队员的体力
    # 恢复力：100
    # 持续时间：21秒
    # ※该技能无法设置到热键栏
    # Gradually restores own HP and the HP of all nearby party members.
    # Cure Potency: 100
    # Duration: 21s
    # ※This action cannot be assigned to a hotbar.
    # related: [不死鸟之翼(0)](Status1868), [不死鸟之翼(1)](Status2030),
    id = 16517
    names = ['不死鸟之翼(SMN)', 'Everlasting Flight(SMN)']
    _orig_names = ['不死鸟之翼', 'Everlasting Flight']
    # remain metas: {'heal_ot': '100'}


class Action16518(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：1300
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：亚灵神不死鸟显现中
    # ※该技能无法设置到热键栏
    # Deals fire damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies.
    # Can only be executed while Demi-Phoenix is summoned.
    # ※This action cannot be assigned to a hotbar.
    id = 16518
    names = ['天启(SMN)', 'Revelation(SMN)']
    _orig_names = ['天启', 'Revelation']
    damage = 1300
    # remain metas: {'aoe_reduce': '60%'}


class Action16519(Action):
    # 对目标发动火属性魔法攻击
    # 威力：150
    # 发动条件：亚灵神不死鸟显现中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 150.
    # Will only execute while Demi-Phoenix is summoned.
    # ※This action cannot be assigned to a hotbar.
    id = 16519
    names = ['赤焰(SMN)', 'Scarlet Flame(SMN)']
    _orig_names = ['赤焰', 'Scarlet Flame']
    damage = 150


class Action17777(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：以太超流
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Aetherflow
    # related: [以太超流](Status304),
    id = 17777
    names = ['Energy Drain(pvp)(SMN)', '能量吸收(pvp)(SMN)']
    _orig_names = ['能量吸收(pvp)', 'Energy Drain(pvp)']
    damage = 800


class Action17778(Action):
    # 对目标发动魔法攻击
    # 威力：2000
    # 发动条件：不死鸟附体状态中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 2,000.
    # Can only be executed while under the effect of Firebird Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [(0)](Status2928), [灵泉之炎](Status2029),
    id = 17778
    names = ['Fountain of Fire(pvp)(SMN)', '灵泉之炎(pvp)(SMN)']
    _orig_names = ['Fountain of Fire(pvp)', '灵泉之炎(pvp)']
    damage = 2000


class Action17779(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1200
    # 发动条件：不死鸟附体状态中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 1,200 to target and all enemies nearby it.
    # Can only be executed while under the effect of Firebird Trance.
    # ※This action cannot be assigned to a hotbar.
    id = 17779
    names = ['Brand of Purgatory(pvp)(SMN)', '炼狱之炎(pvp)(SMN)']
    _orig_names = ['炼狱之炎(pvp)', 'Brand of Purgatory(pvp)']
    damage = 1200


class Action17780(Action):
    # 向目标所在方向发出扇形范围魔法攻击
    # 威力：1600
    # 追加效果：解除目标身上所有的持续恢复效果及防护罩
    # Deals unaspected damage with a potency of 1,600 to all enemies in a cone before you.
    # Additional Effect: Removes all Regen and barrier effects from targets
    # related: [凋零](Status1329),
    id = 17780
    names = ['凋零(pvp)(SMN)', 'Wither(pvp)(SMN)']
    _orig_names = ['Wither(pvp)', '凋零(pvp)']
    damage = 1600


class Action17781(Action):
    # 进入不死鸟附体状态
    # 持续时间：15秒
    # 追加效果：重置三重灾祸的复唱时间
    # 发动条件：龙神附体状态结束，且以太超流2档
    # ※该技能无法设置到热键栏
    # Enters Firebird Trance.
    # Duration: 15s
    # Additional Effect: Resets Tri-disaster recast timer
    # Aetherflow Gauge Cost: 2
    # Can only be executed when Dreadwyrm Trance effect has ended.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙神附体](Status808),
    id = 17781
    names = ['Firebird Trance(pvp)(SMN)', '不死鸟附体(pvp)(SMN)']
    _orig_names = ['不死鸟附体(pvp)', 'Firebird Trance(pvp)']


class Action18937(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1000
    # ※“不死鸟附体”状态中，该技能变为“炼狱之炎”
    # Deals unaspected damage with a potency of 1,000 to target and all enemies nearby it.
    # ※Action changes to Brand of Purgatory while under the effect of Firebird Trance.
    id = 18937
    names = ['Outburst(pvp)(SMN)', '迸裂(pvp)(SMN)']
    _orig_names = ['Outburst(pvp)', '迸裂(pvp)']
    damage = 1000


class Action18938(Action):
    # 对目标及其周围敌人发动范围魔法攻击
    # 威力：1200
    # 追加效果：眩晕
    # 持续时间：2秒
    # 发动条件：以太超流
    # Deals unaspected damage with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Stun
    # Duration: 2s
    # Aetherflow Gauge Cost: 1
    id = 18938
    names = ['痛苦核爆(pvp)(SMN)', 'Painflare(pvp)(SMN)']
    _orig_names = ['痛苦核爆(pvp)', 'Painflare(pvp)']
    damage = 1200


class Action18939(Action):
    # 令自身附加给目标的剧毒菌状态向目标的周围扩散
    # 持续时间：扩散时状态的剩余持续时间
    # 发动条件：以太超流
    # Spreads a target's Bio effect to nearby enemies.
    # Duration: Time remaining on original effect
    # Aetherflow Gauge Cost: 1
    # related: [剧毒菌(0)](Status1326), [剧毒菌(1)](Status1214),
    id = 18939
    names = ['Bane(pvp)(SMN)', '灾祸(pvp)(SMN)']
    _orig_names = ['灾祸(pvp)', 'Bane(pvp)']


class Action18953(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：剧毒菌
    # 剧毒菌效果：持续伤害
    # 威力：600
    # 持续时间：18秒
    # 追加效果：以太超流
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Afflicts target with Bio III, dealing damage over time
    # Potency: 600
    # Duration: 18s
    # Additional Effect: Aetherflow
    # related: [剧毒菌(0)](Status1326), [以太超流](Status304), [剧毒菌(1)](Status1214),
    id = 18953
    names = ['三重灾祸(pvp)(SMN)', 'Tri-disaster(pvp)(SMN)']
    _orig_names = ['三重灾祸(pvp)', 'Tri-disaster(pvp)']
    damage = 800
    # remain metas: {'dmg_ot': '600'}


class Action25798(Action):
    # 召唤协助(job==27?召唤师:秘术师)的宝石兽
    # Summons Carbuncle to your side.
    id = 25798
    names = ['宝石兽召唤(SMN)', 'Summon Carbuncle(SMN)']
    _orig_names = ['宝石兽召唤', 'Summon Carbuncle']


class Action25799(Action):
    # 命令宝石兽发动守护之光
    # 对召唤该宝石兽的召唤师附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力20%的伤害量
    # 持续时间：30秒
    # (job==27?(level>=88?积蓄次数：2
    # :):)发动条件：宝石兽处于同行状态
    # Orders Carbuncle to execute Radiant Aegis.
    # Radiant Aegis Effect: Creates a barrier around self that absorbs damage totaling 20% of your maximum HP
    # Duration: 30s
    # (job==27?(level>=88?Maximum Charges: 2
    # :):)Can only be executed while Carbuncle is summoned.
    # related: [守护之光](Status2702),
    id = 25799
    names = ['守护之光(SMN)(0)', 'Radiant Aegis(SMN)(0)']
    _orig_names = ['守护之光', 'Radiant Aegis']
    # remain metas: {'shield': '目标最大体力20%'}


class Action25800(Action):
    # 为自身附加以太蓄能状态
    # 持续时间：15秒
    # 以太蓄能效果：自身发动毁灭、毁坏、毁荡威力提高50，发动迸裂威力提高20
    # 追加效果：(level>=22?(job==26?红宝石的奥秘、黄宝石的奥秘、绿宝石的奥秘:(job==27?红宝石的奥秘、黄宝石的奥秘、绿宝石的奥秘:(level>=15?(job==26?红宝石的奥秘、黄宝石的奥秘:(job==27?红宝石的奥秘、黄宝石的奥秘:红宝石的奥秘)):红宝石的奥秘))):(level>=15?(job==26?红宝石的奥秘、黄宝石的奥秘:(job==27?红宝石的奥秘、黄宝石的奥秘:红宝石的奥秘)):红宝石的奥秘))
    # 发动条件：自身处于战斗状态且宝石兽处于同行状态
    # 该魔法有单独计算的复唱时间
    # Grants Aethercharge, increasing the potency of Ruin, Ruin II, and Ruin III by 50, and Outburst by 20.
    # Duration: 15s
    # Additional Effect: Grants (level>=22?(job==26?Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum:(job==27?Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum:(level>=15?(job==26?Ruby Arcanum and Topaz Arcanum:(job==27?Ruby Arcanum and Topaz Arcanum:Ruby Arcanum)):Ruby Arcanum))):(level>=15?(job==26?Ruby Arcanum and Topaz Arcanum:(job==27?Ruby Arcanum and Topaz Arcanum:Ruby Arcanum)):Ruby Arcanum))
    # Can only be executed in combat and while Carbuncle is summoned.
    id = 25800
    names = ['Aethercharge(SMN)', '以太蓄能(SMN)']
    _orig_names = ['以太蓄能', 'Aethercharge']


class Action25801(Action):
    # 命令宝石兽发动灼热之光
    # 一定时间内，自身与周围队员发动攻击造成的伤害提高3%
    # 持续时间：30秒
    # 发动条件：自身处于战斗状态且宝石兽处于同行状态
    # Orders Carbuncle to execute Searing Light.
    # Searing Light Effect: Increases damage dealt by self and nearby party members by 3%
    # Duration: 30s
    # Can only be executed in combat and while Carbuncle is summoned.
    # related: [灼热之光](Status2703),
    id = 25801
    names = ['Searing Light(SMN)', '灼热之光(SMN)']
    _orig_names = ['Searing Light', '灼热之光']
    # remain metas: {'dmg_increase': '3%'}


class Action25802(Action):
    # 召唤红宝石兽并命其发动红宝石之辉
    # 令红宝石兽接近目标并发动火属性魔法攻击
    # 威力：400
    # 追加效果：为自身附加2档火属性以太状态
    # 持续时间：30秒
    # 火属性以太效果：宝石耀及宝石辉变为火属性魔法
    # 发动条件：宝石兽处于同行状态且红宝石的奥秘状态中
    # Summons Ruby Carbuncle, and orders it to execute Glittering Ruby.
    # Glittering Ruby Effect: Rushes target and deals fire damage with a potency of 400
    # Additional Effect: Grants 2 stacks of Fire Attunement
    # Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
    # Duration: 30s
    # Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
    id = 25802
    names = ['Summon Ruby(SMN)', '红宝石召唤(SMN)']
    _orig_names = ['Summon Ruby', '红宝石召唤']
    damage = 400


class Action25803(Action):
    # 召唤黄宝石兽并命其发动黄宝石之辉
    # 令黄宝石兽接近目标并发动土属性魔法攻击
    # 威力：400
    # 追加效果：为自身附加4档土属性以太状态
    # 持续时间：30秒
    # 土属性以太效果：宝石耀及宝石辉变为土属性魔法
    # 发动条件：宝石兽处于同行状态且黄宝石的奥秘状态中
    # Summons Topaz Carbuncle, and orders it to execute Glittering Topaz.
    # Glittering Topaz Effect: Rushes target and deals earth damage with a potency of 400
    # Additional Effect: Grants 4 stacks of Earth Attunement
    # Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
    # Duration: 30s
    # Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
    id = 25803
    names = ['黄宝石召唤(SMN)', 'Summon Topaz(SMN)']
    _orig_names = ['Summon Topaz', '黄宝石召唤']
    damage = 400


class Action25804(Action):
    # 召唤绿宝石兽并命其发动绿宝石之辉
    # 令绿宝石兽对目标发动风属性魔法攻击
    # 威力：400
    # 追加效果：为自身附加4档风属性以太状态
    # 持续时间：30秒
    # 风属性以太效果：宝石耀及宝石辉变为风属性魔法
    # 发动条件：宝石兽处于同行状态且绿宝石的奥秘状态中
    # Summons Emerald Carbuncle, and orders it to execute Glittering Emerald.
    # Glittering Emerald Effect: Deals wind damage with a potency of 400
    # Additional Effect: Grants 4 stacks of Wind Attunement
    # Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
    # Duration: 30s
    # Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
    id = 25804
    names = ['绿宝石召唤(SMN)', 'Summon Emerald(SMN)']
    _orig_names = ['Summon Emerald', '绿宝石召唤']
    damage = 400


class Action25805(Action):
    # 召唤伊弗利特之灵并命其发动(job==27?(level>=50?地狱之火炎:燃火强袭):燃火强袭)
    # (job==27?(level>=50?令伊弗利特之灵接近目标并对前方5米发动火属性扇形范围魔法攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # :令伊弗利特之灵接近目标并发动火属性魔法攻击
    # 威力：500
    # ):令伊弗利特之灵接近目标并发动火属性魔法攻击
    # 威力：500
    # )追加效果：为自身附加2档火属性以太状态
    # 持续时间：30秒
    # 火属性以太效果：宝石耀及宝石辉变为火属性魔法
    # (job==27?(level>=86?追加效果：深红旋风预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # :):)发动条件：宝石兽处于同行状态且红宝石的奥秘状态中
    # Summons Ifrit-Egi and orders it to execute (job==27?(level>=50?Inferno:Burning Strike):Burning Strike).
    # (job==27?(level>=50?Inferno Effect: Rushes forward and deals fire damage to all enemies in a 5-yalm cone before it with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Burning Strike Effect: Rushes forward and deals fire damage with a potency of 500):Burning Strike Effect: Rushes forward and deals fire damage with a potency of 500)
    # Additional Effect: Grants 2 stacks of Fire Attunement
    # Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
    # Duration: 30s
    # (job==27?(level>=86?Additional Effect: Grants Ifrit's Favor
    # Effect of Ifrit's Favor ends upon execution of certain summoner actions.
    # :):)Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
    id = 25805
    names = ['Summon Ifrit(SMN)', '火神召唤(SMN)']
    _orig_names = ['火神召唤', 'Summon Ifrit']


class Action25806(Action):
    # 召唤泰坦之灵并命其发动(job==27?(level>=50?大地之怒:碎岩):碎岩)
    # (job==27?(level>=50?令泰坦之灵接近目标并对自身周围5米发动土属性范围魔法攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # :令泰坦之灵接近目标并发动土属性魔法攻击
    # 威力：500
    # ):令泰坦之灵接近目标并发动土属性魔法攻击
    # 威力：500
    # )追加效果：为自身附加4档土属性以太状态
    # 持续时间：30秒
    # 土属性以太效果：宝石耀及宝石辉变为土属性魔法
    # 发动条件：宝石兽处于同行状态且黄宝石的奥秘状态中
    # Summons Titan-Egi and orders it to execute (job==27?(level>=50?Earthen Fury:Rock Buster):Rock Buster).
    # (job==27?(level>=50?Earthen Fury Effect: Rushes forward and deals earth damage to all enemies within 5 yalms with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Rock Buster Effect: Rushes forward and deals earth damage with a potency of 500):Rock Buster Effect: Rushes forward and deals earth damage with a potency of 500)
    # Additional Effect: Grants 4 stacks of Earth Attunement
    # Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
    # Duration: 30s
    # Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
    id = 25806
    names = ['土神召唤(SMN)', 'Summon Titan(SMN)']
    _orig_names = ['Summon Titan', '土神召唤']


class Action25807(Action):
    # 召唤迦楼罗之灵并命其发动(job==27?(level>=50?大气爆发:大气风斩):大气风斩)
    # 令迦楼罗之灵对目标及其周围5米以内的敌人发动风属性范围魔法攻击
    # 威力：(job==27?(level>=50?600:100):100)
    # (job==27?(level>=50?攻击复数敌人时，对目标之外的敌人威力降低60%
    # :):)追加效果：为自身附加4档风属性以太状态
    # 持续时间：30秒
    # 风属性以太效果：宝石耀及宝石辉变为风属性魔法
    # (job==27?(level>=86?追加效果：螺旋气流预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # :):)发动条件：宝石兽处于同行状态且绿宝石的奥秘状态中
    # Summons Garuda-Egi and orders it to execute (job==27?(level>=50?Aerial Blast:Aerial Slash):Aerial Slash).
    # (job==27?(level>=50?Aerial Blast Effect: Deals wind damage to target and all enemies within 5 yalms with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Aerial Slash Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it):Aerial Slash Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it)
    # Additional Effect: Grants 4 stacks of Wind Attunement
    # Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
    # Duration: 30s
    # (job==27?(level>=86?Additional Effect: Grants Garuda's Favor
    # Effect of Garuda's Favor ends upon execution of certain summoner actions.
    # :):)Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
    id = 25807
    names = ['风神召唤(SMN)', 'Summon Garuda(SMN)']
    _orig_names = ['风神召唤', 'Summon Garuda']
    damage = "(job==27?(lv>=50?600:100):100)"
    # remain metas: {'aoe_reduce': '60%:):)追加效果：为自身附加4档风属性以太状态'}


class Action25808(Action):
    # 对目标发动火属性魔法攻击
    # 威力：300
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 300.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25808
    names = ['Ruby Ruin(SMN)', '红宝石毁灭(SMN)']
    _orig_names = ['红宝石毁灭', 'Ruby Ruin']
    damage = 300


class Action25809(Action):
    # 对目标发动土属性魔法攻击
    # 威力：240
    # 发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 240.
    # Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25809
    names = ['黄宝石毁灭(SMN)', 'Topaz Ruin(SMN)']
    _orig_names = ['Topaz Ruin', '黄宝石毁灭']
    damage = 240


class Action25810(Action):
    # 对目标发动风属性魔法攻击
    # 威力：160
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 160.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25810
    names = ['绿宝石毁灭(SMN)', 'Emerald Ruin(SMN)']
    _orig_names = ['Emerald Ruin', '绿宝石毁灭']
    damage = 160


class Action25811(Action):
    # 对目标发动火属性魔法攻击
    # 威力：340
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 340.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25811
    names = ['Ruby Ruin II(SMN)', '红宝石毁坏(SMN)']
    _orig_names = ['Ruby Ruin II', '红宝石毁坏']
    damage = 340


class Action25812(Action):
    # 对目标发动土属性魔法攻击
    # 威力：270
    # 发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 270.
    # Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25812
    names = ['Topaz Ruin II(SMN)', '黄宝石毁坏(SMN)']
    _orig_names = ['Topaz Ruin II', '黄宝石毁坏']
    damage = 270


class Action25813(Action):
    # 对目标发动风属性魔法攻击
    # 威力：170
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 170.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25813
    names = ['绿宝石毁坏(SMN)', 'Emerald Ruin II(SMN)']
    _orig_names = ['绿宝石毁坏', 'Emerald Ruin II']
    damage = 170


class Action25814(Action):
    # 对目标及其周围的敌人发动火属性魔法攻击
    # 威力：140
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 140 to target and all enemies nearby it.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25814
    names = ['Ruby Outburst(SMN)', '红宝石迸裂(SMN)']
    _orig_names = ['Ruby Outburst', '红宝石迸裂']
    damage = 140


class Action25815(Action):
    # 对目标及其周围的敌人发动土属性魔法攻击
    # 威力：110
    # 发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 110 to target and all enemies nearby it.
    # Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25815
    names = ['Topaz Outburst(SMN)', '黄宝石迸裂(SMN)']
    _orig_names = ['黄宝石迸裂', 'Topaz Outburst']
    damage = 110


class Action25816(Action):
    # 对目标及其周围的敌人发动风属性魔法攻击
    # 威力：70
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 70 to target and all enemies nearby it.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25816
    names = ['Emerald Outburst(SMN)', '绿宝石迸裂(SMN)']
    _orig_names = ['Emerald Outburst', '绿宝石迸裂']
    damage = 70


class Action25817(Action):
    # 对目标发动火属性魔法攻击
    # 威力：360
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 360.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25817
    names = ['Ruby Ruin III(SMN)', '红宝石毁荡(SMN)']
    _orig_names = ['红宝石毁荡', 'Ruby Ruin III']
    damage = 360


class Action25818(Action):
    # 对目标发动土属性魔法攻击
    # 威力：300
    # 发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 300.
    # Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25818
    names = ['Topaz Ruin III(SMN)', '黄宝石毁荡(SMN)']
    _orig_names = ['Topaz Ruin III', '黄宝石毁荡']
    damage = 300


class Action25819(Action):
    # 对目标发动风属性魔法攻击
    # 威力：180
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 180.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25819
    names = ['Emerald Ruin III(SMN)', '绿宝石毁荡(SMN)']
    _orig_names = ['绿宝石毁荡', 'Emerald Ruin III']
    damage = 180


class Action25820(Action):
    # 对目标发动无属性魔法攻击
    # 威力：440
    # 发动条件：龙神附体状态中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 440.
    # Can only be executed while in Dreadwyrm Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙神附体](Status808),
    id = 25820
    names = ['星极脉冲(SMN)', 'Astral Impulse(SMN)']
    _orig_names = ['星极脉冲', 'Astral Impulse']
    damage = 440


class Action25821(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：180
    # 发动条件：龙神附体状态中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 180 to target and all enemies nearby it.
    # Can only be executed while in Dreadwyrm Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [龙神附体](Status808),
    id = 25821
    names = ['Astral Flare(SMN)', '星极核爆(SMN)']
    _orig_names = ['星极核爆', 'Astral Flare']
    damage = 180


class Action25822(Action):
    # 发动部分技能后，该技能发生变化
    # 发动(level>=70?(job==27?龙神召唤:龙神附体):龙神附体)时：该技能变为死星核爆(job==27?(level>=80?
    # 发动不死鸟召唤时：该技能变为苏生之炎:):)(job==27?(level>=86?
    # 发动(job==27?(level>=90?火神召唤II:火神召唤):火神召唤)时：该技能变为深红旋风
    # 发动黄宝石之仪及黄宝石灾变时：该技能变为山崩
    # 发动(job==27?(level>=90?风神召唤II:风神召唤):风神召唤)时：该技能变为螺旋气流:):)
    # Channel the energies of your active trance(job==27?(level>=86? or elemental favor:):) to perform one of several actions.
    # Dreadwyrm Trance Effect: Action changes to Deathflare(job==27?(level>=80?
    # Firebird Trance Effect: Action changes to Rekindle:):)(job==27?(level>=86?
    # Ifrit's Favor Effect: Action changes to Crimson Cyclone
    # Titan's Favor Effect: Action changes to Mountain Buster
    # Garuda's Favor Effect: Action changes to Slipstream:):)
    id = 25822
    names = ['星极超流(SMN)', 'Astral Flow(SMN)']
    _orig_names = ['星极超流', 'Astral Flow']


class Action25823(Action):
    # 对目标发动火属性魔法攻击
    # 威力：(job==27?(level>=84?450:430):430)
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of (job==27?(level>=84?450:430):430).
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25823
    names = ['Ruby Rite(SMN)', '红宝石之仪(SMN)']
    _orig_names = ['Ruby Rite', '红宝石之仪']
    damage = "(job==27?(lv>=84?450:430):430)"


class Action25824(Action):
    # 对目标发动土属性魔法攻击
    # 威力：(job==27?(level>=84?330:320):320)
    # (job==27?(level>=86?追加效果：山崩预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # :):)发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of (job==27?(level>=84?330:320):320).
    # (job==27?(level>=86?Additional Effect: Grants Titan's Favor
    # Effect of Titan's Favor ends upon execution of certain summoner actions.
    # :):)Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25824
    names = ['黄宝石之仪(SMN)', 'Topaz Rite(SMN)']
    _orig_names = ['Topaz Rite', '黄宝石之仪']
    damage = "(job==27?(lv>=84?330:320):320)"


class Action25825(Action):
    # 对目标发动风属性魔法攻击
    # 威力：(job==27?(level>=84?230:220):220)
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of (job==27?(level>=84?230:220):220).
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25825
    names = ['绿宝石之仪(SMN)', 'Emerald Rite(SMN)']
    _orig_names = ['Emerald Rite', '绿宝石之仪']
    damage = "(job==27?(lv>=84?230:220):220)"


class Action25826(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：120
    # Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
    id = 25826
    names = ['Tri-disaster(SMN)', '三重灾祸(SMN)']
    _orig_names = ['三重灾祸', 'Tri-disaster']
    damage = 120


class Action25827(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：170
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 170 to target and all enemies nearby it.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25827
    names = ['Ruby Disaster(SMN)', '红宝石灾祸(SMN)']
    _orig_names = ['Ruby Disaster', '红宝石灾祸']
    damage = 170


class Action25828(Action):
    # 对目标及其周围的敌人发动土属性范围魔法攻击
    # 威力：130
    # 发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 130 to target and all enemies nearby it.
    # Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25828
    names = ['Topaz Disaster(SMN)', '黄宝石灾祸(SMN)']
    _orig_names = ['黄宝石灾祸', 'Topaz Disaster']
    damage = 130


class Action25829(Action):
    # 对目标及其周围的敌人发动风属性范围魔法攻击
    # 威力：90
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 90 to target and all enemies nearby it.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25829
    names = ['绿宝石灾祸(SMN)', 'Emerald Disaster(SMN)']
    _orig_names = ['Emerald Disaster', '绿宝石灾祸']
    damage = 90


class Action25830(Action):
    # 以自身或一名队员为目标，恢复目标的体力
    # 恢复力：400
    # 追加效果：为目标附加苏生之炎
    # 持续时间：30秒
    # 苏生之炎效果：体力低于75%时或持续时间结束后，自动持续恢复目标的体力
    # 恢复力：200
    # 持续时间：15秒
    # 发动条件：不死鸟附体状态中
    # ※该技能无法设置到热键栏
    # Restores own or target party member's HP.
    # Cure Potency: 400
    # Additional Effect: Grants Rekindle to target
    # Duration: 30s
    # Rekindle Effect: Healing over time when HP falls below 75% or upon effect duration expiration
    # Cure Potency: 200
    # Duration: 15s
    # Can only be executed while in Firebird Trance.
    # ※This action cannot be assigned to a hotbar.
    # related: [苏生之炎(0)](Status2704), [苏生之炎(1)](Status2705),
    id = 25830
    names = ['Rekindle(SMN)', '苏生之炎(SMN)']
    _orig_names = ['Rekindle', '苏生之炎']
    heal = 400
    # remain metas: {'heal_ot': '200'}


class Action25831(Action):
    # 以一名敌人为目标
    # 为自身附加不死鸟附体状态，令亚灵神不死鸟显现
    # 显现时间：15秒
    # 亚灵神不死鸟显现时会发动不死鸟之翼
    # 同时，亚灵神不死鸟会对召唤师的攻击目标发动赤炎
    # 追加效果：毁荡变为灵泉之炎，三重灾祸变为炼狱之炎
    # 追加效果：为自身附加红宝石的奥秘、黄宝石的奥秘、绿宝石的奥秘状态
    # 该技能发动后，令目标对自身仇恨提高
    # 发动条件：宝石兽处于同行状态
    # 亚灵神不死鸟显现时，之前召唤出的宝石兽会被暂时回收，并在显现时间结束后再次出现
    # ※该技能无法设置到热键栏
    # Enters Firebird Trance and summons Demi-Phoenix to fight by your side, which executes Everlasting Flight as it manifests.
    # Demi-Phoenix will execute Scarlet Flame automatically on the targets attacked by you after summoning.
    # Increases enmity in target when Demi-Phoenix is summoned.
    # Duration: 15s
    # Additional Effect: Changes Ruin III to Fountain of Fire and Tri-disaster to Brand of Purgatory
    # Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
    # Can only be executed in combat and while Carbuncle is summoned.
    id = 25831
    names = ['不死鸟召唤(SMN)', 'Summon Phoenix(SMN)']
    _orig_names = ['不死鸟召唤', 'Summon Phoenix']


class Action25832(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：180
    # 发动条件：火属性以太
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 180 to target and all enemies nearby it.
    # Fire Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25832
    names = ['Ruby Catastrophe(SMN)', '红宝石灾变(SMN)']
    _orig_names = ['Ruby Catastrophe', '红宝石灾变']
    damage = 180


class Action25833(Action):
    # 对目标及其周围的敌人发动土属性范围魔法攻击
    # 威力：140
    # (job==27?(level>=86?追加效果：山崩预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # :):)发动条件：土属性以太
    # ※该技能无法设置到热键栏
    # Deals earth damage with a potency of 140 to target and all enemies nearby it.
    # (job==27?(level>=86?Additional Effect: Grants Titan's Favor
    # Effect of Titan's Favor ends upon execution of certain summoner actions.
    # :):)Earth Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25833
    names = ['Topaz Catastrophe(SMN)', '黄宝石灾变(SMN)']
    _orig_names = ['黄宝石灾变', 'Topaz Catastrophe']
    damage = 140


class Action25834(Action):
    # 对目标及其周围的敌人发动风属性范围魔法攻击
    # 威力：100
    # 发动条件：风属性以太
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 100 to target and all enemies nearby it.
    # Wind Attunement Cost: 1
    # ※This action cannot be assigned to a hotbar.
    id = 25834
    names = ['Emerald Catastrophe(SMN)', '绿宝石灾变(SMN)']
    _orig_names = ['Emerald Catastrophe', '绿宝石灾变']
    damage = 100


class Action25835(Action):
    # 冲向目标并对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：430
    # 攻击复数敌人时，对目标之外的敌人威力降低65%
    # 发动条件：深红旋风预备状态中
    # 止步状态下无法发动
    # 该技能发动后变为深红强袭
    # ※该技能无法设置到热键栏
    # Rushes forward and delivers a fire attack to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
    # Can only be executed while under the effect of Ifrit's Favor.
    # Cannot be executed while bound.
    # ※Action changes to Crimson Strike upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [深红旋风预备](Status2724),
    id = 25835
    names = ['深红旋风(SMN)', 'Crimson Cyclone(SMN)']
    _orig_names = ['Crimson Cyclone', '深红旋风']
    damage = 430
    # remain metas: {'aoe_reduce': '65%'}


class Action25836(Action):
    # 对目标及其周围的敌人发动土属性范围魔法攻击
    # 威力：150
    # 攻击复数敌人时，对目标之外的敌人威力降低70%
    # 发动条件：山崩预备状态中
    # ※该技能无法设置到热键栏
    # Deals earth damage to target and all enemies nearby it with a potency of 150 for the first enemy, and 70% less for all remaining enemies.
    # Can only be executed while under the effect of Titan's Favor.
    # ※This action cannot be assigned to a hotbar.
    # related: [山崩预备](Status2853),
    id = 25836
    names = ['Mountain Buster(SMN)', '山崩(SMN)']
    _orig_names = ['山崩', 'Mountain Buster']
    damage = 150
    # remain metas: {'aoe_reduce': '70%'}


class Action25837(Action):
    # 对目标及其周围的敌人发动风属性范围魔法攻击
    # 威力：430
    # 攻击复数敌人时，对目标之外的敌人威力降低65%
    # 追加效果：以目标为中心产生伤害区域
    # 威力：30
    # 持续时间：15秒
    # 发动条件：螺旋气流预备状态中
    # ※该技能无法设置到热键栏
    # Deals wind damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
    # Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
    # Potency: 30
    # Duration: 15s
    # Can only be executed while under the effect of Garuda's Favor.
    # ※This action cannot be assigned to a hotbar.
    # related: [螺旋气流(0)](Status2706), [螺旋气流(1)](Status1869), [螺旋气流预备](Status2725),
    id = 25837
    names = ['螺旋气流(SMN)', 'Slipstream(SMN)']
    _orig_names = ['螺旋气流', 'Slipstream']
    damage = 430 # TODO: [430, 30]
    # remain metas: {'aoe_reduce': '65%'}


class Action25838(Action):
    # 召唤红宝石伊弗利特并命其发动地狱之火炎
    # 令红宝石伊弗利特对目标及其周围5米以内的敌人发动火属性范围魔法攻击
    # 威力：700
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 追加效果：为自身附加2档火属性以太状态
    # 持续时间：30秒
    # 火属性以太效果：宝石耀及宝石辉变为火属性魔法
    # 追加效果：深红旋风预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # 发动条件：宝石兽处于同行状态且红宝石的奥秘状态中
    # Summons Ruby Ifrit and orders it to execute Inferno.
    # Inferno Effect: Deals fire damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
    # Additional Effect: Grants 2 stacks of Fire Attunement
    # Duration: 30s
    # Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
    # Additional Effect: Grants Ifrit's Favor
    # Effect of Ifrit's Favor ends upon execution of certain summoner actions.
    # Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
    # related: [深红旋风预备](Status2724),
    id = 25838
    names = ['火神召唤II(SMN)', 'Summon Ifrit II(SMN)']
    _orig_names = ['Summon Ifrit II', '火神召唤II']
    damage = 700
    # remain metas: {'aoe_reduce': '60%'}


class Action25839(Action):
    # 召唤黄宝石泰坦并命其发动大地之怒
    # 令黄宝石泰坦对目标及其周围5米以内的敌人发动土属性范围魔法攻击
    # 威力：700
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 追加效果：为自身附加4档土属性以太状态
    # 持续时间：30秒
    # 土属性以太效果：宝石耀及宝石辉变为土属性魔法
    # 发动条件：宝石兽处于同行状态且黄宝石的奥秘状态中
    # Summons Topaz Titan and orders it to execute Earthen Fury.
    # Earthen Fury Effect: Deals earth damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
    # Additional Effect: Grants 4 stacks of Earth Attunement
    # Duration: 30s
    # Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
    # Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
    id = 25839
    names = ['土神召唤II(SMN)', 'Summon Titan II(SMN)']
    _orig_names = ['Summon Titan II', '土神召唤II']
    damage = 700
    # remain metas: {'aoe_reduce': '60%'}


class Action25840(Action):
    # 召唤绿宝石迦楼罗并命其发动大气爆发
    # 令绿宝石迦楼罗对目标及其周围5米以内的敌人发动风属性范围魔法攻击
    # 威力：700
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 追加效果：为自身附加4档风属性以太状态
    # 持续时间：30秒
    # 风属性以太效果：宝石耀及宝石辉变为风属性魔法
    # 追加效果：螺旋气流预备
    # 持续时间：永久
    # 发动其他召唤技能会导致该效果消失
    # 发动条件：宝石兽处于同行状态且绿宝石的奥秘状态中
    # Summons Emerald Garuda and orders it to execute Aerial Blast.
    # Aerial Blast Effect: Deals wind damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
    # Additional Effect: Grants 4 stacks of Wind Attunement
    # Duration: 30s
    # Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
    # Additional Effect: Grants Garuda's Favor
    # Effect of Garuda's Favor ends upon execution of certain summoner actions.
    # Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
    # related: [螺旋气流预备](Status2725),
    id = 25840
    names = ['风神召唤II(SMN)', 'Summon Garuda II(SMN)']
    _orig_names = ['Summon Garuda II', '风神召唤II']
    damage = 700
    # remain metas: {'aoe_reduce': '60%'}


class Action25841(Action):
    # 对召唤该宝石兽的召唤师附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力20%的伤害量
    # 持续时间：30秒
    # ※该技能无法设置到热键栏
    # Creates a barrier around you that absorbs damage totaling 20% of your maximum HP.
    # Duration: 30s
    # ※This action cannot be assigned to a hotbar.
    # related: [守护之光](Status2702),
    id = 25841
    names = ['守护之光(SMN)(1)', 'Radiant Aegis(SMN)(1)']
    _orig_names = ['守护之光', 'Radiant Aegis']
    # remain metas: {'shield': '目标最大体力20%'}


class Action25842(Action):
    # 一定时间内，自身与周围队员发动攻击造成的伤害提高3%
    # 持续时间：30秒
    # ※该技能无法设置到热键栏
    # Increases damage dealt by self and nearby party members by 3%.
    # Duration: 30s
    # ※This action cannot be assigned to a hotbar.
    # related: [灼热之光](Status2703),
    id = 25842
    names = ['灼热之光(pet)(SMN)', 'Searing Light(pet)(SMN)']
    _orig_names = ['Searing Light(pet)', '灼热之光(pet)']
    # remain metas: {'dmg_increase': '3%'}


class Action25883(Action):
    # 根据自身附加的以太发动对应的技能
    # 火属性以太状态中：变为火属性单体攻击魔法
    # 土属性以太状态中：变为土属性单体攻击魔法
    # 风属性以太状态中：变为风属性单体攻击魔法
    # Channel the energies of your active elemental attunement to attack your enemy.
    # Fire Attunement Effect: Deal fire damage to a single target
    # Earth Attunement Effect: Deal earth damage to a single target
    # Wind Attunement Effect: Deal wind damage to a single target
    id = 25883
    names = ['宝石耀(SMN)', 'Gemshine(SMN)']
    _orig_names = ['宝石耀', 'Gemshine']


class Action25884(Action):
    # 根据自身附加的以太发动对应的技能
    # 火属性以太状态中：变为火属性范围攻击魔法
    # 土属性以太状态中：变为土属性范围攻击魔法
    # 风属性以太状态中：变为风属性范围攻击魔法
    # Channel the energies of your active elemental attunement to attack multiple enemies.
    # Fire Attunement Effect: Deal fire damage to a target and all enemies nearby it
    # Earth Attunement Effect: Deal earth damage to a target and all enemies nearby it
    # Wind Attunement Effect: Deal wind damage to a target and all enemies nearby it
    id = 25884
    names = ['Precious Brilliance(SMN)', '宝石辉(SMN)']
    _orig_names = ['宝石辉', 'Precious Brilliance']


class Action25885(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：430
    # 攻击复数敌人时，对目标之外的敌人威力降低65%
    # 连击条件：深红旋风
    # ※该技能无法设置到热键栏
    # Deals fire damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
    # Combo Action: Crimson Cyclone
    # ※This action cannot be assigned to a hotbar.
    id = 25885
    names = ['Crimson Strike(SMN)', '深红强袭(SMN)']
    _orig_names = ['Crimson Strike', '深红强袭']
    combo_action = 25835
    damage = 430
    # remain metas: {'aoe_reduce': '65%'}


