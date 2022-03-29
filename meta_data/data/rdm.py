from ._base import *


class Status2012(Status):
    # 抵消一定伤害
    # A barrier is preventing damage.
    # related: [短兵相接(RDM)](Action7506), [短兵相接(pvp)(RDM)](Action8890),
    id = 2012
    names = ['短兵相接', 'Corps-a-corps']


class Status1234(Status):
    # 可以发动赤火炎
    # Able to cast Verfire.
    # related: [赤火炎(RDM)](Action7510),
    id = 1234
    names = ['赤火炎预备', 'Verfire Ready']


class Status1235(Status):
    # 可以发动赤飞石
    # Able to cast Verstone.
    # related: [赤飞石(RDM)](Action7511), [促进(RDM)](Action7518),
    id = 1235
    names = ['赤飞石预备', 'Verstone Ready']


class Status2013(Status):
    # 自身发动的下一个魔法造成的伤害提高
    # Next spell cast will deal increased damage.
    # related: [移转(RDM)](Action7515), [移转(pvp)(RDM)](Action8891),
    id = 2013
    names = ['移转', 'Displacement']


class Status1238(Status):
    # 下次发动(job==35?(level>=82?赤暴雷或赤暴风:赤闪雷或赤疾风):赤闪雷或赤疾风)、(job==35?(level>=66?冲击:散碎):散碎)不需要咏唱时间同时(job==35?(level>=66?冲击:散碎):散碎)的威力提高，发动(job==35?(level>=82?赤暴雷或赤暴风:赤闪雷或赤疾风):赤闪雷或赤疾风)必定为自身附加赤火炎预备或赤飞石预备状态
    # Next (job==35?(level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (job==35?(level>=66?Impact:Scatter):Scatter) can be cast immediately.
    # Potency of (job==35?(level>=66?Impact:Scatter):Scatter) is increased, and (job==35?(level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively.
    # related: [促进(RDM)](Action7518), [冲击(RDM)](Action16526),
    id = 1238
    names = ['促进', 'Acceleration']


class Status1971(Status):
    # 魔法攻击所造成的伤害提高
    # Magic damage dealt is increased.
    # related: [倍增(RDM)](Action7521),
    id = 1971
    names = ['倍增', 'Manafication']


class Status1498(Status):
    # 受到了强烈冲击，偶尔会无法行动，体力逐渐流失
    # Experiencing periodic immobility while bleeding HP over time.
    # related: [震荡(RDM)](Action7524),
    id = 1498
    names = ['震荡', 'Shocked']


class Status1249(Status):
    # 下次咏唱魔法不需要咏唱时间
    # Next spell will require no time to cast.
    # related: [赤飞石(pvp)(RDM)](Action8883), [赤火炎(pvp)(RDM)](Action8885), [赤治疗(pvp)(RDM)](Action10025), [散碎(pvp)(RDM)](Action17727),
    id = 1249
    names = ['连续咏唱', 'Dualcast']


# class Status1378(Status):
#     # 可连续发动魔法
#     # The next spell will be cast immediately.
#     # related: [赤飞石(pvp)(RDM)](Action8883), [赤火炎(pvp)(RDM)](Action8885), [赤治疗(pvp)(RDM)](Action10025), [散碎(pvp)(RDM)](Action17727),
#     id = 1378
#     names = ['连续咏唱(1)', 'Dualcast(1)']
#
#
# class Status1798(Status):
#     # 可连续发动魔法
#     # The next spell will be cast immediately.
#     # related: [赤飞石(pvp)(RDM)](Action8883), [赤火炎(pvp)(RDM)](Action8885), [赤治疗(pvp)(RDM)](Action10025), [散碎(pvp)(RDM)](Action17727),
#     id = 1798
#     names = ['连续咏唱(2)', 'Dualcast(2)']
#
#
# class Status1393(Status):
#     # 下次咏唱魔法不需要咏唱时间
#     # The next spell will be cast immediately.
#     # related: [赤飞石(pvp)(RDM)](Action8883), [赤火炎(pvp)(RDM)](Action8885), [赤治疗(pvp)(RDM)](Action10025), [散碎(pvp)(RDM)](Action17727),
#     id = 1393
#     names = ['连续咏唱(3)', 'Dualcast(3)']


class Status995(Status):
    # 受到冲击，攻击所造成的伤害降低，积累档数过多会被附加脑震荡状态
    # Suffering mild head trauma. Damage dealt is reduced. Increased trauma results in a Concussion.
    # related: [冲击(pvp)(RDM)](Action8886), [冲击(RDM)](Action16526),
    id = 995
    names = ['冲击', 'Headache']


class Status2033(Status):
    # 抵消一定伤害
    # A barrier is preventing damage.
    # related: [交剑(RDM)](Action16527), [交剑(pvp)(RDM)](Action17786),
    id = 2033
    names = ['交剑', 'Engagement']


class Status2707(Status):
    # 减轻所受到的魔法伤害，同时自身所受体力恢复效果提高
    # Magic damage taken is reduced and HP recovery via healing actions is increased.
    # related: [抗死(RDM)](Action25857),
    id = 2707
    names = ['抗死', 'Magick Barrier']


class Action7503(Action):
    # 对目标发动无属性魔法攻击
    # 威力：170
    # 追加效果：获得2点黑魔元与2点白魔元
    # Deals unaspected damage with a potency of 170.
    # Additional Effect: Increases both Black Mana and White Mana by 2
    id = 7503
    names = ['摇荡(RDM)', 'Jolt(RDM)']
    _orig_names = ['摇荡', 'Jolt']
    damage = 170


class Action7504(Action):
    # 对目标发动物理攻击
    # 威力：130(level>=2?(job==35?
    # 平衡量谱中黑魔元与白魔元都在20点以上时，该技能变为魔回刺:):)
    # Delivers an attack with a potency of 130.(level>=2?(job==35?
    # Action upgraded to Enchanted Riposte if both Black Mana and White Mana are at 20 or more.:):)
    id = 7504
    names = ['Riposte(RDM)', '回刺(RDM)']
    _orig_names = ['Riposte', '回刺']
    damage = 130


class Action7505(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：(job==35?(level>=62?360:300):300)
    # 追加效果：获得6点黑魔元(level>=26?(job==35?
    # 追加效果（发动几率50%）：赤火炎预备
    # 持续时间：30秒:):)
    # Deals lightning damage with a potency of (job==35?(level>=62?360:300):300).
    # Additional Effect: Increases Black Mana by 6(level>=26?(job==35?
    # Additional Effect: 50% chance of becoming Verfire Ready
    # Duration: 30s:):)
    id = 7505
    names = ['Verthunder(RDM)', '赤闪雷(RDM)']
    _orig_names = ['Verthunder', '赤闪雷']
    damage = "(job==35?(lv>=62?360:300):300)"


class Action7506(Action):
    # 冲向目标并发动物理攻击
    # 威力：130
    # 积蓄次数：2
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 130.
    # Maximum Charges: 2
    # Cannot be executed while bound.
    # related: [短兵相接](Status2012),
    id = 7506
    names = ['Corps-a-corps(RDM)', '短兵相接(RDM)']
    _orig_names = ['短兵相接', 'Corps-a-corps']
    damage = 130


class Action7507(Action):
    # 对目标发动风属性魔法攻击
    # 威力：(job==35?(level>=62?360:300):300)
    # 追加效果：获得6点白魔元(level>=30?(job==35?
    # 追加效果（发动几率50%）：赤飞石预备
    # 持续时间：30秒:):)
    # Deals wind damage with a potency of (job==35?(level>=62?360:300):300).
    # Additional Effect: Increases White Mana by 6(level>=30?(job==35?
    # Additional Effect: 50% chance of becoming Verstone Ready
    # Duration: 30s:):)
    id = 7507
    names = ['Veraero(RDM)', '赤疾风(RDM)']
    _orig_names = ['Veraero', '赤疾风']
    damage = "(job==35?(lv>=62?360:300):300)"


class Action7509(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：120
    # (job==35?(level>=50?促进中威力：170
    # :):)追加效果：获得3点黑魔元与3点白魔元
    # Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
    # (job==35?(level>=50?Acceleration Potency: 170:):)
    # Additional Effect: Increases both Black Mana and White Mana by 3
    id = 7509
    names = ['Scatter(RDM)', '散碎(RDM)']
    _orig_names = ['Scatter', '散碎']
    damage = 120


class Action7510(Action):
    # 对目标发动火属性魔法攻击
    # 威力：(job==35?(level>=84?330:(job==35?(level>=62?300:260):260)):(job==35?(level>=62?300:260):260))
    # 追加效果：获得5点黑魔元
    # 发动条件：赤火炎预备状态中
    # Deals fire damage with a potency of (job==35?(level>=84?330:(job==35?(level>=62?300:260):260)):(job==35?(level>=62?300:260):260)).
    # Additional Effect: Increases Black Mana by 5
    # Can only be executed while Verfire Ready is active.
    # related: [赤火炎预备](Status1234),
    id = 7510
    names = ['Verfire(RDM)', '赤火炎(RDM)']
    _orig_names = ['赤火炎', 'Verfire']
    damage = "(job==35?(lv>=84?330:(job==35?(lv>=62?300:260):260)):(job==35?(lv>=62?300:260):260))"


class Action7511(Action):
    # 对目标发动土属性魔法攻击
    # 威力：(job==35?(level>=84?330:(job==35?(level>=62?300:260):260)):(job==35?(level>=62?300:260):260))
    # 追加效果：获得5点白魔元
    # 发动条件：赤飞石预备状态中
    # Deals earth damage with a potency of (job==35?(level>=84?330:(job==35?(level>=62?300:260):260)):(job==35?(level>=62?300:260):260)).
    # Additional Effect: Increases White Mana by 5
    # Can only be executed while Verstone Ready is active.
    # related: [赤飞石预备](Status1235),
    id = 7511
    names = ['Verstone(RDM)', '赤飞石(RDM)']
    _orig_names = ['赤飞石', 'Verstone']
    damage = "(job==35?(lv>=84?330:(job==35?(lv>=62?300:260):260)):(job==35?(lv>=62?300:260):260))"


class Action7512(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：回刺或魔回刺
    # 连击中威力：150
    # 平衡量谱中黑魔元与白魔元都在15点以上时，该技能变为魔交击斩
    # Delivers an attack with a potency of 100.
    # Combo Action: Riposte or Enchanted Riposte
    # Combo Potency: 150
    # Action upgraded to Enchanted Zwerchhau if both Black Mana and White Mana are at 15 or more.
    id = 7512
    names = ['Zwerchhau(RDM)', '交击斩(RDM)']
    _orig_names = ['交击斩', 'Zwerchhau']
    combo_action = 7504
    damage = 100
    combo_damage = 150


class Action7513(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：60
    # 平衡量谱中黑魔元与白魔元都在20点以上时，该技能变为魔划圆斩
    # Delivers an attack with a potency of 60 to all enemies in a cone before you.
    # Action upgraded to Enchanted Moulinet if both Black Mana and White Mana are at 20 or more.
    id = 7513
    names = ['Moulinet(RDM)', '划圆斩(RDM)']
    _orig_names = ['划圆斩', 'Moulinet']
    damage = 60


class Action7514(Action):
    # 恢复目标的体力
    # 恢复力：350
    # Restores target's HP.
    # Cure Potency: 350
    id = 7514
    names = ['Vercure(RDM)', '赤治疗(RDM)']
    _orig_names = ['Vercure', '赤治疗']
    heal = 350


class Action7515(Action):
    # 对目标发动物理攻击
    # 威力：(job==35?(level>=72?180:130):130)
    # 追加效果：后跳15米距离
    # 积蓄次数：2
    # 止步状态下无法发动
    # 与交剑共享复唱时间
    # Delivers an attack with a potency of (job==35?(level>=72?180:130):130).
    # Additional Effect: 15-yalm backstep
    # Maximum Charges: 2
    # Cannot be executed while bound.
    # Shares a recast timer with Engagement.
    # related: [移转](Status2013),
    id = 7515
    names = ['Displacement(RDM)', '移转(RDM)']
    _orig_names = ['移转', 'Displacement']
    damage = "(job==35?(lv>=72?180:130):130)"


class Action7516(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：交击斩或魔交击斩
    # 连击中威力：230
    # 平衡量谱中黑魔元与白魔元都在15点以上时，该技能变为魔连攻
    # Delivers an attack with a potency of 100.
    # Combo Action: Zwerchhau or Enchanted Zwerchhau
    # Combo Potency: 230
    # Action upgraded to Enchanted Redoublement if both Black Mana and White Mana are at 15 or more.
    id = 7516
    names = ['连攻(RDM)', 'Redoublement(RDM)']
    _orig_names = ['连攻', 'Redoublement']
    combo_action = 7512
    damage = 100
    combo_damage = 230


class Action7517(Action):
    # 对目标发动物理攻击
    # 威力：460
    # Delivers an attack with a potency of 460.
    id = 7517
    names = ['Fleche(RDM)', '飞刺(RDM)']
    _orig_names = ['Fleche', '飞刺']
    damage = 460


class Action7518(Action):
    # 持续时间内发动1次(job==35?(level>=82?赤暴雷或赤暴风:赤闪雷或赤疾风):赤闪雷或赤疾风)、(job==35?(level>=66?冲击:散碎):散碎)不需要咏唱时间
    # 持续时间：20秒
    # 追加效果：(job==35?(level>=66?冲击:散碎):散碎)威力提高50
    # 追加效果：发动(job==35?(level>=82?赤暴雷或赤暴风:赤闪雷或赤疾风):赤闪雷或赤疾风)时，必定为自身附加赤火炎预备或赤飞石预备状态(job==35?(level>=88?
    # 积蓄次数：2:):)
    # Ensures the next (job==35?(level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (job==35?(level>=66?Impact:Scatter):Scatter) can be cast immediately.
    # Duration: 20s
    # Additional Effect: Increases the potency of (job==35?(level>=66?Impact:Scatter):Scatter) by 50
    # Additional Effect: Ensures (job==35?(level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively(job==35?(level>=88?
    # Maximum Charges: 2:):)
    # related: [赤飞石预备](Status1235), [促进](Status1238),
    id = 7518
    names = ['Acceleration(RDM)', '促进(RDM)']
    _orig_names = ['促进', 'Acceleration']


class Action7519(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：360
    # Delivers an attack with a potency of 360 to target and all enemies nearby it.
    id = 7519
    names = ['六分反击(RDM)', 'Contre Sixte(RDM)']
    _orig_names = ['Contre Sixte', '六分反击']
    damage = 360


class Action7520(Action):
    # 一定时间内，自身发动魔法攻击造成的伤害提高5%
    # 持续时间：20秒
    # 追加效果：令周围队员发动攻击造成的伤害提高5%
    # 持续时间：20秒
    # Increases own magic damage dealt by 5% and damage dealt by nearby party members by 5%.
    # Duration: 20s
    # related: [鼓励(0)](Status1297), [鼓励(1)](Status1239), [鼓励(2)](Status2282),
    id = 7520
    names = ['Embolden(RDM)', '鼓励(RDM)']
    _orig_names = ['鼓励', 'Embolden']
    # remain metas: {'dmg_increase': '5%'}


class Action7521(Action):
    # 获得50点黑魔元和白魔元
    # (job==35?(level>=78?追加效果：为自身附加(job==35?(level>=90?6:5):5)档倍增状态
    # 持续时间：15秒
    # 倍增效果：自身发动魔法攻击造成的伤害提高5%
    # :):)此技能会中断连击
    # 发动条件：自身处于战斗状态
    # Increases both Black Mana and White Mana by 50.
    # (job==35?(level>=78?Additional Effect: Grants (job==35?(level>=90?6:5):5) stacks of Manafication
    # Manafication Effect: Increases magic damage dealt by 5%
    # Duration: 15s
    # :):)All combos are canceled upon execution of Manafication.
    # Can only be executed while in combat.
    # related: [倍增](Status1971),
    id = 7521
    names = ['Manafication(RDM)', '倍增(RDM)']
    _orig_names = ['Manafication', '倍增']


class Action7523(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43),
    id = 7523
    names = ['赤复活(RDM)', 'Verraise(RDM)']
    _orig_names = ['Verraise', '赤复活']


class Action7524(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==35?(level>=84?310:280):280)
    # 追加效果：获得2点黑魔元与2点白魔元
    # Deals unaspected damage with a potency of (job==35?(level>=84?310:280):280).
    # Additional Effect: Increases both Black Mana and White Mana by 2
    # related: [震荡](Status1498),
    id = 7524
    names = ['Jolt II(RDM)', '震荡(RDM)']
    _orig_names = ['震荡', 'Jolt II']
    damage = "(job==35?(lv>=84?310:280):280)"


class Action7525(Action):
    # 对目标发动火属性魔法攻击
    # 威力：580
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 追加效果：获得11点黑魔元
    # 追加效果（发动几率20%）：赤火炎预备
    # 持续时间：30秒
    # 发动时白魔元高于黑魔元则100%发动追加效果
    # 发动条件：魔元集3档
    # ※该技能无法设置到热键栏
    # Deals fire damage to target and all enemies nearby it with a potency of 580 for the first enemy, and 60% less for all remaining enemies.
    # Additional Effect: Increases Black Mana by 11
    # Additional Effect: 20% chance of becoming Verfire Ready
    # Duration: 30s
    # Chance to become Verfire Ready increases to 100% if White Mana is higher than Black Mana at time of execution.
    # Mana Stack Cost: 3
    # ※This action cannot be assigned to a hotbar.
    id = 7525
    names = ['赤核爆(RDM)', 'Verflare(RDM)']
    _orig_names = ['Verflare', '赤核爆']
    damage = 580
    # remain metas: {'aoe_reduce': '60%'}


class Action7526(Action):
    # 对目标发动无属性魔法攻击
    # 威力：580
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 追加效果：获得11点白魔元
    # 追加效果（发动几率20%）：赤飞石预备
    # 持续时间：30秒
    # 发动时黑魔元高于白魔元则100%发动追加效果
    # 发动条件：魔元集3档
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 580 for the first enemy, and 60% less for all remaining enemies.
    # Additional Effect: Increases White Mana by 11
    # Additional Effect: 20% chance of becoming Verstone Ready
    # Duration: 30s
    # Chance to become Verstone Ready increases to 100% if Black Mana is higher than White Mana at time of execution.
    # Mana Stack Cost: 3
    # ※This action cannot be assigned to a hotbar.
    id = 7526
    names = ['赤神圣(RDM)', 'Verholy(RDM)']
    _orig_names = ['Verholy', '赤神圣']
    damage = 580
    # remain metas: {'aoe_reduce': '60%'}


class Action7527(Action):
    # 对目标发动无属性魔法攻击
    # 威力：220
    # (job==35?(level>=68?追加效果：为自身附加1档魔元集
    # :):)发动条件：黑魔元、白魔元各20点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 220.
    # (job==35?(level>=68?Additional Effect: Grants a Mana Stack
    # :):)Balance Gauge Cost: 20 Black Mana
    # Balance Gauge Cost: 20 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 7527
    names = ['魔回刺(RDM)', 'Enchanted Riposte(RDM)']
    _orig_names = ['Enchanted Riposte', '魔回刺']
    damage = 220


class Action7528(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 连击条件：回刺或魔回刺
    # 连击中威力：290
    # (job==35?(level>=68?追加效果：为自身附加1档魔元集
    # :):)发动条件：黑魔元、白魔元各15点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 100.
    # Combo Action: Riposte or Enchanted Riposte
    # Combo Potency: 290
    # (job==35?(level>=68?Additional Effect: Grants a Mana Stack
    # :):)Balance Gauge Cost: 15 Black Mana
    # Balance Gauge Cost: 15 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 7528
    names = ['Enchanted Zwerchhau(RDM)', '魔交击斩(RDM)']
    _orig_names = ['魔交击斩', 'Enchanted Zwerchhau']
    combo_action = 7504
    damage = 100
    combo_damage = 290


class Action7529(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 连击条件：魔交击斩
    # 连击中威力：470
    # (job==35?(level>=68?追加效果：为自身附加1档魔元集
    # :):)发动条件：黑魔元、白魔元各15点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 100.
    # Combo Action: Enchanted Zwerchhau
    # Combo Potency: 470
    # (job==35?(level>=68?Additional Effect: Grants a Mana Stack
    # :):)Balance Gauge Cost: 15 Black Mana
    # Balance Gauge Cost: 15 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 7529
    names = ['魔连攻(RDM)', 'Enchanted Redoublement(RDM)']
    _orig_names = ['魔连攻', 'Enchanted Redoublement']
    combo_action = 7512
    damage = 100
    combo_damage = 470


class Action7530(Action):
    # 向目标所在方向发出扇形范围魔法攻击
    # 威力：130
    # (job==35?(level>=68?追加效果：为自身附加1档魔元集
    # :):)发动条件：黑魔元、白魔元各20点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 130 to all enemies in a cone before you.
    # (job==35?(level>=68?Additional Effect: Grants a Mana Stack
    # :):)Balance Gauge Cost: 20 Black Mana
    # Balance Gauge Cost: 20 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 7530
    names = ['魔划圆斩(RDM)', 'Enchanted Moulinet(RDM)']
    _orig_names = ['魔划圆斩', 'Enchanted Moulinet']
    damage = 130


class Action8882(Action):
    # 对目标发动魔法攻击
    # 威力：1800
    # 追加效果：获得15点白魔元
    # 发动条件：连续咏唱
    # ※该技能无法设置到热键栏
    # Deals wind damage with a potency of 1,800.
    # Additional Effect: Increases White Mana by 15
    # Can only be cast while under the effect of Dualcast.
    # ※This action cannot be assigned to a hotbar.
    id = 8882
    names = ['Veraero(pvp)(RDM)', '赤疾风(pvp)(RDM)']
    _orig_names = ['赤疾风(pvp)', 'Veraero(pvp)']
    damage = 1800


class Action8883(Action):
    # 对目标发动魔法攻击
    # 威力：1400
    # 追加效果：获得10点白魔元
    # 追加效果：若该技能发动时需要咏唱时间，则对自身附加连续咏唱状态
    # 持续时间：10秒
    # “连续咏唱”效果：下次咏唱魔法不需要咏唱时间
    # ※“连续咏唱”状态中该技能变为“赤疾风”
    # ※“魔连攻”发动后该技能变为“赤神圣”
    # Deals earth damage with a potency of 1,400.
    # Additional Effect: Increases White Mana by 10
    # Additional Effect: Grants Dualcast when spell is cast with a cast time
    # Duration: 10s
    # ※Action changes to Veraero while under the effect of Dualcast.
    # ※Action changes to Verholy after execution of Enchanted Redoublement.
    # related: [连续咏唱(0)](Status1249), [连续咏唱(1)](Status1378), [连续咏唱(2)](Status1798), [连续咏唱(3)](Status1393),
    id = 8883
    names = ['Verstone(pvp)(RDM)', '赤飞石(pvp)(RDM)']
    _orig_names = ['Verstone(pvp)', '赤飞石(pvp)']
    damage = 1400


class Action8884(Action):
    # 对目标发动魔法攻击
    # 威力：1800
    # 追加效果：获得15点黑魔元
    # 发动条件：连续咏唱
    # ※该技能无法设置到热键栏
    # Deals lightning damage with a potency of 1,800.
    # Additional Effect: Increases Black Mana by 15
    # Can only be cast while under the effect of Dualcast.
    # ※This action cannot be assigned to a hotbar.
    id = 8884
    names = ['Verthunder(pvp)(RDM)', '赤闪雷(pvp)(RDM)']
    _orig_names = ['赤闪雷(pvp)', 'Verthunder(pvp)']
    damage = 1800


class Action8885(Action):
    # 对目标发动魔法攻击
    # 威力：1400
    # 追加效果：获得10点黑魔元
    # 追加效果：若该技能发动时需要咏唱时间，则对自身附加连续咏唱状态
    # 持续时间：10秒
    # “连续咏唱”效果：下次咏唱魔法不需要咏唱时间
    # ※“连续咏唱”状态中该技能变为“赤闪雷”
    # ※“魔连攻”发动后该技能变为“赤核爆”
    # Deals fire damage with a potency of 1,400.
    # Additional Effect: Increases Black Mana by 10
    # Additional Effect: Grants Dualcast when spell is cast with a cast time
    # Duration: 10s
    # ※Action changes to Verthunder while under the effect of Dualcast.
    # ※Action changes to Verflare after execution of Enchanted Redoublement.
    # related: [连续咏唱(0)](Status1249), [连续咏唱(1)](Status1378), [连续咏唱(2)](Status1798), [连续咏唱(3)](Status1393),
    id = 8885
    names = ['赤火炎(pvp)(RDM)', 'Verfire(pvp)(RDM)']
    _orig_names = ['赤火炎(pvp)', 'Verfire(pvp)']
    damage = 1400


class Action8886(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1200
    # 追加效果：每命中一个目标都会获得5点白魔元与5点黑魔元
    # 发动条件：连续咏唱
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Increases both Black Mana and White Mana by 5 for each enemy hit
    # Can only be cast while under the effect of Dualcast.
    # ※This action cannot be assigned to a hotbar.
    # related: [冲击](Status995),
    id = 8886
    names = ['Impact(pvp)(RDM)', '冲击(pvp)(RDM)']
    _orig_names = ['冲击(pvp)', 'Impact(pvp)']
    damage = 1200


class Action8887(Action):
    # 对目标发动物理攻击
    # 威力：1600
    # 发动条件：白魔元、黑魔元各50点
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,600.
    # Balance Gauge Cost: 50 Black Mana
    # Balance Gauge Cost: 50 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 8887
    names = ['Enchanted Riposte(pvp)(RDM)', '魔回刺(pvp)(RDM)']
    _orig_names = ['魔回刺(pvp)', 'Enchanted Riposte(pvp)']
    damage = 1600


class Action8888(Action):
    # 对目标发动物理攻击
    # 连击中威力：1800
    # 连击条件：魔回刺
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Enchanted Riposte
    # Combo Potency: 1,800
    # ※This action cannot be assigned to a hotbar.
    id = 8888
    names = ['Enchanted Zwerchhau(pvp)(RDM)', '魔交击斩(pvp)(RDM)']
    _orig_names = ['Enchanted Zwerchhau(pvp)', '魔交击斩(pvp)']
    combo_action = 8887
    combo_damage = 1800


class Action8889(Action):
    # 对目标发动物理攻击
    # 连击中威力：2000
    # 连击条件：魔交击斩
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Enchanted Zwerchhau
    # Combo Potency: 2,000
    # ※This action cannot be assigned to a hotbar.
    id = 8889
    names = ['魔连攻(pvp)(RDM)', 'Enchanted Redoublement(pvp)(RDM)']
    _orig_names = ['魔连攻(pvp)', 'Enchanted Redoublement(pvp)']
    combo_action = 8888
    combo_damage = 2000


class Action8890(Action):
    # 冲向目标并发动物理攻击
    # 威力：800
    # 追加效果：50%加重
    # 持续时间：5秒
    # 积蓄次数：2
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 800.
    # Additional Effect: Heavy +50%
    # Duration: 5s
    # Maximum Charges: 2
    # Cannot be executed while bound.
    # related: [短兵相接](Status2012),
    id = 8890
    names = ['短兵相接(pvp)(RDM)', 'Corps-a-corps(pvp)(RDM)']
    _orig_names = ['Corps-a-corps(pvp)', '短兵相接(pvp)']
    damage = 800


class Action8891(Action):
    # 对目标发动物理攻击同时后跳15米
    # 威力：800
    # 追加效果：止步
    # 持续时间：3秒
    # 积蓄次数：2
    # 止步状态下无法发动
    # Delivers an attack with a potency of 800.
    # Additional Effect: 15-yalm backstep
    # Additional Effect: Bind
    # Duration: 3s
    # Maximum Charges: 2
    # Cannot be executed while bound.
    # related: [移转](Status2013),
    id = 8891
    names = ['Displacement(pvp)(RDM)', '移转(pvp)(RDM)']
    _orig_names = ['Displacement(pvp)', '移转(pvp)']
    damage = 800


class Action9433(Action):
    # 对目标发动魔法攻击
    # 连击中威力：2400
    # 连击条件：魔连攻
    # 追加效果：获得20点白魔元
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target.
    # Combo Action: Enchanted Redoublement
    # Combo Potency: 2,400
    # Additional Effect: Increases White Mana by 20
    # ※This action cannot be assigned to a hotbar.
    id = 9433
    names = ['Verholy(pvp)(RDM)', '赤神圣(pvp)(RDM)']
    _orig_names = ['Verholy(pvp)', '赤神圣(pvp)']
    combo_action = 8889
    combo_damage = 2400


class Action9434(Action):
    # 对目标发动魔法攻击
    # 连击中威力：2400
    # 连击条件：魔连攻
    # 追加效果：获得20点黑魔元
    # ※该技能无法设置到热键栏
    # Deals fire damage to target.
    # Combo Action: Enchanted Redoublement
    # Combo Potency: 2,400
    # Additional Effect: Increases Black Mana by 20
    # ※This action cannot be assigned to a hotbar.
    id = 9434
    names = ['赤核爆(pvp)(RDM)', 'Verflare(pvp)(RDM)']
    _orig_names = ['Verflare(pvp)', '赤核爆(pvp)']
    combo_action = 8889
    combo_damage = 2400


class Action10025(Action):
    # 恢复目标的体力
    # 恢复力：3000
    # 追加效果：获得5点白魔元与5点黑魔元
    # 追加效果发动条件：在战斗状态下为体力减少的目标恢复体力
    # 追加效果：若该技能发动时需要咏唱时间，则对自身附加连续咏唱状态
    # 持续时间：10秒
    # “连续咏唱”效果：下次咏唱魔法不需要咏唱时间
    # Restores target's HP.
    # Cure Potency: 3,000
    # Additional Effect: Grants Dualcast when spell is cast with a cast time
    # Duration: 10s
    # Additional Effect: Increases both Black Mana and White Mana by 5 when used to restore HP of self or a party member while in combat
    # related: [连续咏唱(0)](Status1249), [连续咏唱(1)](Status1378), [连续咏唱(2)](Status1798), [连续咏唱(3)](Status1393),
    id = 10025
    names = ['Vercure(pvp)(RDM)', '赤治疗(pvp)(RDM)']
    _orig_names = ['Vercure(pvp)', '赤治疗(pvp)']
    heal = 3000


class Action16524(Action):
    # 对目标及其周围敌人发动雷属性魔法攻击
    # 威力：(job==35?(level>=84?140:(job==35?(level>=74?120:100):100)):(job==35?(level>=74?120:100):100))
    # 追加效果：获得7点黑魔元
    # Deals lightning damage with a potency of (job==35?(level>=84?140:(job==35?(level>=74?120:100):100)):(job==35?(level>=74?120:100):100)) to target and all enemies nearby it.
    # Additional Effect: Increases Black Mana by 7
    id = 16524
    names = ['赤震雷(RDM)', 'Verthunder II(RDM)']
    _orig_names = ['Verthunder II', '赤震雷']
    damage = "(job==35?(lv>=84?140:(job==35?(lv>=74?120:100):100)):(job==35?(lv>=74?120:100):100))"


class Action16525(Action):
    # 对目标及其周围敌人发动风属性魔法攻击
    # 威力：(job==35?(level>=84?140:(job==35?(level>=74?120:100):100)):(job==35?(level>=74?120:100):100))
    # 追加效果：获得7点白魔元
    # Deals wind damage with a potency of (job==35?(level>=84?140:(job==35?(level>=74?120:100):100)):(job==35?(level>=74?120:100):100)) to target and all enemies nearby it.
    # Additional Effect: Increases White Mana by 7
    id = 16525
    names = ['赤烈风(RDM)', 'Veraero II(RDM)']
    _orig_names = ['赤烈风', 'Veraero II']
    damage = "(job==35?(lv>=84?140:(job==35?(lv>=74?120:100):100)):(job==35?(lv>=74?120:100):100))"


class Action16526(Action):
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：(job==35?(level>=84?210:200):200)
    # 促进状态中威力：(job==35?(level>=84?260:250):250)
    # 追加效果：获得3点黑魔元与3点白魔元
    # Deals unaspected damage with a potency of (job==35?(level>=84?210:200):200) to target and all enemies nearby it.
    # Acceleration Potency: (job==35?(level>=84?260:250):250)
    # Additional Effect: Increases both Black Mana and White Mana by 3
    # related: [冲击](Status995), [促进](Status1238),
    id = 16526
    names = ['冲击(RDM)', 'Impact(RDM)']
    _orig_names = ['Impact', '冲击']
    damage = "(促进状态?(job==35?(lv>=84?260:250):250):(job==35?(lv>=84?210:200):200))"


class Action16527(Action):
    # 对目标发动物理攻击
    # 威力：(job==35?(level>=72?180:130):130)
    # 积蓄次数：2
    # 与移转共享复唱时间
    # Delivers an attack with a potency of (job==35?(level>=72?180:130):130).
    # Maximum Charges: 2
    # Shares a recast timer with Displacement.
    # related: [交剑](Status2033),
    id = 16527
    names = ['Engagement(RDM)', '交剑(RDM)']
    _orig_names = ['交剑', 'Engagement']
    damage = "(job==35?(lv>=72?180:130):130)"


class Action16528(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==35?(level>=84?330:290):290)
    # 发动条件：黑魔元与白魔元各5点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of (job==35?(level>=84?330:290):290).
    # Balance Gauge Cost: 5 Black Mana
    # Balance Gauge Cost: 5 White Mana
    # ※This action cannot be assigned to a hotbar.
    id = 16528
    names = ['魔续斩(RDM)', 'Enchanted Reprise(RDM)']
    _orig_names = ['魔续斩', 'Enchanted Reprise']
    damage = "(job==35?(lv>=84?330:290):290)"


class Action16529(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 平衡量谱中黑魔元与白魔元都在5点以上时，该技能变为魔续斩
    # Delivers an attack with a potency of 100.
    # Action upgraded to Enchanted Reprise if both Black Mana and White Mana are at 5 or more.
    id = 16529
    names = ['续斩(RDM)', 'Reprise(RDM)']
    _orig_names = ['续斩', 'Reprise']
    damage = 100


class Action16530(Action):
    # 对目标及其周围敌人发动无属性魔法攻击
    # 威力：680
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 连击条件：赤核爆或赤神圣
    # 追加效果：获得4点黑魔元与4点白魔元
    # 发动条件：赤核爆或赤神圣成功时
    # 满足发动条件后，震荡变为焦热
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 680 for the first enemy, and 60% less for all remaining enemies.
    # Combo Action: Verflare or Verholy
    # Additional Effect: Increases both Black Mana and White Mana by 4
    # Jolt II and Impact are changed to Scorch upon landing Verflare or Verholy as a combo action.
    # ※This action cannot be assigned to a hotbar.
    id = 16530
    names = ['焦热(RDM)', 'Scorch(RDM)']
    _orig_names = ['焦热', 'Scorch']
    combo_action = 7525
    damage = 680
    # remain metas: {'aoe_reduce': '60%'}


class Action17727(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：800
    # 追加效果：每命中一个目标获得5点黑魔元与5点白魔元
    # 追加效果：若该技能发动时需要咏唱时间，则对自身附加连续咏唱状态
    # 持续时间：10秒
    # 连续咏唱效果：下次咏唱魔法不需要咏唱时间
    # ※“连续咏唱”状态中该技能变为“冲击”
    # Deals unaspected damage with a potency of 800 to target and all enemies nearby it.
    # Additional Effect: Increases both Black Mana and White Mana by 5 for each enemy hit
    # Additional Effect: Grants Dualcast when spell is cast with a cast time
    # Duration: 10s
    # ※Action changes to Impact while under the effect of Dualcast.
    # related: [连续咏唱(0)](Status1249), [连续咏唱(1)](Status1378), [连续咏唱(2)](Status1798), [连续咏唱(3)](Status1393),
    id = 17727
    names = ['散碎(pvp)(RDM)', 'Scatter(pvp)(RDM)']
    _orig_names = ['散碎(pvp)', 'Scatter(pvp)']
    damage = 800


class Action17786(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 追加效果：为自身张开一个防护罩，能抵消相当于恢复力2500的伤害量
    # 持续时间：6秒
    # 积蓄次数：2
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Creates a barrier around self that absorbs damage equivalent to a heal of 2,500 potency.
    # Duration: 6s
    # Maximum Charges: 2
    # related: [交剑](Status2033),
    id = 17786
    names = ['Engagement(pvp)(RDM)', '交剑(pvp)(RDM)']
    _orig_names = ['交剑(pvp)', 'Engagement(pvp)']
    damage = 1200
    # remain metas: {'shield': '恢复力2500'}


class Action17787(Action):
    # 对目标发动魔法攻击
    # 连击中威力：3000
    # 连击条件：赤核爆或赤神圣
    # 追加效果：获得10点黑魔元与10点白魔元
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target.
    # Combo Action: Verflare or Verholy
    # Combo Potency: 3,000
    # Additional Effect: Increases both Black Mana and White Mana by 10
    # ※This action cannot be assigned to a hotbar.
    id = 17787
    names = ['焦热(pvp)(RDM)', 'Scorch(pvp)(RDM)']
    _orig_names = ['Scorch(pvp)', '焦热(pvp)']
    combo_action = 9433
    combo_damage = 3000


class Action17788(Action):
    # 对目标发动远距离物理攻击
    # 威力：2000
    # 发动条件：黑魔元与白魔元各25点
    # Delivers a ranged attack with a potency of 2,000.
    # Balance Gauge Cost: 25 Black Mana
    # Balance Gauge Cost: 25 White Mana
    id = 17788
    names = ['Enchanted Reprise(pvp)(RDM)', '魔续斩(pvp)(RDM)']
    _orig_names = ['Enchanted Reprise(pvp)', '魔续斩(pvp)']
    damage = 2000


class Action18944(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1600
    # 发动条件：黑魔元、白魔元各25点
    # Delivers an attack with a potency of 1,600 to all enemies in a cone before you.
    # Balance Gauge Cost: 25 Black Mana
    # Balance Gauge Cost: 25 White Mana
    id = 18944
    names = ['Enchanted Moulinet(pvp)(RDM)', '魔划圆斩(pvp)(RDM)']
    _orig_names = ['Enchanted Moulinet(pvp)', '魔划圆斩(pvp)']
    damage = 1600


class Action20106(Action):
    # 自身与周围队员攻击造成的伤害提高10%
    # 持续时间：15秒
    # 此效果每3秒降低2%
    # Increases damage dealt by self and nearby party members by 10%. Effect is reduced by 2% every 3s.
    # Duration: 15s
    # related: [鼓励(0)](Status1297), [鼓励(1)](Status1239), [鼓励(2)](Status2282),
    id = 20106
    names = ['Embolden(pvp)(RDM)', '鼓励(pvp)(RDM)']
    _orig_names = ['Embolden(pvp)', '鼓励(pvp)']
    # remain metas: {'dmg_increase': '10%'}


class Action25855(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：380
    # 追加效果：获得6点黑魔元
    # 追加效果（发动几率50%）：赤火炎预备
    # 持续时间：30秒
    # Deals lightning damage with a potency of 380.
    # Additional Effect: Increases Black Mana by 6
    # Additional Effect: 50% chance of becoming Verfire Ready
    # Duration: 30s
    id = 25855
    names = ['Verthunder III(RDM)', '赤暴雷(RDM)']
    _orig_names = ['赤暴雷', 'Verthunder III']
    damage = 380


class Action25856(Action):
    # 对目标发动风属性魔法攻击
    # 威力：380
    # 追加效果：获得6点白魔元
    # 追加效果（发动几率50%）：赤飞石预备
    # 持续时间：30秒
    # Deals wind damage with a potency of 380.
    # Additional Effect: Increases White Mana by 6
    # Additional Effect: 50% chance of becoming Verstone Ready
    # Duration: 30s
    id = 25856
    names = ['赤暴风(RDM)', 'Veraero III(RDM)']
    _orig_names = ['Veraero III', '赤暴风']
    damage = 380


class Action25857(Action):
    # 一定时间内，令自身和周围队员所受到的魔法伤害减轻10%，并且所受的体力恢复效果提高5%
    # 持续时间：10秒
    # Reduces magic damage taken by self and nearby party members by 10%, while increasing HP recovered by healing actions by 5%.
    # Duration: 10s
    # related: [抗死](Status2707),
    id = 25857
    names = ['抗死(RDM)', 'Magick Barrier(RDM)']
    _orig_names = ['Magick Barrier', '抗死']
    # remain metas: {'taken_dmg_reduce': '10%，并且所受的体力恢复效果提高5%'}


class Action25858(Action):
    # 向目标所在方向发出直线无属性范围魔法攻击
    # 威力：750
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 连击条件：焦热
    # 追加效果：获得4点黑魔元与4点白魔元
    # 发动条件：焦热成功时
    # 满足发动条件后，焦热会变为决断
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 750 for the first enemy, and 60% less for all remaining enemies.
    # Combo Action: Scorch
    # Additional Effect: Increases both Black Mana and White Mana by 4
    # Scorch is changed to Resolution upon landing Scorch as a combo action.
    # ※This action cannot be assigned to a hotbar.
    id = 25858
    names = ['Resolution(RDM)', '决断(RDM)']
    _orig_names = ['Resolution', '决断']
    combo_action = 16530
    damage = 750
    # remain metas: {'aoe_reduce': '60%'}


