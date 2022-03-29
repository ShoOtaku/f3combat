from ._base import *


class Status85(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [凶残裂(WAR)](Action37), [凶残裂(pvp)(WAR)](Action8761), 
    id = 85
    names = ['凶残裂', 'Maim']


class Status86(Status):
    # 自身发动战技必定暴击并且直击
    # All weaponskill attacks are both critical and direct hits.
    # related: [狂暴(WAR)](Action38), 
    id = 86
    names = ['狂暴', 'Berserk']


class Status87(Status):
    # 体力最大值提高
    # 习得战栗效果提高后追加效果：自身所受的治疗效果提高
    # Maximum HP is increased.
    # Enhanced Thrill of Battle Effect: HP recovery via healing actions is increased.
    # related: [战栗(WAR)](Action40), 
    id = 87
    names = ['战栗', 'Thrill of Battle']


class Status408(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [暴风斩(WAR)](Action42), [暴风斩(pvp)(WAR)](Action8762), 
    id = 408
    names = ['暴风斩', "Storm's Path"]


class Status89(Status):
    # 受到物理攻击时会发动反击
    # Inflicting a portion of sustained damage back to its source.
    # related: [复仇(WAR)](Action44), 
    id = 89
    names = ['复仇', 'Vengeance']


class Status90(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [暴风碎(WAR)](Action45), 
    id = 90
    names = ['暴风碎', "Storm's Eye"]


class Status2677(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [暴风碎(WAR)](Action45), [秘银暴风(WAR)](Action16462), 
    id = 2677
    names = ['战场风暴', 'Surging Tempest']


class Status1396(Status):
    # 以攻击力降低为代价减少自身所受到的伤害
    # Damage dealt and taken are reduced.
    # related: [守护(WAR)](Action48), 
    id = 1396
    names = ['守护', 'Defiance']


class Status411(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [原初之魂(WAR)](Action49), 
    id = 411
    names = ['原初之魂(0)', 'Inner Beast(0)']


class Status1398(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [原初之魂(WAR)](Action49), 
    id = 1398
    names = ['原初之魂(1)', 'Inner Beast(1)']


class Status1992(Status):
    # 裂石飞环变为狂魂，地毁人亡变为混沌旋风
    # Fell Cleave is upgraded to Inner Chaos, while Decimate is upgraded to Chaotic Cyclone.
    # related: [裂石飞环(WAR)](Action3549), [地毁人亡(WAR)](Action3550), [裂石飞环(pvp)(WAR)](Action8763), [混沌旋风(WAR)](Action16463), [狂魂(WAR)](Action16465), [地毁人亡(pvp)(WAR)](Action17695), [狂魂(pvp)(WAR)](Action17696), [混沌旋风(pvp)(WAR)](Action17697), [战嚎(pvp)(WAR)](Action17698), 
    id = 1992
    names = ['原初的混沌(0)', 'Nascent Chaos(0)']


class Status1897(Status):
    # 地毁人亡变为混沌旋风
    # 习得狂魂后追加效果：裂石飞环变为狂魂
    # Decimate is upgraded to Chaotic Cyclone.
    # Nascent Chaos Effect: Fell Cleave is upgraded to Inner Chaos.
    # related: [裂石飞环(WAR)](Action3549), [地毁人亡(WAR)](Action3550), [裂石飞环(pvp)(WAR)](Action8763), [混沌旋风(WAR)](Action16463), [狂魂(WAR)](Action16465), [地毁人亡(pvp)(WAR)](Action17695), [狂魂(pvp)(WAR)](Action17696), [混沌旋风(pvp)(WAR)](Action17697), [战嚎(pvp)(WAR)](Action17698), 
    id = 1897
    names = ['原初的混沌(1)', 'Nascent Chaos(1)']


class Status735(Status):
    # 自身发动战技命中时可以恢复体力，同时减轻所受到的伤害
    # Damage taken is reduced and HP is restored with each weaponskill successfully delivered.
    # related: [原初的直觉(WAR)](Action3551), 
    id = 735
    names = ['原初的直觉', 'Raw Intuition']


class Status2681(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [泰然自若(WAR)](Action3552), 
    id = 2681
    names = ['泰然自若', 'Equilibrium']


class Status1457(Status):
    # 抵消一定伤害
    # A highly effective defensive maneuver is nullifying damage.
    # related: [摆脱(WAR)](Action7388), [摆脱(pvp)(WAR)](Action17699), 
    id = 1457
    names = ['摆脱(0)', 'Shake It Off(0)']


class Status1993(Status):
    # 抵消一定伤害
    # A barrier is preventing damage.
    # related: [摆脱(WAR)](Action7388), [摆脱(pvp)(WAR)](Action17699), 
    id = 1993
    names = ['摆脱(1)', 'Shake It Off(1)']


class Status1177(Status):
    # 兽魂不会消耗，自身发动战技必定暴击并且直击，不受眩晕、睡眠、止步、加重和除特定攻击之外其他所有击退、吸引的效果影响
    # Beast Gauge consumption is reduced to 0. All weaponskill attacks are both critical and direct hits. All Stun, Sleep, Bind, Heavy, and most knockback and draw-in effects are nullified.
    # related: [原初的解放(WAR)](Action7389), [原初的解放(pvp)(WAR)](Action8768), 
    id = 1177
    names = ['原初的解放(0)', 'Inner Release(0)']


class Status1303(Status):
    # 兽魂不会消耗，不受眩晕、睡眠、止步、加重、沉默、击退、吸引的效果影响
    # Beast Gauge consumption is reduced to 0. All Stun, Sleep, Bind, Heavy, Silence, knockback, and draw-in effects are nullified.
    # related: [原初的解放(WAR)](Action7389), [原初的解放(pvp)(WAR)](Action8768), 
    id = 1303
    names = ['原初的解放(1)', 'Inner Release(1)']


class Status2078(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [混沌旋风(WAR)](Action16463), [混沌旋风(pvp)(WAR)](Action17697), 
    id = 2078
    names = ['混沌旋风', 'Chaotic Cyclone']


class Status1857(Status):
    # 自身发动战技命中时可以恢复体力
    # Restoring HP with each weaponskill successfully delivered.
    # related: [原初的勇猛(WAR)](Action16464), [原初的勇猛(pvp)(WAR)](Action17889), 
    id = 1857
    names = ['原初的勇猛(0)', 'Nascent Flash(0)']


class Status1858(Status):
    # 附加此效果的战士受到原初的勇猛的恢复体力的效果时，会获得相当于其100%的恢复效果。
    # 另外受到攻击的伤害减少
    # Receiving 100% of all HP recovered by the warrior who granted this status via Nascent Flash. Damage taken is reduced.
    # related: [原初的勇猛(WAR)](Action16464), [原初的勇猛(pvp)(WAR)](Action17889), 
    id = 1858
    names = ['原初的武猛(0)', 'Nascent Glint(0)']


class Status2227(Status):
    # 自身的物理攻击命中时会吸收体力
    # Absorbing HP with each physical attack delivered.
    # related: [原初的勇猛(WAR)](Action16464), [原初的勇猛(pvp)(WAR)](Action17889), 
    id = 2227
    names = ['原初的勇猛(1)', 'Nascent Flash(1)']


class Status2679(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [原初的勇猛(WAR)](Action16464), [原初的血气(WAR)](Action25751), 
    id = 2679
    names = ['原初的血潮', 'Stem the Flow']


class Status2061(Status):
    # 自身的物理攻击命中时会吸收体力
    # 另外受到攻击的伤害减少
    # Absorbing HP with each physical attack delivered. Damage taken is also reduced.
    # related: [原初的勇猛(WAR)](Action16464), [原初的勇猛(pvp)(WAR)](Action17889), 
    id = 2061
    names = ['原初的勇猛(2)', 'Nascent Flash(2)']


class Status2062(Status):
    # 对自身附加此效果的战士因原初的勇猛吸收到体力时，自身也会一起恢复相同量的体力
    # 另外受到攻击的伤害减少
    # Damage taken is reduced, and receiving 100% of all HP absorbed by the warrior who granted this status via Nascent Flash.
    # related: [原初的勇猛(WAR)](Action16464), [原初的勇猛(pvp)(WAR)](Action17889), 
    id = 2062
    names = ['原初的武猛(1)', 'Nascent Glint(1)']


class Status2077(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [狂魂(WAR)](Action16465), [狂魂(pvp)(WAR)](Action17696), 
    id = 2077
    names = ['狂魂', 'Inner Chaos']


class Status2680(Status):
    # 抵消一定伤害
    # A highly effective defensive maneuver is nullifying damage.
    # related: [原初的血气(WAR)](Action25751), 
    id = 2680
    names = ['原初的血烟', 'Stem the Tide']


class Status2678(Status):
    # 自身发动战技命中时可以恢复体力，同时减轻所受到的伤害
    # Damage taken is reduced and HP is restored with each weaponskill successfully delivered.
    # related: [原初的血气(WAR)](Action25751), 
    id = 2678
    names = ['原初的血气', 'Bloodwhetting']


class Status2624(Status):
    # 可以发动蛮荒崩裂
    # Able to execute Primal Rend.
    # related: [蛮荒崩裂(WAR)](Action25753), 
    id = 2624
    names = ['蛮荒崩裂预备', 'Primal Rend Ready']


class Action31(Action):
    # 对目标发动物理攻击
    # 威力：(job==21?(level>=84?200:150):150)
    # Delivers an attack with a potency of (job==21?(level>=84?200:150):150).
    id = 31
    names = ['Heavy Swing(WAR)', '重劈(WAR)']
    _orig_names = ['Heavy Swing', '重劈']
    damage = "(job==21?(lv>=84?200:150):150)"


class Action37(Action):
    # 对目标发动物理攻击
    # 威力：(job==21?(level>=84?130:100):100)
    # 连击条件：重劈
    # 连击中威力：(job==21?(level>=84?280:250):250)(level>=30?(job==21?(job==21?(level>=35?
    # 连击成功：获得10点兽魂:):):):)
    # Delivers an attack with a potency of (job==21?(level>=84?130:100):100).
    # Combo Action: Heavy Swing
    # Combo Potency: (job==21?(level>=84?280:250):250)(level>=30?(job==21?(job==21?(level>=35?
    # Combo Bonus: Increases Beast Gauge by 10:):):):)
    # related: [凶残裂](Status85), 
    id = 37
    names = ['Maim(WAR)', '凶残裂(WAR)']
    _orig_names = ['凶残裂', 'Maim']
    combo_action = 31
    damage = "(job==21?(lv>=84?130:100):100)"
    combo_damage = "(job==21?(lv>=84?280:250):250)"


class Action38(Action):
    # 对自身附加3档的狂暴状态
    # 持续时间：15秒
    # 狂暴效果：一定时间内，自身发动的战技必定暴击并且直击(level>=40?(job==3?
    # 追加效果：战场风暴的持续时间延长10秒
    # 最多可延长至60秒:(job==21?
    # 追加效果：战场风暴的持续时间延长10秒
    # 最多可延长至60秒:)):)
    # Grants 3 stacks of Berserk, each stack guaranteeing weaponskill attacks are critical and direct hits.
    # Duration: 15s(level>=40?(job==3?
    # Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s:(job==21?
    # Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s:)):)
    # related: [狂暴](Status86), 
    id = 38
    names = ['Berserk(WAR)', '狂暴(WAR)']
    _orig_names = ['Berserk', '狂暴']


class Action40(Action):
    # 一定时间内，自身的最大体力提高20%
    # (job==21?(level>=78?同时，自身所受的体力恢复效果提高20%
    # :):)发动时恢复最大体力的20%
    # 持续时间：10秒
    # Increases maximum HP by 20% and restores the amount increased.
    # (job==21?(level>=78?Additional Effect: Increases HP recovery via healing actions on self by 20%
    # :):)Duration: 10s
    # related: [战栗](Status87), 
    id = 40
    names = ['Thrill of Battle(WAR)', '战栗(WAR)']
    _orig_names = ['战栗', 'Thrill of Battle']


class Action41(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：110
    # Delivers an attack with a potency of 110 to all enemies in a cone before you.
    id = 41
    names = ['超压斧(WAR)', 'Overpower(WAR)']
    _orig_names = ['超压斧', 'Overpower']
    damage = 110


class Action42(Action):
    # 对目标发动物理攻击
    # 威力：(job==21?(level>=84?120:100):100)
    # 连击条件：凶残裂
    # 连击中威力：(job==21?(level>=84?400:380):380)
    # 连击成功：恢复自身体力
    # 恢复力：250(job==21?(level>=35?
    # 连击成功：获得20点兽魂:):)
    # Delivers an attack with a potency of (job==21?(level>=84?120:100):100).
    # Combo Action: Maim
    # Combo Potency: (job==21?(level>=84?400:380):380)
    # Combo Bonus: Restores own HP
    # Cure Potency: 250(level>=30?(job==21?(job==21?(level>=35?
    # Combo Bonus: Increases Beast Gauge by 20:):):):)
    # related: [暴风斩](Status408), 
    id = 42
    names = ['暴风斩(WAR)', "Storm's Path(WAR)"]
    _orig_names = ['暴风斩', "Storm's Path"]
    combo_action = 37
    damage = "(job==21?(lv>=84?120:100):100)"
    combo_damage = "(job==21?(lv>=84?400:380):380)"
    heal = 250


class Action43(Action):
    # 效果中除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下
    # 当目标为敌人时，禁止目标移动
    # 持续时间：10秒
    # Brace yourself for an enemy onslaught, preventing most attacks from reducing your HP to less than 1.
    # Duration: 10s
    # When a target is selected, halts their movement with chains.
    # related: [死斗(0)](Status1304), [死斗(1)](Status1305), [死斗(2)](Status88), [死斗(3)](Status409), 
    id = 43
    names = ['死斗(WAR)', 'Holmgang(WAR)']
    _orig_names = ['Holmgang', '死斗']


class Action44(Action):
    # 一定时间内，令自身所受到的伤害减轻30%，同时受到物理攻击时会给予对方反击伤害
    # 威力：55
    # 持续时间：15秒
    # Reduces damage taken by 30% and delivers an attack with a potency of 55 every time you suffer physical damage.
    # Duration: 15s
    # related: [复仇](Status89), 
    id = 44
    names = ['复仇(WAR)', 'Vengeance(WAR)']
    _orig_names = ['复仇', 'Vengeance']
    damage = 55
    # remain metas: {'taken_dmg_reduce': '30%，同时受到物理攻击时会给予对方反击伤害'}


class Action45(Action):
    # 对目标发动物理攻击
    # 威力：(job==21?(level>=84?120:100):100)
    # 连击条件：凶残裂
    # 连击中威力：(job==21?(level>=84?400:380):380)
    # 连击成功：战场风暴
    # 持续时间：30秒
    # 战场风暴效果：自身发动攻击造成的伤害提高10%
    # 若自身已经附加战场风暴状态，则持续时间延长30秒
    # 最多可延长至60秒(level>=30?(job==21?
    # 连击成功：获得10点兽魂:):)
    # Delivers an attack with a potency of (job==21?(level>=84?120:100):100).
    # Combo Action: Maim
    # Combo Potency: (job==21?(level>=84?400:380):380)
    # Combo Bonus: Grants Surging Tempest, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Surging Tempest duration by 30s to a maximum of 60s.(level>=30?(job==21?
    # Combo Bonus: Increases Beast Gauge by 10:):)
    # related: [暴风碎](Status90), [战场风暴](Status2677), 
    id = 45
    names = ["Storm's Eye(WAR)", '暴风碎(WAR)']
    _orig_names = ['暴风碎', "Storm's Eye"]
    combo_action = 37
    damage = "(job==21?(lv>=84?120:100):100)"
    combo_damage = "(job==21?(lv>=84?400:380):380)"
    # remain metas: {'dmg_increase': '10%'}


class Action46(Action):
    # 对目标发动远距离物理攻击
    # 威力：150
    # 追加效果：提升仇恨
    # Delivers a ranged attack with a potency of 150.
    # Additional Effect: Increased enmity
    id = 46
    names = ['飞斧(WAR)', 'Tomahawk(WAR)']
    _orig_names = ['Tomahawk', '飞斧']
    damage = 150


class Action48(Action):
    # 极大幅度增加战斗时获得的仇恨量
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Significantly increases enmity generation.
    # Effect ends upon reuse.
    # related: [守护](Status1396), 
    id = 48
    names = ['守护(WAR)', 'Defiance(WAR)']
    _orig_names = ['守护', 'Defiance']


class Action49(Action):
    # 对目标发动物理攻击
    # 威力：330
    # 发动条件：兽魂50点
    # Delivers an attack with a potency of 330.
    # Beast Gauge Cost: 50
    # related: [原初之魂(0)](Status411), [原初之魂(1)](Status1398), 
    id = 49
    names = ['Inner Beast(WAR)', '原初之魂(WAR)']
    _orig_names = ['Inner Beast', '原初之魂']
    damage = 330


class Action51(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：170
    # 发动条件：兽魂50点
    # Delivers an attack with a potency of 170 to all nearby enemies.
    # Beast Gauge Cost: 50
    id = 51
    names = ['Steel Cyclone(WAR)', '钢铁旋风(WAR)']
    _orig_names = ['钢铁旋风', 'Steel Cyclone']
    damage = 170


class Action52(Action):
    # 获得50点兽魂
    # (job==21?(level>=72?追加效果：原初的混沌
    # 持续时间：30秒
    # :):)积蓄次数：2
    # 发动条件：自身处于战斗状态
    # Increases Beast Gauge by 50.
    # (job==21?(level>=72?Additional Effect: Grants Nascent Chaos
    # Duration: 30s
    # :):)Maximum Charges: 2
    # Can only be executed while in combat.
    id = 52
    names = ['Infuriate(WAR)', '战嚎(WAR)']
    _orig_names = ['Infuriate', '战嚎']


class Action3549(Action):
    # 对目标发动物理攻击
    # 威力：460
    # (job==21?(level>=80?该技能在原初的混沌状态中会变为狂魂
    # :):)发动条件：兽魂50点
    # Delivers an attack with a potency of 460.
    # Beast Gauge Cost: 50(job==21?(level>=80?
    # ※Action changes to Inner Chaos while under the effect of Nascent Chaos.:):)
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), 
    id = 3549
    names = ['裂石飞环(WAR)', 'Fell Cleave(WAR)']
    _orig_names = ['裂石飞环', 'Fell Cleave']
    damage = 460


class Action3550(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：200
    # (job==21?(level>=72?该技能在原初的混沌状态中会变为混沌旋风
    # :):)发动条件：兽魂50点
    # Delivers an attack to all nearby enemies with a potency of 200.
    # Beast Gauge Cost: 50(job==21?(level>=72?
    # ※Action changes to Chaotic Cyclone while under the effect of Nascent Chaos.:):)
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), 
    id = 3550
    names = ['地毁人亡(WAR)', 'Decimate(WAR)']
    _orig_names = ['Decimate', '地毁人亡']
    damage = 200


class Action3551(Action):
    # 一定时间内，自身所受的伤害减轻10%
    # 持续时间：6秒
    # 追加效果：自身发动的战技命中时恢复体力
    # 恢复力：400(job==21?(level>=76?
    # 与原初的勇猛共享复唱时间:):)
    # Reduces damage taken by 10%.
    # Duration: 6s
    # Additional Effect: Restores HP with each weaponskill successfully delivered
    # Cure Potency: 400(job==21?(level>=76?
    # Shares a recast timer with Nascent Flash.:):)
    # related: [原初的直觉](Status735), 
    id = 3551
    names = ['Raw Intuition(WAR)', '原初的直觉(WAR)']
    _orig_names = ['Raw Intuition', '原初的直觉']
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '400'}


class Action3552(Action):
    # 恢复自身体力
    # 恢复力：1200(job==21?(level>=84?
    # 追加效果：持续恢复自身的体力
    # 恢复力：200
    # 持续时间：15秒:):)
    # Restores own HP.
    # Cure Potency: 1,200(job==21?(level>=84?
    # Additional Effect: Gradually restores HP
    # Cure Potency: 200
    # Duration: 15s:):)
    # related: [泰然自若](Status2681), 
    id = 3552
    names = ['泰然自若(WAR)', 'Equilibrium(WAR)']
    _orig_names = ['泰然自若', 'Equilibrium']
    heal = 1200


class Action7386(Action):
    # 冲向目标并发动物理攻击
    # 威力：150
    # 积蓄次数：(job==21?(level>=88?3:2):2)
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 150.
    # Maximum Charges: (job==21?(level>=88?3:2):2)
    # Cannot be executed while bound.
    id = 7386
    names = ['Onslaught(WAR)', '猛攻(WAR)']
    _orig_names = ['猛攻', 'Onslaught']
    damage = 150


class Action7387(Action):
    # 对目标发动物理攻击
    # 威力：350(job==21?(level>=86?
    # 与群山隆起共享复唱时间:):)
    # Delivers an attack with a potency of 350.(job==21?(level>=86?
    # Shares a recast timer with Orogeny.:):)
    id = 7387
    names = ['Upheaval(WAR)', '动乱(WAR)']
    _orig_names = ['Upheaval', '动乱']
    damage = 350


class Action7388(Action):
    # 为自身与周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力15%的伤害量
    # 另外，自身处于“战栗”“复仇”(job==21?(level>=82?“原初的血气”:“原初的直觉”):“原初的直觉”)状态时，每解除一个状态，防护罩的效果量上升2%
    # 持续时间：15秒(job==21?(level>=76?
    # 追加效果：恢复自身及周围队员的体力
    # 恢复力：300:):)
    # Creates a barrier around self and all nearby party members that absorbs damage totaling 15% of maximum HP.
    # Dispels Thrill of Battle, Vengeance, and (job==21?(level>=82?Bloodwhetting:Raw Intuition):Raw Intuition), increasing damage absorbed by 2% for each effect removed. 
    # Duration: 15s(job==21?(level>=76?
    # Additional Effect: Restores own HP and the HP of all nearby party members
    # Cure Potency: 300:):)
    # related: [摆脱(0)](Status1457), [摆脱(1)](Status1993), 
    id = 7388
    names = ['摆脱(WAR)', 'Shake It Off(WAR)']
    _orig_names = ['摆脱', 'Shake It Off']
    # remain metas: {'shield': '目标最大体力15%'}


class Action7389(Action):
    # 为自身附加3档原初的解放状态
    # 持续时间：15秒
    # 原初的解放效果：一定时间内不需要消耗兽魂就可以发动特定技能，且自身发动的战技必定暴击并且直击
    # 效果时间内，自身不会受到眩晕、睡眠、止步、加重和除特定攻击之外其他所有击退、吸引的影响
    # 追加效果：战场风暴的持续时间延长10秒
    # 最多可延长至60秒(job==21?(level>=90?
    # 追加效果：蛮荒崩裂预备
    # 持续时间：30秒:):)
    # Grants 3 stacks of Inner Release, each stack allowing the use of Beast Gauge actions without cost and guaranteeing that all attacks are critical and direct hits.
    # Additional Effect: Nullifies Stun, Sleep, Bind, Heavy, and most knockback and draw-in effects
    # Duration: 15s
    # Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s(job==21?(level>=90?
    # Additional Effect: Grants Primal Rend Ready
    # Duration: 30s:):)
    # related: [原初的解放(0)](Status1177), [原初的解放(1)](Status1303), 
    id = 7389
    names = ['Inner Release(WAR)', '原初的解放(WAR)']
    _orig_names = ['原初的解放', 'Inner Release']


class Action8758(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：获得10点兽魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Increases Beast Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8758
    names = ['Heavy Swing(pvp)(WAR)', '重劈(pvp)(WAR)']
    _orig_names = ['Heavy Swing(pvp)', '重劈(pvp)']
    damage = 1000


class Action8761(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：重劈
    # 连击成功：获得10点兽魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Heavy Swing
    # Combo Potency: 1,200
    # Combo Bonus: Increases Beast Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    # related: [凶残裂](Status85), 
    id = 8761
    names = ['凶残裂(pvp)(WAR)', 'Maim(pvp)(WAR)']
    _orig_names = ['凶残裂(pvp)', 'Maim(pvp)']
    combo_action = 8758
    combo_damage = 1200


class Action8762(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：凶残裂
    # 连击成功：恢复伤害量100%的体力
    # 连击成功：获得20点兽魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Maim
    # Combo Potency: 1,400
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Combo Bonus: Increases Beast Gauge by 20
    # ※This action cannot be assigned to a hotbar.
    # related: [暴风斩](Status408), 
    id = 8762
    names = ["Storm's Path(pvp)(WAR)", '暴风斩(pvp)(WAR)']
    _orig_names = ["Storm's Path(pvp)", '暴风斩(pvp)']
    combo_action = 8761
    combo_damage = 1400


class Action8763(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 追加效果：战嚎的复唱时间缩短10秒
    # 发动条件：兽魂50点
    # ※该技能在“原初的混沌”状态中会变为“狂魂”
    # Delivers an attack with a potency of 2,000.
    # Additional Effect: Reduces the recast time of Infuriate by 10 seconds
    # Beast Gauge Cost: 50
    # ※Action changes to Inner Chaos while under the effect of Nascent Chaos.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), 
    id = 8763
    names = ['裂石飞环(pvp)(WAR)', 'Fell Cleave(pvp)(WAR)']
    _orig_names = ['Fell Cleave(pvp)', '裂石飞环(pvp)']
    damage = 2000


class Action8764(Action):
    # 对目标发动远距离物理攻击
    # 威力：800
    # 追加效果：获得10点兽魂
    # Delivers a ranged attack with a potency of 800.
    # Additional Effect: Increases Beast Gauge by 10
    id = 8764
    names = ['Tomahawk(pvp)(WAR)', '飞斧(pvp)(WAR)']
    _orig_names = ['Tomahawk(pvp)', '飞斧(pvp)']
    damage = 800


class Action8765(Action):
    # 冲向目标并发动物理攻击
    # 威力：1200
    # 发动条件：兽魂20点
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 1,200.
    # Beast Gauge Cost: 20
    # Cannot be executed while bound.
    id = 8765
    names = ['猛攻(pvp)(WAR)', 'Onslaught(pvp)(WAR)']
    _orig_names = ['猛攻(pvp)', 'Onslaught(pvp)']
    damage = 1200


class Action8767(Action):
    # 将目标拉向自身，同时禁止自身和目标的移动
    # 持续时间：3秒
    # 该状态不受止步无效和击退无效的影响
    # 效果中所有对自身发动的攻击均无法令体力减少到1以下
    # Draws target towards caster, and binds both.
    # Duration: 3s
    # Ignores target's bind and knockback resistance.
    # Attacks cannot reduce your HP to less than 1.
    # related: [死斗(0)](Status1304), [死斗(1)](Status1305), [死斗(2)](Status88), [死斗(3)](Status409), 
    id = 8767
    names = ['死斗(pvp)(WAR)', 'Holmgang(pvp)(WAR)']
    _orig_names = ['死斗(pvp)', 'Holmgang(pvp)']


class Action8768(Action):
    # 一定时间内可不消耗兽魂发动相关技能
    # 效果时间内，自身不会受到眩晕、睡眠、止步、加重、沉默、击退、吸引的影响
    # 持续时间：6秒
    # Allows the use of Beast Gauge actions without cost and nullifies Stun, Sleep, Bind, Heavy, Silence, and knockback and draw-in effects.
    # Duration: 6s
    # related: [原初的解放(0)](Status1177), [原初的解放(1)](Status1303), 
    id = 8768
    names = ['原初的解放(pvp)(WAR)', 'Inner Release(pvp)(WAR)']
    _orig_names = ['原初的解放(pvp)', 'Inner Release(pvp)']


class Action16462(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：超压斧
    # 连击中威力：150
    # 连击成功：战场风暴
    # 持续时间：30秒
    # 战场风暴效果：自身发动攻击造成的伤害提高10%
    # 若自身已经附加战场风暴状态，则持续时间延长30秒
    # 最多可延长至60秒(job==21?(level>=74?
    # 连击成功：获得20点兽魂:):)
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: Overpower
    # Combo Potency: 150
    # Combo Bonus: Grants Surging Tempest, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Surging Tempest duration by 30s to a maximum of 60s.(job==21?(level>=74?
    # Combo Bonus: Increases Beast Gauge by 20:):)
    # related: [战场风暴](Status2677), 
    id = 16462
    names = ['秘银暴风(WAR)', 'Mythril Tempest(WAR)']
    _orig_names = ['Mythril Tempest', '秘银暴风']
    combo_action = 41
    damage = 100
    combo_damage = 150
    # remain metas: {'dmg_increase': '10%'}


class Action16463(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：320
    # 该技能必定暴击并且直击
    # 追加效果：战嚎的复唱时间缩短5秒
    # 发动后会取消原初的混沌状态
    # 发动条件：原初的混沌状态中且兽魂50点
    # ※该技能无法设置到热键栏
    # Delivers a critical direct hit with a potency of 320 to all nearby enemies.
    # Additional Effect: Reduces the recast time of Infuriate by 5 seconds
    # Beast Gauge Cost: 50
    # Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), [混沌旋风](Status2078), 
    id = 16463
    names = ['Chaotic Cyclone(WAR)', '混沌旋风(WAR)']
    _orig_names = ['混沌旋风', 'Chaotic Cyclone']
    damage = 320


class Action16464(Action):
    # 指定一名队员为目标，对自身附加原初的勇猛状态，为目标附加原初的武猛状态
    # 持续时间：(job==21?(level>=82?8:6):6)秒
    # 原初的勇猛效果：自身发动的战技命中时恢复体力
    # 恢复力：400
    # 原初的武猛效果：恢复战士自身恢复量100%的体力
    # 同时，受到的伤害减轻10%
    # (job==21?(level>=82?追加效果：为目标附加原初的血潮状态
    # 持续时间：4秒
    # 原初的血潮效果：令目标受到的伤害减轻10%
    # 追加效果为目标附加能够抵御一定伤害的防护罩原初的血烟
    # 该防护罩能够抵消相当于恢复力400的伤害量
    # 持续时间：20秒
    # :):)与(job==21?(level>=82?原初的血气:原初的直觉):原初的直觉)共享复唱时间
    # Grants Nascent Flash to self and Nascent Glint to target party member.
    # Nascent Flash Effect: Restores HP with each weaponskill successfully delivered
    # Cure Potency: 400
    # Nascent Glint Effect: Restores HP equaling 100% of that recovered by Nascent Flash while also reducing damage taken by 10%
    # Duration: (job==21?(level>=82?8:6):6)s
    # (job==21?(level>=82?Additional Effect: Grants Stem the Flow to target, reducing damage taken by 10%
    # Duration: 4s
    # Additional Effect: Grants Stem the Tide to target, nullifying damage equivalent to a heal of 400 potency
    # Duration: 20s
    # :):)Shares a recast timer with (job==21?(level>=82?Bloodwhetting:Raw Intuition):Raw Intuition).
    # related: [原初的勇猛(0)](Status1857), [原初的武猛(0)](Status1858), [原初的勇猛(1)](Status2227), [原初的血潮](Status2679), [原初的勇猛(2)](Status2061), [原初的武猛(1)](Status2062), 
    id = 16464
    names = ['Nascent Flash(WAR)', '原初的勇猛(WAR)']
    _orig_names = ['Nascent Flash', '原初的勇猛']
    # remain metas: {'heal_ot': '400', 'taken_dmg_reduce': '10%'}


class Action16465(Action):
    # 对目标发动物理攻击
    # 威力：650
    # 该技能必定暴击并且直击
    # 追加效果：战嚎的复唱时间缩短5秒
    # 发动后会取消原初的混沌状态
    # 发动条件：原初的混沌状态中且兽魂50点
    # ※该技能无法设置到热键栏
    # Delivers a critical direct hit with a potency of 650.
    # Additional Effect: Reduces the recast time of Infuriate by 5 seconds
    # Beast Gauge Cost: 50
    # Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), [狂魂](Status2077), 
    id = 16465
    names = ['狂魂(WAR)', 'Inner Chaos(WAR)']
    _orig_names = ['Inner Chaos', '狂魂']
    damage = 650


class Action17695(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：1200
    # 追加效果：每命中一个目标战嚎的复唱时间都会缩短5秒
    # 发动条件：兽魂50点
    # ※该技能在“原初的混沌”状态中会变为“混沌旋风”
    # Delivers an attack with a potency of 1,200 to all nearby enemies.
    # Additional Effect: Reduces the recast time of Infuriate by 5s for each enemy hit
    # Beast Gauge Cost: 50
    # ※Action changes to Chaotic Cyclone while under the effect of Nascent Chaos.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), 
    id = 17695
    names = ['Decimate(pvp)(WAR)', '地毁人亡(pvp)(WAR)']
    _orig_names = ['地毁人亡(pvp)', 'Decimate(pvp)']
    damage = 1200


class Action17696(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：令目标受到的伤害提高10%
    # 持续时间：10秒
    # 发动后会取消原初的混沌状态
    # 发动条件：原初的混沌状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 2,000.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Increases target's damage taken by 10%
    # Duration: 10s
    # Can only be executed while under the effect of Nascent Chaos. Effect ends upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), [狂魂](Status2077), 
    id = 17696
    names = ['Inner Chaos(pvp)(WAR)', '狂魂(pvp)(WAR)']
    _orig_names = ['狂魂(pvp)', 'Inner Chaos(pvp)']
    damage = 2000
    # remain metas: {'taken_dmg_increase': '10%'}


class Action17697(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：1200
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：令目标受到的伤害提高10%
    # 持续时间：10秒
    # 发动后会取消原初的混沌状态
    # 发动条件：原初的混沌状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200 to all nearby enemies.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Increases target's damage taken by 10%
    # Duration: 10s
    # Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution.
    # ※This action cannot be assigned to a hotbar.
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), [混沌旋风](Status2078), 
    id = 17697
    names = ['混沌旋风(pvp)(WAR)', 'Chaotic Cyclone(pvp)(WAR)']
    _orig_names = ['Chaotic Cyclone(pvp)', '混沌旋风(pvp)']
    damage = 1200
    # remain metas: {'taken_dmg_increase': '10%'}


class Action17698(Action):
    # 对自身附加原初的混沌状态
    # 持续时间：5秒
    # 积蓄次数：2
    # Grants Nascent Chaos.
    # Duration: 5s
    # Maximum Charges: 2
    # related: [原初的混沌(0)](Status1992), [原初的混沌(1)](Status1897), 
    id = 17698
    names = ['Infuriate(pvp)(WAR)', '战嚎(pvp)(WAR)']
    _orig_names = ['Infuriate(pvp)', '战嚎(pvp)']


class Action17699(Action):
    # 为自身与周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力2000的伤害量
    # 持续时间：10秒
    # 另外，自身处于铁壁状态时，会解除该状态并令防护罩的效果量上升到4000
    # Creates a barrier around self and all party members near you that absorbs damage equivalent to a heal of 2,000 potency.
    # Duration: 10s
    # When under the effect of Rampart, the effect is removed, increasing barrier potency to 4,000.
    # related: [摆脱(0)](Status1457), [铁壁(1)](Status71), [铁壁(0)](Status1191), [摆脱(1)](Status1993), [铁壁(2)](Status1978), 
    id = 17699
    names = ['Shake It Off(pvp)(WAR)', '摆脱(pvp)(WAR)']
    _orig_names = ['摆脱(pvp)', 'Shake It Off(pvp)']
    # remain metas: {'shield': '恢复力2000'}


class Action17889(Action):
    # 以一名队员为目标
    # 对自身附加原初的勇猛状态，对目标附加原初的武猛状态
    # 原初的勇猛效果：将攻击所造成伤害的100%转化为自身的体力
    # 同时，受到的伤害减轻10%
    # 原初的武猛效果：恢复战士自身转化量100%的体力
    # 同时，受到的伤害减轻10%
    # 持续时间：6秒
    # Grants Nascent Flash to self and Nascent Glint to target party member.
    # Nascent Flash Effect: Absorbs 100% of damage dealt as HP and reduces damage taken by 10%
    # Nascent Glint Effect: Restores HP equaling that recovered by Nascent Flash and reduces damage taken by 10%
    # Duration: 6s
    # related: [原初的勇猛(0)](Status1857), [原初的武猛(0)](Status1858), [原初的勇猛(1)](Status2227), [原初的勇猛(2)](Status2061), [原初的武猛(1)](Status2062), 
    id = 17889
    names = ['原初的勇猛(pvp)(WAR)', 'Nascent Flash(pvp)(WAR)']
    _orig_names = ['原初的勇猛(pvp)', 'Nascent Flash(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action18904(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：600
    # 追加效果：获得10点兽魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Increases Beast Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 18904
    names = ['Mythril Tempest(pvp)(WAR)', '秘银暴风(pvp)(WAR)']
    _orig_names = ['秘银暴风(pvp)', 'Mythril Tempest(pvp)']
    damage = 600


class Action18905(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 连击中威力：800
    # 连击条件：秘银暴风
    # 连击成功：恢复伤害量100%的体力
    # 连击成功：获得20点兽魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Mythril Tempest
    # Combo Potency: 800
    # Combo Bonus: Absorbs 100% of damage dealt as HP
    # Combo Bonus: Increases Beast Gauge by 20
    # ※This action cannot be assigned to a hotbar.
    id = 18905
    names = ['钢铁旋风(pvp)(WAR)', 'Steel Cyclone(pvp)(WAR)']
    _orig_names = ['Steel Cyclone(pvp)', '钢铁旋风(pvp)']
    combo_action = 18904
    combo_damage = 800


class Action25751(Action):
    # 一定时间内，令自身受到的伤害减轻10%
    # 持续时间：8秒
    # 追加效果：自身发动的战技命中时恢复体力
    # 恢复力：400
    # 追加效果：原初的血潮
    # 持续时间：4秒
    # 原初的血潮效果：令自身受到的伤害减轻10%
    # 追加效果：为目标附加能够抵御一定伤害的防护罩原初的血烟
    # 该防护罩能够抵消相当于恢复力400的伤害量
    # 持续时间：20秒
    # 与原初的勇猛共享复唱时间
    # Reduces damage taken by 10%.
    # Duration: 8s
    # Additional Effect: Restores HP with each weaponskill successfully delivered
    # Cure Potency: 400
    # Additional Effect: Grants Stem the Flow
    # Stem the Flow Effect: Reduces damage taken by 10%
    # Duration: 4s
    # Additional Effect: Grants Stem the Tide
    # Stem the Tide Effect: Creates a barrier around self that absorbs damage equivalent to a heal of 400 potency
    # Duration: 20s
    # Shares a recast timer with Nascent Flash.
    # related: [原初的血烟](Status2680), [原初的血气](Status2678), [原初的血潮](Status2679), 
    id = 25751
    names = ['Bloodwhetting(WAR)', '原初的血气(WAR)']
    _orig_names = ['Bloodwhetting', '原初的血气']
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '400', 'shield': '恢复力400'}


class Action25752(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：150
    # 与动乱共享复唱时间
    # Delivers an attack with a potency of 150 to all nearby enemies.
    # Shares a recast timer with Upheaval.
    id = 25752
    names = ['Orogeny(WAR)', '群山隆起(WAR)']
    _orig_names = ['Orogeny', '群山隆起']
    damage = 150


class Action25753(Action):
    # 跃向目标并对目标及其周围敌人发动范围物理攻击
    # 威力：700
    # 攻击复数敌人时，对目标之外的敌人威力降低70%
    # 该技能必定暴击并且直击
    # 发动该技能不消耗原初的解放档数
    # 发动条件：发动原初的解放后为自身附加的蛮荒崩裂预备状态中
    # 止步状态下无法发动
    # Delivers a critical direct hit to target and all enemies nearby it with a potency of 700 for the first enemy, and 70% less for all remaining enemies.
    # Stacks of Inner Release are not consumed upon execution.
    # Can only be executed while under the effect of Primal Rend Ready, granted by Inner Release.
    # Cannot be executed while bound.
    # related: [蛮荒崩裂预备](Status2624), 
    id = 25753
    names = ['Primal Rend(WAR)', '蛮荒崩裂(WAR)']
    _orig_names = ['Primal Rend', '蛮荒崩裂']
    damage = 700
    # remain metas: {'aoe_reduce': '70%'}


