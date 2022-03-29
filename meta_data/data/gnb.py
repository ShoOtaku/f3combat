from ._base import *


class Status1145(Status):
    # 攻击所造成的伤害增加，但体力会逐渐减少
    # Sustaining damage over time in exchange for dealing increased damage to targets.
    # related: [利刃斩(GNB)](Action16137), [利刃斩(pvp)(GNB)](Action17703),
    id = 1145
    names = ['双刃剑', 'Keen Edge']


class Status1831(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [无情(GNB)](Action16138),
    id = 1831
    names = ['无情', 'No Mercy']


class Status1898(Status):
    # 抵消一定伤害
    # A highly effective defensive maneuver is nullifying damage.
    # related: [残暴弹(GNB)](Action16139), [石之心(GNB)](Action16161), [残暴弹(pvp)(GNB)](Action17704), [刚玉之心(GNB)](Action25758),
    id = 1898
    names = ['残暴弹(0)', 'Brutal Shell(0)']


class Status1997(Status):
    # 抵消一定伤害
    # A highly effective defensive maneuver is nullifying damage.
    # related: [残暴弹(GNB)](Action16139), [石之心(GNB)](Action16161), [残暴弹(pvp)(GNB)](Action17704), [刚玉之心(GNB)](Action25758),
    id = 1997
    names = ['残暴弹(1)', 'Brutal Shell(1)']


class Status1832(Status):
    # 招架发动率提高，减轻所受到的伤害
    # Parry rate is increased while damage taken is reduced.
    # related: [伪装(GNB)](Action16140),
    id = 1832
    names = ['伪装', 'Camouflage']


class Status392(Status):
    # 自身仇恨提高
    # Enmity is increased.
    # related: [王室亲卫(GNB)](Action16142),
    id = 392
    names = ['王室亲卫', 'Royal Guard']


class Status2392(Status):
    # 下次发动战技造成的伤害提高
    # Next weaponskill will deal increased damage.
    # related: [闪雷弹(GNB)](Action16143), [闪雷弹(pvp)(GNB)](Action17717),
    id = 2392
    names = ['闪雷弹', 'Lightning Shot']


class Status2065(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [极光(GNB)](Action16151), [极光(pvp)(GNB)](Action17891),
    id = 2065
    names = ['极光(0)', 'Aurora(0)']


class Status1835(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [极光(GNB)](Action16151), [极光(pvp)(GNB)](Action17891),
    id = 1835
    names = ['极光(1)', 'Aurora(1)']


class Status1836(Status):
    # 除特定攻击之外其他所有攻击均无效化
    # Impervious to most attacks.
    # related: [超火流星(GNB)](Action16152),
    id = 1836
    names = ['超火流星', 'Superbolide']


class Status1837(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [音速破(GNB)](Action16153),
    id = 1837
    names = ['音速破', 'Sonic Break']


class Status2002(Status):
    # 可以发动撕喉
    # Able to execute Jugular Rip.
    # related: [撕喉(GNB)](Action16156), [烈牙(pvp)(GNB)](Action17706), [撕喉(pvp)(GNB)](Action17712),
    id = 2002
    names = ['撕喉预备(pvp)', 'Ready to Rip(pvp)']


class Status1842(Status):
    # 可以发动撕喉
    # Able to execute Jugular Rip.
    # related: [撕喉(GNB)](Action16156), [烈牙(pvp)(GNB)](Action17706), [撕喉(pvp)(GNB)](Action17712),
    id = 1842
    names = ['撕喉预备', 'Ready to Rip']


class Status1843(Status):
    # 可以发动裂膛
    # Able to execute Abdomen Tear.
    # related: [裂膛(GNB)](Action16157), [裂膛(pvp)(GNB)](Action17713),
    id = 1843
    names = ['裂膛预备', 'Ready to Tear']


class Status2003(Status):
    # 可以发动裂膛
    # Able to execute Abdomen Tear.
    # related: [裂膛(GNB)](Action16157), [裂膛(pvp)(GNB)](Action17713),
    id = 2003
    names = ['裂膛预备(pvp)', 'Ready to Tear(pvp)']


class Status2004(Status):
    # 可以发动穿目
    # Able to execute Eye Gouge.
    # related: [穿目(GNB)](Action16158), [穿目(pvp)(GNB)](Action17714),
    id = 2004
    names = ['穿目预备(pvp)', 'Ready to Gouge(pvp)']


class Status1844(Status):
    # 可以发动穿目
    # Able to execute Eye Gouge.
    # related: [穿目(GNB)](Action16158), [穿目(pvp)(GNB)](Action17714),
    id = 1844
    names = ['穿目预备', 'Ready to Gouge']


class Status1838(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [弓形冲波(GNB)](Action16159), [弓形冲波(pvp)(GNB)](Action17748),
    id = 1838
    names = ['弓形冲波', 'Bow Shock']


# class Status2000(Status):
#     # 受到攻击的伤害减少
#     # Damage taken is reduced.
#     # related: [光之心(GNB)](Action16160),
#     id = 2000
#     names = ['光之心(0)', 'Heart of Light(0)']


class Status1839(Status):
    # 减轻所受到的魔法伤害
    # Magic damage taken is reduced.
    # related: [光之心(GNB)](Action16160),
    id = 1839
    names = ['光之心', 'Heart of Light']


class Status1840(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [石之心(GNB)](Action16161),
    id = 1840
    names = ['石之心', 'Heart of Stone']


class Status2683(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [刚玉之心(GNB)](Action25758),
    id = 2683
    names = ['刚玉之心', 'Heart of Corundum']


class Status2684(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [刚玉之心(GNB)](Action25758),
    id = 2684
    names = ['刚玉之清', 'Clarity of Corundum']


class Status2685(Status):
    # 体力降低到一定比例或持续时间结束时自动发动恢复效果
    # HP will be restored automatically upon falling below a certain level or expiration of effect duration.
    # related: [刚玉之心(GNB)](Action25758),
    id = 2685
    names = ['刚玉之净', 'Catharsis of Corundum']


class Status2686(Status):
    # 可以发动超高速
    # Able to execute Hypervelocity.
    # related: [超高速(GNB)](Action25759),
    id = 2686
    names = ['超高速', 'Ready to Blast']


class Action16137(Action):
    # 对目标发动物理攻击
    # 威力：(job==37?(level>=84?170:150):150)
    # Delivers an attack with a potency of (job==37?(level>=84?170:150):150).
    # related: [双刃剑](Status1145),
    id = 16137
    names = ['Keen Edge(GNB)', '利刃斩(GNB)']
    _orig_names = ['Keen Edge', '利刃斩']
    damage = "(job==37?(lv>=84?170:150):150)"


class Action16138(Action):
    # 一定时间内，自身发动攻击造成的伤害提高20%
    # 持续时间：20秒
    # Increases damage dealt by 20%.
    # Duration: 20s
    # related: [无情](Status1831),
    id = 16138
    names = ['No Mercy(GNB)', '无情(GNB)']
    _orig_names = ['无情', 'No Mercy']
    # remain metas: {'dmg_increase': '20%'}


class Action16139(Action):
    # 对目标发动物理攻击
    # 威力：(job==37?(level>=84?120:100):100)
    # 连击条件：利刃斩
    # 连击中威力：(job==37?(level>=84?260:240):240)
    # 连击成功：恢复自身体力
    # 恢复力：200(job==37?(level>=52?
    # 同时为自身附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复量100%的伤害
    # 持续时间：30秒:):)
    # Delivers an attack with a potency of (job==37?(level>=84?120:100):100).
    # Combo Action: Keen Edge
    # Combo Potency: (job==37?(level>=84?260:240):240)
    # Combo Bonus: Restores own HP
    # Cure Potency: 200(job==37?(level>=52?
    # Combo Bonus: Creates a barrier which nullifies damage equaling HP restored
    # Duration: 30s:):)
    # related: [残暴弹(0)](Status1898), [残暴弹(1)](Status1997),
    id = 16139
    names = ['Brutal Shell(GNB)', '残暴弹(GNB)']
    _orig_names = ['残暴弹', 'Brutal Shell']
    combo_action = 16137
    damage = "(job==37?(lv>=84?120:100):100)"
    combo_damage = "(job==37?(lv>=84?260:240):240)"
    heal = 200


class Action16140(Action):
    # 一定时间内，自身的招架发动率提高50%，所受的伤害减轻10%
    # 持续时间：20秒
    # Increases parry rate by 50% while reducing damage taken by 10%.
    # Duration: 20s
    # related: [伪装](Status1832),
    id = 16140
    names = ['伪装(GNB)', 'Camouflage(GNB)']
    _orig_names = ['Camouflage', '伪装']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action16141(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # Delivers an attack with a potency of 100 to all nearby enemies.
    id = 16141
    names = ['Demon Slice(GNB)', '恶魔切(GNB)']
    _orig_names = ['Demon Slice', '恶魔切']
    damage = 100


class Action16142(Action):
    # 极大幅度增加战斗时获得的仇恨量
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Significantly increases enmity generation.
    # Effect ends upon reuse.
    # related: [王室亲卫](Status392),
    id = 16142
    names = ['王室亲卫(GNB)', 'Royal Guard(GNB)']
    _orig_names = ['王室亲卫', 'Royal Guard']


class Action16143(Action):
    # 对目标发动远距离物理攻击
    # 威力：150
    # 追加效果：提升仇恨
    # Delivers a ranged attack with a potency of 150.
    # Additional Effect: Increased enmity
    # related: [闪雷弹](Status2392),
    id = 16143
    names = ['闪雷弹(GNB)', 'Lightning Shot(GNB)']
    _orig_names = ['Lightning Shot', '闪雷弹']
    damage = 150


class Action16144(Action):
    # 对目标发动物理攻击
    # 威力：250
    # Delivers an attack with a potency of 250.
    id = 16144
    names = ['危险领域(GNB)', 'Danger Zone(GNB)']
    _orig_names = ['Danger Zone', '危险领域']
    damage = 250


class Action16145(Action):
    # 对目标发动物理攻击
    # 威力：(job==37?(level>=84?120:100):100)
    # 连击条件：残暴弹
    # 连击中威力：(job==37?(level>=84?340:320):320)(job==37?(level>=30?
    # 连击成功：晶壤:):)
    # Delivers an attack with a potency of (job==37?(level>=84?120:100):100).
    # Combo Action: Brutal Shell
    # Combo Potency: (job==37?(level>=84?340:320):320)(job==37?(level>=30?
    # Combo Bonus: Adds a Cartridge to your Powder Gauge:):)
    id = 16145
    names = ['迅连斩(GNB)', 'Solid Barrel(GNB)']
    _orig_names = ['迅连斩', 'Solid Barrel']
    combo_action = 16139
    damage = "(job==37?(lv>=84?120:100):100)"
    combo_damage = "(job==37?(lv>=84?340:320):320)"


class Action16146(Action):
    # 对目标发动物理攻击
    # 威力：360
    # (job==37?(level>=70?追加效果：撕喉预备
    # 持续时间：10秒
    # 发动战技会导致该效果消失
    # :):)发动条件：晶壤
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 360.
    # (job==37?(level>=70?Additional Effect: Grants Ready to Rip
    # Duration: 10s
    # :):)Cartridge Cost: 1
    # This weaponskill does not share a recast timer with any other actions.
    id = 16146
    names = ['Gnashing Fang(GNB)', '烈牙(GNB)']
    _orig_names = ['烈牙', 'Gnashing Fang']
    damage = 360


class Action16147(Action):
    # 对目标发动物理攻击
    # 威力：440
    # 连击条件：烈牙
    # (job==37?(level>=70?追加效果：裂膛预备
    # 持续时间：10秒
    # 发动战技会导致该效果消失
    # :):)发动条件：满足连击条件
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 440.
    # Combo Action: Gnashing Fang(job==37?(level>=70?
    # Combo Bonus: Grants Ready to Tear
    # Duration: 10s:):)
    # ※This action cannot be assigned to a hotbar.
    id = 16147
    names = ['Savage Claw(GNB)', '猛兽爪(GNB)']
    _orig_names = ['Savage Claw', '猛兽爪']
    combo_action = 16146
    damage = 440


class Action16148(Action):
    # 一定时间内，将自身所受的伤害减轻30%
    # 持续时间：15秒
    # Reduces damage taken by 30%.
    # Duration: 15s
    # related: [星云](Status1834),
    id = 16148
    names = ['星云(GNB)', 'Nebula(GNB)']
    _orig_names = ['星云', 'Nebula']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action16149(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：恶魔切
    # 连击中威力：160
    # 连击成功：晶壤
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: Demon Slice
    # Combo Potency: 160
    # Combo Bonus: Adds a Cartridge to your Powder Gauge
    id = 16149
    names = ['Demon Slaughter(GNB)', '恶魔杀(GNB)']
    _orig_names = ['Demon Slaughter', '恶魔杀']
    combo_action = 16141
    damage = 100
    combo_damage = 160


class Action16150(Action):
    # 对目标发动物理攻击
    # 威力：520
    # 连击条件：猛兽爪
    # (job==37?(level>=70?追加效果：穿目预备
    # 持续时间：10秒
    # 发动战技会导致该效果消失
    # :):)发动条件：满足连击条件
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 520.
    # Combo Action: Savage Claw(job==37?(level>=70?
    # Combo Bonus: Grants Ready to Gouge
    # Duration: 10s:):)
    # ※This action cannot be assigned to a hotbar.
    id = 16150
    names = ['Wicked Talon(GNB)', '凶禽爪(GNB)']
    _orig_names = ['凶禽爪', 'Wicked Talon']
    combo_action = 16147
    damage = 520


class Action16151(Action):
    # 令目标体力持续恢复
    # 恢复力：200
    # 持续时间：18秒(job==37?(level>=84?
    # 积蓄次数：2:):)
    # Grants Regen to target.
    # Cure Potency: 200
    # Duration: 18s(job==37?(level>=84?
    # Maximum Charges: 2:):)
    # related: [极光(0)](Status2065), [极光(1)](Status1835),
    id = 16151
    names = ['Aurora(GNB)', '极光(GNB)']
    _orig_names = ['Aurora', '极光']
    # remain metas: {'heal_ot': '200'}


class Action16152(Action):
    # 发动该技能后，自身的体力降为1，同时在持续时间内，除一部分特定攻击之外，免除自身受到的任何伤害
    # 持续时间：10秒
    # Reduces HP to 1 and renders you impervious to most attacks.
    # Duration: 10s
    # related: [超火流星](Status1836),
    id = 16152
    names = ['超火流星(GNB)', 'Superbolide(GNB)']
    _orig_names = ['超火流星', 'Superbolide']


class Action16153(Action):
    # 对目标发动物理攻击
    # 威力：300
    # 追加效果：持续伤害
    # 威力：60
    # 持续时间：30秒
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 300.
    # Additional Effect: Damage over time
    # Potency: 60
    # Duration: 30s
    # This weaponskill does not share a recast timer with any other actions.
    # related: [音速破](Status1837),
    id = 16153
    names = ['Sonic Break(GNB)', '音速破(GNB)']
    _orig_names = ['音速破', 'Sonic Break']
    damage = 300
    # remain metas: {'dmg_ot': '60'}


class Action16154(Action):
    # 跃向目标并发动物理攻击
    # 威力：150
    # 积蓄次数：2
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 150.
    # Maximum Charges: 2
    # Cannot be executed while bound.
    id = 16154
    names = ['粗分斩(GNB)', 'Rough Divide(GNB)']
    _orig_names = ['Rough Divide', '粗分斩']
    damage = 150


class Action16155(Action):
    # 发动部分技能后，该技能发生变化
    # 发动烈牙后：该技能变为撕喉
    # 发动猛兽爪后：该技能变为裂膛
    # 发动凶禽爪后：该技能变为穿目(job==37?(level>=86?
    # 发动爆发击后：该技能变为超高速:):)
    # Allows the firing of successive rounds with your gunblade.
    # Gnashing Fang may be followed by Jugular Rip.
    # Savage Claw may be followed by Abdomen Tear.
    # Wicked Talon may be followed by Eye Gouge.(job==37?(level>=86?
    # Burst Strike may be followed by Hypervelocity.:):)
    id = 16155
    names = ['续剑(GNB)', 'Continuation(GNB)']
    _orig_names = ['Continuation', '续剑']


class Action16156(Action):
    # 对目标发动物理攻击
    # 威力：180
    # 发动条件：撕喉预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 180.
    # Can only be executed when Ready to Rip.
    # ※This action cannot be assigned to a hotbar.
    # related: [撕喉预备(0)](Status2002), [撕喉预备(1)](Status1842),
    id = 16156
    names = ['Jugular Rip(GNB)', '撕喉(GNB)']
    _orig_names = ['撕喉', 'Jugular Rip']
    damage = 180


class Action16157(Action):
    # 对目标发动物理攻击
    # 威力：220
    # 发动条件：裂膛预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 220.
    # Can only be executed when Ready to Tear.
    # ※This action cannot be assigned to a hotbar.
    # related: [裂膛预备(0)](Status1843), [裂膛预备(1)](Status2003),
    id = 16157
    names = ['Abdomen Tear(GNB)', '裂膛(GNB)']
    _orig_names = ['裂膛', 'Abdomen Tear']
    damage = 220


class Action16158(Action):
    # 对目标发动物理攻击
    # 威力：260
    # 发动条件：穿目预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 260.
    # Can only be executed when Ready to Gouge.
    # ※This action cannot be assigned to a hotbar.
    # related: [穿目预备(0)](Status2004), [穿目预备(1)](Status1844),
    id = 16158
    names = ['Eye Gouge(GNB)', '穿目(GNB)']
    _orig_names = ['穿目', 'Eye Gouge']
    damage = 260


class Action16159(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：150
    # 追加效果：持续伤害
    # 威力：60
    # 持续时间：15秒
    # Delivers an attack with a potency of 150 to all nearby enemies.
    # Additional Effect: Damage over time
    # Potency: 60
    # Duration: 15s
    # related: [弓形冲波](Status1838),
    id = 16159
    names = ['Bow Shock(GNB)', '弓形冲波(GNB)']
    _orig_names = ['弓形冲波', 'Bow Shock']
    damage = 150
    # remain metas: {'dmg_ot': '60'}


class Action16160(Action):
    # 一定时间内，令自身和周围队员所受到的魔法伤害减轻10%
    # 持续时间：15秒
    # Reduces magic damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # related: [光之心(0)](Status2000), [光之心(1)](Status1839),
    id = 16160
    names = ['Heart of Light(GNB)', '光之心(GNB)']
    _orig_names = ['光之心', 'Heart of Light']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action16161(Action):
    # 令自身或一名队员受到的伤害减轻15%
    # 持续时间：7秒
    # 追加效果：对队员使用时，若自身附加了残暴弹状态，则目标队员也会附加该状态
    # 持续时间：30秒
    # Reduces damage taken by a party member or self by 15%.
    # Duration: 7s
    # Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target
    # Duration: 30s
    # related: [石之心](Status1840), [残暴弹(0)](Status1898), [残暴弹(1)](Status1997),
    id = 16161
    names = ['Heart of Stone(GNB)', '石之心(GNB)']
    _orig_names = ['Heart of Stone', '石之心']
    # remain metas: {'taken_dmg_reduce': '15%'}


class Action16162(Action):
    # 对目标发动物理攻击
    # 威力：380
    # (job==37?(level>=86?追加效果：超高速预备
    # 持续时间：10秒
    # 发动战技会导致该效果消失
    # :):)发动条件：晶壤
    # Delivers an attack with a potency of 380.
    # (job==37?(level>=86?Additional Effect: Grants Ready to Blast
    # Duration: 10s
    # :):)Cartridge Cost: 1
    id = 16162
    names = ['Burst Strike(GNB)', '爆发击(GNB)']
    _orig_names = ['爆发击', 'Burst Strike']
    damage = 380


class Action16163(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：290
    # 发动条件：晶壤
    # Delivers an attack with a potency of 290 to all nearby enemies.
    # Cartridge Cost: 1
    id = 16163
    names = ['Fated Circle(GNB)', '命运之环(GNB)']
    _orig_names = ['Fated Circle', '命运之环']
    damage = 290


class Action16164(Action):
    # 以一名敌人为目标
    # 对自身附加(job==37?(level>=88?3:2):2)档晶壤
    # Draws aetheric energy from target, adding (job==37?(level>=88?3:2):2) Cartridges to your Powder Gauge.
    id = 16164
    names = ['血壤(GNB)', 'Bloodfest(GNB)']
    _orig_names = ['血壤', 'Bloodfest']


class Action16165(Action):
    # 对目标发动物理攻击
    # 威力：700
    # Delivers an attack with a potency of 700.
    id = 16165
    names = ['Blasting Zone(GNB)', '爆破领域(GNB)']
    _orig_names = ['Blasting Zone', '爆破领域']
    damage = 700


class Action17703(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # ※This action cannot be assigned to a hotbar.
    # related: [双刃剑](Status1145),
    id = 17703
    names = ['Keen Edge(pvp)(GNB)', '利刃斩(pvp)(GNB)']
    _orig_names = ['利刃斩(pvp)', 'Keen Edge(pvp)']
    damage = 1000


class Action17704(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：利刃斩
    # 连击成功：为自身附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力1200的伤害量
    # 持续时间：10秒
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Keen Edge
    # Combo Potency: 1,200
    # Combo Bonus: Creates a barrier around self that absorbs damage equivalent to a heal of 1,200 potency
    # Duration: 10s
    # ※This action cannot be assigned to a hotbar.
    # related: [残暴弹(0)](Status1898), [残暴弹(1)](Status1997),
    id = 17704
    names = ['Brutal Shell(pvp)(GNB)', '残暴弹(pvp)(GNB)']
    _orig_names = ['残暴弹(pvp)', 'Brutal Shell(pvp)']
    combo_action = 17703
    combo_damage = 1200
    # remain metas: {'shield': '恢复力1200'}


class Action17705(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：残暴弹
    # 连击成功：晶壤
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Brutal Shell
    # Combo Potency: 1,400
    # Combo Bonus: Adds a Cartridge to your Powder Gauge
    # ※This action cannot be assigned to a hotbar.
    id = 17705
    names = ['Solid Barrel(pvp)(GNB)', '迅连斩(pvp)(GNB)']
    _orig_names = ['Solid Barrel(pvp)', '迅连斩(pvp)']
    combo_action = 17704
    combo_damage = 1400


class Action17706(Action):
    # 对目标发动物理攻击
    # 威力：1400
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：撕喉预备
    # 持续时间：5秒
    # 发动条件：晶壤
    # 该战技有单独计算的复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,400.
    # Additional Effect: Grants Ready to Rip
    # Duration: 5s
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Cartridge Cost: 1
    # This weaponskill does not share a recast timer with any other actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [撕喉预备(0)](Status2002), [撕喉预备(1)](Status1842),
    id = 17706
    names = ['烈牙(pvp)(GNB)', 'Gnashing Fang(pvp)(GNB)']
    _orig_names = ['烈牙(pvp)', 'Gnashing Fang(pvp)']
    damage = 1400


class Action17707(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：烈牙
    # 追加效果：恢复伤害量100%的体力
    # 连击成功：裂膛预备
    # 持续时间：5秒
    # 发动条件：晶壤
    # 该战技有单独计算的复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Gnashing Fang
    # Combo Potency: 1,600
    # Combo Bonus: Grants Ready to Tear
    # Duration: 5s
    # Combo Bonus: Absorbs 100% of damage dealt as HP
    # ※This action cannot be assigned to a hotbar.
    id = 17707
    names = ['Savage Claw(pvp)(GNB)', '猛兽爪(pvp)(GNB)']
    _orig_names = ['猛兽爪(pvp)', 'Savage Claw(pvp)']
    combo_action = 17706
    combo_damage = 1600


class Action17708(Action):
    # 对目标发动物理攻击
    # 连击中威力：1800
    # 连击条件：猛兽爪
    # 追加效果：恢复伤害量100%的体力
    # 连击成功：穿目预备
    # 持续时间：5秒
    # 发动条件：晶壤
    # 该战技有单独计算的复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Savage Claw
    # Combo Potency: 1,800
    # Combo Bonus: Grants Ready to Gouge
    # Duration: 5s
    # Combo Bonus: Absorbs 100% of damage dealt as HP
    # ※This action cannot be assigned to a hotbar.
    id = 17708
    names = ['凶禽爪(pvp)(GNB)', 'Wicked Talon(pvp)(GNB)']
    _orig_names = ['Wicked Talon(pvp)', '凶禽爪(pvp)']
    combo_action = 17707
    combo_damage = 1800


class Action17709(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 追加效果：恢复伤害量100%的体力
    # 发动条件：晶壤
    # Delivers an attack with a potency of 1,800.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Cartridge Cost: 1
    id = 17709
    names = ['Burst Strike(pvp)(GNB)', '爆发击(pvp)(GNB)']
    _orig_names = ['爆发击(pvp)', 'Burst Strike(pvp)']
    damage = 1800


class Action17710(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：1200
    # 追加效果：恢复伤害量100%的体力
    # 发动条件：晶壤
    # Delivers an attack with a potency of 1,200 to all nearby enemies.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Cartridge Cost: 1
    id = 17710
    names = ['命运之环(pvp)(GNB)', 'Fated Circle(pvp)(GNB)']
    _orig_names = ['命运之环(pvp)', 'Fated Circle(pvp)']
    damage = 1200


class Action17711(Action):
    # 对目标发动追击
    # 使用烈牙后可以发动撕喉，使用猛兽爪后可以发动裂膛，使用凶禽爪后可以发动穿目
    # Allows the firing of successive rounds with your gunblade.
    # Gnashing Fang may be followed by Jugular Rip.
    # Savage Claw may be followed by Abdomen Tear.
    # Wicked Talon may be followed by Eye Gouge.
    id = 17711
    names = ['Continuation(pvp)(GNB)', '续剑(pvp)(GNB)']
    _orig_names = ['Continuation(pvp)', '续剑(pvp)']


class Action17712(Action):
    # 对目标发动物理攻击
    # 威力：800
    # 发动条件：撕喉预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 800.
    # Can only be executed when Ready to Rip.
    # ※This action cannot be assigned to a hotbar.
    # related: [撕喉预备(0)](Status2002), [撕喉预备(1)](Status1842),
    id = 17712
    names = ['撕喉(pvp)(GNB)', 'Jugular Rip(pvp)(GNB)']
    _orig_names = ['撕喉(pvp)', 'Jugular Rip(pvp)']
    damage = 800


class Action17713(Action):
    # 对目标发动物理攻击
    # 威力：800
    # 发动条件：裂膛预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 800.
    # Can only be executed when Ready to Tear.
    # ※This action cannot be assigned to a hotbar.
    # related: [裂膛预备(0)](Status1843), [裂膛预备(1)](Status2003),
    id = 17713
    names = ['Abdomen Tear(pvp)(GNB)', '裂膛(pvp)(GNB)']
    _orig_names = ['裂膛(pvp)', 'Abdomen Tear(pvp)']
    damage = 800


class Action17714(Action):
    # 对目标发动物理攻击
    # 威力：800
    # 发动条件：穿目预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 800.
    # Can only be executed when Ready to Gouge.
    # ※This action cannot be assigned to a hotbar.
    # related: [穿目预备(0)](Status2004), [穿目预备(1)](Status1844),
    id = 17714
    names = ['Eye Gouge(pvp)(GNB)', '穿目(pvp)(GNB)']
    _orig_names = ['Eye Gouge(pvp)', '穿目(pvp)']
    damage = 800


class Action17716(Action):
    # 冲向目标并发动物理攻击
    # 威力：600
    # 追加效果：晶壤
    # 积蓄次数：2
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 600.
    # Additional Effect: Adds a Cartridge to your Powder Gauge
    # Maximum Charges: 2
    # Cannot be executed while bound.
    id = 17716
    names = ['粗分斩(pvp)(GNB)', 'Rough Divide(pvp)(GNB)']
    _orig_names = ['Rough Divide(pvp)', '粗分斩(pvp)']
    damage = 600


class Action17717(Action):
    # 对目标发动远程物理攻击
    # 威力：800
    # 追加效果：效果时间内，自身发动的1次战技的伤害提高50%
    # 持续时间：5秒
    # Delivers a ranged attack with a potency of 800.
    # Additional Effect: Increases potency of next weaponskill by 50%
    # Duration: 5s
    # related: [闪雷弹](Status2392),
    id = 17717
    names = ['Lightning Shot(pvp)(GNB)', '闪雷弹(pvp)(GNB)']
    _orig_names = ['Lightning Shot(pvp)', '闪雷弹(pvp)']
    damage = 800
    # remain metas: {'dmg_increase': '50%'}


class Action17748(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：1000
    # 抽近融合中追加效果：50%加重
    # 持续时间：5秒
    # 抽远融合中追加效果：止步
    # 持续时间：3秒
    #
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Draw Power Bonus: Heavy +50%
    # Duration: 5s
    # Draw Fortitude Bonus: Bind
    # Duration: 3s
    # related: [弓形冲波](Status1838),
    id = 17748
    names = ['弓形冲波(pvp)(GNB)', 'Bow Shock(pvp)(GNB)']
    _orig_names = ['Bow Shock(pvp)', '弓形冲波(pvp)']
    damage = 1000


class Action17890(Action):
    # 削弱目标的同时强化自身
    # 如果当前已经附加了强化效果，则覆盖当前效果
    # 若目标是以近身攻击为主的职业，则目标受到的伤害提高10%，自身所受伤害减轻10%
    # 若目标是以远程攻击为主的职业，则目标攻击伤害、恢复效果降低10%，自身攻击伤害、恢复效果提高10%
    # 弱化效果持续时间：15秒
    # 强化效果持续时间：15秒
    # Afflicts target with a detrimental effect while granting self a beneficial one.
    # If target is melee DPS or tank, increases target's damage taken by 10% while reducing your damage taken by 10%.
    # If target is ranged DPS or healer, lowers target's damage dealt and healing potency by 10% while increasing your damage dealt and healing potency by 10%.
    # Previously acquired beneficial effects are overwritten on use.
    # Detrimental Effect Duration: 15s
    # Beneficial Effect Duration: 15s
    id = 17890
    names = ['Draw and Junction(pvp)(GNB)', '抽取融合(pvp)(GNB)']
    _orig_names = ['抽取融合(pvp)', 'Draw and Junction(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%', 'taken_dmg_increase': '10%，自身所受伤害减轻10%'}


class Action17891(Action):
    # 恢复目标的体力
    # 恢复力：3000
    # 追加效果：目标体力持续恢复
    # 恢复力：600
    # 持续时间：15秒
    # Restores target's HP.
    # Cure Potency: 3,000
    # Additional Effect: Grants Regen
    # Cure Potency: 600
    # Duration: 15s
    # related: [极光(0)](Status2065), [极光(1)](Status1835),
    id = 17891
    names = ['极光(pvp)(GNB)', 'Aurora(pvp)(GNB)']
    _orig_names = ['极光(pvp)', 'Aurora(pvp)']
    heal = 3000
    # remain metas: {'heal_ot': '600'}


class Action18910(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：600
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # ※This action cannot be assigned to a hotbar.
    id = 18910
    names = ['恶魔切(pvp)(GNB)', 'Demon Slice(pvp)(GNB)']
    _orig_names = ['Demon Slice(pvp)', '恶魔切(pvp)']
    damage = 600


class Action18911(Action):
    # 对自身周围的敌人发动物理攻击
    # 连击中威力：800
    # 连击条件：恶魔切
    # 连击成功：为自身张开一个防护罩，能抵消相当于800恢复力的伤害量
    # 持续时间：10秒
    # 连击成功：晶壤
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Demon Slice
    # Combo Potency: 800
    # Combo Bonus: Creates a barrier around self that absorbs damage equivalent to a heal of 800 potency
    # Duration: 10s
    # Combo Bonus: Adds a Cartridge to your Powder Gauge
    # ※This action cannot be assigned to a hotbar.
    id = 18911
    names = ['Demon Slaughter(pvp)(GNB)', '恶魔杀(pvp)(GNB)']
    _orig_names = ['Demon Slaughter(pvp)', '恶魔杀(pvp)']
    combo_action = 18910
    combo_damage = 800
    # remain metas: {'shield': '800恢复力'}


class Action25758(Action):
    # 令自身或一名队员受到的伤害减轻15%
    # 持续时间：8秒
    # 追加效果：对队员使用时，若自身附加了残暴弹状态，则目标队员也会附加该状态
    # 持续时间：30秒
    # 追加效果：为目标附加刚玉之清状态
    # 持续时间：4秒
    # 刚玉之清效果：令目标受到的伤害减轻15%
    # 追加效果：刚玉之净
    # 持续时间：20秒
    # 刚玉之净效果：体力低于50%时或持续时间结束后自动恢复
    # 恢复力：900
    # Reduces damage taken by a party member or self by 15%.
    # Duration: 8s
    # Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target
    # Duration: 30s
    # Additional Effect: Grants Clarity of Corundum to target
    # Clarity of Corundum Effect: Reduces damage taken by 15%
    # Duration: 4s
    # Additional Effect: Grants Catharsis of Corundum to target
    # Catharsis of Corundum Effect: Restores HP when HP falls below 50% or upon effect duration expiration
    # Cure Potency: 900
    # Duration: 20s
    # related: [残暴弹(1)](Status1997), [残暴弹(0)](Status1898), [刚玉之心](Status2683), [刚玉之清](Status2684), [刚玉之净](Status2685),
    id = 25758
    names = ['Heart of Corundum(GNB)', '刚玉之心(GNB)']
    _orig_names = ['Heart of Corundum', '刚玉之心']
    # remain metas: {'taken_dmg_reduce': '15%', 'heal_ot': '900'}


class Action25759(Action):
    # 对目标发动物理攻击
    # 威力：180
    # 发动条件：超高速预备状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 180.
    # Can only be executed when Ready to Blast.
    # ※This action cannot be assigned to a hotbar.
    # related: [超高速](Status2686),
    id = 25759
    names = ['超高速(GNB)', 'Hypervelocity(GNB)']
    _orig_names = ['超高速', 'Hypervelocity']
    damage = 180


class Action25760(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：1200
    # 攻击复数敌人时，对第一个之外的敌人威力降低20%
    # 发动条件：晶壤2
    # 该战技有单独计算的复唱时间
    # Delivers an attack to all nearby enemies with a potency of 1,200 for the first enemy, and 20% less for all remaining enemies.
    # Cartridge Cost: 2
    # This weaponskill does not share a recast timer with any other actions.
    id = 25760
    names = ['Double Down(GNB)', '倍攻(GNB)']
    _orig_names = ['Double Down', '倍攻']
    damage = 1200
