from ._base import *


class Status1298(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [阵风(SAM)](Action7478), [满月(SAM)](Action7484), [明镜止水(SAM)](Action7499), 
    id = 1298
    names = ['风月', 'Fugetsu']


class Status1299(Status):
    # 自动攻击间隔、战技与魔法的咏唱及复唱时间缩短
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [士风(SAM)](Action7479), [樱花(SAM)](Action7485), [明镜止水(SAM)](Action7499), 
    id = 1299
    names = ['风花', 'Fuka']


class Status1227(Status):
    # 斩击耐性降低
    # Slashing resistance is reduced.
    # related: [雪风(SAM)](Action7480), [雪风(pvp)(SAM)](Action8824), 
    id = 1227
    names = ['雪风(0)', 'Yukikaze(0)']


class Status1318(Status):
    # 受到附加此效果的玩家攻击的伤害增加
    # Sustaining increased damage from target who executed Yukikaze.
    # related: [雪风(SAM)](Action7480), [雪风(pvp)(SAM)](Action8824), 
    id = 1318
    names = ['雪风(1)', 'Yukikaze(1)']


class Status1228(Status):
    # 体力逐渐减少
    # Open wounds are bleeding, causing damage over time.
    # related: [彼岸花(SAM)](Action7489), 
    id = 1228
    names = ['彼岸花(0)', 'Higanbana(0)']


class Status1319(Status):
    # 受到持续伤害，同时自身所受的体力恢复效果降低
    # Open wounds are bleeding, causing damage over time. HP recovery is reduced.
    # related: [彼岸花(SAM)](Action7489), 
    id = 1319
    names = ['彼岸花(1)', 'Higanbana(1)']


class Status1236(Status):
    # 下次发动燕飞的威力提高
    # Next Enpi will deal increased damage.
    # related: [必杀剑·夜天(SAM)](Action7493), 
    id = 1236
    names = ['燕飞效果提高', 'Enhanced Enpi']


class Status1229(Status):
    # 下次发动战技造成的伤害提高
    # Next weaponskill will deal increased damage.
    # related: [必杀剑·回天(SAM)](Action7494), 
    id = 1229
    names = ['必杀剑·回天', 'Kaiten']


class Status1231(Status):
    # 持续获得剑气
    # Storing Kenki.
    # related: [默想(SAM)](Action7497), 
    id = 1231
    names = ['默想', 'Meditate']


class Status1232(Status):
    # 下次受到攻击时所受到的伤害减轻
    # Next damage taken is reduced.
    # related: [心眼(SAM)](Action7498), 
    id = 1232
    names = ['心眼', 'Third Eye']


class Status1320(Status):
    # 将战技的连击置换到最终阶段
    # Final combo prerequisite is met.
    # related: [明镜止水(SAM)](Action7499), 
    id = 1320
    names = ['明镜止水(0)', 'Meikyo Shisui(0)']


class Status1233(Status):
    # 达成战技连击的条件
    # Combo prerequisites are met.
    # related: [明镜止水(SAM)](Action7499), 
    id = 1233
    names = ['明镜止水(1)', 'Meikyo Shisui(1)']


class Status1240(Status):
    # 令自身所受到的伤害减少，同时给予对方反击伤害
    # Damage taken is reduced while countering any physical attacks.
    # related: [必杀剑·地天(pvp)(SAM)](Action7855), 
    id = 1240
    names = ['必杀剑·地天', 'Chiten']


class Status2959(Status):
    # 可以发动奥义斩浪
    # Able to execute Ogi Namikiri.
    # related: [奥义斩浪(SAM)](Action25781), 
    id = 2959
    names = ['奥义斩浪预备', 'Ogi Namikiri Ready']


class Action7477(Action):
    # 对目标发动物理攻击
    # 威力：180(level>=62?(job==34?
    # 追加效果：获得5点剑气:):)
    # Delivers an attack with a potency of 180.(level>=62?(job==34?
    # Additional Effect: Increases Kenki Gauge by 5:):)
    id = 7477
    names = ['Hakaze(SAM)', '刃风(SAM)']
    _orig_names = ['Hakaze', '刃风']
    damage = 180


class Action7478(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：刃风
    # 连击中威力：280
    # 连击成功：风月
    # 持续时间：40秒
    # 风月效果：自身发动攻击造成的伤害提高(job==34?(level>=78?13:10):10)%(level>=62?(job==34?
    # 连击成功：获得5点剑气:):)
    # Delivers an attack with a potency of 100.
    # Combo Action: Hakaze
    # Combo Potency: 280
    # Combo Bonus: Grants Fugetsu
    # Fugetsu Effect: Increases damage dealt by (job==34?(level>=78?13:10):10)%
    # Duration: 40s(level>=62?(job==34?
    # Combo Bonus: Increases Kenki Gauge by 5:):)
    # related: [风月](Status1298), 
    id = 7478
    names = ['阵风(SAM)', 'Jinpu(SAM)']
    _orig_names = ['阵风', 'Jinpu']
    combo_action = 7477
    damage = 100
    combo_damage = 280
    # remain metas: {'dmg_increase': '(job==34?(lv>=78?13:10):10)%'}


class Action7479(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：刃风
    # 连击中威力：280
    # 连击成功：风花
    # 持续时间：40秒
    # 风花效果：自身的自动攻击间隔、战技与魔法的咏唱及复唱时间缩短(job==34?(level>=78?13:10):10)%
    # (level>=62?(job==34?
    # 连击成功：获得5点剑气:):)
    # Delivers an attack with a potency of 100.
    # Combo Action: Hakaze
    # Combo Potency: 280
    # Combo Bonus: Grants Fuka
    # Fuka Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by (job==34?(level>=78?13:10):10)%
    # Duration: 40s(level>=62?(job==34?
    # Combo Bonus: Increases Kenki Gauge by 5:):)
    # related: [风花](Status1299), 
    id = 7479
    names = ['士风(SAM)', 'Shifu(SAM)']
    _orig_names = ['士风', 'Shifu']
    combo_action = 7477
    damage = 100
    combo_damage = 280


class Action7480(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：刃风
    # 连击中威力：280
    # (level>=52?(job==34?连击成功：获得雪之闪与(level>=62?(job==34?15:10):10)点剑气:连击成功：雪之闪):连击成功：雪之闪)
    # Delivers an attack with a potency of 100.
    # Combo Action: Hakaze
    # Combo Potency: 280(level>=52?(job==34?
    # Combo Bonus: Increases Kenki Gauge by (level>=62?(job==34?15:10):10)
    # Combo Bonus: Grants Setsu:
    # Combo Bonus: Grants Setsu):
    # Combo Bonus: Grants Setsu)
    # related: [雪风(0)](Status1227), [雪风(1)](Status1318), 
    id = 7480
    names = ['雪风(SAM)', 'Yukikaze(SAM)']
    _orig_names = ['Yukikaze', '雪风']
    combo_action = 7477
    damage = 100
    combo_damage = 280


class Action7481(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 背面攻击威力:150
    # 连击条件：阵风
    # 连击中威力：320
    # 连击中背面攻击威力：370
    # (level>=52?(job==34?连击成功：获得月之闪与(level>=62?(job==34?10:5):5)点剑气:连击成功：月之闪):连击成功：月之闪)
    # Delivers an attack with a potency of 100.
    # 150 when executed from a target's rear.
    # Combo Action: Jinpu
    # Combo Potency: 320
    # Rear Combo Potency: 370(level>=52?(job==34?
    # Combo Bonus: Increases Kenki Gauge by (level>=62?(job==34?10:5):5):):)
    # Combo Bonus: Grants Getsu
    id = 7481
    names = ['月光(SAM)', 'Gekko(SAM)']
    _orig_names = ['Gekko', '月光']
    combo_action = 7478
    damage = 100
    combo_damage = 320
    back_combo_damage = 370


class Action7482(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 侧面攻击威力：150
    # 连击条件：士风
    # 连击中威力：320
    # 连击中侧面攻击威力：370
    # (level>=62?(job==34?连击成功：获得花之闪与(level>=62?(job==34?10:5):5)点剑气:连击成功：花之闪):连击成功：花之闪)
    # Delivers an attack with a potency of 100.
    # 150 when executed from a target's flank.
    # Combo Action: Shifu
    # Combo Potency: 320
    # Flank Combo Potency: 370(level>=52?(job==34?
    # Combo Bonus: Increases Kenki Gauge by (level>=62?(job==34?10:5):5):):)
    # Combo Bonus: Grants Ka
    id = 7482
    names = ['花车(SAM)', 'Kasha(SAM)']
    _orig_names = ['Kasha', '花车']
    combo_action = 7479
    damage = 100
    combo_damage = 320
    side_damage = 150
    side_combo_damage = 370


class Action7483(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：90(level>=62?(job==34?
    # 追加效果：获得5点剑气:):)
    # Delivers an attack with a potency of 90 to all enemies in a cone before you.(level>=62?(job==34?
    # Additional Effect: Increases Kenki Gauge by 5:):)
    id = 7483
    names = ['风雅(SAM)', 'Fuga(SAM)']
    _orig_names = ['风雅', 'Fuga']
    damage = 90


class Action7484(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：(job==34?(level>=86?风光:风雅):风雅)
    # 连击中威力：110
    # 连击成功：风月
    # 持续时间：40秒
    # 风月效果：自身发动攻击造成的伤害提高(job==34?(level>=78?13:10):10)%(level>=52?(job==34?
    # 连击成功：获得月之闪与(level>=62?(job==34?10:5):5)点剑气:
    # 连击成功：月之闪):
    # 连击成功：月之闪)
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: (job==34?(level>=86?Fuko:Fuga):Fuga)
    # Combo Potency: 110
    # Combo Bonus: Grants Fugetsu
    # Fugetsu Effect: Increases damage dealt by (job==34?(level>=78?13:10):10)%
    # Duration: 40s(level>=52?(job==34?
    # Combo Bonus: Increases Kenki Gauge by (level>=62?(job==34?10:5):5)
    # Combo Bonus: Grants Getsu:
    # Combo Bonus: Grants Getsu):
    # Combo Bonus: Grants Getsu)
    # related: [风月](Status1298), 
    id = 7484
    names = ['满月(SAM)', 'Mangetsu(SAM)']
    _orig_names = ['满月', 'Mangetsu']
    combo_action = 7483
    damage = 100
    combo_damage = 110
    # remain metas: {'dmg_increase': '(job==34?(lv>=78?13:10):10)%'}


class Action7485(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 连击条件：(job==34?(level>=86?风光:风雅):风雅)
    # 连击中威力：110
    # 连击成功：风花
    # 持续时间：40秒
    # 风花效果：自身的自动攻击间隔、战技与魔法的咏唱及复唱时间缩短(job==34?(level>=78?13:10):10)%(level>=52?(job==34?
    # 连击成功：获得花之闪与(level>=62?(job==34?10:5):5)点剑气:
    # 连击成功：花之闪):
    # 连击成功：花之闪)
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Combo Action: (job==34?(level>=86?Fuko:Fuga):Fuga)
    # Combo Potency: 110
    # Combo Bonus: Grants Fuka
    # Fuka Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by (job==34?(level>=78?13:10):10)%
    # Duration: 40s(level>=52?(job==34?
    # Combo Bonus: Increases Kenki Gauge by (level>=62?(job==34?10:5):5)
    # Combo Bonus: Grants Ka:
    # Combo Bonus: Grants Ka):
    # Combo Bonus: Grants Ka)
    # related: [风花](Status1299), 
    id = 7485
    names = ['樱花(SAM)', 'Oka(SAM)']
    _orig_names = ['Oka', '樱花']
    combo_action = 7483
    damage = 100
    combo_damage = 110


class Action7486(Action):
    # 对目标发动远距离物理攻击
    # 威力：100(level>=56?(job==34?
    # “燕飞效果提高”状态中威力：260:):)(level>=52?(job==34?
    # 追加效果：获得(level>=62?(job==34?10:5):5)点剑气:):)
    # Delivers a ranged attack with a potency of 100.(level>=56?(job==34?
    # Enhanced Enpi Bonus Potency: 260:):)(level>=52?(job==34?
    # Additional Effect: Increases Kenki Gauge by (level>=62?(job==34?10:5):5):):)
    id = 7486
    names = ['Enpi(SAM)', '燕飞(SAM)']
    _orig_names = ['燕飞', 'Enpi']
    damage = 100


class Action7487(Action):
    # 对目标发动物理攻击
    # 威力：660
    # (job==34?(level>=80?追加效果：剑压
    # 最大档数：3档
    # 持续时间：永久
    # :):)
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 660.
    # (job==34?(level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3
    # :):)
    # ※This action cannot be assigned to a hotbar.
    id = 7487
    names = ['纷乱雪月花(SAM)', 'Midare Setsugekka(SAM)']
    _orig_names = ['纷乱雪月花', 'Midare Setsugekka']
    damage = 660


class Action7488(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：280
    # (job==34?(level>=80?追加效果：剑压
    # 最大档数：3档
    # 持续时间：永久
    # :):)
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 280 to all enemies in a cone before you.
    # (job==34?(level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3
    # :):)
    # ※This action cannot be assigned to a hotbar.
    id = 7488
    names = ['天下五剑(SAM)', 'Tenka Goken(SAM)']
    _orig_names = ['天下五剑', 'Tenka Goken']
    damage = 280


class Action7489(Action):
    # 对目标发动物理攻击
    # 威力：200
    # 追加效果：持续伤害
    # 威力：30
    # 持续时间：60秒
    # (job==34?(level>=80?追加效果：剑压
    # 最大档数：3档
    # 持续时间：永久
    # :):)
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 200.
    # Additional Effect: Damage over time
    # Potency: 30
    # Duration: 60s
    # (job==34?(level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3
    # :):)
    # ※This action cannot be assigned to a hotbar.
    # related: [彼岸花(0)](Status1228), [彼岸花(1)](Status1319), 
    id = 7489
    names = ['Higanbana(SAM)', '彼岸花(SAM)']
    _orig_names = ['彼岸花', 'Higanbana']
    damage = 200
    # remain metas: {'dmg_ot': '30'}


class Action7490(Action):
    # 对目标发动物理攻击
    # 威力：270
    # 发动条件：剑气25点
    # Delivers an attack with a potency of 270.
    # Kenki Gauge Cost: 25
    id = 7490
    names = ['必杀剑·震天(SAM)', 'Hissatsu: Shinten(SAM)']
    _orig_names = ['Hissatsu: Shinten', '必杀剑·震天']
    damage = 270


class Action7491(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：110
    # 发动条件：剑气25点
    # Delivers an attack with a potency of 110 to all nearby enemies.
    # Kenki Gauge Cost: 25
    id = 7491
    names = ['必杀剑·九天(SAM)', 'Hissatsu: Kyuten(SAM)']
    _orig_names = ['必杀剑·九天', 'Hissatsu: Kyuten']
    damage = 110


class Action7492(Action):
    # 冲向目标并发动物理攻击
    # 威力：100
    # 发动条件：剑气10点
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 100.
    # Kenki Gauge Cost: 10
    # Cannot be executed while bound.
    id = 7492
    names = ['必杀剑·晓天(SAM)', 'Hissatsu: Gyoten(SAM)']
    _orig_names = ['必杀剑·晓天', 'Hissatsu: Gyoten']
    damage = 100


class Action7493(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：后跳10米距离
    # 追加效果：燕飞效果提高
    # 持续时间：15秒
    # 发动条件：剑气10点
    # 止步状态下无法发动
    # Delivers an attack with a potency of 100.
    # Additional Effect: 10-yalm backstep
    # Additional Effect: Grants Enhanced Enpi
    # Duration: 15s
    # Kenki Gauge Cost: 10
    # Cannot be executed while bound.
    # related: [燕飞效果提高](Status1236), 
    id = 7493
    names = ['必杀剑·夜天(SAM)', 'Hissatsu: Yaten(SAM)']
    _orig_names = ['Hissatsu: Yaten', '必杀剑·夜天']
    damage = 100


class Action7494(Action):
    # 效果时间内发动的第1个战技威力提高50%
    # 持续时间：10秒
    # 发动条件：剑气20点
    # Increases potency of next weaponskill by 50%.
    # Duration: 10s
    # Kenki Gauge Cost: 20
    # related: [必杀剑·回天](Status1229), 
    id = 7494
    names = ['必杀剑·回天(SAM)', 'Hissatsu: Kaiten(SAM)']
    _orig_names = ['必杀剑·回天', 'Hissatsu: Kaiten']


class Action7495(Action):
    # 将闪转换为剑气
    # 每一道闪可转换10点剑气
    # 发动条件：雪之闪或月之闪或花之闪状态中
    # Converts Setsu, Getsu, and Ka into Kenki. Each Sen converted increases your Kenki Gauge by 10. Can only be executed if under the effect of at least one of the three statuses.
    id = 7495
    names = ['叶隐(SAM)', 'Hagakure(SAM)']
    _orig_names = ['Hagakure', '叶隐']


class Action7496(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：500
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：剑气25点(job==34?(level>=72?
    # 与必杀剑·闪影共享复唱时间:):)
    # Delivers an attack to all enemies in a straight line before you with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
    # Kenki Gauge Cost: 25(job==34?(level>=72?
    # Shares a recast timer with Hissatsu: Senei.:):)
    id = 7496
    names = ['Hissatsu: Guren(SAM)', '必杀剑·红莲(SAM)']
    _orig_names = ['Hissatsu: Guren', '必杀剑·红莲']
    damage = 500
    # remain metas: {'aoe_reduce': '50%'}


class Action7497(Action):
    # 进入默想状态持续获得剑气
    # 持续时间：15秒
    # (job==34?(level>=80?追加效果：连续叠加剑压状态
    # 最大档数：3档
    # 持续时间：永久
    # :):)效果时间内发动技能或进行移动、转身都会立即解除默想
    # 发动之后会停止自动攻击
    # (job==34?(level>=80?非战斗中无法获得剑气，也不会附加剑压状态:非战斗中无法获得剑气):非战斗中无法获得剑气)
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # Gradually increases your Kenki Gauge.
    # Duration: 15s
    # (job==34?(level>=80?Additional Effect: Grants stacks of Meditation when used in combat, up to a maximum of 3
    # :):)Kenki Gauge not affected when used outside battle.
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), [默想](Status1231), 
    id = 7497
    names = ['默想(SAM)', 'Meditate(SAM)']
    _orig_names = ['Meditate', '默想']


class Action7498(Action):
    # 一定时间内，受到的第一次攻击伤害减轻10%
    # 持续时间：3秒(level>=58?(job==34?
    # 追加效果：成功减轻伤害后获得10点剑气:):)
    # Reduces the amount of damage taken by the next attack by 10%.
    # Duration: 3s(level>=52?(job==34?
    # Additional Effect: Increases Kenki Gauge by 10 when hit:):)
    # related: [心眼](Status1232), 
    id = 7498
    names = ['Third Eye(SAM)', '心眼(SAM)']
    _orig_names = ['Third Eye', '心眼']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action7499(Action):
    # 一定时间内，战技无需连击条件即可连击成功
    # 月光命中后为自身附加风月状态，花车命中后为自身附加风花状态
    # 持续时间结束、发动3次居合术(job==34?(level>=90?或奥义斩浪:):)之外的战技后取消该状态
    # 持续时间：15秒(job==34?(level>=88?
    # 积蓄次数：2:):)
    # Execute up to 3 weaponskill combos without meeting combo prerequisites. Does not affect Iaijutsu(job==34?(level>=90? or Ogi Namikiri:):).
    # Duration: 15s
    # Additional Effect: Successfully landing Gekko grants Fugetsu, and successfully landing Kasha grants Fuka(job==34?(level>=88?
    # Maximum Charges: 2:):)
    # related: [明镜止水(0)](Status1320), [明镜止水(1)](Status1233), [风月](Status1298), [风花](Status1299), 
    id = 7499
    names = ['明镜止水(SAM)', 'Meikyo Shisui(SAM)']
    _orig_names = ['Meikyo Shisui', '明镜止水']


class Action7855(Action):
    # 一定时间内，将自身所受的伤害减轻50%，同时受到攻击时会给予对方反击伤害
    # 威力：1200
    # 持续时间：6秒
    # 反击伤害效果：获得5点剑气
    # 持续时间结束或发动5次反击后取消该状态
    # 发动条件：剑气25点
    # Reduces damage taken by 50% and counters up to the next 5 attacks.
    # Counter Potency: 1,200
    # Duration: 6s
    # Counter Bonus: Increases Kenki Gauge by 5
    # Kenki Gauge Cost: 25
    # related: [必杀剑·地天](Status1240), 
    id = 7855
    names = ['Hissatsu: Chiten(pvp)(SAM)', '必杀剑·地天(pvp)(SAM)']
    _orig_names = ['必杀剑·地天(pvp)', 'Hissatsu: Chiten(pvp)']
    damage = 1200
    # remain metas: {'taken_dmg_reduce': '50%，同时受到攻击时会给予对方反击伤害'}


class Action7857(Action):
    # 迅速移动到指定地点，同时对沿途目标造成物理伤害
    # 威力：1600
    # 发动条件：剑气25点
    # 止步状态下无法发动
    # Move quickly to the specified location, delivering an attack with a potency of 1,600 to all enemies in your path.
    # Kenki Gauge Cost: 25
    # Cannot be executed while bound.
    id = 7857
    names = ['Hissatsu: Soten(pvp)(SAM)', '必杀剑·早天(pvp)(SAM)']
    _orig_names = ['Hissatsu: Soten(pvp)', '必杀剑·早天(pvp)']
    damage = 1600


class Action7867(Action):
    # 根据闪的数量发动居合术
    # 1闪：彼岸花
    # 2闪：天下五剑
    # 3闪：纷乱雪月花
    # Executes a weaponskill depending on current number of Sen stored in Sen Gauge.
    # 1 Sen: Higanbana
    # 2 Sen: Tenka Goken
    # 3 Sen: Midare Setsugekka
    id = 7867
    names = ['居合术(SAM)', 'Iaijutsu(SAM)']
    _orig_names = ['Iaijutsu', '居合术']


class Action8824(Action):
    # 对目标发动物理攻击
    # 威力：1400
    # 追加效果：获得15点剑气
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,400.
    # Additional Effect: Increases Kenki Gauge by 15
    # ※This action cannot be assigned to a hotbar.
    # related: [雪风(0)](Status1227), [雪风(1)](Status1318), 
    id = 8824
    names = ['雪风(pvp)(SAM)', 'Yukikaze(pvp)(SAM)']
    _orig_names = ['Yukikaze(pvp)', '雪风(pvp)']
    damage = 1400


class Action8825(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：雪风
    # 连击成功：获得10点剑气
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Yukikaze
    # Combo Potency: 1,600
    # Combo Bonus: Increases Kenki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8825
    names = ['Gekko(pvp)(SAM)', '月光(pvp)(SAM)']
    _orig_names = ['Gekko(pvp)', '月光(pvp)']
    combo_action = 8824
    combo_damage = 1600


class Action8826(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：月光
    # 连击成功：获得10点剑气
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Gekko
    # Combo Potency: 1,600
    # Combo Bonus: Increases Kenki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8826
    names = ['花车(pvp)(SAM)', 'Kasha(pvp)(SAM)']
    _orig_names = ['花车(pvp)', 'Kasha(pvp)']
    combo_action = 8825
    combo_damage = 1600


class Action8827(Action):
    # 对目标发动远距离物理攻击
    # 威力：1200
    # 追加效果：获得10点剑气
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Increases Kenki Gauge by 10
    id = 8827
    names = ['燕飞(pvp)(SAM)', 'Enpi(pvp)(SAM)']
    _orig_names = ['Enpi(pvp)', '燕飞(pvp)']
    damage = 1200


class Action8830(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1600
    # 追加效果：每命中一个目标都会获得10点剑气
    # 追加效果：剑压
    # 持续时间：永久
    # 最大档数：3档
    # 该战技有单独计算的复唱时间
    # 与纷乱雪月花共享复唱时间
    # Delivers an attack with a potency of 1,600 to all enemies in a cone before you.
    # Additional Effect: Increases Kenki Gauge by 10 for each enemy hit
    # Additional Effect: Grants a stack of Meditation
    # Can be stacked up to 3 times.
    # Shares a recast timer with Midare Setsugekka.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), 
    id = 8830
    names = ['天下五剑(pvp)(SAM)', 'Tenka Goken(pvp)(SAM)']
    _orig_names = ['天下五剑(pvp)', 'Tenka Goken(pvp)']
    damage = 1600


class Action8831(Action):
    # 对目标发动物理攻击
    # 威力：2600
    # 追加效果：获得20点剑气
    # 追加效果：剑压
    # 持续时间：永久
    # 最大档数：3档
    # 该战技有单独计算的复唱时间
    # 与天下五剑共享复唱时间
    # Delivers an attack with a potency of 2,600.
    # Additional Effect: Increases Kenki Gauge by 20
    # Additional Effect: Grants a stack of Meditation
    # Can be stacked up to 3 times.
    # Shares a recast timer with Tenka Goken.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), 
    id = 8831
    names = ['Midare Setsugekka(pvp)(SAM)', '纷乱雪月花(pvp)(SAM)']
    _orig_names = ['Midare Setsugekka(pvp)', '纷乱雪月花(pvp)']
    damage = 2600


class Action8832(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 发动条件：剑气25点
    # Delivers an attack with a potency of 1,200.
    # Kenki Gauge Cost: 25
    id = 8832
    names = ['Hissatsu: Shinten(pvp)(SAM)', '必杀剑·震天(pvp)(SAM)']
    _orig_names = ['Hissatsu: Shinten(pvp)', '必杀剑·震天(pvp)']
    damage = 1200


class Action16481(Action):
    # 对目标发动物理攻击
    # 威力：800
    # 发动条件：剑气25点
    # 与必杀剑·红莲共享复唱时间
    # Delivers an attack with a potency of 800.
    # Kenki Gauge Cost: 25
    # Shares a recast timer with Hissatsu: Guren.
    id = 16481
    names = ['Hissatsu: Senei(SAM)', '必杀剑·闪影(SAM)']
    _orig_names = ['必杀剑·闪影', 'Hissatsu: Senei']
    damage = 800


class Action16482(Action):
    # 获得50点剑气
    # (job==34?(level>=90?追加效果：奥义斩浪预备
    # 持续时间：30秒
    # :):)发动条件：自身处于战斗状态
    # Increases Kenki Gauge by 50.
    # (job==34?(level>=90?Additional Effect: Grants Ogi Namikiri Ready
    # Duration: 30s
    # :):)Can only be executed while in combat.
    id = 16482
    names = ['意气冲天(SAM)', 'Ikishoten(SAM)']
    _orig_names = ['Ikishoten', '意气冲天']


class Action16483(Action):
    # 发动上一次使用的居合术
    # 发动条件：居合术使用完毕
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间(job==34?(level>=84?
    # 积蓄次数：2:):)
    # Repeats the previously executed iaijutsu with increased potency.
    # (job==34?(level>=84?Maximum Charges: 2
    # :):)Can only be executed immediately following Iaijutsu.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    id = 16483
    names = ['燕回返(SAM)', 'Tsubame-gaeshi(SAM)']
    _orig_names = ['Tsubame-gaeshi', '燕回返']


class Action16484(Action):
    # 对目标发动物理攻击
    # 威力：300
    # 追加效果：持续伤害
    # 威力：45
    # 持续时间：60秒
    # 无法与彼岸花的持续伤害叠加
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 300.
    # Additional Effect: Damage over time
    # Potency: 45
    # Duration: 60s
    # Effect cannot be stacked with Higanbana.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # ※This action cannot be assigned to a hotbar.
    id = 16484
    names = ['Kaeshi: Higanbana(SAM)', '回返彼岸花(SAM)']
    _orig_names = ['回返彼岸花', 'Kaeshi: Higanbana']
    damage = 300
    # remain metas: {'dmg_ot': '45'}


class Action16485(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：420
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 420 to all enemies in a cone before you.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # ※This action cannot be assigned to a hotbar.
    id = 16485
    names = ['Kaeshi: Goken(SAM)', '回返五剑(SAM)']
    _orig_names = ['Kaeshi: Goken', '回返五剑']
    damage = 420


class Action16486(Action):
    # 对目标发动物理攻击
    # 威力：990
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 990.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # ※This action cannot be assigned to a hotbar.
    id = 16486
    names = ['回返雪月花(SAM)', 'Kaeshi: Setsugekka(SAM)']
    _orig_names = ['Kaeshi: Setsugekka', '回返雪月花']
    damage = 990


class Action16487(Action):
    # 对目标发动物理攻击
    # 威力：580
    # 发动时会消耗全部的剑压
    # 发动条件：剑压3档
    # 自身处于战斗状态时使用默想、居合术(job==34?(level>=90?、奥义斩浪:):)技能，可以获得剑压
    # 最大档数：3档
    # 持续时间：永久(job==34?(level>=82?
    # 与无明照破共享复唱时间:):)
    # Delivers an attack with a potency of 580.
    # Can only be executed after accumulating three stacks of Meditation by executing Iaijutsu, (job==34?(level>=90?Meditate, or Ogi Namikiri:or Meditate):or Meditate) while in combat.
    # Meditation effect fades upon execution.(job==34?(level>=82?
    # Shares a recast timer with Shoha II.:):)
    id = 16487
    names = ['照破(SAM)', 'Shoha(SAM)']
    _orig_names = ['Shoha', '照破']
    damage = 580


class Action17740(Action):
    # 发动上一次使用的居合术
    # 发动条件：纷乱雪月花或天下五剑使用完毕
    # 该战技有单独计算的复唱时间
    # 积蓄次数：2
    # Repeats the previously executed iaijutsu.
    # Can only be executed immediately following Midare Setsugekka or Tenka Goken.
    # This weaponskill does not share a recast timer with any other actions.
    # Maximum Charges: 2
    id = 17740
    names = ['Tsubame-gaeshi(pvp)(SAM)', '燕回返(pvp)(SAM)']
    _orig_names = ['Tsubame-gaeshi(pvp)', '燕回返(pvp)']


class Action17742(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1600
    # 追加效果：每命中一个目标都会获得10点剑气
    # 追加效果：剑压
    # 持续时间：永久
    # 最大档数：3档
    # 发动条件：天下五剑使用完毕
    # 该战技有单独计算的复唱时间
    # 积蓄次数：2
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,600 to all enemies in a cone before you.
    # Additional Effect: Increases Kenki Gauge by 10 for each enemy hit
    # Additional Effect: Grants Meditation
    # Can be stacked up to 3 times.
    # Maximum Charges: 2
    # Can only be executed following Tenka Goken.
    # This weaponskill does not share a recast timer with any other actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), 
    id = 17742
    names = ['Kaeshi: Goken(pvp)(SAM)', '回返五剑(pvp)(SAM)']
    _orig_names = ['Kaeshi: Goken(pvp)', '回返五剑(pvp)']
    damage = 1600


class Action17743(Action):
    # 对目标发动物理攻击
    # 威力：2600
    # 追加效果：获得20点剑气
    # 追加效果：剑压
    # 持续时间：永久
    # 最大档数：3档
    # 发动条件：纷乱雪月花使用完毕
    # 该战技有单独计算的复唱时间
    # 积蓄次数：2
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 2,600.
    # Additional Effect: Increases Kenki Gauge by 20
    # Additional Effect: Grants Meditation
    # Can be stacked up to 3 times.
    # Maximum Charges: 2
    # Can only be executed following Midare Setsugekka.
    # This weaponskill does not share a recast timer with any other actions.
    # ※This action cannot be assigned to a hotbar.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), 
    id = 17743
    names = ['Kaeshi: Setsugekka(pvp)(SAM)', '回返雪月花(pvp)(SAM)']
    _orig_names = ['回返雪月花(pvp)', 'Kaeshi: Setsugekka(pvp)']
    damage = 2600


class Action18926(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：1000
    # 追加效果：获得10点剑气
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Increases Kenki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 18926
    names = ['Mangetsu(pvp)(SAM)', '满月(pvp)(SAM)']
    _orig_names = ['Mangetsu(pvp)', '满月(pvp)']
    damage = 1000


class Action18927(Action):
    # 对自身周围的敌人发动物理攻击
    # 连击中威力：1000
    # 连击条件：满月
    # 连击成功：获得10点剑气
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Mangetsu
    # Combo Potency: 1,000
    # Combo Bonus: Increases Kenki Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 18927
    names = ['樱花(pvp)(SAM)', 'Oka(pvp)(SAM)']
    _orig_names = ['樱花(pvp)', 'Oka(pvp)']
    combo_action = 18926
    combo_damage = 1000


class Action18929(Action):
    # 对目标发动物理攻击
    # 该技能威力随自身剑压的档数而变化
    # 1档时威力：800
    # 2档时威力：1600
    # 3档时威力：2400
    # 发动时会消耗全部的剑压
    # 发动条件：剑压1档以上
    # Delivers an attack whose potency increases based on your accumulated Meditation.
    # Meditation 1 Potency: 800
    # Meditation 2 Potency: 1,600
    # Meditation 3 Potency: 2,400
    # Meditation effect fades upon execution.
    id = 18929
    names = ['Shoha(pvp)(SAM)', '照破(pvp)(SAM)']
    _orig_names = ['照破(pvp)', 'Shoha(pvp)']
    damage = 1600 # TODO: [1600, 800, 2400]


class Action18988(Action):
    # 对自身周围的敌人发动物理攻击
    # 威力：800
    # 发动条件：剑气25点
    # Delivers an attack with a potency of 800 to all nearby enemies.
    # Kenki Gauge Cost: 25
    id = 18988
    names = ['必杀剑·九天(pvp)(SAM)', 'Hissatsu: Kyuten(pvp)(SAM)']
    _orig_names = ['必杀剑·九天(pvp)', 'Hissatsu: Kyuten(pvp)']
    damage = 800


class Action25779(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：200
    # 发动时会消耗全部的剑压
    # 发动条件：剑压3档
    # 自身处于战斗状态时使用默想、居合术(job==34?(level>=90?、奥义斩浪:):)技能，可以获得剑压
    # 最大档数：3档
    # 持续时间：永久
    # 与照破共享复唱时间
    # Delivers an attack with a potency of 200 to all nearby enemies.
    # Can only be executed after accumulating three stacks of Meditation by executing Iaijutsu, (job==34?(level>=90?Meditate, or Ogi Namikiri:or Meditate):or Meditate) while in combat.
    # Meditation effect fades upon execution.
    # Shares a recast timer with Shoha.
    id = 25779
    names = ['无明照破(SAM)', 'Shoha II(SAM)']
    _orig_names = ['无明照破', 'Shoha II']
    damage = 200


class Action25780(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：100
    # 追加效果：获得10点剑气
    # Delivers an attack with a potency of 100 to all nearby enemies.
    # Additional Effect: Increases Kenki Gauge by 10
    id = 25780
    names = ['风光(SAM)', 'Fuko(SAM)']
    _orig_names = ['风光', 'Fuko']
    damage = 100


class Action25781(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：900
    # 攻击复数敌人时，对目标之外的敌人威力降低75%
    # 追加效果：为自身附加1档剑压
    # 最大档数：3档
    # 持续时间：永久
    # 发动条件：奥义斩浪预备状态中
    # 该技能发动后变为回返斩浪
    # Delivers an attack to all enemies in a cone before you with a potency of 900 for the first enemy, and 75% less for all remaining enemies.
    # Grants a stack of Meditation, up to a maximum of 3.
    # Can only be executed while under the effect of Ogi Namikiri Ready.
    # ※Action changes to Kaeshi: Namikiri upon execution.
    # related: [剑压(0)](Status2176), [剑压(1)](Status1865), [奥义斩浪预备](Status2959), 
    id = 25781
    names = ['奥义斩浪(SAM)', 'Ogi Namikiri(SAM)']
    _orig_names = ['Ogi Namikiri', '奥义斩浪']
    damage = 900
    # remain metas: {'aoe_reduce': '75%'}


class Action25782(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1350
    # 攻击复数敌人时，对目标之外的敌人威力降低75%
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack to all enemies in a cone before you with a potency of 1,350 for the first enemy, and 75% less for all remaining enemies.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # ※This action cannot be assigned to a hotbar.
    id = 25782
    names = ['回返斩浪(SAM)', 'Kaeshi: Namikiri(SAM)']
    _orig_names = ['回返斩浪', 'Kaeshi: Namikiri']
    damage = 1350
    # remain metas: {'aoe_reduce': '75%'}


