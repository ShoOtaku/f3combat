from ._base import *


class Status488(Status):
    # 抵消一定伤害
    # Shadows are nullifying damage.
    # related: [残影(NIN)](Action2241), 
    id = 488
    names = ['残影(0)', 'Shade Shift(0)']


class Status2011(Status):
    # 抵消一定伤害
    # Shadows are nullifying damage.
    # related: [残影(NIN)](Action2241), 
    id = 2011
    names = ['残影(1)', 'Shade Shift(1)']


class Status1952(Status):
    # 隐遁自己的身形，移动速度降低
    # Unable to be detected. Movement speed is severely reduced.
    # related: [隐遁(NIN)](Action2245), [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 1952
    names = ['隐遁(0)', 'Hide']


class Status1316(Status):
    # 隐遁自己的身形
    # Unable to be detected.
    # related: [隐遁(NIN)](Action2245), [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 1316
    names = ['隐遁(1)', 'Hidden(0)']


class Status1108(Status):
    # 隐遁自己的身形，移动速度降低
    # Unable to be detected. Movement speed is severely reduced.
    # related: [隐遁(NIN)](Action2245), [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 1108
    names = ['隐遁(2)', 'Hidden(1)']


class Status615(Status):
    # 隐遁自己的身形，移动速度降低
    # Unable to be detected. Movement speed is severely reduced.
    # related: [隐遁(NIN)](Action2245), [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 615
    names = ['隐遁(3)', 'Hidden(2)']


class Status1705(Status):
    # 隐遁自己的身形，移动速度降低
    # Unable to be detected. Movement speed is severely reduced.
    # related: [隐遁(NIN)](Action2245), [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 1705
    names = ['隐遁(4)', 'Hidden(3)']


class Status1314(Status):
    # 受到持续伤害，同时受到攻击的伤害增加
    # Sustaining damage over time, as well as increased damage.
    # related: [断绝(NIN)](Action2246), [断绝(pvp)(NIN)](Action8814), 
    id = 1314
    names = ['断绝', 'Assassinated']


class Status2014(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [攻其不备(NIN)](Action2258), [攻其不备(pvp)(NIN)](Action17735), 
    id = 2014
    names = ['攻其不备', 'Trick Attack']


class Status496(Status):
    # 结成手印准备发动忍术
    # Readying ninjutsu by combining ritual hand gestures.
    # related: [忍术(NIN)](Action2260), 
    id = 496
    names = ['结印', 'Mudra']


class Status497(Status):
    # 可以发动忍术并且忍术的威力提升
    # Able to execute a ninjutsu with increased potency.
    # related: [生杀予夺(NIN)](Action2264), [天地人(NIN)](Action7403), [劫火灭却之术(NIN)](Action16491), [冰晶乱流之术(NIN)](Action16492), 
    id = 497
    names = ['生杀予夺', 'Kassatsu']


class Status500(Status):
    # 自动攻击间隔缩短，同时战技的复唱时间也会缩短
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [风遁之术(NIN)(0)](Action2269), [劫火灭却之术(pvp)(NIN)](Action17732), [冰晶乱流之术(pvp)(NIN)](Action17733), [风遁之术(NIN)(1)](Action18879), [风来刃(NIN)](Action25876), 
    id = 500
    names = ['风遁之术', 'Huton']


class Status501(Status):
    # 产生土属性攻击区域
    # Foul magicks corrupt the ground, dealing earth damage to any who tread upon it.
    # related: [土遁之术(NIN)(0)](Action2270), [土遁之术(NIN)(1)](Action18880), 
    id = 501
    names = ['土遁之术', 'Doton']


class Status614(Status):
    # 隐遁自己的身形，移动速度降低
    # Unable to be detected. Movement speed is severely reduced.
    # related: [水遁之术(NIN)(0)](Action2271), [隐身之术(pvp)(NIN)](Action8820), [攻其不备(pvp)(NIN)](Action17735), [水遁之术(NIN)(1)](Action18881), 
    id = 614
    names = ['隐遁(5)', 'Hidden(4)']


class Status2839(Status):
    # 不用隐遁身形也能够发动需要在隐遁状态下发动的技能
    # Body is enveloped in a light-bending veil of water, allowing use of actions normally requiring the Hidden status.
    # related: [水遁之术(NIN)(0)](Action2271), [命水(NIN)](Action16489), [水遁之术(NIN)(1)](Action18881), 
    id = 2839
    names = ['水遁之术(0)', 'Suiton(0)']


class Status507(Status):
    # 不用隐遁身形也能够发动需要在隐遁状态下发动的技能
    # Body is enveloped in a light-bending veil of water, allowing use of actions normally requiring the Hidden status.
    # related: [水遁之术(NIN)(0)](Action2271), [命水(NIN)](Action16489), [水遁之术(NIN)(1)](Action18881), 
    id = 507
    names = ['水遁之术(1)', 'Suiton(1)']


class Status2689(Status):
    # 下次发动六道轮回的威力上升
    # Next Bhavacakra will deal increased damage.
    # related: [六道轮回(NIN)](Action7402), [命水(NIN)](Action16489), 
    id = 2689
    names = ['命水', 'Meisui']


class Status1186(Status):
    # 可以连发忍术
    # Able to execute ninjutsu in succession.
    # related: [天地人(NIN)](Action7403), 
    id = 1186
    names = ['天地人', 'Ten Chi Jin']


class Status1317(Status):
    # 可以发动忍术
    # Able to execute any ninjutsu action.
    # related: [三印自在(pvp)(NIN)](Action8816), 
    id = 1317
    names = ['三印自在', 'Three Mudra']


class Status1315(Status):
    # 持续时间内没有受到敌人的攻击则附加隐遁状态
    # Slowly blending in with the environment. If not attacked, you will eventually become hidden.
    # related: [隐身之术(pvp)(NIN)](Action8820), 
    id = 1315
    names = ['隐身之术', 'Kakuremi']


class Status1954(Status):
    # 自身一发动战技就会立刻进行分身攻击
    # Your corporeal shadow is performing an attack each time you execute a weaponskill.
    # related: [分身之术(NIN)](Action16493), [分身之术(pvp)(NIN)](Action17734), 
    id = 1954
    names = ['分身之术(0)', 'Bunshin(0)']


class Status2723(Status):
    # 可以发动残影镰鼬
    # Able to execute Phantom Kamaitachi.
    # related: [分身之术(NIN)](Action16493), [残影镰鼬(NIN)](Action25774), 
    id = 2723
    names = ['残影镰鼬预备', 'Phantom Kamaitachi Ready']


class Status2010(Status):
    # 自身发动战技后分身会跟着进行攻击
    # Your corporeal shadow is performing an attack each time you execute a weaponskill.
    # related: [分身之术(NIN)](Action16493), [分身之术(pvp)(NIN)](Action17734), 
    id = 2010
    names = ['分身之术(1)', 'Bunshin(1)']


class Status2690(Status):
    # 可以发动月影雷兽爪或月影雷兽牙
    # Able to execute Forked Raiju and Fleeting Raiju.
    # related: [月影雷兽爪(NIN)](Action25777), [月影雷兽牙(NIN)](Action25778), 
    id = 2690
    names = ['月影雷兽预备', 'Raiju Ready']


class Action2240(Action):
    # 对目标发动物理攻击
    # 威力：(job==30?(level>=84?210:180):180)(job==30?(level>=62?
    # 追加效果：获得5点忍气:):)
    # Delivers an attack with a potency of (job==30?(level>=84?210:180):180).(job==30?(level>=62?
    # Additional Effect: Increases Ninki Gauge by 5:):)
    id = 2240
    names = ['Spinning Edge(NIN)', '双刃旋(NIN)']
    _orig_names = ['Spinning Edge', '双刃旋']
    damage = "(job==30?(lv>=84?210:180):180)"


class Action2241(Action):
    # 抵消相当于自身最大体力20%的伤害
    # 持续时间：20秒
    # Create shadows that nullify damage up to 20% of maximum HP.
    # Duration: 20s
    # related: [残影(0)](Status488), [残影(1)](Status2011), 
    id = 2241
    names = ['残影(NIN)', 'Shade Shift(NIN)']
    _orig_names = ['残影', 'Shade Shift']
    # remain metas: {'shield': '自身最大体力20%'}


class Action2242(Action):
    # 对目标发动物理攻击
    # 威力：(job==30?(level>=84?160:100):100)
    # 连击条件：双刃旋
    # 连击中威力：(job==30?(level>=84?320:260):260)(job==30?(level>=62?
    # 连击成功：获得5点忍气:):)
    # Delivers an attack with a potency of (job==30?(level>=84?160:100):100).
    # Combo Action: Spinning Edge
    # Combo Potency: (job==30?(level>=84?320:260):260)(job==30?(level>=62?
    # Combo Bonus: Increases Ninki Gauge by 5:):)
    id = 2242
    names = ['绝风(NIN)', 'Gust Slash(NIN)']
    _orig_names = ['Gust Slash', '绝风']
    combo_action = 2240
    damage = "(job==30?(lv>=84?160:100):100)"
    combo_damage = "(job==30?(lv>=84?320:260):260)"


class Action2245(Action):
    # 隐藏自己的身形，大多数敌人都无法发现自己
    # 不过移动速度会降低50%
    # 对比自身等级高出10级的怪物以及部分特殊怪物无效
    # 发动除冲刺以外的其他技能会取消该状态
    # 持续时间：永久
    # (level>=30?(job==30?追加效果：发动后若处于非战斗状态则重置2次忍术的复唱时间
    # :):)发动条件：自身处于非战斗状态
    # Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 50%. Has no effect on enemies 10 levels higher than your own, or certain enemies with special sight.
    # (level>=30?(job==30?Additional Effect: Restores 2 charges to all mudra
    # :):)Cannot be executed while in combat.
    # Effect ends upon use of any action other than Sprint, or upon reuse of Hide.
    # related: [隐遁(0)](Status1952), [隐遁(1)](Status1316), [隐遁(2)](Status1108), [隐遁(3)](Status615), [隐遁(4)](Status1705), 
    id = 2245
    names = ['隐遁(NIN)', 'Hide(NIN)']
    _orig_names = ['Hide', '隐遁']


class Action2246(Action):
    # 对目标发动物理攻击
    # 威力：200
    # Delivers an attack with a potency of 200.
    # related: [断绝](Status1314), 
    id = 2246
    names = ['断绝(NIN)', 'Assassinate(NIN)']
    _orig_names = ['断绝', 'Assassinate']
    damage = 200


class Action2247(Action):
    # 对目标发动远距离物理攻击
    # 威力：120(job==30?(level>=62?
    # 追加效果：获得5点忍气:):)
    # Delivers a ranged attack with a potency of 120.(job==30?(level>=62?
    # Additional Effect: Increases Ninki Gauge by 5:):)
    id = 2247
    names = ['Throwing Dagger(NIN)', '飞刀(NIN)']
    _orig_names = ['Throwing Dagger', '飞刀']
    damage = 120


class Action2248(Action):
    # 对目标发动物理攻击
    # 威力：150
    # 追加效果：用该技能打倒敌人之后有可能会掉落更多的物品(level>=66?(job==30?
    # 追加效果：获得40点忍气:):)
    # Delivers an attack with a potency of 150.
    # Additional Effect: Increases the chance of additional items being dropped by target if Mug is dealt before, or as, the finishing blow(level>=66?(job==30?
    # Additional Effect: Increases Ninki Gauge by 40:):)
    id = 2248
    names = ['夺取(NIN)', 'Mug(NIN)']
    _orig_names = ['夺取', 'Mug']
    damage = 150


class Action2254(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100(job==30?(level>=62?
    # 追加效果：获得5点忍气:):)
    # Delivers an attack with a potency of 100 to all nearby enemies.(job==30?(level>=62?
    # Additional Effect: Increases Ninki Gauge by 5:):)
    id = 2254
    names = ['Death Blossom(NIN)', '血雨飞花(NIN)']
    _orig_names = ['Death Blossom', '血雨飞花']
    damage = 100


class Action2255(Action):
    # 对目标发动物理攻击
    # 威力：(job==30?(level>=84?140:100):100)
    # 背面攻击威力：(job==30?(level>=84?200:160):160)
    # 连击条件：绝风
    # 连击中威力：(job==30?(level>=84?360:320):320)
    # 连击中背面攻击威力：(job==30?(level>=84?420:380):380)(job==30?(level>=62?
    # 连击成功：获得(job==30?(level>=84?15:(job==30?(level>=78?10:5):5)):(job==30?(level>=78?10:5):5))点忍气:):)
    # Delivers an attack with a potency of (job==30?(level>=84?140:100):100).
    # (job==30?(level>=84?200:160):160) when executed from a target's rear.
    # Combo Action: Gust Slash
    # Combo Potency: (job==30?(level>=84?360:320):320)
    # Rear Combo Potency: (job==30?(level>=84?420:380):380)(job==30?(level>=62?
    # Combo Bonus: Increases Ninki Gauge by (job==30?(level>=84?15:(job==30?(level>=78?10:5):5)):(job==30?(level>=78?10:5):5)):):)
    id = 2255
    names = ['旋风刃(NIN)', 'Aeolian Edge(NIN)']
    _orig_names = ['旋风刃', 'Aeolian Edge']
    combo_action = 2242
    damage = "(job==30?(lv>=84?140:100):100)"
    combo_damage = "(job==30?(lv>=84?360:320):320)"
    back_damage = "(job==30?(lv>=84?200:160):160)"
    back_combo_damage = "(job==30?(lv>=84?420:380):380)"


class Action2258(Action):
    # 对目标发动物理攻击
    # 威力：300
    # 追加效果：受伤加重
    # 持续时间：15秒
    # 受伤加重效果：目标所受伤害提高5%
    # 背面攻击威力：400
    # 发动条件：隐遁
    # Delivers an attack with a potency of 300.
    # 400 when executed from a target's rear.
    # Additional Effect: Increases target's damage taken by 5%
    # Duration: 15s
    # Can only be executed while under the effect of Hidden.
    # related: [攻其不备](Status2014), 
    id = 2258
    names = ['攻其不备(NIN)', 'Trick Attack(NIN)']
    _orig_names = ['攻其不备', 'Trick Attack']
    damage = 300
    # remain metas: {'taken_dmg_increase': '5%', 'back_dmg_ot': '400'}


class Action2259(Action):
    # 结成天之印手势
    # 持续时间：6秒
    # 积蓄次数：2
    # 此能力类技能有单独计算的复唱时间
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “heaven.”
    # Duration: 6s
    # Maximum Charges: 2
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 2259
    names = ['Ten(NIN)(0)', '天之印(NIN)(0)']
    _orig_names = ['天之印', 'Ten']


class Action2260(Action):
    # 发动忍术，忍术的具体效果随之前结印的顺序有所不同
    # 在结印状态下发动其他技能会导致忍术失败
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # 此外发动隐遁后若处于非战斗状态则重置2次忍术的复唱时间
    # Executes a specific ninjutsu action coinciding with the combination of mudra made immediately beforehand.
    # If any other action is used before the mudra are combined and the ninjutsu executed, Ninjutsu will fail.
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    # related: [结印](Status496), 
    id = 2260
    names = ['忍术(NIN)', 'Ninjutsu(NIN)']
    _orig_names = ['忍术', 'Ninjutsu']


class Action2261(Action):
    # 结成地之印手势
    # 持续时间：6秒
    # 积蓄次数：2
    # 此能力类技能有单独计算的复唱时间
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “earth.”
    # Duration: 6s
    # Maximum Charges: 2
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 2261
    names = ['Chi(NIN)(0)', '地之印(NIN)(0)']
    _orig_names = ['地之印', 'Chi']


class Action2262(Action):
    # 迅速移动到指定地点
    # (job==30?(level>=74?积蓄次数：2
    # :):)止步状态下无法发动
    # Move quickly to the specified location.
    # (job==30?(level>=74?Maximum Charges: 2
    # :):)Cannot be executed while bound.
    id = 2262
    names = ['Shukuchi(NIN)', '缩地(NIN)']
    _orig_names = ['缩地', 'Shukuchi']


class Action2263(Action):
    # 结成人之印手势
    # 持续时间：6秒
    # 积蓄次数：2
    # 此能力类技能有单独计算的复唱时间
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “man.”
    # Duration: 6s
    # Maximum Charges: 2
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 2263
    names = ['Jin(NIN)(0)', '人之印(NIN)(0)']
    _orig_names = ['人之印', 'Jin']


class Action2264(Action):
    # 一定时间内，可以无视天之印、地之印、人之印的积累次数发动1次忍术
    # 在效果中发动的忍术威力提高30%
    # 持续时间：15秒
    # Allows the execution of a single ninjutsu without consumption of mudra charges.
    # Additional Effect: Increases damage for the next ninjutsu action by 30%
    # Duration: 15s
    # Recast timer of mudra is not affected by the execution of this action.
    # related: [生杀予夺](Status497), 
    id = 2264
    names = ['Kassatsu(NIN)', '生杀予夺(NIN)']
    _orig_names = ['Kassatsu', '生杀予夺']


class Action2265(Action):
    # 对目标发动远距离物理攻击
    # 威力：450
    # 发动条件：结成“天之印”“地之印”“人之印”任意一种印的状态下发动忍术
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers a ranged ninjutsu attack with a potency of 450.
    # Mudra Combination: Any one of the Ten, Chi, or Jin mudra
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 2265
    names = ['风魔手里剑(NIN)(0)', 'Fuma Shuriken(NIN)(0)']
    _orig_names = ['风魔手里剑', 'Fuma Shuriken']
    damage = 450


class Action2266(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：350
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “地之印”→“天之印”或
    # “人之印”→“天之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 350 to target and all enemies nearby it.
    # Mudra Combination: Chi→Ten or Jin→Ten
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 2266
    names = ['Katon(NIN)(0)', '火遁之术(NIN)(0)']
    _orig_names = ['Katon', '火遁之术']
    damage = 350


class Action2267(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：650
    # (job==30?(level>=90?追加效果：月影雷兽预备
    # 积蓄次数：3 
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失
    # :):)发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“地之印”或
    # “人之印”→“地之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals lightning damage with a potency of 650.
    # (job==30?(level>=90?Additional Effect: Grants a stack of Raiju Ready
    # Duration: 30s
    # Maximum Stacks: 3
    # :):)Mudra Combination: Ten→Chi or Jin→Chi
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 2267
    names = ['Raiton(NIN)(0)', '雷遁之术(NIN)(0)']
    _orig_names = ['Raiton', '雷遁之术']
    damage = 650


class Action2268(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：350
    # 追加效果：止步
    # 持续时间：15秒
    # 发动之后会停止自动攻击
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“人之印”或
    # “地之印”→“人之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals ice damage with a potency of 350.
    # Additional Effect: Bind
    # Duration: 15s
    # Mudra Combination: Ten→Jin or Chi→Jin
    # Cancels auto-attack upon execution.
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 2268
    names = ['冰遁之术(NIN)(0)', 'Hyoton(NIN)(0)']
    _orig_names = ['冰遁之术', 'Hyoton']
    damage = 350


class Action2269(Action):
    # 自身的自动攻击间隔、战技的复唱时间缩短15%
    # 持续时间：60秒
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “人之印”→“地之印”→“天之印”或
    # “地之印”→“人之印”→“天之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Reduces weaponskill recast time and auto-attack delay by 15%.
    # Duration: 60s
    # Mudra Combination: Jin→Chi→Ten or Chi→Jin→Ten
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [风遁之术](Status500), 
    id = 2269
    names = ['Huton(NIN)(0)', '风遁之术(NIN)(0)']
    _orig_names = ['风遁之术', 'Huton']


class Action2270(Action):
    # 以自身为中心产生伤害区域，范围内的敌人均会受到土属性伤害
    # 威力：70
    # 持续时间：24秒
    # 追加效果：范围内所有目标附加40%加重
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“人之印”→“地之印”或
    # “人之印”→“天之印”→“地之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Creates a patch of corrupted earth, dealing damage with a potency of 70 to any enemies who enter.
    # Duration: 24s
    # Additional Effect: Heavy +40%
    # Mudra Combination: Ten→Jin→Chi or Jin→Ten→Chi
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [土遁之术](Status501), 
    id = 2270
    names = ['土遁之术(NIN)(0)', 'Doton(NIN)(0)']
    _orig_names = ['土遁之术', 'Doton']
    damage = 70


class Action2271(Action):
    # 对目标发动水属性魔法攻击
    # 威力：500
    # 追加效果：水遁之术
    # 持续时间：20秒
    # 水遁之术效果：不用隐遁身形也能够发动需要在隐遁状态下发动的技能1次
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“地之印”→“人之印”或
    # “地之印”→“天之印”→“人之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals water damage with a potency of 500.
    # Additional Effect: Grants Suiton
    # Duration: 20s
    # Suiton Effect: Allows execution of actions which require the effect of Hidden, without being under that effect
    # Mudra Combination: Ten→Chi→Jin or Chi→Ten→Jin
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [隐遁(0)](Status1952), [隐遁(1)](Status1316), [隐遁(5)](Status614), [隐遁(3)](Status615), [隐遁(4)](Status1705), [隐遁(2)](Status1108), [水遁之术(0)](Status2839), [水遁之术(1)](Status507), 
    id = 2271
    names = ['Suiton(NIN)(0)', '水遁之术(NIN)(0)']
    _orig_names = ['Suiton', '水遁之术']
    damage = 500


class Action2272(Action):
    # 姆咕姆咕？姆咕姆咕？姆咕……
    # Thumpity thump thump, thumpity thump thump...
    id = 2272
    names = ['通灵之术(NIN)', 'Rabbit Medium(NIN)']
    _orig_names = ['通灵之术', 'Rabbit Medium']


class Action3563(Action):
    # 对目标发动物理攻击
    # 威力：(job==30?(level>=84?140:100):100)
    # 侧面攻击威力：(job==30?(level>=84?200:160):160)
    # 连击条件：绝风
    # 连击中威力：(job==30?(level>=84?340:300):300)
    # 连击中侧面攻击威力：(job==30?(level>=84?400:360):360)
    # 连击成功：风遁之术的持续时间延长30秒
    # 最多可延长至60秒(job==30?(level>=62?
    # 连击成功：获得(job==30?(level>=84?15:(job==30?(level>=78?10:5):5)):(job==30?(level>=78?10:5):5))点忍气:):)
    # Delivers an attack with a potency of (job==30?(level>=84?140:100):100).
    # (job==30?(level>=84?200:160):160) when executed from a target's flank.
    # Combo Action: Gust Slash
    # Combo Potency: (job==30?(level>=84?340:300):300)
    # Flank Combo Potency: (job==30?(level>=84?400:360):360)
    # Combo Bonus: Extends Huton duration by 30s to a maximum of 60s(job==30?(level>=62?
    # Combo Bonus: Increases Ninki Gauge by (job==30?(level>=84?15:(job==30?(level>=78?10:5):5)):(job==30?(level>=78?10:5):5)):):)
    id = 3563
    names = ['Armor Crush(NIN)', '强甲破点突(NIN)']
    _orig_names = ['强甲破点突', 'Armor Crush']
    combo_action = 2242
    damage = "(job==30?(lv>=84?140:100):100)"
    combo_damage = "(job==30?(lv>=84?340:300):300)"
    side_damage = "(job==30?(lv>=84?200:160):160)"
    side_combo_damage = "(job==30?(lv>=84?400:360):360)"


class Action3566(Action):
    # 对目标发动连续3次物理攻击
    # 威力：150
    # Delivers a threefold attack, each hit with a potency of 150.
    id = 3566
    names = ['梦幻三段(NIN)', 'Dream Within a Dream(NIN)']
    _orig_names = ['梦幻三段', 'Dream Within a Dream']
    damage = 150


class Action7401(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：160
    # 发动条件：忍气50点
    # 与六道轮回共享复唱时间
    # Deals fire damage with a potency of 160 to target and all enemies nearby it.
    # Ninki Gauge Cost: 50
    # Shares a recast timer with Bhavacakra.
    id = 7401
    names = ['通灵之术·大虾蟆(NIN)', 'Hellfrog Medium(NIN)']
    _orig_names = ['Hellfrog Medium', '通灵之术·大虾蟆']
    damage = 160


class Action7402(Action):
    # 对目标发动无属性魔法攻击
    # 威力：400
    # (job==30?(level>=88?命水状态中威力：500
    # :):)发动条件：忍气50点
    # 与通灵之术·大虾蟆共享复唱时间
    # Deals unaspected damage with a potency of 400.
    # (job==30?(level>=88?Meisui Bonus: Potency is increased to 500 when under the effect of Meisui
    # :):)Ninki Gauge Cost: 50
    # Shares a recast timer with Hellfrog Medium.
    # related: [命水](Status2689), 
    id = 7402
    names = ['Bhavacakra(NIN)', '六道轮回(NIN)']
    _orig_names = ['Bhavacakra', '六道轮回']
    damage = 400


class Action7403(Action):
    # 一定时间内，天之印、地之印、人之印变为忍术
    # 每次发动忍术后会变为别的忍术，最多可发动3种忍术
    # 持续时间：6秒
    # 效果时间内无法发动忍术之外的技能，移动后会立即解除天地人
    # 发动条件：非生杀予夺状态中
    # Temporarily converts each of the three mudra into a ninjutsu action. Executing one of these actions will convert the remaining mudra into different ninjutsu actions until all three have been executed or the Ten Chi Jin effect expires.
    # Duration: 6s
    # Only ninjutsu available while active. The same ninjutsu cannot be executed twice.
    # Cannot be executed while under the effect of Kassatsu. Effect ends upon moving.
    # related: [生杀予夺](Status497), [天地人](Status1186), 
    id = 7403
    names = ['天地人(NIN)', 'Ten Chi Jin(NIN)']
    _orig_names = ['Ten Chi Jin', '天地人']


class Action8807(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：获得10点忍气
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Increases Ninki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8807
    names = ['双刃旋(pvp)(NIN)', 'Spinning Edge(pvp)(NIN)']
    _orig_names = ['双刃旋(pvp)', 'Spinning Edge(pvp)']
    damage = 1000


class Action8808(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：双刃旋
    # 连击成功：获得10点忍气
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Spinning Edge
    # Combo Potency: 1,200
    # Combo Bonus: Increases Ninki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8808
    names = ['绝风(pvp)(NIN)', 'Gust Slash(pvp)(NIN)']
    _orig_names = ['Gust Slash(pvp)', '绝风(pvp)']
    combo_action = 8807
    combo_damage = 1200


class Action8809(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：绝风
    # 连击成功：获得10点忍气
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Gust Slash
    # Combo Potency: 1,400
    # Combo Bonus: Increases Ninki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8809
    names = ['Aeolian Edge(pvp)(NIN)', '旋风刃(pvp)(NIN)']
    _orig_names = ['旋风刃(pvp)', 'Aeolian Edge(pvp)']
    combo_action = 8808
    combo_damage = 1400


class Action8811(Action):
    # 对目标发动远距离物理攻击
    # 威力：800
    # 追加效果：获得10点忍气
    # Delivers a ranged attack with a potency of 800.
    # Additional Effect: Increases Ninki Gauge by 10
    id = 8811
    names = ['飞刀(pvp)(NIN)', 'Throwing Dagger(pvp)(NIN)']
    _orig_names = ['飞刀(pvp)', 'Throwing Dagger(pvp)']
    damage = 800


class Action8812(Action):
    # 迅速移动到指定地点
    # 追加效果：为自身附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力2000的伤害量
    # 持续时间：6秒止步状态下无法发动
    # 积蓄次数：2
    # Move quickly to the specified location.
    # Additional Effect: Creates a barrier around self that absorbs damage equivalent to a heal of 2,000 potency
    # Duration: 6s
    # Maximum Charges: 2
    # Cannot be executed while bound.
    id = 8812
    names = ['缩地(pvp)(NIN)', 'Shukuchi(pvp)(NIN)']
    _orig_names = ['缩地(pvp)', 'Shukuchi(pvp)']
    # remain metas: {'shield': '恢复力2000'}


class Action8814(Action):
    # 对目标发动物理攻击
    # 威力：1000～3000
    # 目标剩余体力越低威力越大
    # 击倒敌人或拿到助攻时重置复唱时间
    # Delivers an attack with a potency of 1,000.
    # Potency increases up to 3,000 as the target's HP decreases.
    # Recast time resets upon earning a kill or an assist.
    # related: [断绝](Status1314), 
    id = 8814
    names = ['Assassinate(pvp)(NIN)', '断绝(pvp)(NIN)']
    _orig_names = ['Assassinate(pvp)', '断绝(pvp)']
    damage = [1000, 3000]


class Action8815(Action):
    # 对目标发动魔法攻击
    # 威力：2000
    # 发动条件：忍气50点
    # Deals unaspected damage with a potency of 2,000.
    # Ninki Gauge Cost: 50
    id = 8815
    names = ['六道轮回(pvp)(NIN)', 'Bhavacakra(pvp)(NIN)']
    _orig_names = ['六道轮回(pvp)', 'Bhavacakra(pvp)']
    damage = 2000


class Action8816(Action):
    # 进入可以发动忍术的状态
    # 持续时间：5秒
    # 积蓄次数：2
    # Allows for immediate execution of any ninjutsu action.
    # Duration: 5s
    # Maximum Charges: 2
    # related: [三印自在](Status1317), 
    id = 8816
    names = ['Three Mudra(pvp)(NIN)', '三印自在(pvp)(NIN)']
    _orig_names = ['三印自在(pvp)', 'Three Mudra(pvp)']


class Action8820(Action):
    # 对自身附加隐身之术状态
    # 持续时间：3秒
    # 隐身之术的持续时间结束后，对自身附加隐遁状态
    # 持续时间：10秒
    # 隐身之术及隐遁状态在发动缩地和疾跑之外的技能或受到敌人攻击后会消失
    # 隐遁状态中无法被敌人看到，也不会成为目标
    # ※“隐遁”状态中该技能变为“攻其不备”
    # Grants the effect of Kakuremi.
    # Duration: 3s
    # Kakuremi will change to Hidden when the effect expires.
    # Duration: 10s
    # Cannot be seen or targeted while under the effect of Hidden.
    # Effects of Kakuremi and Hidden end upon taking damage or using an action other than Shukuchi or Bolt.
    # ※Action changes to Trick Attack while under the effect of Hidden.
    # related: [隐遁(0)](Status1952), [隐身之术](Status1315), [隐遁(1)](Status1316), [隐遁(5)](Status614), [隐遁(3)](Status615), [隐遁(4)](Status1705), [隐遁(2)](Status1108), 
    id = 8820
    names = ['隐身之术(pvp)(NIN)', 'Kakuremi(pvp)(NIN)']
    _orig_names = ['隐身之术(pvp)', 'Kakuremi(pvp)']


class Action16488(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：血雨飞花
    # 连击中威力：120
    # 连击成功：风遁之术的持续时间延长10秒
    # 最多可延长至60秒(job==30?(level>=62?
    # 连击成功：获得5点忍气:):)
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: Death Blossom
    # Combo Potency: 120
    # Combo Bonus: Extends Huton duration by 10s to a maximum of 60s(job==30?(level>=62?
    # Combo Bonus: Increases Ninki Gauge by 5:):)
    id = 16488
    names = ['Hakke Mujinsatsu(NIN)', '八卦无刃杀(NIN)']
    _orig_names = ['Hakke Mujinsatsu', '八卦无刃杀']
    combo_action = 2254
    damage = 100
    combo_damage = 120


class Action16489(Action):
    # 消耗自身附加的水遁之术，获得50点忍气
    # (job==30?(level>=88?追加效果：命水
    # 持续时间：30秒
    # 命水效果：下一次发动的六道轮回威力提高到500
    # :):)发动条件：自身处于战斗状态及水遁之术状态中
    # Dispels Suiton, increasing the Ninki Gauge by 50.
    # (job==30?(level>=88?Additional Effect: Increases the potency of Bhavacakra to 500
    # Duration: 30s
    # :):)Can only be executed while in combat.
    # related: [命水](Status2689), [水遁之术(1)](Status507), [水遁之术(0)](Status2839), 
    id = 16489
    names = ['Meisui(NIN)', '命水(NIN)']
    _orig_names = ['命水', 'Meisui']


class Action16491(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：600
    # 发动条件：在生杀予夺效果时间内，按下列任意一种顺序结印后发动忍术
    # “地之印”→“天之印”或
    # “人之印”→“天之印
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 600 to target and all enemies nearby it.
    # Mudra Combination: Chi→Ten or Jin→Ten
    # Can only be executed while under the effect of Kassatsu.
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [生杀予夺](Status497), 
    id = 16491
    names = ['Goka Mekkyaku(NIN)', '劫火灭却之术(NIN)']
    _orig_names = ['劫火灭却之术', 'Goka Mekkyaku']
    damage = 600


class Action16492(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：1300
    # 发动条件：在生杀予夺效果时间内，按下列任意一种顺序结印后发动忍术
    # “天之印”→“人之印”或
    # “地之印”→“人之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals ice damage with a potency of 1,300.
    # Mudra Combination: Chi→Jin or Ten→Jin
    # Can only be executed while under the effect of Kassatsu.
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [生杀予夺](Status497), 
    id = 16492
    names = ['冰晶乱流之术(NIN)', 'Hyosho Ranryu(NIN)']
    _orig_names = ['冰晶乱流之术', 'Hyosho Ranryu']
    damage = 1300


class Action16493(Action):
    # 对自身附加5档的分身之术状态
    # 持续时间：30秒
    # 分身之术效果：使用战技后，自身的分身会出现并加以追击
    # 分身不受连击影响，且攻击威力固定
    # 近身攻击威力：160
    # 远程攻击威力：160
    # 范围攻击威力：80
    # 分身的攻击命中时自身获得5点忍气
    # (job==30?(level>=82?追加效果：为自身附加残影镰鼬预备状态，且该技能变为残影镰鼬
    # 持续时间：45秒
    # :):)发动条件：忍气50点
    # 
    # Grants 5 stacks of Bunshin, each stack allowing your shadow to attack enemies each time you execute a weaponskill. Shadow attack potency varies based on the attack executed, but is not affected by combo bonuses.
    # Melee Attack Potency: 160
    # Ranged Attack Potency: 160
    # Area Attack Potency: 80
    # Ninki Gauge increases by 5 each time your shadow lands an attack.
    # Duration: 30s
    # (job==30?(level>=82?Additional Effect: Grants Phantom Kamaitachi Ready
    # Duration: 45s
    # :):)Ninki Gauge Cost: 50(job==30?(level>=82?
    # ※Action changes to Phantom Kamaitachi upon execution.:):)
    # related: [分身之术(0)](Status1954), [残影镰鼬预备](Status2723), [分身之术(1)](Status2010), 
    id = 16493
    names = ['分身之术(NIN)', 'Bunshin(NIN)']
    _orig_names = ['Bunshin', '分身之术']
    damage = 80 # TODO: [80, 160]
    # remain metas: {'dmg_ot': '160'}


class Action17731(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1200
    # 发动条件：忍气50点
    # Deals unaspected damage with a potency of 1,200 to target and all enemies nearby it.
    # Ninki Gauge Cost: 50
    id = 17731
    names = ['Hellfrog Medium(pvp)(NIN)', '通灵之术·大虾蟆(pvp)(NIN)']
    _orig_names = ['Hellfrog Medium(pvp)', '通灵之术·大虾蟆(pvp)']
    damage = 1200


class Action17732(Action):
    # 对目标及其周围的敌人发动魔法攻击
    # 威力：1200
    # 追加效果：每命中一个目标都会获得10点忍气
    # 追加效果：风遁之术
    # 持续时间：35秒
    # 风遁之术效果：自身战技的复唱时间缩短15%
    # 发动条件：三印自在
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Increases Ninki Gauge by 10 for each enemy hit
    # Additional Effect: Grants Huton, reducing weaponskill recast time by 15%
    # Duration: 35s
    # Can only be executed while under the effect of Three Mudra.
    # ※This action cannot be assigned to a hotbar.
    # related: [风遁之术](Status500), 
    id = 17732
    names = ['Goka Mekkyaku(pvp)(NIN)', '劫火灭却之术(pvp)(NIN)']
    _orig_names = ['劫火灭却之术(pvp)', 'Goka Mekkyaku(pvp)']
    damage = 1200


class Action17733(Action):
    # 对目标发动魔法攻击
    # 威力：2000
    # 追加效果：获得20点忍气
    # 追加效果：风遁之术
    # 持续时间：35秒
    # 风遁之术效果：自身战技的复唱时间缩短15%
    # 发动条件：三印自在
    # ※该技能无法设置到热键栏
    # Deals ice damage with a potency of 2,000.
    # Additional Effect: Increases Ninki Gauge by 20
    # Additional Effect: Grants Huton, reducing weaponskill recast time by 15%
    # Duration: 35s
    # Can only be executed while under the effect of Three Mudra.
    # ※This action cannot be assigned to a hotbar.
    # related: [风遁之术](Status500), 
    id = 17733
    names = ['Hyosho Ranryu(pvp)(NIN)', '冰晶乱流之术(pvp)(NIN)']
    _orig_names = ['Hyosho Ranryu(pvp)', '冰晶乱流之术(pvp)']
    damage = 2000


class Action17734(Action):
    # 效果时间内使用战技后，自身的分身会出现并加以追击
    # 持续时间结束或发动3次战技后取消该状态
    # 持续时间：10秒
    # 分身攻击威力固定
    # 近身攻击威力：1000
    # 远程攻击威力：600
    # 范围攻击威力：800
    # 分身的攻击命中时自身获得10点忍气
    # For up to three attacks, your shadow becomes animate, attacking enemies each time you execute a weaponskill. Ninki Gauge increases by 10 each time your shadow lands an attack.
    # Shadow attack potency varies based on the attack executed.
    # Melee Attack Potency: 1,000
    # Ranged Attack Potency: 800
    # Area Attack Potency: 600
    # Duration: 10s
    # related: [分身之术(1)](Status2010), [分身之术(0)](Status1954), 
    id = 17734
    names = ['分身之术(pvp)(NIN)', 'Bunshin(pvp)(NIN)']
    _orig_names = ['分身之术(pvp)', 'Bunshin(pvp)']
    damage = 600 # TODO: [600, 800]
    # remain metas: {'dmg_ot': '1000'}


class Action17735(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 追加效果：目标所受伤害提高10%
    # 持续时间：6秒
    # 发动条件：隐遁状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Increases target's damage taken by 10%
    # Duration: 6s
    # Can only be executed while under the effect of Hidden.
    # ※This action cannot be assigned to a hotbar.
    # related: [隐遁(0)](Status1952), [隐遁(1)](Status1316), [隐遁(2)](Status1108), [隐遁(5)](Status614), [隐遁(3)](Status615), [隐遁(4)](Status1705), [攻其不备](Status2014), 
    id = 17735
    names = ['攻其不备(pvp)(NIN)', 'Trick Attack(pvp)(NIN)']
    _orig_names = ['Trick Attack(pvp)', '攻其不备(pvp)']
    damage = 1200
    # remain metas: {'taken_dmg_increase': '10%'}


class Action18805(Action):
    # 结成天之印手势
    # 持续时间：6秒
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “heaven.”
    # Duration: 6s
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 18805
    names = ['Ten(NIN)(1)', '天之印(NIN)(1)']
    _orig_names = ['天之印', 'Ten']


class Action18806(Action):
    # 结成地之印手势
    # 持续时间：6秒
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “earth.”
    # Duration: 6s
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 18806
    names = ['地之印(NIN)(1)', 'Chi(NIN)(1)']
    _orig_names = ['地之印', 'Chi']


class Action18807(Action):
    # 结成人之印手势
    # 持续时间：6秒
    # 此能力类技能发动时会受到公共复唱时间的影响
    # 此能力类技能发动后会产生公共复唱时间
    # Make the ritual mudra hand gesture for “man.”
    # Duration: 6s
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # Conversely, execution of weaponskills triggers the cooldown of this action.
    id = 18807
    names = ['人之印(NIN)(1)', 'Jin(NIN)(1)']
    _orig_names = ['人之印', 'Jin']


class Action18873(Action):
    # 对目标发动远距离物理攻击
    # 威力：450
    # 发动条件：结成“天之印”“地之印”“人之印”任意一种印的状态下发动忍术
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers a ranged ninjutsu attack with a potency of 450.
    # Mudra Combination: Any one of the Ten, Chi, or Jin mudra
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18873
    names = ['风魔手里剑(NIN)(1)', 'Fuma Shuriken(NIN)(1)']
    _orig_names = ['风魔手里剑', 'Fuma Shuriken']
    damage = 450


class Action18874(Action):
    # 对目标发动远距离物理攻击
    # 威力：450
    # 发动条件：结成“天之印”“地之印”“人之印”任意一种印的状态下发动忍术
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers a ranged ninjutsu attack with a potency of 450.
    # Mudra Combination: Any one of the Ten, Chi, or Jin mudra
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18874
    names = ['风魔手里剑(NIN)(2)', 'Fuma Shuriken(NIN)(2)']
    _orig_names = ['风魔手里剑', 'Fuma Shuriken']
    damage = 450


class Action18875(Action):
    # 对目标发动远距离物理攻击
    # 威力：450
    # 发动条件：结成“天之印”“地之印”“人之印”任意一种印的状态下发动忍术
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers a ranged ninjutsu attack with a potency of 450.
    # Mudra Combination: Any one of the Ten, Chi, or Jin mudra
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18875
    names = ['Fuma Shuriken(NIN)(3)', '风魔手里剑(NIN)(3)']
    _orig_names = ['风魔手里剑', 'Fuma Shuriken']
    damage = 450


class Action18876(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：350
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “地之印”→“天之印”或
    # “人之印”→“天之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers fire damage with a potency of 350 to target and all enemies nearby it.
    # Mudra Combination: Chi→Ten or Jin→Ten
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18876
    names = ['Katon(NIN)(1)', '火遁之术(NIN)(1)']
    _orig_names = ['Katon', '火遁之术']
    damage = 350


class Action18877(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：650
    # (job==30?(level>=90?追加效果：月影雷兽预备
    # 积蓄次数：3
    # 持续时间：30秒
    # 发动近身攻击战技会导致该效果消失
    # :):)发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“地之印”或
    # “人之印”→“地之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals lightning damage with a potency of 650.
    # (job==30?(level>=90?Additional Effect: Grants a stack of Raiju Ready
    # Duration: 30s
    # Maximum Stacks: 3
    # :):)Mudra Combination: Ten→Chi or Jin→Chi
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18877
    names = ['雷遁之术(NIN)(1)', 'Raiton(NIN)(1)']
    _orig_names = ['Raiton', '雷遁之术']
    damage = 650


class Action18878(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：350
    # 追加效果：止步
    # 持续时间：15秒
    # 发动之后会停止自动攻击
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“人之印”或
    # “地之印”→“人之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Delivers ice damage with a potency of 350.
    # Additional Effect: Bind
    # Duration: 15s
    # Mudra Combination: Ten→Jin or Chi→Jin
    # Cancels auto-attack upon execution.
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    id = 18878
    names = ['冰遁之术(NIN)(1)', 'Hyoton(NIN)(1)']
    _orig_names = ['冰遁之术', 'Hyoton']
    damage = 350


class Action18879(Action):
    # 自身的自动攻击间隔、战技的复唱时间缩短15%
    # 持续时间：60秒
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “人之印”→“地之印”→“天之印”或
    # “地之印”→“人之印”→“天之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Reduces weaponskill recast time and auto-attack delay by 15%.
    # Duration: 60s
    # Mudra Combination: Jin→Chi→Ten or Chi→Jin→Ten
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [风遁之术](Status500), 
    id = 18879
    names = ['Huton(NIN)(1)', '风遁之术(NIN)(1)']
    _orig_names = ['风遁之术', 'Huton']


class Action18880(Action):
    # 以自身为中心产生伤害区域，范围内的敌人均会受到土属性伤害
    # 威力：70
    # 持续时间：24秒
    # 追加效果：范围内所有目标附加40%加重
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“人之印”→“地之印”或
    # “人之印”→“天之印”→“地之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Creates a patch of corrupted earth, dealing damage with a potency of 70 to any enemies who enter.
    # Duration: 24s
    # Additional Effect: Heavy +40%
    # Mudra Combination: Ten→Jin→Chi or Jin→Ten→Chi
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [土遁之术](Status501), 
    id = 18880
    names = ['土遁之术(NIN)(1)', 'Doton(NIN)(1)']
    _orig_names = ['土遁之术', 'Doton']
    damage = 70


class Action18881(Action):
    # 对目标发动水属性魔法攻击
    # 威力：500
    # 追加效果：水遁之术
    # 持续时间：20秒
    # 水遁之术效果：不用隐遁身形也能够发动需要在隐遁状态下发动的技能1次
    # 发动条件：按下列任意一种顺序结印后发动忍术
    # “天之印”→“地之印”→“人之印”或
    # “地之印”→“天之印”→“人之印”
    # 此能力类技能发动后会产生公共复唱时间
    # ※该技能无法设置到热键栏
    # Deals water damage with a potency of 500.
    # Additional Effect: Grants Suiton
    # Duration: 20s
    # Suiton Effect: Allows execution of actions which require the effect of Hidden, without being under that effect
    # Mudra Combination: Ten→Chi→Jin or Chi→Ten→Jin
    # Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [隐遁(0)](Status1952), [隐遁(1)](Status1316), [隐遁(5)](Status614), [隐遁(3)](Status615), [隐遁(4)](Status1705), [隐遁(2)](Status1108), [水遁之术(0)](Status2839), [水遁之术(1)](Status507), 
    id = 18881
    names = ['水遁之术(NIN)(1)', 'Suiton(NIN)(1)']
    _orig_names = ['Suiton', '水遁之术']
    damage = 500


class Action18921(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：600
    # 追加效果：获得10点忍气
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Increases Ninki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 18921
    names = ['血雨飞花(pvp)(NIN)', 'Death Blossom(pvp)(NIN)']
    _orig_names = ['Death Blossom(pvp)', '血雨飞花(pvp)']
    damage = 600


class Action18922(Action):
    # 对自身周围的敌人发动物理攻击
    # 连击中威力：800
    # 连击条件：血雨飞花
    # 连击成功：获得10点忍气
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Death Blossom
    # Combo Potency: 800
    # Combo Bonus: Increases Ninki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 18922
    names = ['八卦无刃杀(pvp)(NIN)', 'Hakke Mujinsatsu(pvp)(NIN)']
    _orig_names = ['Hakke Mujinsatsu(pvp)', '八卦无刃杀(pvp)']
    combo_action = 18921
    combo_damage = 800


class Action18987(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：800
    # 追加效果：沉默
    # 持续时间：1秒
    # Delivers an attack with a potency of 800 to all nearby enemies.
    # Additional Effect: Silence
    # Duration: 1s
    # related: [沉默(0)](Status1347), [沉默(1)](Status1060), [沉默(2)](Status7), 
    id = 18987
    names = ['尘卷(pvp)(NIN)', 'Ill Wind(pvp)(NIN)']
    _orig_names = ['尘卷(pvp)', 'Ill Wind(pvp)']
    damage = 800


class Action25774(Action):
    # 自身的分身对目标及其周围5米以内的敌人发动风属性范围魔法攻击
    # 威力：550
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：风遁之术的持续时间延长10秒
    # 最多可延长至60秒
    # 连击成功：获得10点忍气
    # 发动条件：发动分身之术后为自身附加的残影镰鼬预备状态中
    # ※该技能无法设置到热键栏
    # Your shadow deals wind damage to all enemies within 5 yalms with a potency of 550 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Extends Huton duration by 10s to a maximum of 60s
    # Additional Effect: Increases Ninki Gauge by 10
    # Can only be executed while under the effect of Phantom Kamaitachi Ready.
    # ※This action cannot be assigned to a hotbar.
    # related: [残影镰鼬预备](Status2723), 
    id = 25774
    names = ['Phantom Kamaitachi(NIN)', '残影镰鼬(NIN)']
    _orig_names = ['Phantom Kamaitachi', '残影镰鼬']
    damage = 550
    # remain metas: {'aoe_reduce': '50%'}


class Action25776(Action):
    # 在自身发动的土遁之术持续时间内通过连击发动八卦无刃杀、残影镰鼬或发动火遁之术、劫火灭却之术时，对土遁之术范围内的敌人发动土属性魔法攻击
    # 威力：50
    # ※该技能无法设置到热键栏
    # All enemies standing in the corrupted earth of Doton take additional earth damage with a potency of 50.
    # Requires Hakke Mujinsatsu to be executed as a combo action or upon executing Katon, Goka Mekkyaku, or Phantom Kamaitachi.
    # Effect can only be triggered while Doton is active.
    # ※This action cannot be assigned to a hotbar.
    id = 25776
    names = ['Hollow Nozuchi(NIN)', '幻影野槌(NIN)']
    _orig_names = ['幻影野槌', 'Hollow Nozuchi']
    # remain metas: {'dmg_ot': '50'}


class Action25777(Action):
    # 冲向目标并发动雷属性魔法攻击
    # 威力：560
    # 追加效果：获得5点忍气
    # 发动条件：月影雷兽预备状态中
    # 止步状态下无法发动
    # Rushes target and delivers a lightning attack with a potency of 560.
    # Additional Effect: Increases Ninki Gauge by 5
    # Can only be executed while under the effect of Raiju Ready.
    # Cannot be executed while bound.
    # related: [月影雷兽预备](Status2690), 
    id = 25777
    names = ['Forked Raiju(NIN)', '月影雷兽爪(NIN)']
    _orig_names = ['Forked Raiju', '月影雷兽爪']
    damage = 560


class Action25778(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：560
    # 追加效果：获得5点忍气
    # 发动条件：月影雷兽预备状态中
    # Deals lightning damage with a potency of 560.
    # Additional Effect: Increases Ninki Gauge by 5
    # Can only be executed while under the effect of Raiju Ready.
    # related: [月影雷兽预备](Status2690), 
    id = 25778
    names = ['Fleeting Raiju(NIN)', '月影雷兽牙(NIN)']
    _orig_names = ['月影雷兽牙', 'Fleeting Raiju']
    damage = 560


class Action25876(Action):
    # 对目标发动物理攻击
    # 威力：200
    # 追加效果：风遁之术
    # 持续时间：60秒(job==30?(level>=62?
    # 追加效果：获得5点忍气:):)
    # Delivers an attack with a potency of 200.
    # Additional Effect: Grants Huton
    # Duration: 60s(job==30?(level>=62?
    # Additional Effect: Increases Ninki Gauge by 5:):)
    # related: [风遁之术](Status500), 
    id = 25876
    names = ['风来刃(NIN)', 'Huraijin(NIN)']
    _orig_names = ['风来刃', 'Huraijin']
    damage = 200


