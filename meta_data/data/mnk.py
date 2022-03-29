from ._base import *

class Status107(Status):

    id = 107
    names = ['魔猿形']

class Status108(Status):

    id = 108
    names = ['盗龙形']

class Status109(Status):

    id = 109
    names = ['猛豹形']

    
class Status1797(Status):
    # 所有的攻击必定打出暴击
    # All attacks are dealing critical damage.
    # related: [连击(MNK)](Action53), [破坏神脚(MNK)](Action25767), 
    id = 1797
    names = ['暴击(0)', 'Critical Strikes(0)']


class Status579(Status):
    # 所有的攻击必定发动暴击
    # All attacks are dealing critical damage.
    # related: [连击(MNK)](Action53), [破坏神脚(MNK)](Action25767), 
    id = 579
    names = ['暴击(1)', 'Critical Strikes(1)']


class Status301(Status):
    # 所有的攻击必定打出暴击
    # All attacks are dealing critical damage.
    # related: [连击(MNK)](Action53), [破坏神脚(MNK)](Action25767), 
    id = 301
    names = ['暴击(2)', 'Critical Strikes(2)']


class Status1622(Status):
    # 所有的攻击必定打出暴击
    # All attacks are dealing critical damage.
    # related: [连击(MNK)](Action53), [破坏神脚(MNK)](Action25767), 
    id = 1622
    names = ['暴击(3)', 'Critical Strikes(3)']


class Status3001(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [双掌打(MNK)](Action61), [四面脚(MNK)](Action16473), 
    id = 3001
    names = ['功力', 'Disciplined Fist']


class Status101(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [双掌打(MNK)](Action61), 
    id = 101
    names = ['双掌打', 'Twin Snakes']


class Status102(Status):
    # 自身所受的治疗效果提高
    # HP recovery via healing actions is increased.
    # related: [真言(MNK)](Action65), 
    id = 102
    names = ['真言', 'Mantra']


class Status1309(Status):
    # 受到持续伤害，持续时间中受到为自己附加此状态的玩家的攻击时伤害增加
    # Sustaining damage over time, as well as increased damage from target who executed Demolish.
    # related: [破碎拳(MNK)](Action66), 
    id = 1309
    names = ['破碎拳(0)', 'Demolish(0)']


class Status246(Status):
    # 体力逐渐减少
    # Internal bleeding is causing damage over time.
    # related: [破碎拳(MNK)](Action66), 
    id = 246
    names = ['破碎拳(1)', 'Demolish(1)']


class Status110(Status):
    # 能够打出三种身形的所有招式
    # Employing all three pugilistic fighting stances─opo-opo, raptor, and coeurl.
    # related: [震脚(MNK)](Action69), 
    id = 110
    names = ['震脚', 'Perfect Balance']


class Status98(Status):
    # 打击耐性降低
    # Blunt resistance is reduced.
    # related: [双龙脚(MNK)](Action74), 
    id = 98
    names = ['双龙脚', 'Dragon Kick']


class Status1861(Status):
    # 下次发动连击的威力提高
    # Next Bootshine will deal increased damage.
    # related: [双龙脚(MNK)](Action74), 
    id = 1861
    names = ['连击效果提高', 'Leaden Fist']


class Status793(Status):
    # 体内积蓄着斗气
    # The first chakra is open.
    # related: [斗魂旋风脚(MNK)](Action3543), [苍气炮(MNK)](Action3545), [斗气(MNK)](Action3546), [阴阳斗气斩(MNK)](Action3547), [连击(pvp)(MNK)](Action8780), [正拳(pvp)(MNK)](Action8781), [阴阳斗气斩(pvp)(MNK)](Action8790), [万象斗气圈(MNK)](Action16474), [落踵踢(pvp)(MNK)](Action17670), [六合星导脚(pvp)(MNK)](Action17719), [万象斗气圈(pvp)(MNK)](Action17720), [四面脚(pvp)(MNK)](Action18914), [铁山靠(MNK)](Action25761), [空鸣拳(MNK)](Action25763), [翻天脚(MNK)](Action25765), [凤凰舞(MNK)](Action25768), [梦幻斗舞(MNK)](Action25769), [爆裂脚(MNK)](Action25882), 
    id = 793
    names = ['斗气', 'First Chakra']


class Status2513(Status):
    # 能够打出三种身形的所有招式，并触发对应的追加效果
    # Employing all three pugilistic fighting stances─opo-opo, raptor, and coeurl. Additional effects of actions used in these forms will also be triggered.
    # related: [斗魂旋风脚(MNK)](Action3543), [苍气炮(MNK)](Action3545), [演武(MNK)](Action4262), [翻天脚(MNK)](Action25765), [凤凰舞(MNK)](Action25768), [梦幻斗舞(MNK)](Action25769), [爆裂脚(MNK)](Action25882), 
    id = 2513
    names = ['无相身形', 'Formless Fist']


class Status2008(Status):
    # 抵消一定伤害
    # A barrier created through profound comprehension of the earth is nullifying damage.
    # related: [金刚极意(MNK)](Action7394), [金刚极意(pvp)(MNK)](Action8788), 
    id = 2008
    names = ['金刚极意(0)', 'Riddle of Earth(0)']


class Status1179(Status):
    # 减轻所受到的一部分伤害
    # Contemplating the riddle of earth. Damage taken is reduced.
    # related: [金刚极意(MNK)](Action7394), [金刚极意(pvp)(MNK)](Action8788), 
    id = 1179
    names = ['金刚极意(1)', 'Riddle of Earth(1)']


class Status1310(Status):
    # 受到一定量的伤害时会发动金刚极意
    # Contemplating the riddle of earth. Taking a certain amount of damage triggers Earth's Reply.
    # related: [金刚极意(MNK)](Action7394), [金刚极意(pvp)(MNK)](Action8788), 
    id = 1310
    names = ['金刚极意(2)', 'Riddle of Earth(2)']


class Status1181(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [红莲极意(MNK)](Action7395), [红莲极意(pvp)(MNK)](Action9639), 
    id = 1181
    names = ['红莲极意(0)', 'Riddle of Fire(0)']


class Status1413(Status):
    # 自身发动的下一次战技所造成的伤害提高
    # Next weaponskill will deal increased damage.
    # related: [红莲极意(MNK)](Action7395), [红莲极意(pvp)(MNK)](Action9639), 
    id = 1413
    names = ['红莲极意(1)', 'Riddle of Fire(1)']


class Status1185(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [义结金兰(MNK)](Action7396), [义结金兰(pvp)(MNK)](Action18915), 
    id = 1185
    names = ['义结金兰：攻击(0)', 'Brotherhood(0)']


class Status2174(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [义结金兰(MNK)](Action7396), [义结金兰(pvp)(MNK)](Action18915), 
    id = 2174
    names = ['义结金兰：攻击(1)', 'Brotherhood(1)']


class Status2173(Status):
    # 自身或队友发动战技或魔法时，一定几率给为自身附加此状态的武僧提升斗气
    # Grants chance to open a chakra to the monk who applied the effect when a weaponskill is used or a spell is cast by any affected party member or self.
    # related: [义结金兰(MNK)](Action7396), [义结金兰(pvp)(MNK)](Action18915), 
    id = 2173
    names = ['义结金兰：斗气(0)', 'Meditative Brotherhood(0)']


class Status1182(Status):
    # 自身或队友发动战技与魔法时，一定几率给为自身附加此状态的武僧提升斗气
    # Grants chance to open a chakra to the monk who applied the effect when a weaponskill is used or a spell is cast by any affected party member or self.
    # related: [义结金兰(MNK)](Action7396), [义结金兰(pvp)(MNK)](Action18915), 
    id = 1182
    names = ['义结金兰：斗气(1)', 'Meditative Brotherhood(1)']


class Status1862(Status):
    # 身形和功力的效果时间停止流逝
    # Form and Disciplined Fist timers are suspended due to a transcendent inner calm.
    # related: [无我(MNK)](Action16475), 
    id = 1862
    names = ['无我', 'Anatman']


class Status2514(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [六合星导脚(MNK)](Action16476), [六合星导脚(pvp)(MNK)](Action17719), 
    id = 2514
    names = ['六合星导脚', 'Six-sided Star']


class Status515(Status):
    # 变成雷电的发射源，体力会逐渐流失，经过一段时间之后会积累得越来越多，体力流失速度会变快
    # Sustaining damage over time. If the effect is not removed, it will continue to stack, increasing the amount of damage inflicted.
    # related: [轻身步法(MNK)](Action25762), 
    id = 515
    names = ['滚雷', 'Thunderclap']


class Status1364(Status):
    # 可以发动疾风极意
    # Able to execute Riddle of Wind.
    # related: [疾风极意(MNK)](Action25766), 
    id = 1364
    names = ['疾风极意(0)', 'Riddle of Wind(0)']


class Status1244(Status):
    # 可以发动疾风极意
    # Able to execute Riddle of Wind.
    # related: [疾风极意(MNK)](Action25766), 
    id = 1244
    names = ['疾风极意(1)', 'Riddle of Wind(1)']


class Status2687(Status):
    # 自动攻击间隔缩短
    # Auto-attack delay is reduced.
    # related: [疾风极意(MNK)](Action25766), 
    id = 2687
    names = ['疾风极意(2)', 'Riddle of Wind(2)']


class Action53(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?210:180):180)
    # (job==20?(level>=50?连击效果提高时威力：(job==20?(level>=84?310:280):280)
    # :):)“魔猿身形”中追加效果：攻击必定暴击
    # 追加效果：盗龙身形
    # 持续时间：30秒
    # Delivers an attack with a potency of (job==20?(level>=84?210:180):180).
    # (job==20?(level>=50?Leaden Fist Potency: (job==20?(level>=84?310:280):280)
    # :):)Opo-opo Form Bonus: Guarantees a critical hit
    # Additional Effect: Changes form to raptor
    # Duration: 30s
    # related: [暴击(0)](Status1797), [暴击(1)](Status579), [暴击(2)](Status301), [暴击(3)](Status1622), 
    id = 53
    names = ['连击(MNK)', 'Bootshine(MNK)']
    _orig_names = ['连击', 'Bootshine']
    damage = "(job==20?(lv>=84?210:180):180)"


class Action54(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?300:270):270)
    # 追加效果：猛豹身形
    # 持续时间：30秒
    # 发动条件：盗龙身形状态中
    # Delivers an attack with a potency of (job==20?(level>=84?300:270):270).
    # Can only be executed when in raptor form.
    # Additional Effect: Changes form to coeurl
    # Duration: 30s
    id = 54
    names = ['正拳(MNK)', 'True Strike(MNK)']
    _orig_names = ['正拳', 'True Strike']
    damage = "(job==20?(lv>=84?300:270):270)"


class Action56(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?250:220):220)
    # 侧面攻击威力：(job==20?(level>=84?310:280):280)
    # 追加效果：魔猿身形
    # 持续时间：30秒
    # 发动条件：猛豹身形状态中
    # Delivers an attack with a potency of (job==20?(level>=84?250:220):220).
    # (job==20?(level>=84?310:280):280) when executed from a target's flank.
    # Can only be executed when in coeurl form.
    # Additional Effect: Changes form to opo-opo
    # Duration: 30s
    id = 56
    names = ['崩拳(MNK)', 'Snap Punch(MNK)']
    _orig_names = ['Snap Punch', '崩拳']
    damage = "(job==20?(lv>=84?250:220):220)"
    side_damage = "(job==20?(lv>=84?310:280):280)"


class Action61(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?280:250):250)
    # 追加效果：对自身附加功力状态
    # 持续时间：15秒
    # 功力效果：令自身攻击造成的伤害提高(job==20?(level>=76?15:10):10)%
    # 追加效果：猛豹身形
    # 持续时间：30秒
    # 发动条件：盗龙身形状态中
    # Delivers an attack with a potency of (job==20?(level>=84?280:250):250).
    # Can only be executed when in raptor form.
    # Additional Effect: Grants Disciplined Fist
    # Disciplined Fist Effect: Increases damage dealt by (job==20?(level>=76?15:10):10)%
    # Duration: 15s
    # Additional Effect: Changes form to coeurl
    # Duration: 30s
    # related: [功力](Status3001), [双掌打](Status101), 
    id = 61
    names = ['Twin Snakes(MNK)', '双掌打(MNK)']
    _orig_names = ['双掌打', 'Twin Snakes']
    damage = "(job==20?(lv>=84?280:250):250)"
    # remain metas: {'dmg_increase': '(job==20?(lv>=76?15:10):10)%'}


class Action62(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # “魔猿身形”中威力：110
    # 追加效果：盗龙身形
    # 持续时间：30秒
    # Delivers an attack with a potency of 100 to all nearby targets.
    # Opo-opo Form Potency: 110
    # Additional Effect: Changes form to raptor
    # Duration: 30s
    id = 62
    names = ['破坏神冲(MNK)', 'Arm of the Destroyer(MNK)']
    _orig_names = ['Arm of the Destroyer', '破坏神冲']
    damage = "(魔猿身形?110:100)"


class Action65(Action):
    # 一定时间内，自身与周围队员所受的体力恢复效果提高10%
    # 持续时间：15秒
    # Increases HP recovery via healing actions by 10% for self and nearby party members.
    # Duration: 15s
    # related: [真言](Status102), 
    id = 65
    names = ['真言(MNK)', 'Mantra(MNK)']
    _orig_names = ['真言', 'Mantra']


class Action66(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?70:40):40)
    # 背面攻击威力：(job==20?(level>=84?130:100):100)
    # 追加效果：持续伤害
    # 威力：70
    # 持续时间：18秒
    # 追加效果：魔猿身形
    # 持续时间：30秒
    # 发动条件：猛豹身形状态中
    # Delivers an attack with a potency of (job==20?(level>=84?70:40):40).
    # (job==20?(level>=84?130:100):100) when executed from a target's rear.
    # Can only be executed when in coeurl form.
    # Additional Effect: Damage over time
    # Potency: 70
    # Duration: 18s
    # Additional Effect: Changes form to opo-opo
    # Duration: 30s
    # related: [破碎拳(0)](Status1309), [破碎拳(1)](Status246), 
    id = 66
    names = ['破碎拳(MNK)', 'Demolish(MNK)']
    _orig_names = ['Demolish', '破碎拳']
    damage = "(job==20?(lv>=84?70:40):40)"
    back_damage = "(job==20?(lv>=84?130:100):100)"
    # remain metas: {'dmg_ot': '70'}


class Action69(Action):
    # 对自身附加3档的震脚状态
    # 持续时间：20秒
    # 震脚效果：可以无视身形要求发动战技
    # (job==20?(level>=60?追加效果：自身发动魔猿身形、盗龙身形、猛豹身形的战技时，获得对应的脉轮
    # 魔猿身形的战技：魔猿脉轮
    # 盗龙身形的战技：盗龙脉轮
    # 猛豹身形的战技：猛豹脉轮
    # :):)积蓄次数：2
    # 发动条件：自身处于战斗状态
    # Grants 3 stacks of Perfect Balance, each stack allowing the execution of a weaponskill that requires a certain form, without being in that form.
    # Duration: 20s
    # (job==20?(level>=60?Additional Effect: Grants Opo-opo Chakra, Coeurl Chakra, or Raptor Chakra depending on the form required by actions executed
    # :):)Maximum Charges: 2
    # Can only be executed while in combat.
    # related: [震脚](Status110), 
    id = 69
    names = ['Perfect Balance(MNK)', '震脚(MNK)']
    _orig_names = ['震脚', 'Perfect Balance']


class Action70(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：130
    # 追加效果：魔猿身形
    # 持续时间：30秒
    # 发动条件：猛豹身形状态中
    # Delivers an attack with a potency of 130 to all nearby enemies.
    # Can only be executed when in coeurl form.
    # Additional Effect: Changes form to opo-opo
    # Duration: 30s
    id = 70
    names = ['Rockbreaker(MNK)', '地烈劲(MNK)']
    _orig_names = ['地烈劲', 'Rockbreaker']
    damage = 130


class Action74(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?320:290):290)
    # “魔猿身形”中追加效果：连击效果提高
    # 持续时间：30秒
    # 追加效果：盗龙身形
    # 持续时间：30秒
    # Delivers an attack with a potency of (job==20?(level>=84?320:290):290).
    # Opo-opo Form Bonus: Grants Leaden Fist
    # Duration: 30s
    # Additional Effect: Changes form to raptor
    # Duration: 30s
    # related: [双龙脚](Status98), [连击效果提高](Status1861), 
    id = 74
    names = ['双龙脚(MNK)', 'Dragon Kick(MNK)']
    _orig_names = ['Dragon Kick', '双龙脚']
    damage = "(job==20?(lv>=84?320:290):290)"


class Action3543(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：850
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 追加效果：无相身形
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：太阴斗气及太阳斗气状态中且脉轮3档
    # ※该技能无法设置到热键栏
    # Delivers an attack to target and all enemies nearby it with a potency of 850 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of Lunar Nadi and Solar Nadi, as well as three Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 3543
    names = ['Tornado Kick(MNK)', '斗魂旋风脚(MNK)']
    _orig_names = ['斗魂旋风脚', 'Tornado Kick']
    damage = 850


class Action3545(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：600
    # 攻击复数敌人时，对第一个之外的敌人威力降低70%
    # 追加效果：太阴斗气
    # 追加效果：无相身形
    # 持续时间30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：同一身形的脉轮3档
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies with a potency of 600 for the first enemy, and 70% less for all remaining enemies.
    # Additional Effect: Opens the Lunar Nadi
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of three of the same Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 3545
    names = ['Elixir Field(MNK)', '苍气炮(MNK)']
    _orig_names = ['Elixir Field', '苍气炮']
    damage = 600


class Action3546(Action):
    # 对自身附加斗气状态，最多可以积累5档
    # 持续时间：永久
    # 自身处于非战斗状态时直接获得5档斗气
    # 当斗气累积5档时，该技能会变为(job==20?(level>=54?阴阳斗气斩:铁山靠):铁山靠)
    # 与战技共享复唱时间
    # Opens a chakra. Up to five chakra can be opened at once.
    # Opens all five chakra when used outside of combat.
    # Shares a recast timer with all other weaponskills.
    # ※Action changes to (job==20?(level>=54?The Forbidden Chakra:Steel Peak):Steel Peak) when all five chakra are open.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), [斗气](Status793), 
    id = 3546
    names = ['斗气(MNK)', 'Meditation(MNK)']
    _orig_names = ['斗气', 'Meditation']


class Action3547(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?340:310):310)
    # 发动后会取消斗气状态
    # 发动条件：自身处于战斗状态且斗气5档
    # 与(job==20?(level>=74?万象斗气圈:空鸣拳):空鸣拳)共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of (job==20?(level>=84?340:310):310).
    # Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
    # Shares a recast timer with (job==20?(level>=74?Enlightenment:Howling Fist):Howling Fist).
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), 
    id = 3547
    names = ['the Forbidden Chakra(MNK)', '阴阳斗气斩(MNK)']
    _orig_names = ['阴阳斗气斩', 'the Forbidden Chakra']
    damage = "(job==20?(lv>=84?340:310):310)"


class Action4262(Action):
    # 对自身附加无相身形状态
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # Grants Formless Fist to self, allowing the execution of a weaponskill that requires a certain form, without being in that form.
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # related: [无相身形](Status2513), 
    id = 4262
    names = ['演武(MNK)', 'Form Shift(MNK)']
    _orig_names = ['演武', 'Form Shift']


class Action7394(Action):
    # 对自身附加3档的金刚极意状态
    # 持续时间结束或发动3次战技后取消该状态
    # 持续时间：10秒
    # 金刚极意效果：自身所受的伤害减轻20%
    # 积蓄次数：3
    # Grants 3 stacks of Riddle of Earth, each stack reducing damage taken by 20%.
    # Duration: 10s
    # Maximum Charges: 3
    # Effect ends when time expires or upon execution of three weaponskills.
    # related: [金刚极意(0)](Status2008), [金刚极意(1)](Status1179), [金刚极意(2)](Status1310), 
    id = 7394
    names = ['Riddle of Earth(MNK)', '金刚极意(MNK)']
    _orig_names = ['Riddle of Earth', '金刚极意']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action7395(Action):
    # 一定时间内，自身发动攻击造成的伤害提高15%
    # 持续时间：20秒
    # Increases damage dealt by 15%.
    # Duration: 20s
    # related: [红莲极意(0)](Status1181), [红莲极意(1)](Status1413), 
    id = 7395
    names = ['红莲极意(MNK)', 'Riddle of Fire(MNK)']
    _orig_names = ['红莲极意', 'Riddle of Fire']
    # remain metas: {'dmg_increase': '15%'}


class Action7396(Action):
    # 为自身与周围队员附加义结金兰：攻击和义结金兰：斗气状态
    # 持续时间：15秒
    # 义结金兰：攻击效果：发动攻击造成的伤害提高5%
    # (job==20?(level>=88?义结金兰：斗气效果（自身发动几率100%，小队成员发动几率20%）：自身与周围队员发动战技与魔法时，为自身附加1档斗气:义结金兰：斗气效果（发动几率20%）：自身与周围队员发动战技与魔法时，为自身附加1档斗气):义结金兰：斗气效果（发动几率20%）：自身与周围队员发动战技与魔法时，为自身附加1档斗气)
    # Grants Brotherhood and Meditative Brotherhood to self and all nearby party members.
    # Brotherhood Effect: Increases damage dealt by 5%
    # Meditative Brotherhood Effect: (job==20?(level>=88?20% chance you open a chakra when party members under this effect execute a weaponskill or cast a spell
    # Chance is 100% when you execute a weaponskill or cast a spell while under the effect of Meditative Brotherhood.:20% chance you open a chakra when you or party members under this effect execute a weaponskill or cast a spell):20% chance you open a chakra when you or party members under this effect execute a weaponskill or cast a spell)
    # Duration: 15s
    # related: [义结金兰：攻击(0)](Status1185), [义结金兰：攻击(1)](Status2174), [义结金兰：斗气(0)](Status2173), [义结金兰：斗气(1)](Status1182), 
    id = 7396
    names = ['义结金兰(MNK)', 'Brotherhood(MNK)']
    _orig_names = ['义结金兰', 'Brotherhood']
    # remain metas: {'dmg_increase': '5%'}


class Action8780(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：斗气
    # 持续时间：永久
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Opens a chakra
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), 
    id = 8780
    names = ['Bootshine(pvp)(MNK)', '连击(pvp)(MNK)']
    _orig_names = ['连击(pvp)', 'Bootshine(pvp)']
    damage = 1000


class Action8781(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：连击
    # 追加效果：斗气
    # 持续时间：永久
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Bootshine
    # Combo Potency: 1,200
    # Additional Effect: Opens a chakra
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), 
    id = 8781
    names = ['True Strike(pvp)(MNK)', '正拳(pvp)(MNK)']
    _orig_names = ['True Strike(pvp)', '正拳(pvp)']
    combo_action = 8780
    combo_damage = 1200


class Action8782(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：正拳
    # 连击成功：斗气
    # 持续时间：永久
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: True Strike
    # Combo Potency: 1,400
    # Combo Bonus: Opens a chakra
    # ※This action cannot be assigned to a hotbar.
    id = 8782
    names = ['崩拳(pvp)(MNK)', 'Snap Punch(pvp)(MNK)']
    _orig_names = ['Snap Punch(pvp)', '崩拳(pvp)']
    combo_action = 8781
    combo_damage = 1400


class Action8787(Action):
    # 冲向目标并发动物理攻击
    # 威力：800
    # 积蓄次数：3
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 800.
    # Maximum Charges: 3
    # Cannot be executed while bound.
    id = 8787
    names = ['Shoulder Tackle(pvp)(MNK)', '罗刹冲(pvp)(MNK)']
    _orig_names = ['Shoulder Tackle(pvp)', '罗刹冲(pvp)']
    damage = 800


class Action8788(Action):
    # 令自身受到的伤害减轻10%
    # 持续时间：6秒
    # 追加效果：为自身附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力2500的伤害量
    # 持续时间：6秒
    # Reduces damage taken by 10%.
    # Duration: 6s
    # Additional Effect: Creates a barrier around self that absorbs damage equivalent to a heal of 2,500 potency
    # Duration: 6s
    # related: [金刚极意(0)](Status2008), [金刚极意(1)](Status1179), [金刚极意(2)](Status1310), 
    id = 8788
    names = ['Riddle of Earth(pvp)(MNK)', '金刚极意(pvp)(MNK)']
    _orig_names = ['Riddle of Earth(pvp)', '金刚极意(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%', 'shield': '恢复力2500'}


class Action8789(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 积蓄次数：2
    # Delivers an attack with a potency of 1,800.
    # Maximum Charges: 2
    id = 8789
    names = ['Tornado Kick(pvp)(MNK)', '斗魂旋风脚(pvp)(MNK)']
    _orig_names = ['斗魂旋风脚(pvp)', 'Tornado Kick(pvp)']
    damage = 1800


class Action8790(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 发动后会取消斗气状态
    # 发动条件：斗气5档
    # Delivers an attack with a potency of 2,000.
    # Can only be executed while under the effect of the Fifth Chakra. The five chakra close upon execution.
    # related: [斗气](Status793), 
    id = 8790
    names = ['The Forbidden Chakra(pvp)(MNK)', '阴阳斗气斩(pvp)(MNK)']
    _orig_names = ['The Forbidden Chakra(pvp)', '阴阳斗气斩(pvp)']
    damage = 2000


class Action9639(Action):
    # 攻击伤害提高10%
    # 持续时间：6秒
    # 追加效果：效果时间内，自身发动的1次战技的伤害提高10%
    # 持续时间：6秒
    # Increases damage dealt by 10%.
    # Duration: 6s
    # Additional Effect: Increases damage dealt by next weaponskill by 10%
    # Duration: 6s
    # related: [红莲极意(0)](Status1181), [红莲极意(1)](Status1413), 
    id = 9639
    names = ['红莲极意(pvp)(MNK)', 'Riddle of Fire(pvp)(MNK)']
    _orig_names = ['Riddle of Fire(pvp)', '红莲极意(pvp)']
    # remain metas: {'dmg_increase': '10%'}


class Action16473(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：120
    # 追加效果：功力
    # 持续时间：15秒
    # 功力效果：令自身攻击造成的伤害提高(job==20?(level>=76?15:10):10)%
    # 追加效果：猛豹身形
    # 持续时间：30秒
    # 发动条件：盗龙身形状态中
    # Delivers an attack with a potency of 120 to all nearby enemies.
    # Can only be executed when in raptor form.
    # Additional Effect: Grants Disciplined Fist
    # Disciplined Fist Effect: Increases damage dealt by (job==20?(level>=76?15:10):10)%
    # Duration: 15s
    # Additional Effect: Changes form to coeurl
    # Duration: 30s
    # related: [功力](Status3001), 
    id = 16473
    names = ['Four-point Fury(MNK)', '四面脚(MNK)']
    _orig_names = ['Four-point Fury', '四面脚']
    damage = 120
    # remain metas: {'dmg_increase': '(job==20?(lv>=76?15:10):10)%'}


class Action16474(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：170
    # 发动后会取消斗气状态
    # 发动条件：自身处于战斗状态且斗气5档
    # 与阴阳斗气斩共享复唱时间
    # Delivers an attack with a potency of 170 to all enemies in a straight line before you.
    # Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
    # Shares a recast timer with The Forbidden Chakra.
    # related: [斗气](Status793), 
    id = 16474
    names = ['万象斗气圈(MNK)', 'Enlightenment(MNK)']
    _orig_names = ['万象斗气圈', 'Enlightenment']
    damage = 170


class Action16475(Action):
    # 令自身附加的身形与功力的持续时间恢复到最大值，同时暂停持续时间的流逝
    # 效果时间内发动技能或进行移动、转身都会立即解除无我
    # 发动之后会停止自动攻击
    # 持续时间：30秒
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # Extends the duration of Disciplined Fist and your present form to maximum and halts their expiration.
    # Duration: 30s
    # Cancels auto-attack upon execution. Effect ends upon using another action or moving (including facing a different direction).
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # related: [无我](Status1862), 
    id = 16475
    names = ['无我(MNK)', 'Anatman(MNK)']
    _orig_names = ['无我', 'Anatman']


class Action16476(Action):
    # 对目标发动物理攻击
    # 威力：(job==20?(level>=84?550:500):500)
    # 追加效果：提高自身的移动速度
    # 持续时间：5秒
    # 该战技有单独计算的复唱时间，发动后其他战技与魔法会产生与该战技相同的复唱时间
    # Delivers an attack with a potency of (job==20?(level>=84?550:500):500).
    # Additional Effect: Increases movement speed
    # Duration: 5s
    # This weaponskill does not share a recast timer with any other actions. Upon execution, the recast timer for this action will be applied to all other weaponskills and magic actions.
    # related: [六合星导脚](Status2514), 
    id = 16476
    names = ['六合星导脚(MNK)', 'Six-sided Star(MNK)']
    _orig_names = ['六合星导脚', 'Six-sided Star']
    damage = "(job==20?(lv>=84?550:500):500)"


class Action17670(Action):
    # 对周围的敌人发动范围物理攻击
    # 威力：1000
    # 追加效果：每命中一个目标获得1档斗气
    # 持续时间：永久
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Opens a chakra for each enemy hit
    # related: [斗气](Status793), 
    id = 17670
    names = ['落踵踢(pvp)(MNK)', 'Axe Kick(pvp)(MNK)']
    _orig_names = ['落踵踢(pvp)', 'Axe Kick(pvp)']
    damage = 1000


class Action17719(Action):
    # 对目标发动物理攻击
    # 威力：2400
    # 追加效果：斗气
    # 持续时间：永久
    # Delivers an attack with a potency of 2,400.
    # Additional Effect: Opens a chakra
    # related: [斗气](Status793), [六合星导脚](Status2514), 
    id = 17719
    names = ['六合星导脚(pvp)(MNK)', 'Six-sided Star(pvp)(MNK)']
    _orig_names = ['Six-sided Star(pvp)', '六合星导脚(pvp)']
    damage = 2400


class Action17720(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：1200
    # 发动后会取消斗气状态
    # 发动条件：斗气5档
    # Delivers an attack with a potency of 1,200 to all enemies in a straight line before you.
    # Can only be executed while under the effect of the Fifth Chakra. The five chakra close upon execution.
    # related: [斗气](Status793), 
    id = 17720
    names = ['Enlightenment(pvp)(MNK)', '万象斗气圈(pvp)(MNK)']
    _orig_names = ['Enlightenment(pvp)', '万象斗气圈(pvp)']
    damage = 1200


class Action18913(Action):
    # 对自身周围的敌人发动物理攻击
    # 连击中威力：800
    # 连击条件：四面脚
    # 连击成功：斗气
    # 持续时间：永久
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Four-point Fury
    # Combo Potency: 800
    # Combo Bonus: Opens a chakra
    # ※This action cannot be assigned to a hotbar.
    id = 18913
    names = ['地烈劲(pvp)(MNK)', 'Rockbreaker(pvp)(MNK)']
    _orig_names = ['Rockbreaker(pvp)', '地烈劲(pvp)']
    combo_action = 18914
    combo_damage = 800


class Action18914(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：600
    # 追加效果：斗气
    # 持续时间：永久
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 600 to all nearby enemies.
    # Additional Effect: Opens a chakra
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), 
    id = 18914
    names = ['四面脚(pvp)(MNK)', 'Four-point Fury(pvp)(MNK)']
    _orig_names = ['Four-point Fury(pvp)', '四面脚(pvp)']
    damage = 600


class Action18915(Action):
    # 为自身与周围队员附加义结金兰：斗气状态，自身与周围队员发动战技时有50%几率为自身附加斗气
    # 为自身与周围队员附加义结金兰：攻击状态，发动物理攻击造成的伤害提高5%
    # 持续时间：10秒
    # Grants Brotherhood and Meditative Brotherhood to all nearby party members.
    # Brotherhood Effect: Increases damage dealt by 5%
    # Meditative Brotherhood Effect: 50% chance you open a chakra when party members under this effect execute a weaponskill or cast a spell
    # Duration: 10s
    # related: [义结金兰：攻击(0)](Status1185), [义结金兰：攻击(1)](Status2174), [义结金兰：斗气(0)](Status2173), [义结金兰：斗气(1)](Status1182), 
    id = 18915
    names = ['义结金兰(pvp)(MNK)', 'Brotherhood(pvp)(MNK)']
    _orig_names = ['义结金兰(pvp)', 'Brotherhood(pvp)']
    # remain metas: {'dmg_increase': '5%'}


class Action25761(Action):
    # 对目标发动物理攻击
    # 威力：180
    # 发动后会取消斗气状态
    # 发动条件：自身处于战斗状态且斗气5档
    # 与空鸣拳共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 180.
    # Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
    # Shares a recast timer with Howling Fist.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), 
    id = 25761
    names = ['铁山靠(MNK)', 'Steel Peak(MNK)']
    _orig_names = ['Steel Peak', '铁山靠']
    damage = 180


class Action25762(Action):
    # 指定一名敌人或队员为目标，自身快速移动到目标身边
    # 积蓄次数：(job==20?(level>=84?3:2):2)
    # 止步状态下无法发动
    # Rush to a targeted enemy's or party member's location.
    # Maximum Charges: (job==20?(level>=84?3:2):2)
    # Cannot be executed while bound.
    # related: [滚雷](Status515), 
    id = 25762
    names = ['Thunderclap(MNK)', '轻身步法(MNK)']
    _orig_names = ['Thunderclap', '轻身步法']


class Action25763(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：100
    # 发动后会取消斗气状态
    # 发动条件：自身处于战斗状态且斗气5档
    # 与(job==20?(level>=54?阴阳斗气斩:铁山靠):铁山靠)共享复唱时间
    # Delivers an attack with a potency of 100 to all enemies in a straight line before you.
    # Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
    # Shares a recast timer with (job==20?(level>=54?The Forbidden Chakra:Steel Peak):Steel Peak).
    # related: [斗气](Status793), 
    id = 25763
    names = ['空鸣拳(MNK)', 'Howling Fist(MNK)']
    _orig_names = ['Howling Fist', '空鸣拳']
    damage = 100


class Action25764(Action):
    # 当自身处于3档脉轮状态时，根据附加的脉轮发动必杀技
    # 1种脉轮：发动苍气炮
    # 2种脉轮：发动翻天脚
    # 3种脉轮：发动(job==20?(level>=86?凤凰舞:爆裂脚):爆裂脚)
    # 3种脉轮和太阴斗气及太阳斗气：(job==20?(level>=90?梦幻斗舞:斗魂旋风脚):斗魂旋风脚)
    # Strike the enemy with a technique fueled by the power of your Beast Chakra.
    # The technique used is determined by the number of different types of Beast Chakra opened.
    # 1 Beast Chakra Type: Elixir Field
    # 2 Beast Chakra Types: Celestial Revolution
    # 3 Beast Chakra Types: (job==20?(level>=86?Rising Phoenix:Flint Strike):Flint Strike)
    # 3 Beast Chakra and Both Nadi: (job==20?(level>=90?Phantom Rush:Tornado Kick):Tornado Kick)
    id = 25764
    names = ['Masterful Blitz(MNK)', '必杀技(MNK)']
    _orig_names = ['Masterful Blitz', '必杀技']


class Action25765(Action):
    # 对目标发动物理攻击
    # 威力：450
    # 追加效果：为自身附加太阴斗气状态
    # 若自身已附加太阴斗气状态，则为自身附加太阳斗气状态
    # 追加效果：无相身形
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：脉轮3档
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 450.
    # Additional Effect: Opens the Lunar Nadi
    # If the Lunar Nadi is already open, opens the Solar Nadi instead.
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of three Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 25765
    names = ['Celestial Revolution(MNK)', '翻天脚(MNK)']
    _orig_names = ['Celestial Revolution', '翻天脚']
    damage = 450


class Action25766(Action):
    # 令自身发动的自动攻击间隔缩短50%
    # 持续时间：15秒
    # Reduces auto-attack delay by 50%.
    # Duration: 15s
    # related: [疾风极意(0)](Status1364), [疾风极意(1)](Status1244), [疾风极意(2)](Status2687), 
    id = 25766
    names = ['Riddle of Wind(MNK)', '疾风极意(MNK)']
    _orig_names = ['疾风极意', 'Riddle of Wind']


class Action25767(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：110
    # “魔猿身形”中追加效果：攻击必定暴击
    # 追加效果：盗龙身形
    # 持续时间：30秒
    # Delivers an attack with a potency of 110 to all nearby enemies.
    # Opo-opo Form Bonus: Guarantees a critical hit
    # Additional Effect: Changes form to raptor
    # Duration: 30s
    # related: [暴击(0)](Status1797), [暴击(1)](Status579), [暴击(2)](Status301), [暴击(3)](Status1622), 
    id = 25767
    names = ['破坏神脚(MNK)', 'Shadow of the Destroyer(MNK)']
    _orig_names = ['破坏神脚', 'Shadow of the Destroyer']
    damage = 110


class Action25768(Action):
    # 对自身周围的敌人发动火属性范围物理攻击
    # 威力：700
    # 攻击复数敌人时，对第一个之外的敌人威力降低70%
    # 追加效果：太阳斗气
    # 追加效果：无相身形
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：不同身形的脉轮3档
    # ※该技能无法设置到热键栏
    # Deals physical fire damage to all nearby enemies with a potency of 700 for the first enemy, and 70% less for all remaining enemies.
    # Additional Effect: Opens the Solar Nadi
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of three distinct Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 25768
    names = ['Rising Phoenix(MNK)', '凤凰舞(MNK)']
    _orig_names = ['Rising Phoenix', '凤凰舞']
    damage = 700


class Action25769(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：1150
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：无相身形
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：太阴斗气和太阳斗气状态中且脉轮3档
    # ※该技能无法设置到热键栏
    # Delivers an attack to target and all enemies nearby it with a potency of 1,150 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of Lunar Nadi and Solar Nadi, as well as three Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 25769
    names = ['梦幻斗舞(MNK)', 'Phantom Rush(MNK)']
    _orig_names = ['梦幻斗舞', 'Phantom Rush']
    damage = 1150
    # remain metas: {'aoe_reduce': '50%'}


class Action25882(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：600
    # 攻击复数敌人时，对第一个之外的敌人威力降低70%
    # 追加效果：太阳斗气
    # 追加效果：无相身形
    # 持续时间：30秒
    # 无相身形效果：可以无视身形要求发动战技，同时触发追加效果
    # 发动条件：不同身形的脉轮3档
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies with a potency of 600 for the first enemy, and 70% less for all remaining enemies.
    # Additional Effect: Opens the Solar Nadi
    # Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
    # Duration: 30s
    # Any additional effects associated with the executed action will also be applied.
    # Can only be executed while under the effect of three distinct Beast Chakra.
    # ※This action cannot be assigned to a hotbar.
    # related: [斗气](Status793), [无相身形](Status2513), 
    id = 25882
    names = ['爆裂脚(MNK)', 'Flint Strike(MNK)']
    _orig_names = ['Flint Strike', '爆裂脚']
    damage = 600


