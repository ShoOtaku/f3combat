from ._base import *


class Status289(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 289
    names = ['水毒(0)', 'Dropsy(0)']


class Status485(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 485
    names = ['水毒(1)', 'Dropsy(1)']


class Status2950(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 2950
    names = ['水毒(2)', 'Dropsy(2)']


class Status2087(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 2087
    names = ['水毒(3)', 'Dropsy(3)']


class Status1736(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 1736
    names = ['水毒(4)', 'Dropsy(4)']


class Status2921(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 2921
    names = ['水毒(5)', 'Dropsy(5)']


class Status272(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 272
    names = ['水毒(6)', 'Dropsy(6)']


class Status531(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 531
    names = ['水毒(7)', 'Dropsy(7)']


class Status283(Status):
    # 水属性持续伤害，体力逐渐流失
    # Sustaining water damage over time.
    # related: [高压电流(BLU)](Action11387), [狂风暴雪(BLU)](Action18297), 
    id = 283
    names = ['水毒(8)', 'Dropsy(8)']


class Status1088(Status):
    # 陷于黑暗之中，命中率降低
    # Encroaching darkness is lowering accuracy.
    # related: [臭气(BLU)](Action11388), [喷墨(BLU)](Action11422), 
    id = 1088
    names = ['失明(0)', 'Blind(0)']


class Status15(Status):
    # 陷于黑暗之中，命中率降低
    # Encroaching darkness is lowering accuracy.
    # related: [臭气(BLU)](Action11388), [喷墨(BLU)](Action11422), 
    id = 15
    names = ['失明(1)', 'Blind(1)']


class Status1524(Status):
    # 陷于黑暗之中，命中率降低
    # Encroaching darkness is lowering accuracy.
    # related: [臭气(BLU)](Action11388), [喷墨(BLU)](Action11422), 
    id = 1524
    names = ['失明(2)', 'Blind(2)']


class Status571(Status):
    # 陷于黑暗之中，命中率降低
    # Encroaching darkness is lowering accuracy.
    # related: [臭气(BLU)](Action11388), [喷墨(BLU)](Action11422), 
    id = 571
    names = ['失明(3)', 'Blind(3)']


class Status402(Status):
    # 受到挑衅愤怒不已，会不停地追赶挑衅者
    # Provoked beyond all mortal limits and heedless of danger. Can only pursue the target.
    # related: [怒发冲冠(BLU)](Action11393), 
    id = 402
    names = ['怒发冲冠', 'Thrown for a Loop']


class Status2118(Status):
    # 下一个发动的魔法属于物理攻击时威力提升
    # Potency of next physical damage spell is increased.
    # related: [怒发冲冠(BLU)](Action11393), 
    id = 2118
    names = ['攻击准备', 'Harmonized']


class Status211(Status):
    # 菜刀的攻击力提升
    # Next Lateral Slash is changed to Sharpened Knife, increasing damage dealt.
    # related: [锋利菜刀(BLU)](Action11400), 
    id = 211
    names = ['打磨好的菜刀', 'Sharpened Knife']


class Status2127(Status):
    # 意志产生了动摇，无法使用部分需要赴死的技能
    # Your resolve has deserted you. You are unable to perform actions that would result in your death.
    # related: [终极针(BLU)](Action11407), [自爆(BLU)](Action11408), [融合(BLU)](Action11409), 
    id = 2127
    names = ['意志薄弱', 'Brush with Death']


class Status1737(Status):
    # 回避率提高
    # Evasion is enhanced.
    # related: [自爆(BLU)](Action11408), [油性分泌物(BLU)](Action11410), 
    id = 1737
    names = ['油性分泌物', 'Toad Oil']


class Status1717(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [破防(BLU)](Action11411), 
    id = 1717
    names = ['破防', 'Off-guard']


class Status1727(Status):
    # 无法发动自动攻击、魔法、战技和能力
    # Unable to auto-attack or use spells, weaponskills, and abilities.
    # related: [月之笛(BLU)](Action11415), 
    id = 1727
    names = ['狂战士化的副作用', 'Waning Nocturne']


class Status1769(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero. Effect dissipates once fully healed.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 1769
    names = ['死亡宣告(0)', 'Doom(0)']


class Status1738(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 1738
    names = ['死亡宣告(1)', 'Doom(1)']


class Status910(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 910
    names = ['死亡宣告(2)', 'Doom(2)']


class Status1970(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 1970
    names = ['死亡宣告(3)', 'Doom(3)']


class Status210(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 210
    names = ['死亡宣告(4)', 'Doom(4)']


class Status2516(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 2516
    names = ['死亡宣告(5)', 'Doom(5)']


class Status2519(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [死亡宣告(BLU)](Action11416), 
    id = 2519
    names = ['死亡宣告(6)', 'Doom(6)']


class Status2528(Status):
    # 能够发动冰属性反击，追加减速效果
    # Elemental spikes are dealing ice damage to and slowing down attackers.
    # related: [冰棘屏障(BLU)](Action11418), 
    id = 2528
    names = ['冰棘屏障(0)', 'Ice Spikes(0)']


class Status198(Status):
    # 能够发动冰属性反击，偶尔会追加减速效果
    # Elemental spikes are dealing ice damage to and sometimes slowing down attackers.
    # related: [冰棘屏障(BLU)](Action11418), 
    id = 198
    names = ['冰棘屏障(1)', 'Ice Spikes(1)']


class Status1720(Status):
    # 受到物理攻击时，攻击方将受到冰属性伤害，并有一定几率被附加减速状态
    # Upon taking physical damage, sharpened spikes deal ice damage to the attacking opponent, potentially slowing them.
    # related: [冰棘屏障(BLU)](Action11418), 
    id = 1720
    names = ['冰棘屏障(2)', 'Ice Spikes(2)']


class Status1307(Status):
    # 受到物理攻击时，攻击方将受到冰属性伤害，并有一定几率被附加减速状态
    # Upon taking physical damage, sharpened spikes deal ice damage to the attacking opponent, potentially slowing them.
    # related: [冰棘屏障(BLU)](Action11418), 
    id = 1307
    names = ['冰棘屏障(3)', 'Ice Spikes(3)']


class Status2658(Status):
    # 被冻住，无法做出任何行动
    # Frozen solid and unable to execute actions.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 2658
    names = ['冻结(0)', 'Deep Freeze(0)']


class Status1731(Status):
    # 被冻住，无法做出任何行动
    # Frozen solid and unable to execute actions.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 1731
    names = ['冻结(1)', 'Deep Freeze(1)']


class Status1254(Status):
    # 身体被冻结无法行动，体力逐渐流失
    # Your body is encased in ice, preventing action and dealing damage over time.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 1254
    names = ['冻结(2)', 'Deep Freeze(2)']


class Status487(Status):
    # 身体被冻结无法行动，体力逐渐流失
    # Your body is encased in ice, preventing action and dealing damage over time.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 487
    names = ['冻结(3)', 'Deep Freeze(3)']


class Status2252(Status):
    # 身体被冻住，无法做出任何行动
    # Your body is encased in ice, preventing action.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 2252
    names = ['冻结(4)', 'Deep Freeze(4)']


class Status1758(Status):
    # 身体被冻结无法行动，体力逐渐流失
    # Your body is encased in ice, preventing action and dealing damage over time.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 1758
    names = ['冻结(5)', 'Deep Freeze(5)']


class Status1150(Status):
    # 身体被冻结无法行动，体力逐渐流失
    # Your body is encased in ice, preventing action and dealing damage over time.
    # related: [寒冰咆哮(BLU)](Action11419), [雷电咆哮(BLU)](Action11420), [狂风暴雪(BLU)](Action18297), [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 1150
    names = ['冻结(6)', 'Deep Freeze(6)']


class Status1722(Status):
    # 无法自由活动，但受到攻击的伤害减少
    # Though unable to move, damage taken is reduced.
    # related: [超硬化(BLU)](Action11424), 
    id = 1722
    names = ['超硬化', 'Diamondback']


class Status1718(Status):
    # 造成的伤害和移动速度提高，效果结束时将被附加狂战士化的副作用
    # Damage dealt and movement speed are increased. Waning Nocturne will take hold when the effect ends.
    # related: [超硬化(BLU)](Action11424), 
    id = 1718
    names = ['狂战士化', 'Waxing Nocturne']


class Status1724(Status):
    # 受到攻击时，攻击方将受到水属性伤害
    # Dealing water damage to attackers upon taking damage.
    # related: [水神的面纱(BLU)](Action11431), 
    id = 1724
    names = ['水神的面纱(0)', 'Veil of the Whorl(0)']


class Status478(Status):
    # 反射远程物理攻击所造成的伤害
    # Reflecting damage dealt by ranged attacks.
    # related: [水神的面纱(BLU)](Action11431), 
    id = 478
    names = ['水神的面纱(1)', 'Veil of the Whorl(1)']


class Status2126(Status):
    # 复制了治疗职业的以太
    # Copying the aetherial properties of a healer.
    # related: [绒绒治疗(BLU)](Action18303), [哥布防御(BLU)](Action18304), [蜕皮(BLU)](Action18318), [以太复制(BLU)(0)](Action18322), [以太复制(BLU)(1)](Action19238), [以太复制(BLU)(2)](Action19239), [赞歌(BLU)(0)](Action23269), [天使的点心(BLU)](Action23272), [赞歌(BLU)(1)](Action23416), 
    id = 2126
    names = ['以太复制：治疗', 'Aetherial Mimicry: Healer']


class Status2114(Status):
    # 抵消一定伤害
    # Hardened flesh is absorbing damage.
    # related: [哥布防御(BLU)](Action18304), 
    id = 2114
    names = ['哥布防御', 'Gobskin']


class Status2116(Status):
    # 下达了防御指示，让特定队员替自己承受伤害
    # A designated party member is protecting you.
    # related: [防御指示(BLU)](Action18306), 
    id = 2116
    names = ['防御指示(0)', 'Meatily Shielded']


class Status2117(Status):
    # 被下达了防御指示，替特定队员承受伤害
    # You are protecting a party member.
    # related: [防御指示(BLU)](Action18306), 
    id = 2117
    names = ['防御指示(1)', 'Meat Shield']


class Status880(Status):
    # 根据档数的不同会附带各种各样的制作效果
    # Synthesis-related effects granted based on stack size.
    # related: [口笛(BLU)](Action18309), 
    id = 880
    names = ['工作小调', 'Whistle']


class Status193(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 193
    names = ['减速(0)', 'Slow(0)']


class Status1346(Status):
    # 战技与魔法的咏唱及复唱时间延长
    # Weaponskill and spell cast time and recast time are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 1346
    names = ['减速(1)', 'Slow(1)']


class Status561(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 561
    names = ['减速(2)', 'Slow(2)']


class Status1509(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 1509
    names = ['减速(3)', 'Slow(3)']


class Status2246(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 2246
    names = ['减速(4)', 'Slow(4)']


class Status9(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 9
    names = ['减速(5)', 'Slow(5)']


class Status442(Status):
    # 自动攻击间隔延长，同时战技与魔法的咏唱及复唱时间也会延长
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are increased.
    # related: [黑骑士之旅(BLU)](Action18311), 
    id = 442
    names = ['减速(6)', 'Slow(6)']


class Status2124(Status):
    # 复制了防护职业的以太
    # Copying the aetherial properties of a tank.
    # related: [仙人盾(BLU)](Action18315), [捕食(BLU)](Action18320), [以太复制(BLU)(0)](Action18322), [以太复制(BLU)(2)](Action19239), [以太复制(BLU)(3)](Action19240), [玄结界(BLU)](Action23273), [玄天武水壁(BLU)](Action23274), [龙之力(BLU)](Action23280), 
    id = 2124
    names = ['以太复制：防护', 'Aetherial Mimicry: Tank']


class Status2119(Status):
    # 受到的伤害降低
    # Damage taken is reduced.
    # related: [仙人盾(BLU)](Action18315), 
    id = 2119
    names = ['仙人盾', 'Cactguard']


class Status421(Status):
    # 被吞了下去无法做出任何行动，体力逐渐减少
    # Being devoured is preventing the execution of actions and causing damage over time. 
    # related: [捕食(BLU)](Action18320), 
    id = 421
    names = ['捕食', 'Devoured']


class Status934(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 934
    names = ['物理受伤加重(0)', 'Physical Vulnerability Up(0)']


class Status200(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 200
    names = ['物理受伤加重(1)', 'Physical Vulnerability Up(1)']


class Status2121(Status):
    # 对抗火、风、雷属性的耐性有所降低
    # Fire-, wind-, and lightning-aspected damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 2121
    names = ['星极性耐性降低', 'Astral Attenuation']


class Status2090(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 2090
    names = ['物理受伤加重(2)', 'Physical Vulnerability Up(2)']


class Status2123(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 2123
    names = ['物理受伤加重(3)', 'Physical Attenuation']


class Status2122(Status):
    # 对抗水、土、冰属性的耐性有所降低
    # Water-, earth-, and ice-aspected damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 2122
    names = ['灵极性耐性降低', 'Umbral Attenuation']


class Status493(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 493
    names = ['物理受伤加重(4)', 'Physical Vulnerability Up(3)']


class Status657(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 657
    names = ['物理受伤加重(5)', 'Physical Vulnerability Up(4)']


class Status695(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 695
    names = ['物理受伤加重(6)', 'Physical Vulnerability Up(5)']


class Status56(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 56
    names = ['物理受伤加重(7)', 'Physical Vulnerability Up(6)']


class Status2940(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 2940
    names = ['物理受伤加重(8)', 'Physical Vulnerability Up(7)']


class Status126(Status):
    # 受到物理攻击的伤害增加
    # Physical damage taken is increased.
    # related: [小侦测(BLU)](Action18321), 
    id = 126
    names = ['物理受伤加重(9)', 'Physical Vulnerability Up(8)']


class Status2125(Status):
    # 复制了进攻职业的以太
    # Copying the aetherial properties of a DPS.
    # related: [以太复制(BLU)(0)](Action18322), [以太复制(BLU)(1)](Action19238), [以太复制(BLU)(3)](Action19240), [马特拉魔术(BLU)](Action23285), 
    id = 2125
    names = ['以太复制：进攻', 'Aetherial Mimicry: DPS']


class Status2492(Status):
    # 下一个发动的魔法属于物理攻击时威力提升
    # Potency of next physical damage spell is increased.
    # related: [哔哩哔哩(BLU)](Action23265), 
    id = 2492
    names = ['哔哩哔哩', 'Tingling']


class Status2493(Status):
    # 被彻骨雾寒包裹，受到伤害后将附加冰雾状态
    # Enveloped in a cold fog. Any damage taken will grant the effect of Touch of Frost.
    # related: [彻骨雾寒(BLU)](Action23267), 
    id = 2493
    names = ['彻骨雾寒', 'Cold Fog']


class Status2494(Status):
    # 被冰雾包裹，可以使用青魔法“冰雾”
    # Enveloped in an icy fog. Able to execute the blue magic spell White Death.
    # related: [彻骨雾寒(BLU)](Action23267), [冰雾(BLU)](Action23268), 
    id = 2494
    names = ['冰雾', 'Touch of Frost']


class Status2495(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [天使的点心(BLU)](Action23272), 
    id = 2495
    names = ['天使的点心', "Angel's Snack"]


class Status2496(Status):
    # 减轻所受到的伤害，受到一定伤害后将附加玄天武水壁状态
    # Damage taken is reduced. Taking a certain amount of damage grants the effect of Auspicious Trance.
    # related: [玄结界(BLU)](Action23273), 
    id = 2496
    names = ['玄结界', 'Chelonian Gate']


class Status2497(Status):
    # 可以使用青魔法“玄天武水壁”
    # Able to execute the blue magic spell Divine Cataract.
    # related: [玄结界(BLU)](Action23273), [玄天武水壁(BLU)](Action23274), 
    id = 2497
    names = ['玄天武水壁', 'Auspicious Trance']


class Status2498(Status):
    # 自身攻击造成的伤害及治疗魔法的治疗量提高并且移动速度上升，无视“强力守护”造成的伤害降低效果
    # Movement speed, damage dealt, and healing magic potency are increased. Mighty Guard will not reduce damage dealt while Basic Instinct is in effect.
    # related: [斗争本能(BLU)](Action23276), 
    id = 2498
    names = ['斗争本能', 'Basic Instinct']


class Status1090(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 1090
    names = ['伤害降低(0)', 'Damage Down(0)']


class Status2404(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 2404
    names = ['伤害降低(1)', 'Damage Down(1)']


class Status2092(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 2092
    names = ['伤害降低(2)', 'Damage Down(2)']


class Status628(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 628
    names = ['伤害降低(3)', 'Damage Down(3)']


class Status215(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 215
    names = ['伤害降低(4)', 'Damage Down(4)']


class Status696(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 696
    names = ['伤害降低(5)', 'Damage Down(5)']


class Status1016(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 1016
    names = ['伤害降低(6)', 'Damage Down(6)']


class Status2522(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 2522
    names = ['伤害降低(7)', 'Damage Down(7)']


class Status62(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 62
    names = ['伤害降低(8)', 'Damage Down(8)']


class Status2911(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [斗争本能(BLU)](Action23276), 
    id = 2911
    names = ['伤害降低(9)', 'Damage Down(9)']


class Status2250(Status):
    # 头晕，受到特定攻击时会陷入脑震荡状态
    # Experiencing dizziness. Certain attacks will cause Concussion.
    # related: [芥末爆弹(BLU)](Action23279), [生成外设(BLU)](Action23286), 
    id = 2250
    names = ['头晕(0)', 'Lightheaded(0)']


class Status2501(Status):
    # 陷入头晕，受到特定的技能攻击时会发生追加效果
    # Experiencing dizziness. Certain attacks will cause additional effects.
    # related: [芥末爆弹(BLU)](Action23279), [生成外设(BLU)](Action23286), 
    id = 2501
    names = ['头晕(1)', 'Lightheaded(1)']


class Status306(Status):
    # 得到了龙眼的力量
    # Under control of the dragon's eye.
    # related: [龙之力(BLU)](Action23280), 
    id = 306
    names = ['龙之力(0)', 'Inner Dragon']


class Status2500(Status):
    # 受到的伤害降低
    # Damage taken is reduced.
    # related: [龙之力(BLU)](Action23280), 
    id = 2500
    names = ['龙之力(1)', 'Dragon Force']


class Status2502(Status):
    # 正在踢出鬼宿脚
    # Executing Phantom Flurry.
    # related: [鬼宿脚(BLU)(0)](Action23288), [鬼宿脚(BLU)(1)](Action23289), 
    id = 2502
    names = ['鬼宿脚', 'Phantom Flurry']


class Action11383(Action):
    # 将自身前方扇形范围内的敌人击退20米
    # Deals a 20-yalm knockback to all enemies in a cone before you.
    id = 11383
    names = ['鼻息(BLU)', 'Snort(BLU)']
    _orig_names = ['鼻息', 'Snort']


class Action11384(Action):
    # 对指定地点发动无属性范围物理攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：40%加重
    # 持续时间：30秒
    # Drops a 4-tonze weight dealing physical damage at a designated location with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Heavy +40%
    # Duration: 30s
    id = 11384
    names = ['4-tonze Weight(BLU)', '4星吨(BLU)']
    _orig_names = ['4星吨', '4-tonze Weight']
    damage = 200


class Action11385(Action):
    # 对目标发动水属性魔法攻击
    # 威力：200
    # Deals water damage with a potency of 200.
    id = 11385
    names = ['水炮(BLU)', 'Water Cannon(BLU)']
    _orig_names = ['水炮', 'Water Cannon']
    damage = 200


class Action11386(Action):
    # 对目标发动无属性魔法攻击
    # 威力：50
    # 追加效果：无属性持续伤害
    # 威力：50
    # 持续时间：30秒
    # Deals unaspected damage with a potency of 50.
    # Additional Effect: Unaspected damage over time
    # Potency: 50
    # Duration: 30s
    id = 11386
    names = ['Song of Torment(BLU)', '苦闷之歌(BLU)']
    _orig_names = ['苦闷之歌', 'Song of Torment']
    damage = 50
    # remain metas: {'dmg_ot': '50'}


class Action11387(Action):
    # 对自身周围的敌人发动雷属性范围魔法攻击
    # 威力：180
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：麻痹
    # 持续时间：15秒
    # 追加效果：目标处于水毒状态时威力提高，持续时间增加
    # 目标处于水毒状态时威力：220
    # 目标处于水毒状态时持续时间：30秒
    # 
    # Deals lightning damage to all nearby enemies with a potency of 180 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Paralysis
    # Duration: 15s
    # Additional Effect: Potency increased to 220 when target is afflicted with Dropsy
    # Additional Effect: Duration of Paralysis is increased to 30 seconds when target is afflicted with Dropsy
    # related: [水毒(0)](Status289), [水毒(1)](Status485), [水毒(2)](Status2950), [水毒(3)](Status2087), [水毒(4)](Status1736), [水毒(5)](Status2921), [水毒(6)](Status272), [水毒(7)](Status531), [水毒(8)](Status283), 
    id = 11387
    names = ['高压电流(BLU)', 'High Voltage(BLU)']
    _orig_names = ['High Voltage', '高压电流']
    damage = 180
    # remain metas: {'dmg_ot': '220'}


class Action11388(Action):
    # 向自身前方扇形范围内喷吐臭气
    # 令范围内的敌人陷入中毒、伤害降低10%、加重40%、减速20%、失明、麻痹状态
    # 中毒威力：20
    # 持续时间：15秒
    # 同时中断目标的技能咏唱
    # Blow noxious breath on all enemies in a cone before you, inflicting Slow +20%, Heavy +40%, Blind, and Paralysis.
    # Additional Effect: Poison
    # Potency: 20
    # Additional Effect: Damage dealt reduced 10%
    # Duration: 15s
    # Additional Effect: Interrupts target
    # related: [失明(0)](Status1088), [中毒(0)](Status801), [中毒(1)](Status2089), [中毒(2)](Status686), [失明(1)](Status15), [中毒(3)](Status559), [中毒(4)](Status560), [中毒(5)](Status18), [中毒(6)](Status275), [失明(2)](Status1524), [中毒(7)](Status2104), [失明(3)](Status571), 
    id = 11388
    names = ['Bad Breath(BLU)', '臭气(BLU)']
    _orig_names = ['臭气', 'Bad Breath']
    damage = 20
    # remain metas: {'dmg_reduce': '10%、加重40%、减速20%、失明、麻痹状态'}


class Action11389(Action):
    # 跃向目标并对目标及其周围敌人发动范围物理攻击
    # 威力：150
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 止步状态下无法发动
    # Delivers a jumping physical attack to target and all enemies nearby it with a potency of 150 for the first enemy, and 50% less for all remaining enemies.
    # Cannot be executed while bound.
    id = 11389
    names = ['Flying Frenzy(BLU)', '狂乱(BLU)']
    _orig_names = ['Flying Frenzy', '狂乱']
    damage = 150
    # remain metas: {'aoe_reduce': '50%'}


class Action11390(Action):
    # 向自身前方发动水属性扇形范围魔法攻击
    # 威力：140
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：水属性持续伤害
    # 威力：20
    # 持续时间：12秒
    # Deals water damage to all enemies in a cone before you with a potency of 140 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Inflicts Dropsy, dealing water damage over time
    # Potency: 20
    # Duration: 12s
    id = 11390
    names = ['Aqua Breath(BLU)', '水流吐息(BLU)']
    _orig_names = ['Aqua Breath', '水流吐息']
    damage = 140
    # remain metas: {'dmg_ot': '20'}


class Action11391(Action):
    # 对自身周围的敌人发动土属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # Deals earth damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 11391
    names = ['平原震裂(BLU)', 'Plaincracker(BLU)']
    _orig_names = ['平原震裂', 'Plaincracker']
    damage = 220


class Action11392(Action):
    # 令目标及其周围的敌人陷入睡眠状态
    # 持续时间：30秒
    # 发动之后会停止自动攻击
    # Puts target and all enemies nearby it to sleep.
    # Duration: 30s
    # Cancels auto-attack upon execution.
    id = 11392
    names = ['Acorn Bomb(BLU)', '橡果炸弹(BLU)']
    _orig_names = ['Acorn Bomb', '橡果炸弹']


class Action11393(Action):
    # 效果时间内，自身发动的1次魔法威力提升50%
    # 持续时间：30秒
    # 无法与攻击准备效果共存
    # Increases the potency of the next spell cast by 50%.
    # Duration: 30s
    # Effect cannot be stacked with Harmonized.
    # related: [怒发冲冠](Status402), [攻击准备](Status2118), 
    id = 11393
    names = ['Bristle(BLU)', '怒发冲冠(BLU)']
    _orig_names = ['怒发冲冠', 'Bristle']


class Action11394(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：麻痹
    # 持续时间：30秒
    # Deals unaspected damage to all nearby enemies with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Paralysis
    # Duration: 30s
    id = 11394
    names = ['精神冲击(BLU)', 'Mind Blast(BLU)']
    _orig_names = ['精神冲击', 'Mind Blast']
    damage = 200


class Action11395(Action):
    # 对目标发动无属性魔法攻击
    # 威力：50
    # 追加效果：恢复自身魔力
    # Deals unaspected damage with a potency of 50.
    # Additional Effect: Restores MP
    id = 11395
    names = ['吸血(BLU)', 'Blood Drain(BLU)']
    _orig_names = ['吸血', 'Blood Drain']
    damage = 50


class Action11396(Action):
    # 对指定地点发动火属性范围魔法攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：眩晕
    # 持续时间：3秒
    # Deals fire damage at a designated location with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Stun
    # Duration: 3s
    id = 11396
    names = ['投弹(BLU)', 'Bomb Toss(BLU)']
    _orig_names = ['Bomb Toss', '投弹']
    damage = 200


class Action11397(Action):
    # 对自身周围的敌人发动无属性范围物理攻击
    # 固定伤害：1000
    # 伤害由范围内的敌人分摊
    # Deals a fixed 1,000 points of physical damage which is shared by all enemies around you.
    id = 11397
    names = ['千针刺(BLU)', '1000 Needles(BLU)']
    _orig_names = ['1000 Needles', '千针刺']


class Action11398(Action):
    # 向目标所在方向发出无属性直线范围物理攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 目标处于石化状态时威力提高
    # 目标处于石化状态时威力：600
    # 追加效果：解除敌对目标身上的石化状态
    # Deals physical damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Potency is increased to 600 when target is afflicted with Petrification. The Petrification effect is also removed.
    id = 11398
    names = ['Drill Cannons(BLU)', '钻头炮(BLU)']
    _orig_names = ['Drill Cannons', '钻头炮']
    damage = 600 # TODO: [600, 200]


class Action11399(Action):
    # 向自身前方发动无属性扇形范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：提升仇恨
    # Deals unaspected damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Increased enmity
    id = 11399
    names = ['the Look(BLU)', '诡异视线(BLU)']
    _orig_names = ['the Look', '诡异视线']
    damage = 220


class Action11400(Action):
    # 对目标发动无属性物理攻击
    # 威力：220
    # 目标处于眩晕状态时威力提高
    # 目标处于眩晕状态时威力：450
    # Deals physical damage with a potency of 220.
    # Additional Effect: Potency is increased to 450 when target is stunned
    # related: [打磨好的菜刀](Status211), 
    id = 11400
    names = ['锋利菜刀(BLU)', 'Sharpened Knife(BLU)']
    _orig_names = ['Sharpened Knife', '锋利菜刀']
    damage = 450 # TODO: [450, 220]


class Action11401(Action):
    # 迅速移动到指定地点
    # 止步状态下无法发动
    # Move quickly to the specified location.
    # Cannot be executed while bound.
    id = 11401
    names = ['Loom(BLU)', '若隐若现(BLU)']
    _orig_names = ['Loom', '若隐若现']


class Action11402(Action):
    # 向自身前方发动火属性扇形范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # Deals fire damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 11402
    names = ['火炎放射(BLU)', 'Flame Thrower(BLU)']
    _orig_names = ['Flame Thrower', '火炎放射']
    damage = 220


class Action11403(Action):
    # 令自身前方扇形范围内的敌人陷入眩晕状态
    # 持续时间：6秒
    # Stuns all enemies in a cone before you.
    # Duration: 6s
    id = 11403
    names = ['Faze(BLU)', '拍掌(BLU)']
    _orig_names = ['拍掌', 'Faze']


class Action11404(Action):
    # 向目标所在方向发出雷属性直线范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：麻痹
    # 持续时间：6秒
    # Deals lightning damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Paralysis
    # Duration: 6s
    id = 11404
    names = ['怒视(BLU)', 'Glower(BLU)']
    _orig_names = ['怒视', 'Glower']
    damage = 220


class Action11405(Action):
    # 给予目标等同其当前体力50%的伤害
    # 命中率较低
    # 目标等级高于自身等级时无效
    # Deals damage equal to 50% of target's current HP.
    # Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
    id = 11405
    names = ['Missile(BLU)', '导弹(BLU)']
    _orig_names = ['导弹', 'Missile']


class Action11406(Action):
    # 恢复自身及周围队员的体力，恢复量等同于自身当前的体力量
    # Restores own HP and the HP of all nearby party members by an amount equal to your current HP.
    id = 11406
    names = ['白风(BLU)', 'White Wind(BLU)']
    _orig_names = ['白风', 'White Wind']


class Action11407(Action):
    # 对目标发动无属性物理攻击
    # 威力：2000
    # 发动后自身陷入无法战斗状态
    # 追加效果：意志薄弱
    # 即使进入无法战斗状态也不会解除意志薄弱
    # 持续时间：600秒
    # 发动条件：非意志薄弱状态中
    # Deals physical damage with a potency of 2,000 while incapacitating self.
    # Additional Effect: Inflicts Brush with Death on self
    # Duration: 600s
    # Effect will not be removed upon revival or further incapacitation.
    # Cannot be executed while under the effect of Brush with Death.
    # related: [意志薄弱](Status2127), 
    id = 11407
    names = ['Final Sting(BLU)', '终极针(BLU)']
    _orig_names = ['Final Sting', '终极针']
    damage = 2000


class Action11408(Action):
    # 对自身周围的敌人发动火属性范围魔法攻击
    # 威力：1500
    # 自身处于油性分泌物状态时威力提高至1800
    # 发动后自身陷入无法战斗状态
    # 追加效果：意志薄弱
    # 即使进入无法战斗状态也不会解除意志薄弱
    # 持续时间：600秒
    # 发动条件：非意志薄弱状态中
    # Deals fire damage with a potency of 1,500 to all nearby enemies while incapacitating self.
    # Additional Effect: Potency is increased to 1,800 when you are under the effect of Toad Oil
    # Additional Effect: Inflicts Brush with Death on self
    # Duration: 600s
    # Effect will not be removed upon revival or further incapacitation.
    # Cannot be executed while under the effect of Brush with Death.
    # related: [油性分泌物](Status1737), [意志薄弱](Status2127), 
    id = 11408
    names = ['自爆(BLU)', 'Self-destruct(BLU)']
    _orig_names = ['Self-destruct', '自爆']
    damage = 1500


class Action11409(Action):
    # 令一名队员的体力与魔力完全恢复
    # 发动后自身陷入无法战斗状态
    # 追加效果：意志薄弱
    # 即使进入无法战斗状态也不会解除意志薄弱
    # 持续时间：600秒
    # 发动条件：非意志薄弱状态中
    # Restores all HP and MP of a single party member while incapacitating self.
    # Additional Effect: Inflicts Brush with Death on self
    # Duration: 600s
    # Effect will not be removed upon revival or further incapacitation.
    # Cannot be executed while under the effect of Brush with Death.
    # related: [意志薄弱](Status2127), 
    id = 11409
    names = ['Transfusion(BLU)', '融合(BLU)']
    _orig_names = ['Transfusion', '融合']


class Action11410(Action):
    # 一定时间内，自身的回避率提高20%
    # 持续时间：180秒
    # Increases evasion by 20%.
    # Duration: 180s
    # related: [油性分泌物](Status1737), 
    id = 11410
    names = ['油性分泌物(BLU)', 'Toad Oil(BLU)']
    _orig_names = ['Toad Oil', '油性分泌物']


class Action11411(Action):
    # 一定时间内，目标所受伤害提高5%
    # 持续时间：15秒
    # 该魔法有单独计算的复唱时间，不受其他魔法复唱时间的影响
    # 与惊奇光共享复唱时间
    # Increases target's damage taken by 5%.
    # Duration: 15s
    # Recast timer cannot be affected by other spells. However, this action shares a recast timer with Peculiar Light.
    # related: [破防](Status1717), 
    id = 11411
    names = ['Off-guard(BLU)', '破防(BLU)']
    _orig_names = ['破防', 'Off-guard']
    # remain metas: {'taken_dmg_increase': '5%'}


class Action11412(Action):
    # 将目标拉向自身，同时令目标陷入眩晕状态
    # 持续时间：4秒
    # 追加效果：提升仇恨
    # Draws target towards caster.
    # Additional Effect: Stun
    # Duration: 4s
    # Additional Effect: Increased enmity
    id = 11412
    names = ['Sticky Tongue(BLU)', '滑舌(BLU)']
    _orig_names = ['滑舌', 'Sticky Tongue']


class Action11413(Action):
    # 令目标的体力降至个位数
    # 命中率较低
    # 目标等级高于自身等级时无效
    # Reduces target's HP to a single digit.
    # Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
    id = 11413
    names = ['螺旋尾(BLU)', 'Tail Screw(BLU)']
    _orig_names = ['螺旋尾', 'Tail Screw']


class Action11414(Action):
    # 令自身前方扇形范围内等级为5的倍数的敌人陷入石化状态
    # 持续时间：20秒
    # 命中率较低
    # 目标等级高于自身等级时无效
    # Petrifies all enemies in a cone before you.
    # Duration: 20s
    # Chance of successful attack is low.
    # Enemy level must be a multiple of 5. Has no effect on enemies whose level is higher than your own.
    id = 11414
    names = ['5级石化(BLU)', 'Level 5 Petrify(BLU)']
    _orig_names = ['Level 5 Petrify', '5级石化']


class Action11415(Action):
    # 令自身发动攻击造成的伤害提高50%，同时移动速度提高30%
    # 持续时间：15秒
    # 效果结束后对自身附加狂战士化的副作用状态
    # 持续时间：15秒
    # 狂战士化的副作用效果：无法发动自动攻击、魔法、战技、能力
    # Grants the effect of Waxing Nocturne, increasing damage dealt by 50% and movement speed by 30%.
    # Duration: 15s
    # When effect ends, the player is afflicted with Waning Nocturne, preventing the use of auto-attack, weaponskills, spells, or abilities.
    # Duration: 15s
    # related: [狂战士化的副作用](Status1727), 
    id = 11415
    names = ['Moon Flute(BLU)', '月之笛(BLU)']
    _orig_names = ['月之笛', 'Moon Flute']
    # remain metas: {'dmg_increase': '50%，同时移动速度提高30%'}


class Action11416(Action):
    # 令目标陷入死亡宣告状态
    # 持续时间：15秒
    # 持续时间结束后，目标陷入无法战斗状态
    # 命中率较低
    # 目标等级高于自身等级时无效
    # Inflicts Doom on target.
    # Duration: 15s
    # When effect expires, the target will be KO'd.
    # Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
    # related: [死亡宣告(0)](Status1769), [死亡宣告(1)](Status1738), [死亡宣告(2)](Status910), [死亡宣告(3)](Status1970), [死亡宣告(4)](Status210), [死亡宣告(5)](Status2516), [死亡宣告(6)](Status2519), 
    id = 11416
    names = ['Doom(BLU)', '死亡宣告(BLU)']
    _orig_names = ['死亡宣告', 'Doom']


class Action11417(Action):
    # 令自身所受到的伤害减轻40%，同时以令攻击造成的伤害降低40%为代价提升自身仇恨
    # 持续时间内咏唱不会因受到伤害而中断
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Reduces damage taken by 40% while reducing damage dealt by 40%, increasing enmity generation, and preventing casting interruptions via damage taken.
    # Effect ends upon reuse.
    id = 11417
    names = ['Mighty Guard(BLU)', '强力守护(BLU)']
    _orig_names = ['Mighty Guard', '强力守护']
    # remain metas: {'taken_dmg_reduce': ['40%为代价提升自身仇恨', '40%，同时以令攻击造成的伤害降低40%为代价提升自身仇恨']}


class Action11418(Action):
    # 一定时间内，自身受到物理攻击时会对对方造成冰属性魔法伤害
    # 威力：40
    # 持续时间：15秒
    # 追加效果（发动几率50%）：减速20%
    # 持续时间：15秒
    # Counters enemies with ice damage every time you suffer physical damage.
    # Counter Potency: 40
    # Duration: 15s
    # Additional Effect: 50% chance that when you are struck, the striker will be afflicted with Slow +20%
    # Duration: 15s
    # related: [冰棘屏障(0)](Status2528), [冰棘屏障(1)](Status198), [冰棘屏障(2)](Status1720), [冰棘屏障(3)](Status1307), 
    id = 11418
    names = ['冰棘屏障(BLU)', 'Ice Spikes(BLU)']
    _orig_names = ['冰棘屏障', 'Ice Spikes']
    damage = 40


class Action11419(Action):
    # 对自身周围的敌人发动冰属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：冻结
    # 持续时间：12秒
    # Deals ice damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Deep Freeze
    # Duration: 12s
    # related: [冻结(0)](Status2658), [冻结(1)](Status1731), [冻结(2)](Status1254), [冻结(3)](Status487), [冻结(4)](Status2252), [冻结(5)](Status1758), [冻结(6)](Status1150), 
    id = 11419
    names = ['寒冰咆哮(BLU)', "the Ram's Voice(BLU)"]
    _orig_names = ['寒冰咆哮', "the Ram's Voice"]
    damage = 220


class Action11420(Action):
    # 对自身周围的敌人发动雷属性范围魔法攻击
    # 威力：200
    # 无法攻击到自身周围8米以内的敌人
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：麻痹
    # 持续时间：9秒
    # 目标处于冻结状态时威力提高，对特定敌人无效
    # 冻结状态时威力：400
    # 追加效果：解除目标身上的冻结状态，对特定敌人无效
    # Deals lightning damage to all nearby enemies with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Enemies within an 8-yalm radius will be unaffected.
    # Additional Effect: Paralysis
    # Duration: 9s
    # Additional Effect: Potency is increased to 400 against most enemies afflicted with Deep Freeze. The Deep Freeze effect is also removed.
    # related: [冻结(0)](Status2658), [冻结(1)](Status1731), [冻结(2)](Status1254), [冻结(3)](Status487), [冻结(4)](Status2252), [冻结(6)](Status1150), [冻结(5)](Status1758), 
    id = 11420
    names = ["the Dragon's Voice(BLU)", '雷电咆哮(BLU)']
    _orig_names = ["the Dragon's Voice", '雷电咆哮']
    damage = 200
    # remain metas: {'dmg_ot': '400'}


class Action11421(Action):
    # 令自身周围的敌人所受到的魔法伤害提高5%
    # 持续时间：15秒
    # 该魔法有单独计算的复唱时间，不受其他魔法复唱时间的影响
    # 与破防共享复唱时间
    # Increases magic damage taken by all nearby enemies by 5%.
    # Duration: 15s
    # Recast timer cannot be affected by other spells. However, this action shares a recast timer with Off-guard.
    # related: [惊奇光](Status1721), 
    id = 11421
    names = ['Peculiar Light(BLU)', '惊奇光(BLU)']
    _orig_names = ['Peculiar Light', '惊奇光']
    # remain metas: {'taken_dmg_increase': '5%'}


class Action11422(Action):
    # 向自身前方发动无属性扇形范围魔法攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：失明
    # 持续时间：30秒
    # Deals unaspected damage to all enemies in a cone before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Blind
    # Duration: 30s
    # related: [失明(0)](Status1088), [失明(3)](Status571), [失明(2)](Status1524), [失明(1)](Status15), 
    id = 11422
    names = ['Ink Jet(BLU)', '喷墨(BLU)']
    _orig_names = ['喷墨', 'Ink Jet']
    damage = 200


class Action11423(Action):
    # 对目标发动无属性物理攻击
    # 威力：10
    # 追加效果：中断目标的技能咏唱
    # Deals physical damage with a potency of 10.
    # Additional Effect: Interrupts target
    id = 11423
    names = ['投掷沙丁鱼(BLU)', 'Flying Sardine(BLU)']
    _orig_names = ['Flying Sardine', '投掷沙丁鱼']
    damage = 10


class Action11424(Action):
    # 一定时间内，将自身所受的伤害减轻90%，同时除特定攻击之外其他所有击退与吸引效果失效
    # 但是持续时间内无法移动或使用技能
    # 持续时间：10秒
    # 追加效果：解除自身的狂战士化状态
    # 此技能发动后无法主动中断
    # Reduces damage taken by 90% and nullifies most knockback and draw-in effects.
    # Unable to move or take action for the duration of this effect.
    # Duration: 10s
    # If used when Waxing Nocturne is active, its effect will transition immediately to Waning Nocturne.
    # The effect of this action cannot be ended manually.
    # related: [吸引(0)](Status2529), [超硬化](Status1722), [狂战士化](Status1718), [吸引(1)](Status2486), 
    id = 11424
    names = ['Diamondback(BLU)', '超硬化(BLU)']
    _orig_names = ['超硬化', 'Diamondback']
    # remain metas: {'taken_dmg_reduce': '90%，同时除特定攻击之外其他所有击退与吸引效果失效'}


class Action11425(Action):
    # 对目标及其周围的敌人发动火属性范围物理攻击
    # 威力：200
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals physical fire damage to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    id = 11425
    names = ['Fire Angon(BLU)', '火投枪(BLU)']
    _orig_names = ['火投枪', 'Fire Angon']
    damage = 200
    # remain metas: {'aoe_reduce': '50%'}


class Action11426(Action):
    # 对指定地点发动风属性范围魔法攻击
    # 威力：220
    # 追加效果：风属性持续伤害
    # 威力：40
    # 持续时间：6秒
    # 与部分青魔法共享复唱时间
    # Deals wind damage with a potency of 220 to all enemies at a designated location.
    # Additional Effect: Wind damage over time
    # Potency: 40
    # Duration: 6s
    # Shares a recast timer with certain blue magic spells.
    id = 11426
    names = ['飞翎雨(BLU)', 'Feather Rain(BLU)']
    _orig_names = ['飞翎雨', 'Feather Rain']
    damage = 220
    # remain metas: {'dmg_ot': '40'}


class Action11427(Action):
    # 对指定地点发动火属性范围魔法攻击
    # 威力：300
    # 与部分青魔法共享复唱时间
    # Deals fire damage with a potency of 300 to all enemies at a designated location.
    # Shares a recast timer with certain blue magic spells.
    id = 11427
    names = ['地火喷发(BLU)', 'Eruption(BLU)']
    _orig_names = ['地火喷发', 'Eruption']
    damage = 300


class Action11428(Action):
    # 向自身前方发动土属性扇形范围物理攻击
    # 威力：400
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 与部分青魔法共享复唱时间
    # Deals physical earth damage to all enemies in a cone before you with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
    # Shares a recast timer with certain blue magic spells.
    id = 11428
    names = ['Mountain Buster(BLU)', '山崩(BLU)']
    _orig_names = ['山崩', 'Mountain Buster']
    damage = 400


class Action11429(Action):
    # 对目标及其周围的敌人发动雷属性范围魔法攻击
    # 威力：400
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 与部分青魔法共享复唱时间
    # Deals lightning damage to target and all enemies nearby it with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
    # Shares a recast timer with certain blue magic spells.
    id = 11429
    names = ['轰雷(BLU)', 'Shock Strike(BLU)']
    _orig_names = ['轰雷', 'Shock Strike']
    damage = 400
    # remain metas: {'aoe_reduce': '50%'}


class Action11430(Action):
    # 向自身前方与两侧发动冰属性扇形范围魔法攻击
    # 威力：350
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 与部分青魔法共享复唱时间
    # Deals ice damage to all enemies in a wide arc to your fore and flanks with a potency of 350 for the first enemy, and 50% less for all remaining enemies.
    # Shares a recast timer with certain blue magic spells.
    id = 11430
    names = ['冰雪乱舞(BLU)', 'Glass Dance(BLU)']
    _orig_names = ['冰雪乱舞', 'Glass Dance']
    damage = 350


class Action11431(Action):
    # 一定时间内，自身受到攻击时会对对方造成水属性魔法伤害
    # 威力：50
    # 持续时间：30秒
    # 与部分青魔法共享复唱时间
    # Counters enemies with water damage every time you suffer damage.
    # Counter Potency: 50
    # Duration: 30s
    # Shares a recast timer with certain blue magic spells.
    # related: [水神的面纱(0)](Status1724), [水神的面纱(1)](Status478), 
    id = 11431
    names = ['Veil of the Whorl(BLU)', '水神的面纱(BLU)']
    _orig_names = ['水神的面纱', 'Veil of the Whorl']
    damage = 50


class Action18295(Action):
    # 向目标所在方向发出风属性直线范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # Deals wind damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 18295
    names = ['高山气流(BLU)', 'Alpine Draft(BLU)']
    _orig_names = ['高山气流', 'Alpine Draft']
    damage = 220


class Action18296(Action):
    # 向自身前方发动水属性扇形范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：将范围内的敌人击退15米
    # Deals water damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: 15-yalm knockback
    id = 18296
    names = ['Protean Wave(BLU)', '万变水波(BLU)']
    _orig_names = ['Protean Wave', '万变水波']
    damage = 220


class Action18297(Action):
    # 向自身前方发动冰属性扇形范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：敌人处于水毒状态时解除该状态，同时附加冻结状态
    # 持续时间：20秒
    # Deals ice damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Enemies affected by Dropsy are frozen. The Dropsy effect is also removed.
    # Duration: 20s
    # related: [水毒(0)](Status289), [冻结(0)](Status2658), [冻结(1)](Status1731), [水毒(1)](Status485), [水毒(2)](Status2950), [水毒(3)](Status2087), [水毒(4)](Status1736), [水毒(5)](Status2921), [冻结(2)](Status1254), [冻结(3)](Status487), [冻结(4)](Status2252), [冻结(5)](Status1758), [水毒(6)](Status272), [水毒(7)](Status531), [水毒(8)](Status283), [冻结(6)](Status1150), 
    id = 18297
    names = ['狂风暴雪(BLU)', 'Northerlies(BLU)']
    _orig_names = ['Northerlies', '狂风暴雪']
    damage = 220


class Action18298(Action):
    # 对目标及其周围的敌人发动雷属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals lightning damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 18298
    names = ['生物电(BLU)', 'Electrogenesis(BLU)']
    _orig_names = ['Electrogenesis', '生物电']
    damage = 220
    # remain metas: {'aoe_reduce': '50%'}


class Action18299(Action):
    # 向自身前方发出无属性扇形范围物理攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # Deals physical damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 18299
    names = ['Kaltstrahl(BLU)', '寒光(BLU)']
    _orig_names = ['Kaltstrahl', '寒光']
    damage = 220


class Action18300(Action):
    # 对目标发动无属性物理攻击
    # 威力：220
    # 追加效果：麻痹
    # 持续时间：30秒
    # Deals physical damage with a potency of 220.
    # Additional Effect: Paralysis
    # Duration: 30s
    id = 18300
    names = ['Abyssal Transfixion(BLU)', '深渊贯穿(BLU)']
    _orig_names = ['深渊贯穿', 'Abyssal Transfixion']
    damage = 220


class Action18301(Action):
    # 令自身周围的敌人陷入睡眠状态
    # 持续时间：40秒
    # 发动之后会停止自动攻击
    # Puts all nearby enemies to sleep.
    # Duration: 40s
    # Cancels auto-attack upon execution.
    id = 18301
    names = ['Chirp(BLU)', '唧唧咋咋(BLU)']
    _orig_names = ['唧唧咋咋', 'Chirp']


class Action18302(Action):
    # 解除自身周围敌人身上强化效果中的一种
    # Removes one beneficial effect from all nearby enemies.
    id = 18302
    names = ['Eerie Soundwave(BLU)', '怪音波(BLU)']
    _orig_names = ['Eerie Soundwave', '怪音波']


class Action18303(Action):
    # 恢复目标的体力
    # 恢复力：100
    # 自身处于以太复制：治疗状态时
    # 恢复力：500
    # Restores target's HP.
    # Cure Potency: 100
    # Cure potency is increased to 500 when you are under the effect of Aetherial Mimicry: Healer.
    # related: [以太复制：治疗](Status2126), 
    id = 18303
    names = ['Pom Cure(BLU)', '绒绒治疗(BLU)']
    _orig_names = ['Pom Cure', '绒绒治疗']
    heal = 100 # TODO: [100, 500]


class Action18304(Action):
    # 为自身和周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力100的伤害量
    # 持续时间：30秒
    # 自身处于以太复制：治疗状态时
    # 该防护罩能够抵消相当于恢复力250的伤害量
    # 无法与学者的鼓舞和贤者的均衡诊断及均衡预后效果共存
    # Creates a barrier around self and all nearby party members that absorbs damage equivalent to a heal of 100 potency.
    # Duration: 30s
    # Barrier strength is increased to absorb damage equivalent to a heal of 250 potency when you are under the effect of Aetherial Mimicry: Healer.
    # Effect cannot be stacked with those of scholar's Galvanize or sage's Eukrasian Diagnosis and Eukrasian Prognosis.
    # related: [均衡预后(0)](Status2609), [哥布防御](Status2114), [鼓舞(1)](Status1331), [均衡预后(1)](Status2866), [鼓舞(0)](Status297), [以太复制：治疗](Status2126), 
    id = 18304
    names = ['Gobskin(BLU)', '哥布防御(BLU)']
    _orig_names = ['哥布防御', 'Gobskin']
    # remain metas: {'shield': ['恢复力250', '恢复力100']}


class Action18305(Action):
    # 对目标及其周围的敌人发动无属性魔法攻击
    # 威力：250
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：令目标的智力与精神降低10%
    # 持续时间：10秒
    # 追加效果：恢复自身最大魔力的10%
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to target and all enemies nearby it with a potency of 250 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Lowers intelligence and mind attributes by 10%
    # Duration: 10s
    # Additional Effect: Restores 10% of maximum MP
    # This action does not share a recast timer with any other actions.
    id = 18305
    names = ['魔法锤(BLU)', 'Magic Hammer(BLU)']
    _orig_names = ['魔法锤', 'Magic Hammer']
    damage = 250
    # remain metas: {'aoe_reduce': '50%'}


class Action18306(Action):
    # 让目标队员替自己承受来自敌人的攻击
    # 但对部分攻击无效
    # 持续时间：12秒
    # 与目标的距离不能超过10米
    # 该魔法有单独计算的复唱时间
    # Direct damage intended for you to another party member.
    # Duration: 12s
    # Can only be executed when member is within 10 yalms. Does not activate with certain attacks.
    # This action does not share a recast timer with any other actions.
    # related: [防御指示(0)](Status2116), [防御指示(1)](Status2117), 
    id = 18306
    names = ['防御指示(BLU)', 'Avail(BLU)']
    _orig_names = ['防御指示', 'Avail']


class Action18307(Action):
    # 向周围的敌人进行挑衅，令自身的仇恨变为最高
    # Provoke nearby enemies, placing yourself at the top of their enmity list.
    id = 18307
    names = ['蛙腿(BLU)', 'Frog Legs(BLU)']
    _orig_names = ['Frog Legs', '蛙腿']


class Action18308(Action):
    # 对目标发动风属性魔法攻击
    # 威力：210
    # Deals wind damage with a potency of 210.
    id = 18308
    names = ['Sonic Boom(BLU)', '音爆(BLU)']
    _orig_names = ['Sonic Boom', '音爆']
    damage = 210


class Action18309(Action):
    # 效果时间内自身发动的1次魔法为物理攻击时，威力提升80%
    # 持续时间：30秒
    # 无法与蓄力效果共存
    # Increases the potency of the next physical damage spell cast by 80%.
    # Duration: 30s
    # Effect cannot be stacked with Boost.
    # related: [工作小调](Status880), [蓄力(0)](Status2448), [蓄力(1)](Status1716), [蓄力(2)](Status1656), [蓄力(3)](Status203), 
    id = 18309
    names = ['口笛(BLU)', 'Whistle(BLU)']
    _orig_names = ['Whistle', '口笛']


class Action18310(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：200
    # 敌人处于止步状态时解除该状态，同时提升威力
    # 敌人处于止步状态时威力：400
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：减速20%
    # 持续时间：20秒
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Potency is increased to 400 when enemies are bound. The Bind effect is also removed.
    # Additional Effect: Slow +20%
    # Duration: 20s
    id = 18310
    names = ["White Knight's Tour(BLU)", '白骑士之旅(BLU)']
    _orig_names = ["White Knight's Tour", '白骑士之旅']
    damage = 200 # TODO: [200, 400]


class Action18311(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：200
    # 敌人处于减速状态时解除该状态，同时提升威力
    # 敌人处于减速状态时威力：400
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：止步
    # 持续时间：20秒
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Potency is increased to 400 when enemies are under the effect of Slow. The Slow effect is also removed.
    # Additional Effect: Bind
    # Duration: 20s
    # related: [减速(0)](Status193), [减速(1)](Status1346), [减速(2)](Status561), [减速(3)](Status1509), [减速(4)](Status2246), [减速(5)](Status9), [减速(6)](Status442), 
    id = 18311
    names = ['黑骑士之旅(BLU)', "Black Knight's Tour(BLU)"]
    _orig_names = ['黑骑士之旅', "Black Knight's Tour"]
    damage = 200 # TODO: [200, 400]


class Action18312(Action):
    # 令自身周围等级为5的倍数的敌人陷入无法战斗状态
    # 命中率较低
    # 目标等级高于自身等级时无效
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # KOs all nearby enemies.
    # Chance of successful attack is low.
    # Enemy level must be a multiple of 5. Has no effect on enemies whose level is higher than your own.
    # Shares a recast timer with certain blue magic spells.
    id = 18312
    names = ['Level 5 Death(BLU)', '5级即死(BLU)']
    _orig_names = ['5级即死', 'Level 5 Death']


class Action18313(Action):
    # 给予自身周围敌人等同其当前体力50%或30%或20%或10%的伤害
    # 目标等级高于自身等级时无效
    # Delivers an attack to all nearby enemies randomly dealing 50%, 30%, 20%, or 10% of their HP.
    # Has no effect on enemies whose level is higher than your own.
    id = 18313
    names = ['Launcher(BLU)', '火箭炮(BLU)']
    _orig_names = ['Launcher', '火箭炮']


class Action18314(Action):
    # 对目标发动无属性魔法攻击
    # 威力：220
    # 追加效果：眩晕
    # 持续时间：1秒
    # 该技能的眩晕效果不受其他眩晕影响
    # Deals unaspected damage with a potency of 220.
    # Additional Effect: Stun
    # Duration: 1s
    # Ignores target's Stun resistance.
    id = 18314
    names = ['Perpetual Ray(BLU)', '永恒射线(BLU)']
    _orig_names = ['Perpetual Ray', '永恒射线']
    damage = 220


class Action18315(Action):
    # 指定一名队员，令其受到的伤害减轻5%
    # 持续时间：6秒
    # 自身处于以太复制：防护状态时
    # 队员受到的伤害减轻15%
    # Reduces target party member's damage taken by 5%.
    # Duration: 6s
    # Increases damage reduction to 15% when you are under the effect of Aetherial Mimicry: Tank.
    # related: [以太复制：防护](Status2124), [仙人盾](Status2119), 
    id = 18315
    names = ['Cactguard(BLU)', '仙人盾(BLU)']
    _orig_names = ['Cactguard', '仙人盾']
    # remain metas: {'taken_dmg_reduce': ['5%', '15%']}


class Action18316(Action):
    # 对目标发动无属性物理攻击
    # 威力：50
    # 自身剩余体力在20%以下时威力提升
    # 体力在20%以下时：500
    # Deals physical damage with a potency of 50.
    # Potency is increased to 500 when your HP is below 20%.
    id = 18316
    names = ['复仇冲击(BLU)', 'Revenge Blast(BLU)']
    _orig_names = ['Revenge Blast', '复仇冲击']
    damage = 50


class Action18317(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # 该魔法有单独计算的复唱时间
    # Resurrects target to a weakened state.
    # This action does not share a recast timer with any other actions.
    # related: [衰弱](Status43), 
    id = 18317
    names = ['天使低语(BLU)', 'Angel Whisper(BLU)']
    _orig_names = ['Angel Whisper', '天使低语']


class Action18318(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：50
    # 追加效果：解除部分弱化效果中的一种
    # 自身处于以太复制：治疗状态时
    # 恢复力：300
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 50
    # Additional Effect: Removes one detrimental effect from all nearby party members
    # Cure potency is increased to 300 when you are under the effect of Aetherial Mimicry: Healer.
    # related: [以太复制：治疗](Status2126), 
    id = 18318
    names = ['Exuviation(BLU)', '蜕皮(BLU)']
    _orig_names = ['蜕皮', 'Exuviation']
    heal = 50 # TODO: [50, 300]


class Action18319(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：220
    # 追加效果：40%加重
    # 持续时间：10秒
    # 该技能的加重效果不受其他加重影响
    # Deals lightning damage with a potency of 220.
    # Additional Effect: Heavy +40%
    # Duration: 10s
    # Ignores target's Heavy resistance.
    id = 18319
    names = ['Reflux(BLU)', '逆流(BLU)']
    _orig_names = ['逆流', 'Reflux']
    damage = 220


class Action18320(Action):
    # 对目标发动无属性魔法攻击
    # 威力：250
    # 追加效果：一定时间内，自身的最大体力提高20%
    # 持续时间：15秒
    # 以太复制：防护状态下的持续时间变为70秒
    # 追加效果：恢复伤害量100%的体力
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage with a potency of 250.
    # Additional Effect: Increases maximum HP by 20%
    # Duration: 15s
    # Increases duration to 70s when you are under the effect of Aetherial Mimicry: Tank.
    # Additional Effect: Restores an amount of own HP equal to damage dealt
    # This action does not share a recast timer with any other actions.
    # related: [以太复制：防护](Status2124), [捕食](Status421), 
    id = 18320
    names = ['Devour(BLU)', '捕食(BLU)']
    _orig_names = ['捕食', 'Devour']
    damage = 250


class Action18321(Action):
    # 对目标随机附加星极性耐性降低、灵极性耐性降低、物理受伤加重状态
    # 持续时间：30秒
    # 星极性耐性降低效果：所受火、风、雷属性伤害提高5%
    # 灵极性耐性降低效果：所受水、土、冰属性伤害提高5%
    # 物理受伤加重效果：所受物理伤害提高5%
    # 以上状态无法叠加
    # Afflicts target with Physical Attenuation, Astral Attenuation, or Umbral Attenuation.
    # Duration: 30s
    # Physical Attenuation Effect: Increases damage taken from physical attacks by 5%
    # Astral Attenuation Effect: Increases damage taken from fire-, wind-, and lightning-aspected attacks by 5%
    # Umbral Attenuation Effect: Increases damage taken from water-, earth-, and ice-aspected attacks by 5%
    # Only one of these statuses can be applied to a target at a time.
    # related: [物理受伤加重(0)](Status934), [物理受伤加重(1)](Status200), [星极性耐性降低](Status2121), [物理受伤加重(2)](Status2090), [物理受伤加重(3)](Status2123), [灵极性耐性降低](Status2122), [物理受伤加重(4)](Status493), [物理受伤加重(5)](Status657), [物理受伤加重(6)](Status695), [物理受伤加重(7)](Status56), [物理受伤加重(8)](Status2940), [物理受伤加重(9)](Status126), 
    id = 18321
    names = ['Condensed Libra(BLU)', '小侦测(BLU)']
    _orig_names = ['小侦测', 'Condensed Libra']
    # remain metas: {'taken_dmg_increase': '5%'}


class Action18322(Action):
    # 指定一名除自身外的玩家，复制其以太特性
    # 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种
    # 指定玩家的职能将决定附加的状态
    # 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法
    # 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20%，同时强化部分青魔法
    # 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
    # If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
    # If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
    # If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
    # Cannot be cast on self. Effect ends upon reuse.
    # related: [以太复制：防护](Status2124), [以太复制：进攻](Status2125), [以太复制：治疗](Status2126), 
    id = 18322
    names = ['Aetherial Mimicry(BLU)(0)', '以太复制(BLU)(0)']
    _orig_names = ['以太复制', 'Aetherial Mimicry']


class Action18323(Action):
    # 向自身前方发出土属性扇形范围魔法攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 积蓄次数：4
    # 追加效果：穿甲散弹的威力提高50%
    # 最大档数：3档
    # 持续时间：3秒
    # 若在持续时间中发动穿甲散弹之外的技能，会立即解除该状态
    # Deals earth damage to all enemies in a cone before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Grants Surpanakha's Fury, increasing potency of Surpanakha by 50%
    # Duration: 3s
    # Can be stacked up to 3 times.
    # Maximum Charges: 4
    # Effect is canceled upon execution of any action other than Surpanakha.
    id = 18323
    names = ['Surpanakha(BLU)', '穿甲散弹(BLU)']
    _orig_names = ['Surpanakha', '穿甲散弹']
    damage = 200


class Action18324(Action):
    # 对自身周围的敌人发动无属性魔法攻击
    # 威力：300
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 与部分青魔法共享复唱时间
    # Deals unaspected damage to all nearby enemies with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
    # Shares a recast timer with certain blue magic spells.
    id = 18324
    names = ['Quasar(BLU)', '类星体(BLU)']
    _orig_names = ['类星体', 'Quasar']
    damage = 300


class Action18325(Action):
    # 跳起接近目标并发动无属性范围物理攻击
    # 威力：300
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 止步状态下无法发动
    # 与部分青魔法共享复唱时间
    # Delivers a jumping physical attack to target and all enemies nearby it with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
    # Cannot be executed while bound.
    # Shares a recast timer with certain blue magic spells.
    id = 18325
    names = ['正义飞踢(BLU)', 'J Kick(BLU)']
    _orig_names = ['正义飞踢', 'J Kick']
    damage = 300
    # remain metas: {'aoe_reduce': '50%'}


class Action19238(Action):
    # 指定一名除自身外的玩家，复制其以太特性
    # 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种
    # 指定玩家的职能将决定附加的状态
    # 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法
    # 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20%，同时强化部分青魔法
    # 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
    # If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
    # If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
    # If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
    # Cannot be cast on self. Effect ends upon reuse.
    # related: [以太复制：进攻](Status2125), [以太复制：治疗](Status2126), 
    id = 19238
    names = ['Aetherial Mimicry(BLU)(1)', '以太复制(BLU)(1)']
    _orig_names = ['以太复制', 'Aetherial Mimicry']


class Action19239(Action):
    # 指定一名除自身外的玩家，复制其以太特性
    # 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种
    # 指定玩家的职能将决定附加的状态
    # 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法
    # 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20%，同时强化部分青魔法
    # 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
    # If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
    # If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
    # If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
    # Cannot be cast on self. Effect ends upon reuse.
    # related: [以太复制：防护](Status2124), [以太复制：治疗](Status2126), 
    id = 19239
    names = ['以太复制(BLU)(2)', 'Aetherial Mimicry(BLU)(2)']
    _orig_names = ['以太复制', 'Aetherial Mimicry']


class Action19240(Action):
    # 指定一名除自身外的玩家，复制其以太特性
    # 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种
    # 指定玩家的职能将决定附加的状态
    # 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法
    # 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20%，同时强化部分青魔法
    # 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
    # If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
    # If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
    # If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
    # Cannot be cast on self. Effect ends upon reuse.
    # related: [以太复制：防护](Status2124), [以太复制：进攻](Status2125), 
    id = 19240
    names = ['以太复制(BLU)(3)', 'Aetherial Mimicry(BLU)(3)']
    _orig_names = ['以太复制', 'Aetherial Mimicry']


class Action23264(Action):
    # 对目标发动连续3次物理攻击
    # 威力：150
    # 该魔法有单独计算的复唱时间
    # Delivers a threefold attack, each hit with a potency of 150.
    # This action does not share a recast timer with any other actions.
    id = 23264
    names = ['Triple Trident(BLU)', '渔叉三段(BLU)']
    _orig_names = ['Triple Trident', '渔叉三段']
    damage = 150


class Action23265(Action):
    # 对目标及其周围敌人发动雷属性范围魔法攻击
    # 威力：100
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：效果时间内自身发动的1次魔法为物理攻击时，威力提升100
    # 持续时间：15秒
    # Deals lightning damage to target and all enemies nearby it with a potency of 100 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Increases the potency of the next physical damage spell cast by 100
    # Duration: 15s
    # related: [哔哩哔哩](Status2492), 
    id = 23265
    names = ['Tingle(BLU)', '哔哩哔哩(BLU)']
    _orig_names = ['哔哩哔哩', 'Tingle']
    damage = 100
    # remain metas: {'aoe_reduce': '50%'}


class Action23266(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：220
    # 追加效果：眩晕
    # 持续时间：3秒
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Stun
    # Duration: 3s
    id = 23266
    names = ['掀地板之术(BLU)', 'Tatami-gaeshi(BLU)']
    _orig_names = ['Tatami-gaeshi', '掀地板之术']
    damage = 220
    # remain metas: {'aoe_reduce': '50%'}


class Action23267(Action):
    # 对自身附加彻骨雾寒状态
    # 持续时间：5秒
    # 持续时间内如果受到敌人的攻击，则效果会变化成冰雾
    # 冰雾效果：技能彻骨雾寒变化为冰雾
    # 持续时间：15秒
    # 该魔法有单独计算的复唱时间
    # 冰雾
    # 对目标发动冰属性魔法攻击
    # 威力：400
    # 追加效果：冻结
    # 持续时间：10秒
    # 发动条件：冰雾状态中
    # Grants Cold Fog to self.
    # Duration: 5s
    # Effect changes to Touch of Frost if damage is taken.
    # Touch of Frost Effect: Action changes from Cold Fog to White Death
    # Duration: 15s
    # White Death
    # Deals ice damage with a potency of 400.
    # Additional Effect: Deep Freeze
    # Duration: 10s
    # Can only be executed while under the effect of Touch of Frost.
    # related: [冻结(0)](Status2658), [冻结(1)](Status1731), [冻结(2)](Status1254), [冻结(3)](Status487), [冻结(4)](Status2252), [冻结(5)](Status1758), [冻结(6)](Status1150), [彻骨雾寒](Status2493), [冰雾](Status2494), 
    id = 23267
    names = ['彻骨雾寒(BLU)', 'Cold Fog(BLU)']
    _orig_names = ['彻骨雾寒', 'Cold Fog']
    # remain metas: {'dmg_ot': '400'}


class Action23268(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：400
    # 追加效果：冻结
    # 持续时间：10秒
    # 发动条件：冰雾状态中
    # Deals ice damage with a potency of 400.
    # Additional Effect: Deep Freeze
    # Duration: 10s
    # Can only be executed while under the effect of Touch of Frost.
    # related: [冻结(0)](Status2658), [冻结(1)](Status1731), [冻结(2)](Status1254), [冻结(3)](Status487), [冻结(4)](Status2252), [冻结(5)](Status1758), [冻结(6)](Status1150), [冰雾](Status2494), 
    id = 23268
    names = ['冰雾(BLU)', 'White Death(BLU)']
    _orig_names = ['White Death', '冰雾']
    damage = 400


class Action23269(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：140
    # 自身处于以太复制：治疗状态时效果变为
    # 恢复自身及周围队员的体力
    # 恢复力：300
    # Deals unaspected damage with a potency of 140 to all nearby enemies.
    # Action effect changes, restoring own HP and the HP of all nearby party members when you are under the effect of Aetherial Mimicry: Healer.
    # Cure Potency: 300
    # related: [以太复制：治疗](Status2126), 
    id = 23269
    names = ['赞歌(BLU)(0)', 'Stotram(BLU)(0)']
    _orig_names = ['赞歌', 'Stotram']
    damage = 140
    heal = 300


class Action23270(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：100
    # 目标为不死系怪物时，威力提高
    # 对不死系怪物的威力：500
    # Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
    # Potency increases to 500 when used against undead enemies.
    id = 23270
    names = ['圣光射线(BLU)', 'Saintly Beam(BLU)']
    _orig_names = ['Saintly Beam', '圣光射线']
    damage = 100 # TODO: [100, 500]


class Action23271(Action):
    # 向目标所在方向发出土属性直线范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals earth damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 23271
    names = ['Feculent Flood(BLU)', '污泥泼洒(BLU)']
    _orig_names = ['污泥泼洒', 'Feculent Flood']
    damage = 220
    # remain metas: {'aoe_reduce': '50%'}


class Action23272(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：400
    # 自身处于以太复制：治疗状态时
    # 追加效果：令目标体力持续恢复
    # 恢复力：200
    # 持续时间：15秒
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 400
    # Additional Effect: Grants healing over time effect when you are under the effect of Aetherial Mimicry: Healer
    # Cure Potency: 200
    # Duration: 15s
    # Shares a recast timer with certain blue magic spells.
    # related: [以太复制：治疗](Status2126), [天使的点心](Status2495), 
    id = 23272
    names = ["Angel's Snack(BLU)", '天使的点心(BLU)']
    _orig_names = ["Angel's Snack", '天使的点心']
    heal = 400
    # remain metas: {'heal_ot': '200'}


class Action23273(Action):
    # 展开玄结界，令自身所受的伤害减轻20%
    # 持续时间：10秒
    # 追加效果：持续时间内如果受到超过自身最大体力30%的伤害，则对自身附加玄天武水壁
    # 玄天武水壁效果：技能玄结界变化为玄天武水壁
    # 效果时间内发动技能或进行移动、转身都会使玄结界立即消失
    # 此外当玄结界消失时，玄天武水壁也会同时消失
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # 玄天武水壁
    # 对自身周围的敌人发动水属性范围魔法攻击
    # 威力：500
    # 自身处于以太复制：防护状态时
    # 威力：1000
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 效果发动条件：玄天武水壁状态中
    # Summons a chelonian gate, reducing damage taken by 20%.
    # Duration: 10s
    # Additional Effect: Grants Auspicious Trance after taking damage equal to 30% of maximum HP
    # Auspicious Trance Effect: Action changes from Chelonian Gate to Divine Cataract
    # Chelonian Gate effect ends upon using another action or moving (including facing a different direction).
    # Auspicious Trance ends upon losing the effect of Chelonian Gate.
    # Shares a recast timer with certain blue magic spells.
    # Divine Cataract
    # Deals water damage to all nearby enemies with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
    # Potency increases to 1,000 when you are under the effect of Aetherial Mimicry: Tank.
    # Can only be executed when under the effect of Auspicious Trance.
    # related: [玄结界](Status2496), [玄天武水壁](Status2497), [以太复制：防护](Status2124), 
    id = 23273
    names = ['Chelonian Gate(BLU)', '玄结界(BLU)']
    _orig_names = ['玄结界', 'Chelonian Gate']
    damage = 1000
    # remain metas: {'taken_dmg_reduce': '20%', 'dmg_ot': '500', 'aoe_reduce': '50%'}


class Action23274(Action):
    # 对自身周围的敌人发动水属性范围魔法攻击
    # 威力：500
    # 自身处于以太复制：防护状态时
    # 威力：1000
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 效果发动条件：玄天武水壁状态中
    # Deals water damage to all nearby enemies with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
    # Potency increases to 1,000 when you are under the effect of Aetherial Mimicry: Tank.
    # Can only be executed when under the effect of Auspicious Trance.
    # related: [玄天武水壁](Status2497), [以太复制：防护](Status2124), 
    id = 23274
    names = ['玄天武水壁(BLU)', 'Divine Cataract(BLU)']
    _orig_names = ['Divine Cataract', '玄天武水壁']
    damage = 500 # TODO: [500, 1000]
    # remain metas: {'aoe_reduce': '50%'}


class Action23275(Action):
    # 对目标发动无属性魔法攻击
    # 威力：400
    # 追加效果：击退10米
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # Deals unaspected damage with a potency of 400.
    # Additional Effect: 10-yalm knockback
    # Shares a recast timer with certain blue magic spells.
    id = 23275
    names = ['The Rose of Destruction(BLU)', '斗灵弹(BLU)']
    _orig_names = ['The Rose of Destruction', '斗灵弹']
    damage = 400


class Action23276(Action):
    # 此技能仅限在非单人任务中，且由自己单独进行攻略时或除自身外其他小队成员均陷入无法战斗状态时才会生效
    # 令自身的移动速度提升30%，自身攻击造成的伤害及治疗魔法的治疗量提高100%，并无视强力守护所造成的伤害降低效果
    # 持续时间：永久
    # 此效果在小队成员回归战斗状态后立即解除
    # Increases movement speed by 30%, and healing magic potency and damage dealt by 100%. Also ignores the damage penalty inflicted by Mighty Guard.
    # Can only be used in duties intended for two or more players while playing alone, while no other party members are in the instance, or when all party members are incapacitated. Effect ends when joined by one or more party members.
    # related: [斗争本能](Status2498), [伤害降低(0)](Status1090), [伤害降低(1)](Status2404), [伤害降低(2)](Status2092), [伤害降低(3)](Status628), [伤害降低(4)](Status215), [伤害降低(5)](Status696), [伤害降低(6)](Status1016), [伤害降低(7)](Status2522), [伤害降低(8)](Status62), [伤害降低(9)](Status2911), 
    id = 23276
    names = ['斗争本能(BLU)', 'Basic Instinct(BLU)']
    _orig_names = ['斗争本能', 'Basic Instinct']
    # remain metas: {'dmg_reduce': '效果'}


class Action23277(Action):
    # 在自身周围产生超音波，令冻结或石化状态中的敌人必定陷入无法战斗状态
    # 对部分敌人无效
    # 目标等级高于自身等级时无效
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # KOs all nearby enemies afflicted with Deep Freeze or Petrification. Has no effect on enemies whose level is higher than your own, and certain others.
    # Shares a recast timer with certain blue magic spells.
    id = 23277
    names = ['Ultravibration(BLU)', '超振动(BLU)']
    _orig_names = ['Ultravibration', '超振动']


class Action23278(Action):
    # 对目标及其周围的敌人发动冰属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals ice damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    id = 23278
    names = ['Blaze(BLU)', '冰焰(BLU)']
    _orig_names = ['冰焰', 'Blaze']
    damage = 220
    # remain metas: {'aoe_reduce': '50%'}


class Action23279(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：如果目标处于头晕状态中，则附加火属性持续伤害
    # 威力：50
    # 持续时间：15秒
    # Deals fire damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Enemies affected by Lightheaded suffer damage over time
    # Potency: 50
    # Duration: 15s
    # related: [头晕(0)](Status2250), [头晕(1)](Status2501), 
    id = 23279
    names = ['芥末爆弹(BLU)', 'Mustard Bomb(BLU)']
    _orig_names = ['芥末爆弹', 'Mustard Bomb']
    damage = 220
    # remain metas: {'aoe_reduce': '50%', 'dmg_ot': '50'}


class Action23280(Action):
    # 一定时间内，将自身所受的伤害减轻20%
    # 持续时间：15秒
    # 以太复制：防护状态下的伤害减轻变为40%
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # Reduces damage taken by 20%.
    # Duration: 15s
    # Increases damage reduction to 40% when you are under the effect of Aetherial Mimicry: Tank.
    # Shares a recast timer with certain blue magic spells.
    # related: [龙之力(0)](Status306), [龙之力(1)](Status2500), [以太复制：防护](Status2124), 
    id = 23280
    names = ['Dragon Force(BLU)', '龙之力(BLU)']
    _orig_names = ['龙之力', 'Dragon Force']
    # remain metas: {'taken_dmg_reduce': ['变为40%', '20%']}


class Action23281(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：50
    # 追加效果：无属性持续伤害
    # 威力：50
    # 持续时间：15秒
    # Deals unaspected damage with a potency of 50 to all enemies in a straight line before you.
    # Additional Effect: Unaspected damage over time
    # Potency: 50
    # Duration: 15s
    id = 23281
    names = ['Aetherial Spark(BLU)', '以太火花(BLU)']
    _orig_names = ['以太火花', 'Aetherial Spark']
    damage = 50
    # remain metas: {'dmg_ot': '50'}


class Action23282(Action):
    # 对自身周围的敌人发动水属性范围魔法攻击
    # 威力：220
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：把敌人吸引到身边
    # Deals water damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Draw-in
    id = 23282
    names = ['水力吸引(BLU)', 'Hydro Pull(BLU)']
    _orig_names = ['Hydro Pull', '水力吸引']
    damage = 220


class Action23283(Action):
    # 向自身前方发出水属性直线范围魔法攻击
    # 威力：200
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：将范围内的敌人与小队成员击退10米
    # 目标身中部分弱化效果或处于非战斗状态时无效
    # Deals water damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: 10-yalm knockback to all enemies and party members in range
    # Cannot be used outside of combat or when target is suffering from certain enfeeblements.
    id = 23283
    names = ['Malediction of Water(BLU)', '水脉诅咒(BLU)']
    _orig_names = ['水脉诅咒', 'Malediction of Water']
    damage = 200


class Action23284(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：200
    # 如果小队中存在自己的专属陆行鸟，则技能威力上升
    # 专属陆行鸟在小队时威力：300
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals unaspected damage to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
    # Potency increases to 300 when partied with your personal chocobo.
    id = 23284
    names = ['陆行鸟陨石(BLU)', 'Choco Meteor(BLU)']
    _orig_names = ['陆行鸟陨石', 'Choco Meteor']
    damage = 200 # TODO: [200, 300]
    # remain metas: {'aoe_reduce': '50%'}


class Action23285(Action):
    # 对目标发动连续8次无属性魔法攻击
    # 威力：50
    # 自身处于以太复制：进攻状态时
    # 威力：100
    # 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间
    # Deals an unaspected eightfold attack, each hit with a potency of 50.
    # Potency is increased to 100 when you are under the effect of Aetherial Mimicry: DPS.
    # Shares a recast timer with certain blue magic spells.
    # related: [以太复制：进攻](Status2125), 
    id = 23285
    names = ['Matra Magic(BLU)', '马特拉魔术(BLU)']
    _orig_names = ['Matra Magic', '马特拉魔术']
    damage = 100 # TODO: [100, 50]


class Action23286(Action):
    # 向目标所在方向发出无属性直线范围物理攻击
    # 威力：220
    # 追加效果：附加头晕
    # 持续时间：5秒
    # 短时间内对同一目标重复使用时，每次可令目标头晕的时间都会减少，直至完全无效
    # 令目标陷入头晕状态时威力上升
    # 令目标陷入头晕状态时威力：400
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # Deals physical damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
    # Potency increased to 400 when target becomes afflicted with Lightheaded.
    # Additional Effect: Inflicts Lightheaded
    # Duration: 5s
    # Repeated use of this action in a short period will reduce the additional effect's duration, eventually rendering targets immune to Lightheaded.
    # related: [头晕(0)](Status2250), [头晕(1)](Status2501), 
    id = 23286
    names = ['Peripheral Synthesis(BLU)', '生成外设(BLU)']
    _orig_names = ['生成外设', 'Peripheral Synthesis']
    damage = 220
    # remain metas: {'dmg_ot': '400', 'aoe_reduce': '50%'}


class Action23287(Action):
    # 对自身周围的敌人发动无属性范围物理攻击
    # 威力：600
    # 与部分青魔法共享复唱时间
    # Deals unaspected damage with a potency of 600 to all nearby enemies.
    # Shares a recast timer with certain blue magic spells.
    id = 23287
    names = ['Both Ends(BLU)', '如意大旋风(BLU)']
    _orig_names = ['Both Ends', '如意大旋风']
    damage = 600


class Action23288(Action):
    # 持续向自身前方发出扇形范围攻击
    # 每秒对范围内的敌人造成伤害
    # 威力：200
    # 持续时间：5秒
    # 持续时间内再次使用时，向自身前方发出无属性扇形范围攻击
    # 威力：600
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 效果时间内发动鬼宿脚以外的技能或进行移动、转身都会使鬼宿脚立即消失
    # Deals unaspected damage over time with a potency of 200 to all enemies in a cone before you.
    # Duration: 5s
    # Executing Phantom Flurry again before its effect expires deals unaspected damage to all enemies in a cone before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
    # Effect ends upon using an action other than Phantom Flurry or moving (including facing a different direction).
    # related: [鬼宿脚](Status2502), 
    id = 23288
    names = ['Phantom Flurry(BLU)(0)', '鬼宿脚(BLU)(0)']
    _orig_names = ['Phantom Flurry', '鬼宿脚']
    # remain metas: {'dmg_ot': ['600', '200']}


class Action23289(Action):
    # 持续向自身前方发出扇形范围攻击
    # 每秒对范围内的敌人造成伤害
    # 威力：200
    # 持续时间：5秒
    # 持续时间内再次使用时，向自身前方发出无属性扇形范围攻击
    # 威力：600
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 效果时间内发动鬼宿脚以外的技能或进行移动、转身都会使鬼宿脚立即消失
    # Deals unaspected damage over time with a potency of 200 to all enemies in a cone before you.
    # Duration: 5s
    # Executing Phantom Flurry again before its effect expires deals unaspected damage to all enemies in a cone before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
    # Effect ends upon using an action other than Phantom Flurry or moving (including facing a different direction).
    # related: [鬼宿脚](Status2502), 
    id = 23289
    names = ['Phantom Flurry(BLU)(1)', '鬼宿脚(BLU)(1)']
    _orig_names = ['Phantom Flurry', '鬼宿脚']
    # remain metas: {'dmg_ot': ['600', '200']}


class Action23290(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：400
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：对目标附加无属性持续伤害状态
    # 威力：75
    # 持续时间：60秒
    # 与部分青魔法共享复唱时间
    # Deals unaspected damage to all nearby enemies with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Unaspected damage over time
    # Potency: 75
    # Duration: 60s
    id = 23290
    names = ['月下彼岸花(BLU)', 'Nightbloom(BLU)']
    _orig_names = ['月下彼岸花', 'Nightbloom']
    damage = 400
    # remain metas: {'dmg_ot': '75'}


class Action23416(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：140
    # 自身处于以太复制：治疗状态时效果变为
    # 恢复自身及周围队员的体力
    # 恢复力：300
    # Deals unaspected damage with a potency of 140 to all nearby enemies.
    #  Action effect changes, restoring own HP and the HP of all nearby party members when you are under the effect of Aetherial Mimicry: Healer.
    #  Cure Potency: 300
    # related: [以太复制：治疗](Status2126), 
    id = 23416
    names = ['Stotram(BLU)(1)', '赞歌(BLU)(1)']
    _orig_names = ['赞歌', 'Stotram']
    damage = 140
    heal = 300


