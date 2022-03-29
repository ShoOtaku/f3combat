from ._base import *


class Status130(Status):
    # 暴击发动率提高
    # Critical hit rate is increased.
    # related: [直线射击(BRD)](Action98),
    id = 130
    names = ['直线射击', 'Straight Shot']


class Status122(Status):
    # 可以发动直线射击
    # Able to execute Straight Shot.
    # related: [直线射击(BRD)](Action98), [纷乱箭(BRD)](Action107), [辉煌箭(BRD)](Action7409),
    id = 122
    names = ['直线射击预备', 'Straight Shot Ready']


class Status124(Status):
    # 身中剧毒，体力会逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [伶牙俐齿(BRD)](Action3560),
    id = 124
    names = ['毒咬箭', 'Venomous Bite']


class Status125(Status):
    # 攻击造成的伤害提高
    # Damage dealt is increased.
    # related: [猛者强击(BRD)](Action101),
    id = 125
    names = ['猛者强击', 'Raging Strikes']


class Status128(Status):
    # 自身发动的下一次战技会变为多次攻击
    # Striking multiple times per weaponskill.
    # related: [纷乱箭(BRD)](Action107), [影噬箭(BRD)](Action16494),
    id = 128
    names = ['纷乱箭', 'Barrage']


# class Status1407(Status):
#     # 自身发动的下一次战技会变为多次攻击
#     # Striking multiple times per weaponskill.
#     # related: [纷乱箭(BRD)](Action107), [影噬箭(BRD)](Action16494),
#     id = 1407
#     names = ['纷乱箭(1)', 'Barrage(1)']


class Status2017(Status):
    # 战技造成的伤害提高
    # Damage dealt by weaponskills is increased.
    # related: [后跃射击(BRD)](Action112), [后跃射击(pvp)(BRD)](Action8839),
    id = 2017
    names = ['后跃射击', 'Repelling Shot']


class Status129(Status):
    # 风属性持续伤害，体力逐渐流失
    # Wounds are exposed to the elements, causing wind damage over time.
    # related: [风蚀箭(BRD)](Action113),
    id = 129
    names = ['风蚀箭', 'Windbite']


# class Status135(Status):
#     # 对一定范围内的队友附加魔力持续恢复效果，自身攻击所造成的伤害降低，并且会持续消耗魔力
#     # Using MP to gradually restore the MP of nearby party members. Damage dealt is reduced.
#     # related: [贤者的叙事谣(BRD)](Action114),
#     id = 135
#     names = ['贤者的叙事谣(0)', "Mage's Ballad(0)"]
#
#
# class Status136(Status):
#     # 魔力持续恢复
#     # Restoring MP over time.
#     # related: [贤者的叙事谣(BRD)](Action114),
#     id = 136
#     names = ['贤者的叙事谣(1)', "Mage's Ballad(1)"]


class Status2217(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [贤者的叙事谣(BRD)](Action114),
    id = 2217
    names = ['贤者的叙事谣', "Mage's Ballad"]


# class Status2214(Status):
#     # 战技与魔法的咏唱及复唱时间缩短
#     # Weaponskill and spell cast and recast time are reduced.
#     # related: [军神的赞美歌(BRD)](Action116), [九天连箭(pvp)(BRD)](Action8838), [后跃射击(pvp)(BRD)](Action8839), [军神的赞美歌(pvp)(BRD)](Action8844), [爆发射击(pvp)(BRD)](Action17745),
#     id = 2214
#     names = ['军神的赞美歌(0)', "Army's Paeon(0)"]
#
#
# class Status137(Status):
#     # 对一定范围内的队友附加技力持续恢复效果，自身攻击所造成的伤害降低，并且会持续消耗魔力
#     # Using MP to gradually refresh the TP of self and nearby party members. Damage dealt is reduced.
#     # related: [军神的赞美歌(BRD)](Action116), [九天连箭(pvp)(BRD)](Action8838), [后跃射击(pvp)(BRD)](Action8839), [军神的赞美歌(pvp)(BRD)](Action8844), [爆发射击(pvp)(BRD)](Action17745),
#     id = 137
#     names = ['军神的赞美歌(1)', "Army's Paeon(1)"]


class Status2218(Status):
    # 直击发动率提高
    # Direct hit rate is increased.
    # related: [军神的赞美歌(BRD)](Action116), [九天连箭(pvp)(BRD)](Action8838), [后跃射击(pvp)(BRD)](Action8839), [军神的赞美歌(pvp)(BRD)](Action8844), [爆发射击(pvp)(BRD)](Action17745),
    id = 2218
    names = ['军神的赞美歌', "Army's Paeon"]


# class Status138(Status):
#     # 技力持续恢复
#     # Gradually regenerating TP.
#     # related: [军神的赞美歌(BRD)](Action116), [九天连箭(pvp)(BRD)](Action8838), [后跃射击(pvp)(BRD)](Action8839), [军神的赞美歌(pvp)(BRD)](Action8844), [爆发射击(pvp)(BRD)](Action17745),
#     id = 138
#     names = ['军神的赞美歌(3)', "Army's Paeon(3)"]


class Status247(Status):
    # 回避率降低
    # Evasion is reduced.
    # related: [死亡箭雨(BRD)](Action117),
    id = 247
    names = ['死亡箭雨', 'Rain of Death']


class Status141(Status):
    # 直击发动率提高
    # Direct hit rate is increased.
    # related: [战斗之声(BRD)](Action118),
    id = 141
    names = ['战斗之声', 'Battle Voice']


# class Status865(Status):
#     # 攻击造成的伤害提高的同时，对弓箭手和吟游诗人的战技附加额外的咏唱时间
#     # Damage dealt is increased while cast time is added to all archer and bard weaponskills.
#     # related: [放浪神的小步舞曲(BRD)](Action3559), [完美音调(BRD)](Action7404), [放浪神的小步舞曲(pvp)(BRD)](Action8843),
#     id = 865
#     names = ['放浪神的小步舞曲(0)', "The Wanderer's Minuet(0)"]
#
#
# class Status2215(Status):
#     # 攻击所造成的伤害提高
#     # Damage dealt is increased.
#     # related: [放浪神的小步舞曲(BRD)](Action3559), [完美音调(BRD)](Action7404), [放浪神的小步舞曲(pvp)(BRD)](Action8843),
#     id = 2215
#     names = ['放浪神的小步舞曲(1)', "The Wanderer's Minuet(1)"]


class Status2216(Status):
    # 暴击发动率提高
    # Critical hit rate is increased.
    # related: [放浪神的小步舞曲(BRD)](Action3559), [完美音调(BRD)](Action7404), [放浪神的小步舞曲(pvp)(BRD)](Action8843),
    id = 2216
    names = ['放浪神的小步舞曲', "The Wanderer's Minuet"]


class Status1200(Status):
    # 身中剧毒，体力会逐渐减少
    # Toxins are causing damage over time.
    # related: [伶牙俐齿(BRD)](Action3560), [烈毒咬箭(BRD)](Action7406),
    id = 1200
    names = ['烈毒咬箭', 'Caustic Bite']


# class Status1321(Status):
#     # 受到持续伤害
#     # Toxins are causing damage over time.
#     # related: [伶牙俐齿(BRD)](Action3560), [烈毒咬箭(BRD)](Action7406),
#     id = 1321
#     names = ['烈毒咬箭(1)', 'Caustic Bite(1)']


class Status866(Status):
    # 下次异常状态效果无效
    # Impervious to the next enfeeblement.
    # related: [光阴神的礼赞凯歌(BRD)](Action3561),
    id = 866
    names = ['光阴神的礼赞凯歌', "The Warden's Paean"]


class Status1201(Status):
    # 风属性持续伤害，体力逐渐流失
    # Wounds are exposed to the elements, causing wind damage over time.
    # related: [狂风蚀箭(BRD)](Action7407),
    id = 1201
    names = ['狂风蚀箭', 'Stormbite']


# class Status1322(Status):
#     # 受到持续伤害
#     # Wounds are exposed to the elements, causing damage over time.
#     # related: [狂风蚀箭(BRD)](Action7407),
#     id = 1322
#     names = ['狂风蚀箭(1)', 'Stormbite(1)']


class Status1202(Status):
    # 自身所受的治疗效果提高
    # HP recovery via healing actions is increased.
    # related: [大地神的抒情恋歌(BRD)](Action7408), [大地神的抒情恋歌(pvp)(BRD)](Action19071),
    id = 1202
    names = ['大地神的抒情恋歌', "Nature's Minne"]


# class Status2178(Status):
#     # 减轻所受到的伤害，自身所受体力恢复效果提高
#     # Damage taken is reduced while HP recovered via healing actions is increased.
#     # related: [大地神的抒情恋歌(BRD)](Action7408), [大地神的抒情恋歌(pvp)(BRD)](Action19071),
#     id = 2178
#     names = ['大地神的抒情恋歌(1)', "Nature's Minne(1)"]


class Status3002(Status):
    # 可以发动影噬箭
    # Able to execute Shadowbite.
    # related: [影噬箭(BRD)](Action16494),
    id = 3002
    names = ['影噬箭预备', 'Shadowbite Ready']


class Status2692(Status):
    # 可以发动爆破箭
    # Able to execute Blast Arrow.
    # related: [爆破箭(BRD)](Action25784),
    id = 2692
    names = ['爆破箭预备', 'Blast Arrow Ready']


class Status2722(Status):
    # 光明神的最终乐章状态中
    # Playing a most radiant finale.
    # related: [光明神的最终乐章(BRD)](Action25785),
    id = 2722
    names = ['光明神的最终乐章(自己)', 'Radiant Finale(self)']


class Status2964(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [光明神的最终乐章(BRD)](Action25785),
    id = 2964
    names = ['光明神的最终乐章(队伍)', 'Radiant Finale(party)']


class Action97(Action):
    # 对目标发动物理攻击
    # 威力：160(level>=2?(job==5?
    # 追加效果（发动几率20%）：直线射击预备
    # 持续时间：30秒:(job==23?
    # 追加效果（发动几率20%）：直线射击预备
    # 持续时间：30秒:)):)
    # Delivers an attack with a potency of 160.(level>=2?(job==5?
    # Additional Effect: 20% chance of becoming Straight Shot Ready
    # Duration: 30s:(job==23?
    # Additional Effect: 20% chance of becoming Straight Shot Ready
    # Duration: 30s:)):)
    id = 97
    names = ['Heavy Shot(BRD)', '强力射击(BRD)']
    _orig_names = ['Heavy Shot', '强力射击']
    damage = 160


class Action98(Action):
    # 对目标发动物理攻击
    # 威力：200
    # 发动条件：直线射击预备状态中
    # Delivers an attack with a potency of 200.
    # Can only be executed when Straight Shot Ready.
    # related: [直线射击](Status130), [直线射击预备](Status122),
    id = 98
    names = ['Straight Shot(BRD)', '直线射击(BRD)']
    _orig_names = ['直线射击', 'Straight Shot']
    damage = 200


class Action100(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：中毒
    # 威力：15
    # 持续时间：45秒
    # Delivers an attack with a potency of 100.
    # Additional Effect: Venom
    # Potency: 15
    # Duration: 45s
    # related: [中毒(0)](Status801), [中毒(1)](Status2089), [中毒(2)](Status686), [中毒(3)](Status559), [中毒(4)](Status560), [中毒(5)](Status18), [中毒(6)](Status275), [中毒(7)](Status2104), [毒咬箭](Status124),
    id = 100
    names = ['毒咬箭(BRD)', 'Venomous Bite(BRD)']
    _orig_names = ['Venomous Bite', '毒咬箭']
    damage = 100  # TODO: [100, 15]


class Action101(Action):
    # 一定时间内，自身发动攻击造成的伤害提高15%
    # 持续时间：20秒
    # Increases damage dealt by 15%.
    # Duration: 20s
    # related: [猛者强击](Status125),
    id = 101
    names = ['猛者强击(BRD)', 'Raging Strikes(BRD)']
    _orig_names = ['猛者强击', 'Raging Strikes']
    # remain metas: {'dmg_increase': '15%'}


class Action106(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：110(job==23?(level>=72?
    # 追加效果（发动几率35%）：影噬箭预备
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of 110 to all enemies in a cone before you.(job==23?(level>=72?
    # Additional Effect: 35% chance of becoming Shadowbite Ready
    # Duration: 30s:):)
    id = 106
    names = ['连珠箭(BRD)', 'Quick Nock(BRD)']
    _orig_names = ['Quick Nock', '连珠箭']
    damage = 110


class Action107(Action):
    # 效果时间内，自身发动的1次单体攻击战技连续发动3次，但该战技的追加效果只发动1次
    # (job==23?(level>=72?效果时间内，影噬箭威力提高至270
    # :):)持续时间：10秒
    # 追加效果：直线射击预备
    # 持续时间：30秒
    # Triples the number of strikes for a single-target weaponskill. Additional effects added only once.
    # Duration: 10s
    # (job==23?(level>=72?Additional Effect: Increases the potency of Shadowbite to 270
    # :):)Additional Effect: Grants Straight Shot Ready
    # Duration: 30s
    # related: [纷乱箭(0)](Status128), [直线射击预备](Status122), [纷乱箭(1)](Status1407),
    id = 107
    names = ['Barrage(BRD)', '纷乱箭(BRD)']
    _orig_names = ['纷乱箭', 'Barrage']


class Action110(Action):
    # 对目标发动物理攻击
    # 威力：110
    # 积蓄次数：(job==23?(level>=84?3:2):2)(level>=45?(job==23?
    # 与死亡箭雨共享复唱时间:):)
    # Delivers an attack with a potency of 110.
    # Maximum Charges: (job==23?(level>=84?3:2):2)(level>=45?(job==23?
    # Shares a recast timer with Rain of Death.:):)
    id = 110
    names = ['失血箭(BRD)', 'Bloodletter(BRD)']
    _orig_names = ['Bloodletter', '失血箭']
    damage = 110


class Action112(Action):
    # 射击目标，同时后跳10米距离
    # 止步状态下无法发动
    # Jump 10 yalms away from current target.
    # Cannot be executed while bound.
    # related: [后跃射击](Status2017),
    id = 112
    names = ['Repelling Shot(BRD)', '后跃射击(BRD)']
    _orig_names = ['后跃射击', 'Repelling Shot']


class Action113(Action):
    # 对目标发动风属性物理攻击
    # 威力：60
    # 追加效果：风属性持续伤害
    # 威力：20
    # 持续时间：45秒
    # Deals wind damage with a potency of 60.
    # Additional Effect: Wind damage over time
    # Potency: 20
    # Duration: 45s
    # related: [风蚀箭](Status129),
    id = 113
    names = ['Windbite(BRD)', '风蚀箭(BRD)']
    _orig_names = ['风蚀箭', 'Windbite']
    damage = 60
    # remain metas: {'dmg_ot': '20'}


class Action114(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 弹唱贤者的叙事谣，
    # 令自身及周围30米内的队员攻击伤害提高1%
    # 持续时间：45秒
    # 追加效果（发动几率80%）：诗心
    # “诗心”效果：失血箭(level>=45?(job==23?及死亡箭雨:):)的复唱时间缩短7.5秒(job==23?(level>=90?
    # 追加效果：贤者的尾声:):)
    # Deals unaspected damage with a potency of 100.
    # Additional Effect: Grants Mage's Ballad to self and all party members within 30 yalms, increasing damage dealt by 1%
    # Duration: 45s
    # Additional Effect: 80% chance to grant Repertoire
    # Repertoire Effect: Reduces the recast time of Bloodletter(level>=45?(job==23? and Rain of Death:):) by 7.5s(job==23?(level>=90?
    # Additional Effect: Grants Mage's Coda:):)
    # related: [贤者的叙事谣(0)](Status135), [贤者的叙事谣(1)](Status136), [贤者的叙事谣(2)](Status2217),
    id = 114
    names = ['贤者的叙事谣(BRD)', "Mage's Ballad(BRD)"]
    _orig_names = ["Mage's Ballad", '贤者的叙事谣']
    damage = 100
    # remain metas: {'dmg_increase': '1%'}


class Action116(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 弹唱军神的赞美歌，
    # 令自身及周围30米内的队员直击发动率提高3%
    # 持续时间：45秒
    # 追加效果（发动几率80%）：诗心
    # “诗心”效果：每档可令自身的自动攻击间隔、战技与魔法的咏唱及复唱时间缩短4%
    # 最大档数：4档(job==23?(level>=90?
    # 追加效果：军神的尾声:):)
    # Deals unaspected damage with a potency of 100.
    # Additional Effect: Grants Army's Paeon to self and all party members within 30 yalms, increasing direct hit rate by 3%
    # Duration: 45s
    # Additional Effect: 80% chance to grant Repertoire
    # Repertoire Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 4%
    # Can be stacked up to 4 times.(job==23?(level>=90?
    # Additional Effect: Grants Army's Coda:):)
    # related: [军神的赞美歌(0)](Status2214), [军神的赞美歌(1)](Status137), [军神的赞美歌(2)](Status2218), [军神的赞美歌(3)](Status138),
    id = 116
    names = ['军神的赞美歌(BRD)', "Army's Paeon(BRD)"]
    _orig_names = ['军神的赞美歌', "Army's Paeon"]
    damage = 100


class Action117(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：100
    # 积蓄次数：(job==23?(level>=84?3:2):2)
    # 与失血箭共享复唱时间
    # Delivers an attack with a potency of 100 to target and all enemies nearby it.
    # Maximum Charges: (job==23?(level>=84?3:2):2)
    # Shares a recast timer with Bloodletter.
    # related: [死亡箭雨](Status247),
    id = 117
    names = ['死亡箭雨(BRD)', 'Rain of Death(BRD)']
    _orig_names = ['死亡箭雨', 'Rain of Death']
    damage = 100


class Action118(Action):
    # 一定时间内，自身及周围队员的直击发动率提高20%
    # 持续时间：15秒
    # 发动条件：正在使用贤者的叙事谣、军神的赞美歌、放浪神的小步舞曲任意一种
    # Increases direct hit rate of self and all nearby party members by 20%.
    # Duration: 15s
    # Can only be executed while singing Mage's Ballad, Army's Paeon, or the Wanderer's Minuet.
    # related: [战斗之声](Status141),
    id = 118
    names = ['战斗之声(BRD)', 'Battle Voice(BRD)']
    _orig_names = ['Battle Voice', '战斗之声']


class Action3558(Action):
    # 对目标发动物理攻击
    # 威力：200
    # Delivers an attack with a potency of 200.
    id = 3558
    names = ['九天连箭(BRD)', 'Empyreal Arrow(BRD)']
    _orig_names = ['Empyreal Arrow', '九天连箭']
    damage = 200


class Action3559(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 弹唱放浪神的小步舞曲，令自身及周围30米内的队员暴击发动率提高2%
    # 持续时间：45秒
    # 追加效果（发动几率80%）：诗心
    # “诗心”效果：可发动完美音调
    # 最大档数：3档(job==23?(level>=90?
    # 追加效果：放浪神的尾声:):)
    # Deals unaspected damage with a potency of 100.
    # Additional Effect: Grants the Wanderer's Minuet to self and all party members within 30 yalms, increasing critical hit rate by 2%
    # Duration: 45s
    # Additional Effect: 80% chance to grant Repertoire
    # Repertoire Effect: Allows execution of Pitch Perfect
    # Can be stacked up to 3 times.(job==23?(level>=90?
    # Additional Effect: Grants Wanderer's Coda:):)
    # related: [放浪神的小步舞曲(0)](Status865), [放浪神的小步舞曲(1)](Status2215), [放浪神的小步舞曲(2)](Status2216),
    id = 3559
    names = ['放浪神的小步舞曲(BRD)', "the Wanderer's Minuet(BRD)"]
    _orig_names = ['放浪神的小步舞曲', "the Wanderer's Minuet"]
    damage = 100


class Action3560(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：重置自身对目标施加的(level>=64?(job==23?烈毒咬箭和狂风蚀箭:毒咬箭和风蚀箭):毒咬箭和风蚀箭)的持续时间
    # 自身没有对目标施加上述持续伤害状态时无效(job==23?(level>=76?
    # 追加效果（发动几率35%）：直线射击预备
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of 100.
    # Additional Effect: If the target is suffering from a (level>=64?(job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) effect inflicted by you, the effect timer is reset(job==23?(level>=76?
    # Additional Effect: 35% chance of becoming Straight Shot Ready
    # Duration: 30s:):)
    # related: [烈毒咬箭(0)](Status1200), [烈毒咬箭(1)](Status1321), [毒咬箭](Status124),
    id = 3560
    names = ['Iron Jaws(BRD)', '伶牙俐齿(BRD)']
    _orig_names = ['伶牙俐齿', 'Iron Jaws']
    damage = 100


class Action3561(Action):
    # 解除一名队员身上部分弱化效果中的一种
    # 如果未能触发该效果，则为该队员张开防护罩
    # 防护罩可免疫一次目标所受到的部分弱化效果中的一种
    # 持续时间：30秒
    # Removes one select detrimental effect from self or target party member. If the target is not enfeebled, a barrier is created nullifying the target's next detrimental effect suffered.
    # Duration: 30s
    # related: [光阴神的礼赞凯歌](Status866),
    id = 3561
    names = ["the Warden's Paean(BRD)", '光阴神的礼赞凯歌(BRD)']
    _orig_names = ['光阴神的礼赞凯歌', "the Warden's Paean"]


class Action3562(Action):
    # 对目标发动物理攻击
    # 威力：300
    # Delivers an attack with a potency of 300.
    id = 3562
    names = ['Sidewinder(BRD)', '侧风诱导箭(BRD)']
    _orig_names = ['Sidewinder', '侧风诱导箭']
    damage = 300


class Action7404(Action):
    # 对目标发动物理攻击
    # 根据自身附加的诗心档数给与相应伤害
    # 诗心1档时威力：100
    # 诗心2档时威力：220
    # 诗心3档时威力：360
    # 发动条件：放浪神的小步舞曲状态中且诗心1档以上
    # Delivers an attack to the target. Potency varies with number of Repertoire stacks.
    # 1 Repertoire Stack: 100
    # 2 Repertoire Stacks: 220
    # 3 Repertoire Stacks: 360
    # Can only be executed when the Wanderer's Minuet is active.
    # related: [放浪神的小步舞曲(2)](Status2216), [放浪神的小步舞曲(0)](Status865), [放浪神的小步舞曲(1)](Status2215),
    id = 7404
    names = ['Pitch Perfect(BRD)', '完美音调(BRD)']
    _orig_names = ['Pitch Perfect', '完美音调']
    damage = 100  # TODO: [100, 360, 220]


class Action7405(Action):
    # 一定时间内，令自身和周围队员所受到的伤害减轻10%
    # 持续时间：15秒
    # 无法与机工士的策动、舞者的防守之桑巴效果共存
    # Reduces damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # Effect cannot be stacked with machinist's Tactician or dancer's Shield Samba.
    # related: [策动(0)](Status2177), [防守之桑巴](Status1826), [策动(1)](Status1197), [行吟](Status1934), [策动(2)](Status1951),
    id = 7405
    names = ['行吟(BRD)', 'Troubadour(BRD)']
    _orig_names = ['行吟', 'Troubadour']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action7406(Action):
    # 对目标发动物理攻击
    # 威力：150
    # 追加效果：中毒
    # 威力：20
    # 持续时间：45秒(job==23?(level>=76?
    # 追加效果（发动几率35%）：直线射击预备
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of 150.
    # Additional Effect: Poison
    # Potency: 20
    # Duration: 45s(job==23?(level>=76?
    # Additional Effect: 35% chance of becoming Straight Shot Ready
    # Duration: 30s:):)
    # related: [中毒(0)](Status801), [烈毒咬箭(1)](Status1321), [中毒(1)](Status2089), [中毒(2)](Status686), [中毒(3)](Status559), [烈毒咬箭(0)](Status1200), [中毒(4)](Status560), [中毒(5)](Status18), [中毒(6)](Status275), [中毒(7)](Status2104),
    id = 7406
    names = ['Caustic Bite(BRD)', '烈毒咬箭(BRD)']
    _orig_names = ['烈毒咬箭', 'Caustic Bite']
    damage = 150  # TODO: [150, 20]


class Action7407(Action):
    # 对目标发动风属性物理攻击
    # 威力：100
    # 追加效果：风属性持续伤害
    # 威力：25
    # 持续时间：45秒(job==23?(level>=76?
    # 追加效果（发动几率35%）：直线射击预备
    # 持续时间：30秒:):)
    # Deals wind damage with a potency of 100.
    # Additional Effect: Wind damage over time
    # Potency: 25
    # Duration: 45s(job==23?(level>=76?
    # Additional Effect: 35% chance of becoming Straight Shot Ready
    # Duration: 30s:):)
    # related: [狂风蚀箭(0)](Status1201), [狂风蚀箭(1)](Status1322),
    id = 7407
    names = ['Stormbite(BRD)', '狂风蚀箭(BRD)']
    _orig_names = ['狂风蚀箭', 'Stormbite']
    damage = 100
    # remain metas: {'dmg_ot': '25'}


class Action7408(Action):
    # 令自身或其他一名队员所受的体力恢复效果提高20%
    # 持续时间：15秒
    # Increases HP recovery via healing actions for a party member or self by 20%.
    # Duration: 15s
    # related: [大地神的抒情恋歌(0)](Status1202), [大地神的抒情恋歌(1)](Status2178),
    id = 7408
    names = ["Nature's Minne(BRD)", '大地神的抒情恋歌(BRD)']
    _orig_names = ["Nature's Minne", '大地神的抒情恋歌']


class Action7409(Action):
    # 对目标发动物理攻击
    # 威力：280
    # 发动条件：直线射击预备状态中
    # Delivers an attack with a potency of 280.
    # Can only be executed when Straight Shot Ready.
    # related: [直线射击预备](Status122),
    id = 7409
    names = ['Refulgent Arrow(BRD)', '辉煌箭(BRD)']
    _orig_names = ['Refulgent Arrow', '辉煌箭']
    damage = 280


class Action8838(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # “放浪神的小步舞曲”与“军神的赞美歌”状态中追加效果：
    # 自身获得诗心，同时获得10点灵魂之声
    # 积蓄次数：2
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Grants Repertoire if under the effect of the Wanderer's Minuet or Army's Paeon
    # Additional Effect: Increases Soul Voice Gauge by 10 if under the effect of the Wanderer's Minuet or Army's Paeon
    # Maximum Charges: 2
    # related: [军神的赞美歌(2)](Status2218), [军神的赞美歌(1)](Status137), [军神的赞美歌(3)](Status138), [军神的赞美歌(0)](Status2214),
    id = 8838
    names = ['Empyreal Arrow(pvp)(BRD)', '九天连箭(pvp)(BRD)']
    _orig_names = ['九天连箭(pvp)', 'Empyreal Arrow(pvp)']
    damage = 1000


class Action8839(Action):
    # 对目标发动物理攻击同时后跳10米
    # 威力：800
    # “放浪神的小步舞曲”与“军神的赞美歌”状态中追加效果：
    # 自身获得诗心，同时获得20点灵魂之声
    # 止步状态下无法发动
    # Delivers an attack with a potency of 800.
    # Additional Effect: 10-yalm backstep
    # Additional Effect: Grants Repertoire if under the effect of the Wanderer's Minuet or Army's Paeon
    # Additional Effect: Increases Soul Voice Gauge by 20 if under the effect of the Wanderer's Minuet or Army's Paeon
    # Cannot be executed while bound.
    # related: [后跃射击](Status2017), [军神的赞美歌(0)](Status2214), [军神的赞美歌(3)](Status138), [军神的赞美歌(1)](Status137), [军神的赞美歌(2)](Status2218),
    id = 8839
    names = ['后跃射击(pvp)(BRD)', 'Repelling Shot(pvp)(BRD)']
    _orig_names = ['Repelling Shot(pvp)', '后跃射击(pvp)']
    damage = 800


class Action8841(Action):
    # 对目标发动物理攻击
    # 威力：800～2400
    # 目标剩余体力越低威力越大
    # Delivers an attack with a potency of 800.
    # Potency increases up to 2,400 as the target's HP decreases.
    id = 8841
    names = ['侧风诱导箭(pvp)(BRD)', 'Sidewinder(pvp)(BRD)']
    _orig_names = ['侧风诱导箭(pvp)', 'Sidewinder(pvp)']
    damage = [800, 2400]


class Action8842(Action):
    # 对目标发动物理攻击
    # 根据自身附加的诗心档数给与相应伤害
    # 诗心1档时威力：600
    # 诗心2档时威力：1200
    # 诗心3档时威力：1800
    # 发动条件：放浪神的小步舞曲加诗心1档以上
    # ※该技能无法设置到热键栏
    # Delivers an attack whose potency increases based on your stacks of Repertoire.
    # Repertoire 1 Potency: 600
    # Repertoire 2 Potency: 1,200
    # Repertoire 3 Potency: 1,800
    # Can only be executed when the Wanderer's Minuet is active.
    id = 8842
    names = ['Pitch Perfect(pvp)(BRD)', '完美音调(pvp)(BRD)']
    _orig_names = ['完美音调(pvp)', 'Pitch Perfect(pvp)']
    damage = 600  # TODO: [600, 1800, 1200]


class Action8843(Action):
    # 对目标发动魔法攻击
    # 威力：600
    # 追加效果：对自身附加放浪神的小步舞曲状态
    # 持续时间：30秒
    # 放浪神的小步舞曲效果：令周围30米内的队员攻击伤害提高5%
    # 放浪神的小步舞曲状态中诗心效果：
    # 可发动完美音调
    # 最多积累3档
    # Deals unaspected damage with a potency of 600.
    # Additional Effect: Grants the Wanderer's Minuet, increasing damage dealt by all party members within a radius of 30 yalms by 5%
    # Duration: 30s
    # Repertoire Effect: Allows execution of Pitch Perfect while under the effect of the Wanderer's Minuet
    # Can be stacked up to 3 times.
    # related: [放浪神的小步舞曲(0)](Status865), [放浪神的小步舞曲(1)](Status2215), [放浪神的小步舞曲(2)](Status2216),
    id = 8843
    names = ["The Wanderer's Minuet(pvp)(BRD)", '放浪神的小步舞曲(pvp)(BRD)']
    _orig_names = ["The Wanderer's Minuet(pvp)", '放浪神的小步舞曲(pvp)']
    damage = 600
    # remain metas: {'dmg_increase': '5%'}


class Action8844(Action):
    # 对目标发动魔法攻击
    # 威力：600
    # 追加效果：对自身附加军神的赞美歌状态
    # 持续时间：30秒
    # 军神的赞美歌效果：令周围30米内的队员战技与魔法的咏唱及复唱时间缩短5%
    # 军神的赞美歌状态中诗心效果：
    # 自身战技的复唱时间缩短5%
    # 最多积累4档
    # Deals unaspected damage with a potency of 600.
    # Additional Effect: Grants Army's Paeon, reducing weaponskill cast time and recast time, as well as spell cast time and recast time of all party members within a radius of 30 yalms by 5%
    # Duration: 30s
    # Repertoire Effect: Reduces weaponskill cast time and recast time by 5%
    # Can be stacked up to 4 times.
    # related: [军神的赞美歌(0)](Status2214), [军神的赞美歌(1)](Status137), [军神的赞美歌(2)](Status2218), [军神的赞美歌(3)](Status138),
    id = 8844
    names = ['军神的赞美歌(pvp)(BRD)', "Army's Paeon(pvp)(BRD)"]
    _orig_names = ['军神的赞美歌(pvp)', "Army's Paeon(pvp)"]
    damage = 600


class Action16494(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：170
    # 纷乱箭状态中威力：270
    # 发动条件：影噬箭预备状态中
    # Delivers an attack with a potency of 170 to target and all enemies nearby it.
    # Barrage Potency: 270
    # Can only be executed when Shadowbite Ready.
    # related: [纷乱箭(0)](Status128), [影噬箭预备](Status3002), [纷乱箭(1)](Status1407),
    id = 16494
    names = ['影噬箭(BRD)', 'Shadowbite(BRD)']
    _orig_names = ['Shadowbite', '影噬箭']
    damage = "(纷乱箭状态?270:170)"


class Action16495(Action):
    # 对目标发动物理攻击
    # 威力：220
    # 追加效果（发动几率35%）：直线射击预备
    # 持续时间：30秒
    # Delivers an attack with a potency of 220.
    # Additional Effect: 35% chance of becoming Straight Shot Ready
    # Duration: 30s
    id = 16495
    names = ['Burst Shot(BRD)', '爆发射击(BRD)']
    _orig_names = ['Burst Shot', '爆发射击']
    damage = 220


class Action16496(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：100～500
    # 发动时会消耗全部的灵魂之声
    # 灵魂之声消耗量越高威力越大
    # (job==23?(level>=86?追加效果（灵魂之声消耗量80以上时）：爆破箭预备
    # 持续时间：10秒
    # :):)发动条件：灵魂之声20点以上
    # Delivers an attack with a potency of 100 to all enemies in a straight line before you.
    # Soul Voice Gauge Cost: 20
    # Potency increases up to 500 as Soul Voice Gauge exceeds minimum cost.
    # (job==23?(level>=86?Additional Effect: Grants Blast Arrow Ready upon execution while Soul Voice Gauge is 80 or higher
    # Duration: 10s
    # :):)Consumes Soul Voice Gauge upon execution.(job==23?(level>=86?
    # ※Action changes to Blast Arrow while under the effect of Blast Arrow Ready.:):)
    id = 16496
    names = ['绝峰箭(BRD)', 'Apex Arrow(BRD)']
    _orig_names = ['绝峰箭', 'Apex Arrow']
    damage = [100, 500]


class Action17745(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # “放浪神的小步舞曲”与“军神的赞美歌”状态中追加效果：
    # 自身获得诗心，同时获得10点灵魂之声
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Grants Repertoire if under the effect of the Wanderer's Minuet or Army's Paeon
    # Additional Effect: Increases Soul Voice Gauge by 10 if under the effect of the Wanderer's Minuet or Army's Paeon
    # related: [军神的赞美歌(2)](Status2218), [军神的赞美歌(1)](Status137), [军神的赞美歌(3)](Status138), [军神的赞美歌(0)](Status2214),
    id = 17745
    names = ['爆发射击(pvp)(BRD)', 'Burst Shot(pvp)(BRD)']
    _orig_names = ['Burst Shot(pvp)', '爆发射击(pvp)']
    damage = 1200


class Action17747(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：1200～2400
    # 发动时会消耗全部的灵魂之声
    # 灵魂之声消耗量越高威力越大
    # 发动条件：灵魂之声50点以上
    # Delivers an attack with a potency of 1,200 to all enemies in a straight line before you.
    # Soul Voice Gauge Cost: 50
    # Potency increases up to 2,400 as Soul Voice Gauge exceeds minimum cost.
    # Consumes Soul Voice Gauge upon execution.
    id = 17747
    names = ['绝峰箭(pvp)(BRD)', 'Apex Arrow(pvp)(BRD)']
    _orig_names = ['Apex Arrow(pvp)', '绝峰箭(pvp)']
    damage = [1200, 2400]


class Action18930(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：800
    # “放浪神的小步舞曲”及“军神的赞美歌”中追加效果：每命中一个目标获得10点灵魂之声
    # Delivers an attack with a potency of 800 to all enemies in a cone before you.
    # Additional Effect: Increases Soul Voice Gauge by 10 for each enemy hit while under the effect of the Wanderer's Minuet or Army's Paeon
    id = 18930
    names = ['Quick Nock(pvp)(BRD)', '连珠箭(pvp)(BRD)']
    _orig_names = ['连珠箭(pvp)', 'Quick Nock(pvp)']
    damage = 800


class Action18931(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：600～1800
    # 目标剩余的体力越多威力越大
    # Delivers an attack with a potency of 600 to target and all enemies nearby it.
    # Potency increases up to 1,800 as target's HP nears maximum.
    id = 18931
    names = ['影噬箭(pvp)(BRD)', 'Shadowbite(pvp)(BRD)']
    _orig_names = ['影噬箭(pvp)', 'Shadowbite(pvp)']
    damage = [600, 1800]


class Action19071(Action):
    # 令自身或其他一名队员受到的伤害减轻10%，并且所受的体力恢复效果提高10%
    # 持续时间：15秒
    # Reduces damage taken by self or target party member by 10%, while increasing HP recovered by healing actions by 10%.
    # Duration: 15s
    # related: [大地神的抒情恋歌(0)](Status1202), [大地神的抒情恋歌(1)](Status2178),
    id = 19071
    names = ['大地神的抒情恋歌(pvp)(BRD)', "Nature's Minne(pvp)(BRD)"]
    _orig_names = ["Nature's Minne(pvp)", '大地神的抒情恋歌(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%，并且所受的体力恢复效果提高10%'}


class Action25783(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：130
    # 追加效果（发动几率35%）：影噬箭预备
    # 持续时间：30秒
    # Delivers an attack with a potency of 130 to all enemies in a cone before you.
    # Additional Effect: 35% chance of becoming Shadowbite Ready
    # Duration: 30s
    id = 25783
    names = ['Ladonsbite(BRD)', '百首龙牙箭(BRD)']
    _orig_names = ['百首龙牙箭', 'Ladonsbite']
    damage = 130


class Action25784(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：爆破箭预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack to all enemies in a straight line before you with a potency of 600 for the first enemy, and 60% less for all remaining enemies.
    # Can only be executed while under the effect of Blast Arrow Ready.
    # ※This action cannot be assigned to a hotbar.
    # related: [爆破箭预备](Status2692),
    id = 25784
    names = ['Blast Arrow(BRD)', '爆破箭(BRD)']
    _orig_names = ['Blast Arrow', '爆破箭']
    damage = 600
    # remain metas: {'aoe_reduce': '60%'}


class Action25785(Action):
    # 一定时间内，自身与周围队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 该技能的效果量根据自身附加的尾声标识的种类数发生变化
    # 1种尾声标识时：2%
    # 2种尾声标识时：4%
    # 3种尾声标识时：6%
    # 发动条件：尾声标识1种以上
    # Increases damage dealt by self and nearby party members.
    # Duration: 15s
    # Effectiveness is determined by the number of different Coda active in the Song Gauge.
    # 1 Coda: 2%
    # 2 Coda: 4%
    # 3 Coda: 6%
    # Can only be executed when at least 1 coda is active.
    # related: [光明神的最终乐章(0)](Status2722), [光明神的最终乐章(1)](Status2964),
    id = 25785
    names = ['光明神的最终乐章(BRD)', 'Radiant Finale(BRD)']
    _orig_names = ['光明神的最终乐章', 'Radiant Finale']
    # remain metas: {'dmg_increase': ''}
