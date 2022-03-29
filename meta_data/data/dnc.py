from ._base import *


class Status2693(Status):
    # 可以发动逆瀑泻或升风车
    # Able to execute Reverse Cascade or Rising Windmill.
    # related: [逆瀑泻(DNC)](Action15991), [升风车(DNC)](Action15995), [百花争艳(DNC)](Action16013),
    id = 2693
    names = ['对称投掷', 'Flourishing Symmetry']


class Status2694(Status):
    # 可以发动坠喷泉或落血雨
    # Able to execute Fountainfall or Bloodshower.
    # related: [坠喷泉(DNC)](Action15992), [落血雨(DNC)](Action15996), [百花争艳(DNC)](Action16013),
    id = 2694
    names = ['非对称投掷', 'Flourishing Flow']


class Status1818(Status):
    # 进入了跳舞模式。无法发动舞步技能和标准舞步结束、前冲步、职能技能、冲刺、极限技以外的技能
    # Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, Standard Finish, and En Avant.
    # related: [标准舞步(DNC)](Action15997), [标准舞步(pvp)(DNC)](Action17766),
    id = 1818
    names = ['标准舞步', 'Standard Step']


# class Status2023(Status):
#     # 进入了跳舞模式。无法发动舞步技能和标准舞步结束、前冲步、伤头、疾跑、军用恢复药、额外技能以外的技能
#     # Caught up in the dance and only able to execute step actions, additional actions, Head Graze, Bolt, Medical Kit, Standard Finish, and En Avant.
#     # related: [标准舞步(DNC)](Action15997), [标准舞步(pvp)(DNC)](Action17766),
#     id = 2023
#     names = ['标准舞步(1)', 'Standard Step(1)']


# class Status2049(Status):
#     # 进入了跳舞模式。无法发动舞步技能和技巧舞步结束、前冲步、伤头、疾跑、军用恢复药、额外技能以外的技能
#     # Caught up in the dance and only able to execute step actions, additional actions, Technical Finish, En Avant, Head Graze, Bolt, and Medical Kit.
#     # related: [技巧舞步(DNC)](Action15998), [技巧舞步(pvp)(DNC)](Action17824),
#     id = 2049
#     names = ['技巧舞步(0)', 'Technical Step(0)']


class Status1819(Status):
    # 进入了跳舞模式。无法发动舞步技能和技巧舞步结束、前冲步、职能技能、冲刺、极限技以外的技能
    # Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, Technical Finish, and En Avant.
    # related: [技巧舞步(DNC)](Action15998), [技巧舞步(pvp)(DNC)](Action17824),
    id = 1819
    names = ['技巧舞步', 'Technical Step']


class Status1824(Status):
    # 附加此效果的舞者发动了特定技能时，会对自身发动追加效果
    # Sharing the effects of certain actions executed by your dancer companion.
    # related: [标准舞步结束(DNC)](Action16003), [闭式舞姿(DNC)](Action16006), [进攻之探戈(DNC)](Action16011), [治疗之华尔兹(DNC)](Action16015), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [剑舞(pvp)(DNC)](Action17760), [扇舞·急(pvp)(DNC)](Action17762), [治疗之华尔兹(pvp)(DNC)](Action17763), [闭式舞姿(pvp)(DNC)](Action17765), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [提拉纳(DNC)](Action25790),
    id = 1824
    names = ['舞伴', 'Dance Partner']


# class Status2113(Status):
#     # 战技与魔法的咏唱及复唱时间缩短
#     # Weaponskill and spell cast and recast time are reduced.
#     # related: [标准舞步结束(DNC)](Action16003), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [标准舞步结束(pvp)(DNC)](Action17771), [提拉纳(DNC)](Action25790),
#     id = 2113
#     names = ['标准舞步结束(0)', 'Standard Finish(0)']


class Status2051(Status):
    # 附加此效果的舞者或小队成员发动战技或魔法攻击命中时，舞者获得伶俐
    # The Esprit Gauge is increasing when you or a party member executes a weaponskill or casts a spell.
    # related: [标准舞步结束(DNC)](Action16003), [技巧舞步结束(DNC)](Action16004), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [瀑泻(pvp)(DNC)](Action17756), [逆瀑泻(pvp)(DNC)](Action17758), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [技巧舞步结束(pvp)(DNC)](Action17825), [单色技巧舞步结束(pvp)(DNC)](Action17826), [双色技巧舞步结束(pvp)(DNC)](Action17827), [三色技巧舞步结束(pvp)(DNC)](Action17828), [四色技巧舞步结束(pvp)(DNC)](Action17829), [风车(pvp)(DNC)](Action18993), [升风车(pvp)(DNC)](Action18995), [提拉纳(DNC)](Action25790),
    id = 2051
    names = ['伶俐(0)', 'Esprit(0)']


# class Status2024(Status):
#     # 战技与魔法的咏唱及复唱时间缩短
#     # Weaponskill and spell cast and recast time are reduced.
#     # related: [标准舞步结束(DNC)](Action16003), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [标准舞步结束(pvp)(DNC)](Action17771), [提拉纳(DNC)](Action25790),
#     id = 2024
#     names = ['标准舞步结束(1)', 'Standard Finish(1)']


class Status2025(Status):
    # 附加此效果的舞者或被指定为舞伴的队员发动战技或魔法攻击命中时，舞者获得伶俐
    # The Esprit Gauge is increasing when you or the party member designated as your Dance Partner executes a weaponskill or casts a spell.
    # related: [标准舞步结束(DNC)](Action16003), [技巧舞步结束(DNC)](Action16004), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [瀑泻(pvp)(DNC)](Action17756), [逆瀑泻(pvp)(DNC)](Action17758), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [技巧舞步结束(pvp)(DNC)](Action17825), [单色技巧舞步结束(pvp)(DNC)](Action17826), [双色技巧舞步结束(pvp)(DNC)](Action17827), [三色技巧舞步结束(pvp)(DNC)](Action17828), [四色技巧舞步结束(pvp)(DNC)](Action17829), [风车(pvp)(DNC)](Action18993), [升风车(pvp)(DNC)](Action18995), [提拉纳(DNC)](Action25790),
    id = 2025
    names = ['伶俐(1)', 'Esprit(1)']


# class Status2027(Status):
#     # 附加此效果的舞者发动了特定技能时，会对自身发动追加效果
#     # Sharing the effects of certain actions executed by your dancer companion.
#     # related: [标准舞步结束(DNC)](Action16003), [闭式舞姿(DNC)](Action16006), [进攻之探戈(DNC)](Action16011), [治疗之华尔兹(DNC)](Action16015), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [剑舞(pvp)(DNC)](Action17760), [扇舞·急(pvp)(DNC)](Action17762), [治疗之华尔兹(pvp)(DNC)](Action17763), [闭式舞姿(pvp)(DNC)](Action17765), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [提拉纳(DNC)](Action25790),
#     id = 2027
#     names = ['舞伴(1)', 'Dance Partner(1)']


class Status1847(Status):
    # 附加此效果的舞者或被指定为舞伴的队员发动战技或魔法攻击命中时，舞者获得伶俐
    # The Esprit Gauge is increasing when you or the party member designated as your Dance Partner executes a weaponskill or casts a spell.
    # related: [标准舞步结束(DNC)](Action16003), [技巧舞步结束(DNC)](Action16004), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [瀑泻(pvp)(DNC)](Action17756), [逆瀑泻(pvp)(DNC)](Action17758), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [技巧舞步结束(pvp)(DNC)](Action17825), [单色技巧舞步结束(pvp)(DNC)](Action17826), [双色技巧舞步结束(pvp)(DNC)](Action17827), [三色技巧舞步结束(pvp)(DNC)](Action17828), [四色技巧舞步结束(pvp)(DNC)](Action17829), [风车(pvp)(DNC)](Action18993), [升风车(pvp)(DNC)](Action18995), [提拉纳(DNC)](Action25790),
    id = 1847
    names = ['伶俐(2)', 'Esprit(2)']


class Status1848(Status):
    # 附加此效果的舞者或小队成员发动战技或魔法攻击命中时，舞者获得伶俐
    # The Esprit Gauge is increasing when you or a party member executes a weaponskill or casts a spell.
    # related: [标准舞步结束(DNC)](Action16003), [技巧舞步结束(DNC)](Action16004), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [瀑泻(pvp)(DNC)](Action17756), [逆瀑泻(pvp)(DNC)](Action17758), [标准舞步结束(pvp)(DNC)](Action17771), [单色标准舞步结束(pvp)(DNC)](Action17772), [双色标准舞步结束(pvp)(DNC)](Action17773), [技巧舞步结束(pvp)(DNC)](Action17825), [单色技巧舞步结束(pvp)(DNC)](Action17826), [双色技巧舞步结束(pvp)(DNC)](Action17827), [三色技巧舞步结束(pvp)(DNC)](Action17828), [四色技巧舞步结束(pvp)(DNC)](Action17829), [风车(pvp)(DNC)](Action18993), [升风车(pvp)(DNC)](Action18995), [提拉纳(DNC)](Action25790),
    id = 1848
    names = ['伶俐(3)', 'Esprit(3)']


# class Status2105(Status):
#     # 攻击所造成的伤害提高
#     # Damage dealt is increased.
#     # related: [标准舞步结束(DNC)](Action16003), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [标准舞步结束(pvp)(DNC)](Action17771), [提拉纳(DNC)](Action25790),
#     id = 2105
#     names = ['标准舞步结束(2)', 'Standard Finish(2)']


class Status1821(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [标准舞步结束(DNC)](Action16003), [单色标准舞步结束(DNC)](Action16191), [双色标准舞步结束(DNC)](Action16192), [标准舞步结束(pvp)(DNC)](Action17771), [提拉纳(DNC)](Action25790),
    id = 1821
    names = ['标准舞步结束', 'Standard Finish']


# class Status2050(Status):
#     # 战技与魔法的咏唱及复唱时间缩短
#     # Weaponskill and spell cast and recast time are reduced.
#     # related: [技巧舞步结束(DNC)](Action16004), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [技巧舞步结束(pvp)(DNC)](Action17825),
#     id = 2050
#     names = ['技巧舞步结束(0)', 'Technical Finish(0)']


class Status1822(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [技巧舞步结束(DNC)](Action16004), [单色技巧舞步结束(DNC)](Action16193), [双色技巧舞步结束(DNC)](Action16194), [三色技巧舞步结束(DNC)](Action16195), [四色技巧舞步结束(DNC)](Action16196), [技巧舞步结束(pvp)(DNC)](Action17825),
    id = 1822
    names = ['技巧舞步结束', 'Technical Finish(1)']


class Status2022(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [剑舞(DNC)](Action16005), [剑舞(pvp)(DNC)](Action17760),
    id = 2022
    names = ['剑舞', 'Saber Dance']


# class Status2026(Status):
#     # 使用部分技能时，对指定队员发动追加效果
#     # Sharing the effects of certain actions with target party member.
#     # related: [闭式舞姿(DNC)](Action16006), [闭式舞姿(pvp)(DNC)](Action17765), [解除闭式舞姿(DNC)](Action18073), [解除闭式舞姿(pvp)(DNC)](Action18076),
#     id = 2026
#     names = ['闭式舞姿(0)', 'Closed Position(0)']


class Status1823(Status):
    # 使用部分技能时，对指定队员发动追加效果
    # Sharing the effects of certain actions with target party member.
    # related: [闭式舞姿(DNC)](Action16006), [闭式舞姿(pvp)(DNC)](Action17765), [解除闭式舞姿(DNC)](Action18073), [解除闭式舞姿(pvp)(DNC)](Action18076),
    id = 1823
    names = ['闭式舞姿', 'Closed Position']


# class Status2021(Status):
#     # 可以发动扇舞·急
#     # Able to execute Fan Dance III.
#     # related: [扇舞·急(DNC)](Action16009), [扇舞·序(pvp)(DNC)](Action17761), [扇舞·破(pvp)(DNC)](Action18997),
#     id = 2021
#     names = ['扇舞·急预备(0)', 'Flourishing Fan Dance']


class Status2052(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [扇舞·急(DNC)](Action16009), [扇舞·急(pvp)(DNC)](Action17762),
    id = 2052
    names = ['扇舞·急', 'Fan Dance III']


class Status1820(Status):
    # 可以发动扇舞·急
    # Able to execute Fan Dance III.
    # related: [扇舞·急(DNC)](Action16009), [扇舞·序(pvp)(DNC)](Action17761), [扇舞·破(pvp)(DNC)](Action18997),
    id = 1820
    names = ['扇舞·急预备', 'Threefold Fan Dance']


class Status2048(Status):
    # 瀑泻变为逆瀑泻，喷泉变为坠喷泉，风车变为升风车，落刃雨变为落血雨
    # Cascade is upgraded to Reverse Cascade, Fountain is upgraded to Fountainfall, Windmill is upgraded to Rising Windmill, and Bladeshower is upgraded to Bloodshower.
    # related: [前冲步(DNC)](Action16010), [瀑泻(pvp)(DNC)](Action17756), [喷泉(pvp)(DNC)](Action17757), [逆瀑泻(pvp)(DNC)](Action17758), [坠喷泉(pvp)(DNC)](Action17759), [前冲步(pvp)(DNC)](Action17764), [风车(pvp)(DNC)](Action18993), [落刃雨(pvp)(DNC)](Action18994), [升风车(pvp)(DNC)](Action18995), [落血雨(pvp)(DNC)](Action18996),
    id = 2048
    names = ['前冲步', 'En Avant']


class Status1825(Status):
    # 暴击发动率和直击发动率提高
    # Critical hit rate and direct hit rate are increased.
    # related: [进攻之探戈(DNC)](Action16011),
    id = 1825
    names = ['进攻之探戈', 'Devilment']


class Status1827(Status):
    # 即兴跳舞
    # Dancing to the beat of your own drum.
    # related: [即兴表演(DNC)](Action16014), [即兴表演结束(DNC)](Action25789),
    id = 1827
    names = ['即兴表演', 'Improvisation(self)']


# class Status1828(Status):
#     # 自身所受的治疗效果提高
#     # Healing magic potency is increased.
#     # related: [即兴表演(DNC)](Action16014),
#     id = 1828
#     names = ['享受即兴表演(0)', 'Improvisation(1)']


class Status2695(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [即兴表演(DNC)](Action16014),
    id = 2695
    names = ['享受即兴表演(队伍)', 'Improvisation(party)']


class Status2696(Status):
    # 即兴表演结束效果提高
    # Potency of Improvised Finish is increased.
    # related: [即兴表演(DNC)](Action16014),
    id = 2696
    names = ['舞动的热情', 'Rising Rhythm']


class Status2697(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [即兴表演结束(DNC)](Action25789),
    id = 2697
    names = ['即兴表演结束', 'Improvised Finish']


class Status2698(Status):
    # 可以发动提拉纳
    # Able to execute Tillana.
    # related: [提拉纳(DNC)](Action25790),
    id = 2698
    names = ['提拉纳预备', 'Flourishing Finish']


class Status2699(Status):
    # 可以发动扇舞·终
    # Able to execute Fan Dance IV.
    # related: [扇舞·终(DNC)](Action25791),
    id = 2699
    names = ['扇舞·终', 'Fourfold Fan Dance']


class Status2700(Status):
    # 可以发动流星舞
    # Able to execute Starfall Dance.
    # related: [流星舞(DNC)](Action25792),
    id = 2700
    names = ['流星舞预备', 'Flourishing Starfall']


class Action15989(Action):
    # 对目标发动物理攻击
    # 威力：220
    # 追加效果（发动几率50%）：对称投掷
    # 持续时间：30秒
    # 跳舞模式中该技能变为蔷薇曲脚步
    # Delivers an attack with a potency of 220.
    # Additional Effect: 50% chance of granting Flourishing Symmetry
    # Duration: 30s
    # ※Action changes to Emboite while dancing.
    id = 15989
    names = ['瀑泻(DNC)', 'Cascade(DNC)']
    _orig_names = ['Cascade', '瀑泻']
    damage = 220


class Action15990(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：瀑泻
    # 连击中威力：280
    # 连击成功（发动几率50%）：非对称投掷
    # 持续时间：30秒
    # 跳舞模式中该技能变为小鸟交叠跳
    # Delivers an attack with a potency of 100.
    # Combo Action: Cascade
    # Combo Potency: 280
    # Combo Bonus: 50% chance of granting Flourishing Flow
    # Duration: 30s
    # ※Action changes to Entrechat while dancing.
    id = 15990
    names = ['Fountain(DNC)', '喷泉(DNC)']
    _orig_names = ['喷泉', 'Fountain']
    combo_action = 15989
    damage = 100
    combo_damage = 280


class Action15991(Action):
    # 对目标发动物理攻击
    # 威力：280
    # (job==38?(level>=30?追加效果（发动几率50%）：幻扇
    # :):)发动条件：对称投掷状态中
    # 跳舞模式中该技能变为绿叶小踢腿
    # Delivers an attack with a potency of 280.
    # (job==38?(level>=30?Additional Effect: 50% chance of granting a Fourfold Feather
    # :):)Can only be executed while under the effect of Flourishing Symmetry.
    # ※Action changes to Jete while dancing.
    # related: [对称投掷](Status2693),
    id = 15991
    names = ['逆瀑泻(DNC)', 'Reverse Cascade(DNC)']
    _orig_names = ['逆瀑泻', 'Reverse Cascade']
    damage = 280


class Action15992(Action):
    # 对目标发动物理攻击
    # 威力：340
    # 追加效果（发动几率50%）：幻扇
    # 发动条件：非对称投掷状态中
    # 跳舞模式中该技能变为金冠趾尖转
    # Delivers an attack with a potency of 340.
    # Additional Effect: 50% chance of granting a Fourfold Feather
    # Can only be executed while under the effect of Flourishing Flow.
    # ※Action changes to Pirouette while dancing.
    # related: [非对称投掷](Status2694),
    id = 15992
    names = ['坠喷泉(DNC)', 'Fountainfall(DNC)']
    _orig_names = ['坠喷泉', 'Fountainfall']
    damage = 340


class Action15993(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 追加效果（发动几率50%）：对称投掷
    # 持续时间：30秒
    # 跳舞模式中该技能变为蔷薇曲脚步
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Additional Effect: 50% chance of granting Flourishing Symmetry
    # Duration: 30s
    # ※Action changes to Emboite while dancing.
    id = 15993
    names = ['风车(DNC)', 'Windmill(DNC)']
    _orig_names = ['风车', 'Windmill']
    damage = 100


class Action15994(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：风车
    # 连击中威力：140
    # 连击成功（发动几率50%）：非对称投掷
    # 持续时间：30秒
    # 跳舞模式中该技能变为小鸟交叠跳
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: Windmill
    # Combo Potency: 140
    # Combo Bonus: 50% chance of granting Flourishing Flow
    # Duration: 30s
    # ※Action changes to Entrechat while dancing.
    id = 15994
    names = ['Bladeshower(DNC)', '落刃雨(DNC)']
    _orig_names = ['落刃雨', 'Bladeshower']
    combo_action = 15993
    damage = 100
    combo_damage = 140


class Action15995(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：140
    # 追加效果（发动几率50%）：幻扇
    # 发动条件：对称投掷状态中
    # 跳舞模式中该技能变为绿叶小踢腿
    # Delivers an attack with a potency of 140 to all nearby enemies.
    # Additional Effect: 50% chance of granting a Fourfold Feather
    # Can only be executed while under the effect of Flourishing Symmetry.
    # ※Action changes to Jete while dancing.
    # related: [对称投掷](Status2693),
    id = 15995
    names = ['Rising Windmill(DNC)', '升风车(DNC)']
    _orig_names = ['Rising Windmill', '升风车']
    damage = 140


class Action15996(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：180
    # 追加效果（发动几率50%）：幻扇
    # 发动条件：非对称投掷状态中
    # 跳舞模式中该技能变为金冠趾尖转
    # Delivers an attack with a potency of 180 to all nearby enemies.
    # Additional Effect: 50% chance of granting a Fourfold Feather
    # Can only be executed while under the effect of Flourishing Flow.
    # ※Action changes to Pirouette while dancing.
    # related: [非对称投掷](Status2694),
    id = 15996
    names = ['Bloodshower(DNC)', '落血雨(DNC)']
    _orig_names = ['落血雨', 'Bloodshower']
    damage = 180


class Action15997(Action):
    # 进入跳舞模式，对自身附加标准舞步状态
    # 持续时间：15秒
    # 跳舞模式中该技能变为标准舞步结束
    # 此时只能使用舞步技能、标准舞步结束、前冲步、职能技能、冲刺和极限技
    # 此战技的复唱时间不受装备和状态的影响
    # Begin dancing, granting yourself Standard Step.
    # Duration: 15s
    # Action changes to Standard Finish while dancing.
    # Only Standard Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing.
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # related: [标准舞步(0)](Status1818), [标准舞步(1)](Status2023),
    id = 15997
    names = ['Standard Step(DNC)', '标准舞步(DNC)']
    _orig_names = ['Standard Step', '标准舞步']


class Action15998(Action):
    # 进入跳舞模式，对自身附加技巧舞步状态
    # 持续时间：15秒
    # 跳舞模式中该技能变为技巧舞步结束
    # 此时只能使用舞步技能、技巧舞步结束、前冲步、职能技能、冲刺和极限技
    # 此战技的复唱时间不受装备和状态的影响
    # Begin dancing, granting yourself Technical Step.
    # Duration: 15s
    # Action changes to Technical Finish while dancing.
    # Only Technical Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing.
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # related: [技巧舞步(0)](Status2049), [技巧舞步(1)](Status1819),
    id = 15998
    names = ['技巧舞步(DNC)', 'Technical Step(DNC)']
    _orig_names = ['技巧舞步', 'Technical Step']


class Action15999(Action):
    # 发动蔷薇曲脚步舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Perform an emboite.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 15999
    names = ['蔷薇曲脚步(DNC)', 'Emboite(DNC)']
    _orig_names = ['Emboite', '蔷薇曲脚步']


class Action16000(Action):
    # 发动小鸟交叠跳舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Perform an entrechat.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 16000
    names = ['小鸟交叠跳(DNC)', 'Entrechat(DNC)']
    _orig_names = ['小鸟交叠跳', 'Entrechat']


class Action16001(Action):
    # 发动绿叶小踢腿舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Perform a jete.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 16001
    names = ['Jete(DNC)', '绿叶小踢腿(DNC)']
    _orig_names = ['绿叶小踢腿', 'Jete']


class Action16002(Action):
    # 发动金冠趾尖转舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Perform a pirouette.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 16002
    names = ['金冠趾尖转(DNC)', 'Pirouette(DNC)']
    _orig_names = ['金冠趾尖转', 'Pirouette']


class Action16003(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束和伶俐状态:舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态):舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态)
    # 持续时间：60秒
    # 该技能的威力与标准舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力360
    # 成功1次时：威力540且效果量为2%
    # 成功2次时：威力720且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 360
    # 1 Step: 540
    # 2 Steps: 720
    # (job==38?(level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
    # Damage bonus of Standard Finish varies with number of successful steps.
    # 1 Step: 2%
    # 2 Steps: 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [标准舞步结束(0)](Status2113), [伶俐(0)](Status2051), [标准舞步结束(1)](Status2024), [伶俐(1)](Status2025), [舞伴(1)](Status2027), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [标准舞步结束(2)](Status2105), [标准舞步结束(3)](Status1821),
    id = 16003
    names = ['标准舞步结束(DNC)', 'Standard Finish(DNC)']
    _orig_names = ['标准舞步结束', 'Standard Finish']


class Action16004(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束和伶俐状态
    # :舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # ):舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # )持续时间：20秒
    # 该技能的威力与技巧舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力350
    # 成功1次时：威力540且效果量为1%
    # 成功2次时：威力720且效果量为2%
    # 成功3次时：威力900且效果量为3%
    # 成功4次时：威力1200且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # (job==38?(level>=82?追加效果：提拉纳预备
    # 持续时间：30秒
    # :):)此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 350
    # 1 Step: 540
    # 2 Steps: 720
    # 3 Steps: 900
    # 4 Steps: 1,200
    # (job==38?(level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
    # Damage bonus of Technical Finish varies with number of successful steps.
    # 1 Step: 1%
    # 2 Steps: 2%
    # 3 Steps: 3%
    # 4 Steps: 5%
    # Duration: 20s
    # Additional Effect: Activates the Esprit Gauge
    # (job==38?(level>=82?Additional Effect: Grants Flourishing Finish
    # Duration: 30s
    # :):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # (job==38?(level>=82?※Action changes to Tillana upon execution.
    # :):)※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 16004
    names = ['Technical Finish(DNC)', '技巧舞步结束(DNC)']
    _orig_names = ['Technical Finish', '技巧舞步结束']


class Action16005(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：480
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：伶俐50点
    # Delivers an attack to target and all enemies nearby it with a potency of 480 for the first enemy, and 50% less for all remaining enemies.
    # Esprit Gauge Cost: 50
    # related: [剑舞](Status2022),
    id = 16005
    names = ['剑舞(DNC)', 'Saber Dance(DNC)']
    _orig_names = ['Saber Dance', '剑舞']
    damage = 480
    # remain metas: {'aoe_reduce': '50%'}


class Action16006(Action):
    # 指定一名队员为目标，对自身附加闭式舞姿状态，对目标附加舞伴状态
    # 在该状态下发动标准舞步结束、进攻之探戈、治疗之华尔兹、提拉纳时，附加舞伴状态的队员也可以获得同样的效果
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Grants you Closed Position and designates a party member as your Dance Partner, allowing you to share the effects of Standard Finish, Curing Waltz, Devilment, and Tillana with said party member.
    # Effect ends upon reuse.
    # related: [舞伴(0)](Status1824), [闭式舞姿(0)](Status2026), [舞伴(1)](Status2027), [闭式舞姿(1)](Status1823),
    id = 16006
    names = ['闭式舞姿(DNC)', 'Closed Position(DNC)']
    _orig_names = ['Closed Position', '闭式舞姿']


class Action16007(Action):
    # 对目标发动物理攻击
    # 威力：150
    # 追加效果（发动几率50%）：扇舞·急预备
    # 持续时间：30秒
    # 发动条件：幻扇
    # Delivers an attack with a potency of 150.
    # Additional Effect: 50% chance of granting Threefold Fan Dance
    # Duration: 30s
    # Can only be executed while in possession of Fourfold Feathers.
    id = 16007
    names = ['扇舞·序(DNC)', 'Fan Dance(DNC)']
    _orig_names = ['扇舞·序', 'Fan Dance']
    damage = 150


class Action16008(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 追加效果（发动几率50%）：扇舞·急预备
    # 持续时间：30秒
    # 发动条件：幻扇
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Additional Effect: 50% chance of granting Threefold Fan Dance
    # Duration: 30s
    # Can only be executed while in possession of Fourfold Feathers.
    id = 16008
    names = ['Fan Dance II(DNC)', '扇舞·破(DNC)']
    _orig_names = ['扇舞·破', 'Fan Dance II']
    damage = 100


class Action16009(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：200
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：扇舞·急预备状态中
    # Delivers an attack to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Can only be executed while under the effect of Threefold Fan Dance.
    # related: [扇舞·急预备(0)](Status2021), [扇舞·急](Status2052), [扇舞·急预备(1)](Status1820),
    id = 16009
    names = ['Fan Dance III(DNC)', '扇舞·急(DNC)']
    _orig_names = ['Fan Dance III', '扇舞·急']
    damage = 200
    # remain metas: {'aoe_reduce': '50%'}


class Action16010(Action):
    # 迅速移动到自身前方10米处
    # (job==38?(level>=68?积蓄次数：(job==38?(level>=78?3:2):2)
    # :):)止步状态下无法发动
    # Quickly dash 10 yalms forward.
    # (job==38?(level>=68?Maximum Charges: (job==38?(level>=78?3:2):2)
    # :):)Cannot be executed while bound.
    # related: [前冲步](Status2048),
    id = 16010
    names = ['En Avant(DNC)', '前冲步(DNC)']
    _orig_names = ['前冲步', 'En Avant']


class Action16011(Action):
    # 一定时间内，自身的暴击发动率和直击发动率提高20%
    # 持续时间：20秒
    # 追加效果：带有舞伴状态的队员也会附加同样的效果(job==38?(level>=90?
    # 追加效果：流星舞预备
    # 持续时间：20秒:):)
    # Increases critical hit rate and direct hit rate by 20%.
    # Duration: 20s
    # Additional Effect: Party member designated as your Dance Partner will also receive the effect of Devilment(job==38?(level>=90?
    # Additional Effect: Grants Flourishing Starfall
    # Duration: 20s:):)
    # related: [舞伴(0)](Status1824), [进攻之探戈](Status1825), [舞伴(1)](Status2027),
    id = 16011
    names = ['进攻之探戈(DNC)', 'Devilment(DNC)']
    _orig_names = ['Devilment', '进攻之探戈']


class Action16012(Action):
    # 一定时间内，令自身和周围队员所受到的伤害减轻10%
    # 持续时间：15秒
    # 无法与吟游诗人的行吟、机工士的策动效果共存
    # Reduces damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # Effect cannot be stacked with bard's Troubadour or machinist's Tactician.
    # related: [策动(0)](Status2177), [防守之桑巴](Status1826), [策动(1)](Status1197), [行吟](Status1934), [策动(2)](Status1951),
    id = 16012
    names = ['Shield Samba(DNC)', '防守之桑巴(DNC)']
    _orig_names = ['防守之桑巴', 'Shield Samba']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action16013(Action):
    # 对自身附加对称投掷、非对称投掷、扇舞·急预备(job==38?(level>=86?、扇舞·终预备:):)状态
    # 发动条件：自身处于战斗状态
    # Grants you the effects of Flourishing Symmetry, Flourishing Flow, (job==38?(level>=86?Threefold Fan Dance, and Fourfold Fan Dance:and Threefold Fan Dance):and Threefold Fan Dance).
    # Can only be executed while in combat.
    # related: [对称投掷](Status2693), [非对称投掷](Status2694),
    id = 16013
    names = ['百花争艳(DNC)', 'Flourish(DNC)']
    _orig_names = ['百花争艳', 'Flourish']


class Action16014(Action):
    # 原地起舞，对自身附加舞动的热情状态
    # 持续时间：15秒
    # 每3秒获得1档舞动的热情状态，最多可累积4档
    # 追加效果：令范围内的自身及队员体力持续恢复
    # 恢复力：100
    # 持续时间：15秒
    # 效果时间内发动技能或进行移动、转身都会立即中断即兴表演
    # 发动之后会停止自动攻击
    # 该技能发动后变为即兴表演结束
    # Dance to the beat of your own drum, granting Rising Rhythm to self.
    # Stacks increase every 3 seconds, up to a maximum of 4.
    # Additional Effect: Healing over time for self and nearby party members
    # Cure Potency: 100
    # Duration: 15s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # ※Action changes to Improvised Finish upon execution.
    # related: [即兴表演](Status1827), [享受即兴表演(0)](Status1828), [享受即兴表演(1)](Status2695), [舞动的热情](Status2696),
    id = 16014
    names = ['即兴表演(DNC)', 'Improvisation(DNC)']
    _orig_names = ['Improvisation', '即兴表演']
    # remain metas: {'heal_ot': '100'}


class Action16015(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：300
    # 追加效果：带有自身舞伴状态的队员也会产生同样的范围恢复效果
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 300
    # Additional Effect: Party member designated as your Dance Partner will also heal self and nearby party members
    # related: [舞伴(0)](Status1824), [舞伴(1)](Status2027),
    id = 16015
    names = ['Curing Waltz(DNC)', '治疗之华尔兹(DNC)']
    _orig_names = ['治疗之华尔兹', 'Curing Waltz']
    heal = 300


class Action16191(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束和伶俐状态:舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态):舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态)
    # 持续时间：60秒
    # 该技能的威力与标准舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力360
    # 成功1次时：威力540且效果量为2%
    # 成功2次时：威力720且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 360
    # 1 Step: 540
    # 2 Steps: 720
    # (job==38?(level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
    # Damage bonus of Standard Finish varies with number of successful steps.
    # 1 Step: 2%
    # 2 Steps: 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [标准舞步结束(0)](Status2113), [伶俐(0)](Status2051), [标准舞步结束(1)](Status2024), [伶俐(1)](Status2025), [舞伴(1)](Status2027), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [标准舞步结束(2)](Status2105), [标准舞步结束(3)](Status1821),
    id = 16191
    names = ['单色标准舞步结束(DNC)', 'Single Standard Finish(DNC)']
    _orig_names = ['单色标准舞步结束', 'Single Standard Finish']


class Action16192(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束和伶俐状态:舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态):舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束状态)
    # 持续时间：60秒
    # 该技能的威力与标准舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力360
    # 成功1次时：威力540且效果量为2%
    # 成功2次时：威力720且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 360
    # 1 Step: 540
    # 2 Steps: 720
    # (job==38?(level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner)
    # Damage bonus of Standard Finish varies with number of successful steps.
    # 1 Step: 2%
    # 2 Steps: 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [标准舞步结束(0)](Status2113), [伶俐(0)](Status2051), [标准舞步结束(1)](Status2024), [伶俐(1)](Status2025), [舞伴(1)](Status2027), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [标准舞步结束(2)](Status2105), [标准舞步结束(3)](Status1821),
    id = 16192
    names = ['双色标准舞步结束(DNC)', 'Double Standard Finish(DNC)']
    _orig_names = ['双色标准舞步结束', 'Double Standard Finish']


class Action16193(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束和伶俐状态
    # :舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # ):舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # )持续时间：20秒
    # 该技能的威力与技巧舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力350
    # 成功1次时：威力540且效果量为1%
    # 成功2次时：威力720且效果量为2%
    # 成功3次时：威力900且效果量为3%
    # 成功4次时：威力1200且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # (job==38?(level>=82?追加效果：提拉纳预备
    # 持续时间：30秒
    # :):)此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 350
    # 1 Step: 540
    # 2 Steps: 720
    # 3 Steps: 900
    # 4 Steps: 1,200
    # (job==38?(level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
    # Damage bonus of Technical Finish varies with number of successful steps.
    # 1 Step: 1%
    # 2 Steps: 2%
    # 3 Steps: 3%
    # 4 Steps: 5%
    # Duration: 20s
    # (job==38?(level>=82?Additional Effect: Grants Flourishing Finish
    # Duration: 30s
    # :):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # (job==38?(level>=82?※Action changes to Tillana upon execution.
    # :):)※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 16193
    names = ['单色技巧舞步结束(DNC)', 'Single Technical Finish(DNC)']
    _orig_names = ['Single Technical Finish', '单色技巧舞步结束']


class Action16194(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束和伶俐状态
    # :舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # ):舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # )持续时间：20秒
    # 该技能的威力与技巧舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力350
    # 成功1次时：威力540且效果量为1%
    # 成功2次时：威力720且效果量为2%
    # 成功3次时：威力900且效果量为3%
    # 成功4次时：威力1200且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # (job==38?(level>=82?追加效果：提拉纳预备
    # 持续时间：30秒
    # :):)此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 350
    # 1 Step: 540
    # 2 Steps: 720
    # 3 Steps: 900
    # 4 Steps: 1,200
    # (job==38?(level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
    # Damage bonus of Technical Finish varies with number of successful steps.
    # 1 Step: 1%
    # 2 Steps: 2%
    # 3 Steps: 3%
    # 4 Steps: 5%
    # Duration: 20s
    # (job==38?(level>=82?Additional Effect: Grants Flourishing Finish
    # Duration: 30s
    # :):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # (job==38?(level>=82?※Action changes to Tillana upon execution.
    # :):)※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 16194
    names = ['Double Technical Finish(DNC)', '双色技巧舞步结束(DNC)']
    _orig_names = ['双色技巧舞步结束', 'Double Technical Finish']


class Action16195(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束和伶俐状态
    # :舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # ):舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # )持续时间：20秒
    # 该技能的威力与技巧舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力350
    # 成功1次时：威力540且效果量为1%
    # 成功2次时：威力720且效果量为2%
    # 成功3次时：威力900且效果量为3%
    # 成功4次时：威力1200且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # (job==38?(level>=82?追加效果：提拉纳预备
    # 持续时间：30秒
    # :):)此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 350
    # 1 Step: 540
    # 2 Steps: 720
    # 3 Steps: 900
    # 4 Steps: 1,200
    # (job==38?(level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
    # Damage bonus of Technical Finish varies with number of successful steps.
    # 1 Step: 1%
    # 2 Steps: 2%
    # 3 Steps: 3%
    # 4 Steps: 5%
    # Duration: 20s
    # (job==38?(level>=82?Additional Effect: Grants Flourishing Finish
    # Duration: 30s
    # :):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # (job==38?(level>=82?※Action changes to Tillana upon execution.
    # :):)※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 16195
    names = ['Triple Technical Finish(DNC)', '三色技巧舞步结束(DNC)']
    _orig_names = ['Triple Technical Finish', '三色技巧舞步结束']


class Action16196(Action):
    # 对自身周围的敌人发动范围物理攻击
    # (job==38?(level>=76?舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束和伶俐状态
    # :舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # ):舞步成功时追加效果：对自身及周围的队员附加技巧舞步结束状态
    # )持续时间：20秒
    # 该技能的威力与技巧舞步结束状态的效果量随舞步技能的成功次数而有所不同
    # 成功0次时：威力350
    # 成功1次时：威力540且效果量为1%
    # 成功2次时：威力720且效果量为2%
    # 成功3次时：威力900且效果量为3%
    # 成功4次时：威力1200且效果量为5%
    # 攻击复数敌人时，对第一个之外的敌人威力降低75%
    # (job==38?(level>=82?追加效果：提拉纳预备
    # 持续时间：30秒
    # :):)此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies.
    # 0 Steps: 350
    # 1 Step: 540
    # 2 Steps: 720
    # 3 Steps: 900
    # 4 Steps: 1,200
    # (job==38?(level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members)
    # Damage bonus of Technical Finish varies with number of successful steps.
    # 1 Step: 1%
    # 2 Steps: 2%
    # 3 Steps: 3%
    # 4 Steps: 5%
    # Duration: 20s
    # (job==38?(level>=82?Additional Effect: Grants Flourishing Finish
    # Duration: 30s
    # :):)Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # (job==38?(level>=82?※Action changes to Tillana upon execution.
    # :):)※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 16196
    names = ['四色技巧舞步结束(DNC)', 'Quadruple Technical Finish(DNC)']
    _orig_names = ['四色技巧舞步结束', 'Quadruple Technical Finish']


class Action17756(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：获得10点伶俐
    # ※“前冲步”状态中该技能变为“逆瀑泻”
    # ※跳舞模式中该技能变为“蔷薇曲脚步”
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Increases Esprit Gauge by 10
    # ※Action changes to Reverse Cascade while under the effect of En Avant.
    # ※Action changes to Emboite while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025),
    id = 17756
    names = ['Cascade(pvp)(DNC)', '瀑泻(pvp)(DNC)']
    _orig_names = ['Cascade(pvp)', '瀑泻(pvp)']
    damage = 1000


class Action17757(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 连击条件：瀑泻或逆瀑泻
    # 连击成功：幻扇
    # 连击成功：获得10点伶俐
    # ※“前冲步”状态中该技能变为“坠喷泉”
    # ※跳舞模式中该技能变为“蔷薇曲脚步”
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Cascade or Reverse Cascade
    # Combo Potency: 1,200
    # Combo Bonus: Grants a Fourfold Feather
    # Combo Bonus: Increases Esprit Gauge by 10
    # ※Action changes to Fountainfall while under the effect of En Avant.
    # ※Action changes to Emboite while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048),
    id = 17757
    names = ['喷泉(pvp)(DNC)', 'Fountain(pvp)(DNC)']
    _orig_names = ['喷泉(pvp)', 'Fountain(pvp)']
    combo_action = 17756
    damage = 1200


class Action17758(Action):
    # 对目标发动物理攻击
    # 威力：1600
    # 追加效果：获得10点伶俐
    # 发动后会取消前冲步状态
    # 发动条件：前冲步状态中
    # ※跳舞模式中该技能变为“蔷薇曲脚步”
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,600.
    # Additional Effect: Increases Esprit Gauge by 10
    # Can only be executed while under the effect of En Avant. Effect fades upon execution.
    # ※Action changes to Emboite while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025),
    id = 17758
    names = ['逆瀑泻(pvp)(DNC)', 'Reverse Cascade(pvp)(DNC)']
    _orig_names = ['逆瀑泻(pvp)', 'Reverse Cascade(pvp)']
    damage = 1600


class Action17759(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 连击条件：瀑泻或逆瀑泻
    # 连击成功：幻扇
    # 连击成功：获得10点伶俐
    # 发动后会取消前冲步状态
    # 发动条件：前冲步状态中
    # ※跳舞模式中该技能变为“蔷薇曲脚步”
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Cascade or Reverse Cascade
    # Combo Potency: 1,800
    # Combo Bonus: Grants a Fourfold Feather
    # Combo Bonus: Increases Esprit Gauge by 10
    # Can only be executed while under the effect of En Avant. Effect fades upon execution.
    # ※Action changes to Emboite while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048),
    id = 17759
    names = ['Fountainfall(pvp)(DNC)', '坠喷泉(pvp)(DNC)']
    _orig_names = ['坠喷泉(pvp)', 'Fountainfall(pvp)']
    combo_action = 17756
    damage = 1800


class Action17760(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：2000
    # 追加效果：自身以及带有自身舞伴状态的队员发动攻击造成的伤害提高10%
    # 持续时间：15秒
    # 发动条件：伶俐50点
    # Delivers an attack with a potency of 2,000 to target and all enemies nearby it.
    # Additional Effect: Increases damage dealt by self and party member designated as your Dance Partner by 10%
    # Duration: 15s
    # Esprit Gauge Cost: 50
    # related: [舞伴(0)](Status1824), [舞伴(1)](Status2027), [剑舞](Status2022),
    id = 17760
    names = ['剑舞(pvp)(DNC)', 'Saber Dance(pvp)(DNC)']
    _orig_names = ['Saber Dance(pvp)', '剑舞(pvp)']
    damage = 2000
    # remain metas: {'dmg_increase': '10%'}


class Action17761(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：扇舞·急预备
    # 持续时间：15秒
    # 发动条件：幻扇
    # ※跳舞模式中该技能变为“绿叶小踢腿”
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Grants Flourishing Fan Dance
    # Duration: 15s
    # Can only be executed while in possession of Fourfold Feathers.
    # ※Action changes to Jete while dancing.
    # related: [扇舞·急预备(1)](Status1820), [扇舞·急预备(0)](Status2021),
    id = 17761
    names = ['扇舞·序(pvp)(DNC)', 'Fan Dance(pvp)(DNC)']
    _orig_names = ['扇舞·序(pvp)', 'Fan Dance(pvp)']
    damage = 1000


class Action17762(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：1200
    # 追加效果：自身以及带有自身舞伴状态的队员所受的伤害减轻10%
    # 持续时间：15秒
    # 发动条件：扇舞·急预备
    # 积蓄次数：2
    # Delivers an attack with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Reduces damage taken by self and party member designated as your Dance Partner by 10%
    # Duration: 15s
    # Maximum Charges: 2
    # Can only be executed while under the effect of Flourishing Fan Dance. Effect fades upon execution.
    # related: [舞伴(0)](Status1824), [舞伴(1)](Status2027), [扇舞·急](Status2052),
    id = 17762
    names = ['扇舞·急(pvp)(DNC)', 'Fan Dance III(pvp)(DNC)']
    _orig_names = ['Fan Dance III(pvp)', '扇舞·急(pvp)']
    damage = 1200
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action17763(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # 追加效果：带有自身舞伴状态的队员也会产生同样的范围恢复效果
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    # Additional Effect: Party member designated as your Dance Partner will also heal self and nearby party members
    # related: [舞伴(0)](Status1824), [舞伴(1)](Status2027),
    id = 17763
    names = ['Curing Waltz(pvp)(DNC)', '治疗之华尔兹(pvp)(DNC)']
    _orig_names = ['治疗之华尔兹(pvp)', 'Curing Waltz(pvp)']
    heal = 2000


class Action17764(Action):
    # 迅速移动到自身前方10米处
    # 追加效果：前冲步
    # 持续时间：5秒
    # 积蓄次数：3
    # 止步状态下无法发动
    # Quickly dash 10 yalms forward.
    # Additional Effect: Grants En Avant
    # Duration: 5s
    # Maximum Charges: 3
    # Effect fades upon execution of Reverse Cascade, Fountainfall, Rising Windmill, or Bloodshower.
    # Cannot be executed while bound.
    # related: [前冲步](Status2048),
    id = 17764
    names = ['En Avant(pvp)(DNC)', '前冲步(pvp)(DNC)']
    _orig_names = ['前冲步(pvp)', 'En Avant(pvp)']


class Action17765(Action):
    # 指定一名队员为目标，对自身附加闭式舞姿状态，对目标附加舞伴状态
    # 在该状态下发动标准舞步结束、剑舞、扇舞·急、治疗之华尔兹时，附加舞伴状态的队员也可以获得同样的效果
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Grants you Closed Position and designates a party member as your Dance Partner, allowing you to share the effects of Standard Finish, Saber Dance, Fan Dance III, and Curing Waltz with said party member.
    # Effect ends upon reuse.
    # related: [舞伴(0)](Status1824), [闭式舞姿(0)](Status2026), [舞伴(1)](Status2027), [闭式舞姿(1)](Status1823),
    id = 17765
    names = ['闭式舞姿(pvp)(DNC)', 'Closed Position(pvp)(DNC)']
    _orig_names = ['闭式舞姿(pvp)', 'Closed Position(pvp)']


class Action17766(Action):
    # 进入跳舞模式，对自身附加标准舞步状态
    # 持续时间：10秒
    # 跳舞模式中该技能变为标准舞步结束
    # 此时只能使用舞步技能、标准舞步结束、前冲步、伤头、疾跑、军用恢复药和额外技能
    # 发动技能后，战技会进入复唱时间
    # Begin dancing, granting yourself Standard Step.
    # Duration: 10s
    # Action changes to Standard Finish while dancing.
    # Only step actions, Standard Finish, En Avant, Head Graze, Bolt, Medical Kit, Adrenaline Rush, and additional actions can be performed while dancing.
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # related: [标准舞步(0)](Status1818), [标准舞步(1)](Status2023),
    id = 17766
    names = ['标准舞步(pvp)(DNC)', 'Standard Step(pvp)(DNC)']
    _orig_names = ['标准舞步(pvp)', 'Standard Step(pvp)']


class Action17767(Action):
    # 发动蔷薇曲脚步舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 发动技能后，舞步技能与结束技能会产生复唱时间
    # ※该技能无法设置到热键栏
    # Perform an emboite.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 17767
    names = ['蔷薇曲脚步(pvp)(DNC)', 'Emboite(pvp)(DNC)']
    _orig_names = ['Emboite(pvp)', '蔷薇曲脚步(pvp)']


class Action17768(Action):
    # 发动小鸟交叠跳舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 发动技能后，舞步技能与结束技能会产生复唱时间
    # ※该技能无法设置到热键栏
    # Perform an entrechat.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 17768
    names = ['小鸟交叠跳(pvp)(DNC)', 'Entrechat(pvp)(DNC)']
    _orig_names = ['小鸟交叠跳(pvp)', 'Entrechat(pvp)']


class Action17769(Action):
    # 发动绿叶小踢腿舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 发动技能后，舞步技能与结束技能会产生复唱时间
    # ※该技能无法设置到热键栏
    # Perform a jete.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 17769
    names = ['Jete(pvp)(DNC)', '绿叶小踢腿(pvp)(DNC)']
    _orig_names = ['绿叶小踢腿(pvp)', 'Jete(pvp)']


class Action17770(Action):
    # 发动金冠趾尖转舞步技能
    # 成功按照舞步量谱显示的顺序发动舞步技能，可以提高结束技能的效果
    # 发动技能后，舞步技能与结束技能会产生复唱时间
    # ※该技能无法设置到热键栏
    # Perform a pirouette.
    # When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased.
    # Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    id = 17770
    names = ['Pirouette(pvp)(DNC)', '金冠趾尖转(pvp)(DNC)']
    _orig_names = ['金冠趾尖转(pvp)', 'Pirouette(pvp)']


class Action17771(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：60秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and party member designated as your Dance Partner by 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [标准舞步结束(0)](Status2113), [伶俐(0)](Status2051), [标准舞步结束(1)](Status2024), [伶俐(1)](Status2025), [舞伴(1)](Status2027), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [标准舞步结束(2)](Status2105), [标准舞步结束(3)](Status1821),
    id = 17771
    names = ['Standard Finish(pvp)(DNC)', '标准舞步结束(pvp)(DNC)']
    _orig_names = ['Standard Finish(pvp)', '标准舞步结束(pvp)']


class Action17772(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：60秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and party member designated as your Dance Partner by 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [舞伴(1)](Status2027),
    id = 17772
    names = ['Single Standard Finish(pvp)(DNC)', '单色标准舞步结束(pvp)(DNC)']
    _orig_names = ['Single Standard Finish(pvp)', '单色标准舞步结束(pvp)']


class Action17773(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及带有自身舞伴状态的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：60秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and party member designated as your Dance Partner by 5%
    # Duration: 60s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [舞伴(1)](Status2027),
    id = 17773
    names = ['双色标准舞步结束(pvp)(DNC)', 'Double Standard Finish(pvp)(DNC)']
    _orig_names = ['Double Standard Finish(pvp)', '双色标准舞步结束(pvp)']


class Action17824(Action):
    # 进入跳舞模式，对自身附加技巧舞步状态
    # 持续时间：10秒
    # 跳舞模式中该技能变为技巧舞步结束
    # 此时只能使用舞步技能、技巧舞步结束、前冲步、伤头、疾跑、军用恢复药和额外技能
    # 发动技能后，战技会进入复唱时间
    # Begin dancing, granting yourself Technical Step.
    # Duration: 10s
    # Action changes to Technical Finish while dancing.
    # Only step actions, Technical Finish, En Avant, Head Graze, Bolt, Medical Kit, Adrenaline Rush, and additional actions can be performed while dancing.
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # related: [技巧舞步(0)](Status2049), [技巧舞步(1)](Status1819),
    id = 17824
    names = ['Technical Step(pvp)(DNC)', '技巧舞步(pvp)(DNC)']
    _orig_names = ['Technical Step(pvp)', '技巧舞步(pvp)']


class Action17825(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及周围的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：15秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 成功3次时：威力1200～2400
    # 成功4次时：威力1500～3000
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # 3 Steps: 1,200
    # 4 Steps: 1,500
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and nearby party members by 5%
    # Duration: 15s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [技巧舞步结束(0)](Status2050), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025), [技巧舞步结束(1)](Status1822),
    id = 17825
    names = ['技巧舞步结束(pvp)(DNC)', 'Technical Finish(pvp)(DNC)']
    _orig_names = ['技巧舞步结束(pvp)', 'Technical Finish(pvp)']


class Action17826(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及周围的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：15秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 成功3次时：威力1200～2400
    # 成功4次时：威力1500～3000
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # 3 Steps: 1,200
    # 4 Steps: 1,500
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and nearby party members by 5%
    # Duration: 15s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [伶俐(3)](Status1848), [伶俐(1)](Status2025), [伶俐(0)](Status2051), [伶俐(2)](Status1847),
    id = 17826
    names = ['单色技巧舞步结束(pvp)(DNC)', 'Single Technical Finish(pvp)(DNC)']
    _orig_names = ['Single Technical Finish(pvp)', '单色技巧舞步结束(pvp)']


class Action17827(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及周围的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：15秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 成功3次时：威力1200～2400
    # 成功4次时：威力1500～3000
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # 3 Steps: 1,200
    # 4 Steps: 1,500
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and nearby party members by 5%
    # Duration: 15s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [伶俐(3)](Status1848), [伶俐(1)](Status2025), [伶俐(0)](Status2051), [伶俐(2)](Status1847),
    id = 17827
    names = ['Double Technical Finish(pvp)(DNC)', '双色技巧舞步结束(pvp)(DNC)']
    _orig_names = ['Double Technical Finish(pvp)', '双色技巧舞步结束(pvp)']


class Action17828(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及周围的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：15秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 成功3次时：威力1200～2400
    # 成功4次时：威力1500～3000
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # 3 Steps: 1,200
    # 4 Steps: 1,500
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and nearby party members by 5%
    # Duration: 15s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [伶俐(3)](Status1848), [伶俐(1)](Status2025), [伶俐(0)](Status2051), [伶俐(2)](Status1847),
    id = 17828
    names = ['三色技巧舞步结束(pvp)(DNC)', 'Triple Technical Finish(pvp)(DNC)']
    _orig_names = ['三色技巧舞步结束(pvp)', 'Triple Technical Finish(pvp)']


class Action17829(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 与目标距离越近威力越大
    # 追加效果：每命中一个目标都会获得5点伶俐
    # 舞步成功时追加效果：对自身以及周围的队员附加战技与魔法的咏唱及复唱时间缩短5%的效果
    # 持续时间：15秒
    # 该技能的威力随舞步技能的成功次数而有所不同
    # 成功0次时：威力300～600
    # 成功1次时：威力600～1200
    # 成功2次时：威力900～1800
    # 成功3次时：威力1200～2400
    # 成功4次时：威力1500～3000
    # 发动技能后，战技会产生复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies. Potency increases by up to 300% based on proximity to enemies.
    # 0 Steps: 300
    # 1 Step: 600
    # 2 Steps: 900
    # 3 Steps: 1,200
    # 4 Steps: 1,500
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Step Bonus: Reduces weaponskill cast time and recast time, as well as spell cast time and recast time for self and nearby party members by 5%
    # Duration: 15s
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [伶俐(3)](Status1848), [伶俐(1)](Status2025), [伶俐(0)](Status2051), [伶俐(2)](Status1847),
    id = 17829
    names = ['Quadruple Technical Finish(pvp)(DNC)', '四色技巧舞步结束(pvp)(DNC)']
    _orig_names = ['Quadruple Technical Finish(pvp)', '四色技巧舞步结束(pvp)']


class Action18073(Action):
    # 取消闭式舞姿状态
    # Ends dance with your partner.
    # related: [闭式舞姿(0)](Status2026), [闭式舞姿(1)](Status1823),
    id = 18073
    names = ['Ending(DNC)', '解除闭式舞姿(DNC)']
    _orig_names = ['解除闭式舞姿', 'Ending']


class Action18076(Action):
    # 取消闭式舞姿状态
    # Ends dance with your partner.
    # related: [闭式舞姿(0)](Status2026), [闭式舞姿(1)](Status1823),
    id = 18076
    names = ['解除闭式舞姿(pvp)(DNC)', 'Ending(pvp)(DNC)']
    _orig_names = ['Ending(pvp)', '解除闭式舞姿(pvp)']


class Action18993(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：600
    # 追加效果：每命中一个目标获得5点伶俐
    # ※“前冲步”状态中，该技能变为“升风车”
    # ※跳舞模式中该技能变为“小鸟交叠跳”
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # ※Action changes to Rising Windmill while under the effect of En Avant.
    # ※Action changes to Entrechat while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025),
    id = 18993
    names = ['风车(pvp)(DNC)', 'Windmill(pvp)(DNC)']
    _orig_names = ['风车(pvp)', 'Windmill(pvp)']
    damage = 600


class Action18994(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：800
    # 连击条件：风车或升风车
    # 连击成功：幻扇
    # 连击成功：每命中一个目标获得5点伶俐
    # ※“前冲步”状态中，该技能变为“落血雨”
    # ※跳舞模式中该技能变为“小鸟交叠跳”
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Windmill or Rising Windmill
    # Combo Potency: 800
    # Combo Bonus: Grants a Fourfold Feather
    # Combo Bonus: Increases Esprit Gauge by 5 for each enemy hit
    # ※Action changes to Bloodshower while under the effect of En Avant.
    # ※Action changes to Entrechat while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048),
    id = 18994
    names = ['落刃雨(pvp)(DNC)', 'Bladeshower(pvp)(DNC)']
    _orig_names = ['Bladeshower(pvp)', '落刃雨(pvp)']
    combo_action = 18993
    damage = 800


class Action18995(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：1000
    # 追加效果：每命中一个目标获得5点伶俐
    # 发动时解除前冲步状态
    # 发动条件：前冲步
    # ※跳舞模式中该技能变为“小鸟交叠跳”
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Increases Esprit Gauge by 5 for each enemy hit
    # Can only be executed while under the effect of En Avant. Effect fades upon execution.
    # ※Action changes to Entrechat while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048), [伶俐(0)](Status2051), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [伶俐(1)](Status2025),
    id = 18995
    names = ['升风车(pvp)(DNC)', 'Rising Windmill(pvp)(DNC)']
    _orig_names = ['Rising Windmill(pvp)', '升风车(pvp)']
    damage = 1000


class Action18996(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：1200
    # 连击条件：风车或升风车
    # 连击成功：幻扇
    # 连击成功：每命中一个目标获得5点伶俐
    # 发动时解除前冲步状态
    # 发动条件：前冲步
    # ※跳舞模式中该技能变为“小鸟交叠跳”
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Windmill or Rising Windmill
    # Combo Potency: 1,200
    # Combo Bonus: Grants a Fourfold Feather
    # Combo Bonus: Increases Esprit Gauge by 5 for each enemy hit
    # Can only be executed while under the effect of En Avant. Effect fades upon execution.
    # ※Action changes to Entrechat while dancing.
    # ※This action cannot be assigned to a hotbar.
    # related: [前冲步](Status2048),
    id = 18996
    names = ['Bloodshower(pvp)(DNC)', '落血雨(pvp)(DNC)']
    _orig_names = ['落血雨(pvp)', 'Bloodshower(pvp)']
    combo_action = 18993
    damage = 1200


class Action18997(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：600
    # 追加效果：扇舞·急预备
    # 持续时间：15秒
    # 发动条件：幻扇
    # ※跳舞模式中该技能变为“金冠趾尖转”
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Grants Flourishing Fan Dance
    # Duration: 15s
    # Can only be executed while in possession of Fourfold Feathers.
    # ※Action changes to Pirouette while dancing.
    # related: [扇舞·急预备(1)](Status1820), [扇舞·急预备(0)](Status2021),
    id = 18997
    names = ['Fan Dance II(pvp)(DNC)', '扇舞·破(pvp)(DNC)']
    _orig_names = ['扇舞·破(pvp)', 'Fan Dance II(pvp)']
    damage = 600


class Action25789(Action):
    # 为自身与周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩的效果量根据自身附加的舞动的热情的档数变化
    # 0档时：抵消相当于目标最大体力5%的伤害量
    # 1档时：抵消相当于目标最大体力6%的伤害量
    # 2档时：抵消相当于目标最大体力7%的伤害量
    # 3档时：抵消相当于目标最大体力8%的伤害量
    # 4档时：抵消相当于目标最大体力10%的伤害量
    # 持续时间：30秒
    # 发动条件：即兴表演状态中
    # ※该技能无法设置到热键栏
    # Creates a barrier around self and all nearby party members. Damage absorbed increases with stacks of Rising Rhythm.
    # 0 Stacks: 5% of maximum HP
    # 1 Stack: 6% of maximum HP
    # 2 Stacks: 7% of maximum HP
    # 3 Stacks: 8% of maximum HP
    # 4 Stacks: 10% of maximum HP
    # Duration: 30s
    # Can only be executed while Improvisation is active.
    # ※This action cannot be assigned to a hotbar.
    # related: [即兴表演结束](Status2697), [即兴表演](Status1827),
    id = 25789
    names = ['Improvised Finish(DNC)', '即兴表演结束(DNC)']
    _orig_names = ['即兴表演结束', 'Improvised Finish']
    # remain metas: {'shield': ['目标最大体力8%', '目标最大体力6%', '目标最大体力7%', '目标最大体力5%', '目标最大体力10%']}


class Action25790(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：360
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：对自身以及带有自身舞伴状态的队员附加标准舞步结束和伶俐状态
    # 持续时间：60秒
    # 标准舞步结束效果量：5%
    # 发动条件：提拉纳预备状态中
    # 此战技的复唱时间不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies with a potency of 360 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner
    # Standard Finish Effect: Increases damage dealt by 5%
    # Duration: 60s
    # Can only be executed while under the effect of Flourishing Finish.
    # Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [舞伴(0)](Status1824), [标准舞步结束(0)](Status2113), [伶俐(0)](Status2051), [标准舞步结束(1)](Status2024), [伶俐(1)](Status2025), [提拉纳预备](Status2698), [舞伴(1)](Status2027), [伶俐(2)](Status1847), [伶俐(3)](Status1848), [标准舞步结束(2)](Status2105), [标准舞步结束(3)](Status1821),
    id = 25790
    names = ['提拉纳(DNC)', 'Tillana(DNC)']
    _orig_names = ['Tillana', '提拉纳']
    damage = 360


class Action25791(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：300
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：扇舞·终预备状态中
    # Delivers an attack to all enemies in a cone before you with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
    # Can only be executed while under the effect of Fourfold Fan Dance.
    # related: [扇舞·终](Status2699),
    id = 25791
    names = ['Fan Dance IV(DNC)', '扇舞·终(DNC)']
    _orig_names = ['扇舞·终', 'Fan Dance IV']
    damage = 300
    # remain metas: {'aoe_reduce': '50%'}


class Action25792(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低75%
    # 该技能必定暴击并且直击
    # 发动条件：流星舞预备状态中
    # Delivers a critical direct hit to all enemies in a straight line before you with a potency of 600 for the first enemy, and 75% less for all remaining enemies.
    # Can only be executed while under the effect of Flourishing Starfall.
    # related: [流星舞预备](Status2700),
    id = 25792
    names = ['Starfall Dance(DNC)', '流星舞(DNC)']
    _orig_names = ['流星舞', 'Starfall Dance']
    damage = 600
    # remain metas: {'aoe_reduce': '75%'}
