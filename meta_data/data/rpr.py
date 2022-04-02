from ._base import *


class Status2586(Status):
    # 受到附加此状态的玩家攻击时所受伤害增加
    # 效果时间内被打倒时，附加此状态的钐镰客的灵魂量值上升
    # Damage taken from the reaper who applied this effect is increased. Increases said reaper's Soul Gauge if defeated before effect expires.
    # related: [死亡之影(RPR)](Action24378), [死亡之涡(RPR)](Action24379),
    id = 2586
    names = ['死亡烙印', "Death's Design"]


class Status2854(Status):
    # 可以发动绞决或缢杀或断首
    # Able to execute Gibbet, Gallows, and Guillotine.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [断首(RPR)](Action24384), [隐匿挥割(RPR)](Action24389), [绞决爪(RPR)](Action24390), [缢杀爪(RPR)](Action24391), [束缚挥割(RPR)](Action24392), [暴食(RPR)](Action24393), [隐匿挥割(pvp)(RPR)](Action27810), [绞决爪(pvp)(RPR)](Action27811), [缢杀爪(pvp)(RPR)](Action27812), [束缚挥割(pvp)(RPR)](Action27813), [暴食(pvp)(RPR)](Action27814),
    id = 2854
    names = ['妖异之镰(pvp)', 'Soul Reaver(pvp)']


class Status2855(Status):
    # 下次发动绞决的威力提高
    # Next Gibbet will deal increased damage.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [绞决(pvp)(RPR)](Action27798), [缢杀(pvp)(RPR)](Action27799),
    id = 2855
    names = ['绞决效果提高(pvp)', 'Enhanced Gibbet(pvp)']


class Status2856(Status):
    # 下次发动缢杀的威力提高
    # Next Gallows will deal increased damage.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [绞决(pvp)(RPR)](Action27798), [缢杀(pvp)(RPR)](Action27799),
    id = 2856
    names = ['缢杀效果提高(pvp)', 'Enhanced Gallows(pvp)']


class Status2587(Status):
    # 可以发动绞决或缢杀或断首
    # Able to execute Gibbet, Gallows, and Guillotine.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [断首(RPR)](Action24384), [隐匿挥割(RPR)](Action24389), [绞决爪(RPR)](Action24390), [缢杀爪(RPR)](Action24391), [束缚挥割(RPR)](Action24392), [暴食(RPR)](Action24393), [隐匿挥割(pvp)(RPR)](Action27810), [绞决爪(pvp)(RPR)](Action27811), [缢杀爪(pvp)(RPR)](Action27812), [束缚挥割(pvp)(RPR)](Action27813), [暴食(pvp)(RPR)](Action27814),
    id = 2587
    names = ['妖异之镰', 'Soul Reaver']


class Status2588(Status):
    # 下次发动绞决的威力提高
    # Next Gibbet will deal increased damage.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [绞决(pvp)(RPR)](Action27798), [缢杀(pvp)(RPR)](Action27799),
    id = 2588
    names = ['绞决效果提高', 'Enhanced Gibbet']


class Status2589(Status):
    # 下次发动缢杀的威力提高
    # Next Gallows will deal increased damage.
    # related: [绞决(RPR)](Action24382), [缢杀(RPR)](Action24383), [绞决(pvp)(RPR)](Action27798), [缢杀(pvp)(RPR)](Action27799),
    id = 2589
    names = ['缢杀效果提高', 'Enhanced Gallows']


class Status2972(Status):
    # 从受到自身祭祀环影响的目标身上获得死亡祭品
    # Able to gain stacks of Immortal Sacrifice from party members under the effect of your Circle of Sacrifice.
    # related: [大丰收(RPR)](Action24385),
    id = 2972
    names = ['死亡祭祀', 'Bloodsown Circle']


class Status2592(Status):
    # 从可以发动大丰收
    #
    # related: [大丰收(RPR)](Action24385),
    id = 2592
    names = ['死亡祭品', 'Immortal Sacrifice']


class Status2594(Status):
    # 可以发动收获月
    # Able to execute Harvest Moon.
    # related: [播魂种(RPR)](Action24387),
    id = 2594
    names = ['播魂种', 'Soulsow']


class Status2593(Status):
    # 化身附体
    # Playing host to an avatar.
    # related: [夜游魂衣(RPR)](Action24394), [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [阴冷收割(RPR)](Action24397), [团契(RPR)](Action24398), [团契(pvp)(RPR)](Action27807), [夜游魂衣(pvp)(RPR)](Action27821),
    id = 2593
    names = ['夜游魂', 'Enshrouded']


class Status2863(Status):
    # 化身附体
    # Playing host to an avatar.
    # related: [夜游魂衣(RPR)](Action24394), [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [阴冷收割(RPR)](Action24397), [团契(RPR)](Action24398), [团契(pvp)(RPR)](Action27807), [夜游魂衣(pvp)(RPR)](Action27821),
    id = 2863
    names = ['夜游魂(1)', 'Enshrouded(1)']


class Status2857(Status):
    # 下次发动虚无收割的威力提高
    # Next Void Reaping will deal increased damage.
    # related: [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [虚无收割(pvp)(RPR)](Action27800), [交错收割(pvp)(RPR)](Action27801),
    id = 2857
    names = ['虚无收割效果提高(0)', 'Enhanced Void Reaping(0)']


class Status2858(Status):
    # 下次发动交错收割的威力提高
    # Next Cross Reaping will deal increased damage.
    # related: [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [虚无收割(pvp)(RPR)](Action27800), [交错收割(pvp)(RPR)](Action27801),
    id = 2858
    names = ['交错收割效果提高(0)', 'Enhanced Cross Reaping(0)']


class Status2590(Status):
    # 下次发动虚无收割的威力提高
    # Next Void Reaping will deal increased damage.
    # related: [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [虚无收割(pvp)(RPR)](Action27800), [交错收割(pvp)(RPR)](Action27801),
    id = 2590
    names = ['虚无收割效果提高', 'Enhanced Void Reaping(1)']


class Status2591(Status):
    # 下次发动交错收割的威力提高
    # Next Cross Reaping will deal increased damage.
    # related: [虚无收割(RPR)](Action24395), [交错收割(RPR)](Action24396), [虚无收割(pvp)(RPR)](Action27800), [交错收割(pvp)(RPR)](Action27801),
    id = 2591
    names = ['交错收割效果提高', 'Enhanced Cross Reaping']


class Status2595(Status):
    # 可以发动回退
    # Able to execute Regress.
    # related: [地狱入境(RPR)](Action24401), [地狱出境(RPR)](Action24402), [地狱入境(pvp)(RPR)](Action27817), [地狱出境(pvp)(RPR)](Action27818),
    id = 2595
    names = ['回退预备', 'Threshold']


class Status2860(Status):
    # 可以发动回退
    # Able to execute Regress.
    # related: [地狱入境(RPR)](Action24401), [地狱出境(RPR)](Action24402), [地狱入境(pvp)(RPR)](Action27817), [地狱出境(pvp)(RPR)](Action27818),
    id = 2860
    names = ['回退预备(pvp)', 'Threshold(pvp)']


class Status2599(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [神秘环(RPR)](Action24405),
    id = 2599
    names = ['神秘环', 'Arcane Circle']


class Status2862(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [神秘纹(pvp)(RPR)](Action27820),
    id = 2862
    names = ['活性纹(0)', 'Crest of Time Returned(0)']


class Status2598(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [神秘纹(pvp)(RPR)](Action27820),
    id = 2598
    names = ['活性纹(1)', 'Crest of Time Returned(1)']


class Status2845(Status):
    # 下次发动勾刃不需要咏唱时间
    # Next Harpe will require no time to cast.
    # related:
    id = 2845
    names = ['勾刃效果提高', 'Enhanced Harpe']


class Status2859(Status):
    # 下次发动勾刃不需要咏唱时间
    # Next Harpe will require no time to cast.
    # related:
    id = 2859
    names = ['勾刃效果提高(pvp)', 'Enhanced Harpe(pvp)']


class Action24373(Action):
    # 对目标发动物理攻击
    # 威力：(job==39?(level>=60?300:260):260)(job==39?(level>=50?
    # 追加效果：获得10点灵魂:):)
    # Delivers an attack with a potency of (job==39?(level>=60?300:260):260).(job==39?(level>=50?
    # Additional Effect: Increases Soul Gauge by 10:):)
    id = 24373
    names = ['Slice(RPR)', '切割(RPR)']
    _orig_names = ['Slice', '切割']
    damage = "(job==39?(lv>=60?300:260):260)"


class Action24374(Action):
    # 对目标发动物理攻击
    # 威力：(job==39?(level>=60?140:100):100)
    # 连击条件：切割
    # 连击中威力：(job==39?(level>=60?380:340):340)(job==39?(level>=50?
    # 连击成功：获得10点灵魂:):)
    # Delivers an attack with a potency of (job==39?(level>=60?140:100):100).
    # Combo Action: Slice
    # Combo Potency: (job==39?(level>=60?380:340):340)(job==39?(level>=50?
    # Combo Bonus: Increases Soul Gauge by 10:):)
    id = 24374
    names = ['Waxing Slice(RPR)', '增盈切割(RPR)']
    _orig_names = ['Waxing Slice', '增盈切割']
    combo_action = 24373
    damage = "(job==39?(lv>=60?140:100):100)"
    combo_damage = "(job==39?(lv>=60?380:340):340)"


class Action24375(Action):
    # 对目标发动物理攻击
    # 威力：(job==39?(level>=60?140:100):100)
    # 连击条件：增盈切割
    # 连击中威力：(job==39?(level>=60?460:420):420)(job==39?(level>=50?
    # 连击成功：获得10点灵魂:):)
    # Delivers an attack with a potency of (job==39?(level>=60?140:100):100).
    # Combo Action: Waxing Slice
    # Combo Potency: (job==39?(level>=60?460:420):420)(job==39?(level>=50?
    # Combo Bonus: Increases Soul Gauge by 10:):)
    id = 24375
    names = ['Infernal Slice(RPR)', '地狱切割(RPR)']
    _orig_names = ['Infernal Slice', '地狱切割']
    combo_action = 24374
    damage = "(job==39?(lv>=60?140:100):100)"
    combo_damage = "(job==39?(lv>=60?460:420):420)"


class Action24376(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：(job==39?(level>=60?140:120):120)(job==39?(level>=50?
    # 追加效果：获得10点灵魂:):)
    # Delivers an attack with a potency of (job==39?(level>=60?140:120):120) to all nearby enemies.(job==39?(level>=50?
    # Additional Effect: Increases Soul Gauge by 10:):)
    id = 24376
    names = ['旋转钐割(RPR)', 'Spinning Scythe(RPR)']
    _orig_names = ['旋转钐割', 'Spinning Scythe']
    damage = "(job==39?(lv>=60?140:120):120)"


class Action24377(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：(job==39?(level>=60?120:100):100)
    # 连击条件：旋转钐割
    # 连击中威力：(job==39?(level>=60?180:160):160)(job==39?(level>=50?
    # 连击成功：获得10点灵魂:):)
    # Delivers an attack with a potency of (job==39?(level>=60?120:100):100) to all nearby enemies.
    # Combo Action: Spinning Scythe
    # Combo Potency: (job==39?(level>=60?180:160):160)(job==39?(level>=50?
    # Combo Bonus: Increases Soul Gauge by 10:):)
    id = 24377
    names = ['噩梦钐割(RPR)', 'Nightmare Scythe(RPR)']
    _orig_names = ['噩梦钐割', 'Nightmare Scythe']
    combo_action = 24376
    damage = "(job==39?(lv>=60?120:100):100)"
    combo_damage = "(job==39?(lv>=60?180:160):160)"


class Action24378(Action):
    # 对目标发动物理攻击
    # 威力：(job==39?(level>=60?300:240):240)
    # 追加效果：为目标附加死亡烙印状态
    # 持续时间：30秒
    # 死亡烙印效果：自身对目标造成的伤害提高10%
    # (job==39?(level>=50?持续时间内目标被打倒时，获得10点灵魂
    # :):)若已经附加死亡烙印状态，则持续时间延长30秒
    # 最多可延长至60秒
    # Delivers an attack with a potency of (job==39?(level>=60?300:240):240).
    # Additional Effect: Afflicts target with Death's Design, increasing damage you deal target by 10%
    # Duration: 30s
    # Extends duration of Death's Design by 30s to a maximum of 60s.(job==39?(level>=50?
    # Additional Effect: Increases Soul Gauge by 10 if target is KO'd before effect expires:):)
    # related: [死亡烙印](Status2586),
    id = 24378
    names = ['Shadow of Death(RPR)', '死亡之影(RPR)']
    _orig_names = ['死亡之影', 'Shadow of Death']
    damage = "(job==39?(lv>=60?300:240):240)"
    # remain metas: {'dmg_increase': '10%'}


class Action24379(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：(job==39?(level>=60?100:80):80)
    # 追加效果：为目标附加死亡烙印状态
    # 持续时间：30秒
    # 死亡烙印效果：自身对目标造成的伤害提高10%
    # (job==39?(level>=50?持续时间内目标被打倒时，获得10点灵魂
    # :):)若已经附加死亡烙印状态，则持续时间延长30秒
    # 最多可延长至60秒
    # Delivers an attack with a potency of (job==39?(level>=60?100:80):80) to all nearby enemies.
    # Additional Effect: Afflicts target with Death's Design, increasing damage you deal target by 10%
    # Duration: 30s
    # Extends duration of Death's Design by 30s to a maximum of 60s.(job==39?(level>=50?
    # Additional Effect: Increases Soul Gauge by 10 if target is KO'd before effect expires:):)
    # related: [死亡烙印](Status2586),
    id = 24379
    names = ['死亡之涡(RPR)', 'Whorl of Death(RPR)']
    _orig_names = ['Whorl of Death', '死亡之涡']
    damage = "(job==39?(lv>=60?100:80):80)"
    # remain metas: {'dmg_increase': '10%'}


class Action24380(Action):
    # 对目标发动物理攻击
    # 威力：460
    # 追加效果：获得50点灵魂
    # (job==39?(level>=78?积蓄次数：2
    # :):)该战技不仅有单独计算的复唱时间，还会与灵魂钐割共享复唱时间
    # Delivers an attack with a potency of 460.
    # Additional Effect: Increases Soul Gauge by 50
    # (job==39?(level>=78?Maximum Charges: 2
    # :):)Shares a recast timer with Soul Scythe.
    id = 24380
    names = ['Soul Slice(RPR)', '灵魂切割(RPR)']
    _orig_names = ['Soul Slice', '灵魂切割']
    damage = 460


class Action24381(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：180
    # 追加效果：获得50点灵魂
    # (job==39?(level>=78?积蓄次数：2
    # :):)该战技不仅有单独计算的复唱时间，还会与灵魂切割共享复唱时间
    # Delivers an attack with a potency of 180 to all nearby enemies.
    # Additional Effect: Increases Soul Gauge by 50
    # (job==39?(level>=78?Maximum Charges: 2
    # :):)Shares a recast timer with Soul Slice.
    id = 24381
    names = ['Soul Scythe(RPR)', '灵魂钐割(RPR)']
    _orig_names = ['Soul Scythe', '灵魂钐割']
    damage = 180


class Action24382(Action):
    # 对目标发动物理攻击
    # 威力：400
    # 绞决效果提高中威力：460
    # 侧面攻击威力：460
    # 绞决效果提高中侧面攻击威力：520
    # 追加效果：缢杀效果提高
    # 持续时间：60秒
    # 持续时间内隐匿挥割变为缢杀爪
    # (job==39?(level>=80?追加效果：获得10点魂衣
    # :):)发动条件：妖异之镰
    # Delivers an attack with a potency of 400.
    # 460 when executed from a target's flank.
    # Enhanced Gibbet Potency: 460
    # Flank Enhanced Potency: 520
    # Additional Effect: Grants Enhanced Gallows
    # Duration: 60s
    # The action Blood Stalk changes to Unveiled Gallows while under the effect of Enhanced Gallows.
    # (job==39?(level>=80?Additional Effect: Increases Shroud Gauge by 10
    # :):)Can only be executed while under the effect of Soul Reaver.(job==39?(level>=80?
    # ※Action changes to Void Reaping while under the effect of Enshrouded.:):)
    # related: [妖异之镰(0)](Status2854), [绞决效果提高(0)](Status2855), [缢杀效果提高(0)](Status2856), [妖异之镰(1)](Status2587), [绞决效果提高(1)](Status2588), [缢杀效果提高(1)](Status2589),
    id = 24382
    names = ['Gibbet(RPR)', '绞决(RPR)']
    _orig_names = ['绞决', 'Gibbet']
    damage = "(绞决效果提高?460:400)"
    side_damage = "(绞决效果提高?520:460)"


class Action24383(Action):
    # 对目标发动物理攻击
    # 威力：400
    # 缢杀效果提高中威力：460
    # 背面攻击威力：460
    # 缢杀效果提高中背面攻击威力：520
    # 追加效果：绞决效果提高
    # 持续时间：60秒
    # 持续时间内隐匿挥割变为绞决爪
    # (job==39?(level>=80?追加效果：获得10点魂衣
    # :):)发动条件：妖异之镰
    # Delivers an attack with a potency of 400.
    # 460 when executed from a target's rear.
    # Enhanced Gallows Potency: 460
    # Rear Enhanced Potency: 520
    # Additional Effect: Grants Enhanced Gibbet
    # Duration: 60s
    # The action Blood Stalk changes to Unveiled Gibbet while under the effect of Enhanced Gibbet.
    # (job==39?(level>=80?Additional Effect: Increases Shroud Gauge by 10
    # :):)Can only be executed while under the effect of Soul Reaver.(job==39?(level>=80?
    # ※Action changes to Cross Reaping while under the effect of Enshrouded.:):)
    # related: [妖异之镰(0)](Status2854), [绞决效果提高(0)](Status2855), [缢杀效果提高(0)](Status2856), [妖异之镰(1)](Status2587), [绞决效果提高(1)](Status2588), [缢杀效果提高(1)](Status2589),
    id = 24383
    names = ['Gallows(RPR)', '缢杀(RPR)']
    _orig_names = ['Gallows', '缢杀']
    damage = "(缢杀效果提高?460:400)"
    back_damage = "(缢杀效果提高?520:460)"


class Action24384(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：200
    # (job==39?(level>=80?追加效果：获得10点魂衣
    # :):)发动条件：妖异之镰
    # Delivers an attack with a potency of 200 to all enemies in a cone before you.
    # (job==39?(level>=80?Additional Effect: Increases Shroud Gauge by 10
    # :):)Can only be executed while under the effect of Soul Reaver.(job==39?(level>=80?
    # ※Action changes to Grim Reaping while under the effect of Enshrouded.:):)
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24384
    names = ['断首(RPR)', 'Guillotine(RPR)']
    _orig_names = ['断首', 'Guillotine']
    damage = 200


class Action24385(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 自身附加的死亡祭品档数越高，威力越大
    # 威力：520～800
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动大丰收时会消耗全部的死亡祭品
    # 追加效果：获得50点魂衣
    # 发动条件：非死亡祭祀状态中且死亡祭品1档以上
    # Delivers an attack to all enemies in a straight line before you with a potency of 520 for the first enemy, and 60% less for all remaining enemies.
    # Immortal Sacrifice Cost: 1 stack
    # Potency increases up to 800 as stacks of Immortal Sacrifice exceed minimum cost.
    # Additional Effect: Increases Shroud Gauge by 50
    # Cannot be executed while under the effect of Bloodsown Circle.
    # Consumes all stacks of Immortal Sacrifice upon execution.
    # related: [死亡祭祀](Status2972),
    id = 24385
    names = ['Plentiful Harvest(RPR)', '大丰收(RPR)']
    _orig_names = ['大丰收', 'Plentiful Harvest']
    damage = [520, 800]
    # remain metas: {'aoe_reduce': '60%'}


class Action24386(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==39?(level>=60?300:200):200)
    # Deals unaspected damage with a potency of (job==39?(level>=60?300:200):200).
    id = 24386
    names = ['Harpe(RPR)', '勾刃(RPR)']
    _orig_names = ['Harpe', '勾刃']
    damage = "(job==39?(lv>=60?300:200):200)"


class Action24387(Action):
    # 为自身附加播魂种状态，该技能变为收获月
    # 持续时间：永久
    # 非战斗状态下发动该技能不需要咏唱时间
    # Grants Soulsow to self, changing the action to Harvest Moon.
    # Cast time is instant when used outside of battle.
    # related: [播魂种](Status2594),
    id = 24387
    names = ['Soulsow(RPR)', '播魂种(RPR)']
    _orig_names = ['播魂种', 'Soulsow']


class Action24388(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 发动条件：播魂种
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to target and all enemies nearby it with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
    # Can only be executed while under the effect of Soulsow.
    # ※This action cannot be assigned to a hotbar.
    id = 24388
    names = ['收获月(RPR)', 'Harvest Moon(RPR)']
    _orig_names = ['Harvest Moon', '收获月']
    damage = 600
    # remain metas: {'aoe_reduce': '50%'}


class Action24389(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：340
    # (job==39?(level>=70?追加效果：为自身附加1档妖异之镰状态
    # 持续时间：30秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # :):)发动条件：灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # Summons your avatar to deliver an attack with a potency of 340.
    # (job==39?(level>=70?Additional Effect: Grants Soul Reaver
    # Duration: 30s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # :):)Soul Gauge Cost: 50
    # Shares a recast timer with all avatar attacks except Gluttony.(job==39?(level>=86?
    # ※Action changes to Lemure's Slice while under the effect of Enshrouded.:):)
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24389
    names = ['隐匿挥割(RPR)', 'Blood Stalk(RPR)']
    _orig_names = ['隐匿挥割', 'Blood Stalk']
    damage = 340


class Action24390(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：400
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：30秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：绞决效果提高状态中且灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # ※该技能无法设置到热键栏
    # Summons your avatar to deliver an attack with a potency of 400.
    # Additional Effect: Grants Soul Reaver
    # Duration: 30s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Can only be executed while under the effect of Enhanced Gibbet.
    # Shares a recast timer with all avatar attacks except Gluttony.
    # ※This action cannot be assigned to a hotbar.
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24390
    names = ['Unveiled Gibbet(RPR)', '绞决爪(RPR)']
    _orig_names = ['绞决爪', 'Unveiled Gibbet']
    damage = 400


class Action24391(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：400
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：30秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：缢杀效果提高状态中且灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # ※该技能无法设置到热键栏
    # Summons your avatar to deliver an attack with a potency of 400.
    # Additional Effect: Grants Soul Reaver
    # Duration: 30s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Can only be executed while under the effect of Enhanced Gallows.
    # Shares a recast timer with all avatar attacks except Gluttony.
    # ※This action cannot be assigned to a hotbar.
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24391
    names = ['缢杀爪(RPR)', 'Unveiled Gallows(RPR)']
    _orig_names = ['缢杀爪', 'Unveiled Gallows']
    damage = 400


class Action24392(Action):
    # 召唤化身对目标所在方向发出扇形范围物理攻击
    # 威力：140
    # (job==39?(level>=70?追加效果：为自身附加1档妖异之镰状态
    # 持续时间：30秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # :):)发动条件：灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # Summons your avatar to deliver an attack with a potency of 140 to all enemies in a cone before you.
    # (job==39?(level>=70?Additional Effect: Grants Soul Reaver
    # Duration: 30s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # :):)Soul Gauge Cost: 50
    # Shares a recast timer with all avatar attacks except Gluttony.(job==39?(level>=86?
    # ※Action changes to Lemure's Scythe while under the effect of Enshrouded.:):)
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24392
    names = ['Grim Swathe(RPR)', '束缚挥割(RPR)']
    _orig_names = ['束缚挥割', 'Grim Swathe']
    damage = 140


class Action24393(Action):
    # 召唤化身对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：500
    # 攻击复数敌人时，对目标之外的敌人威力降低25%
    # 追加效果：为自身附加2档妖异之镰
    # 持续时间：30秒
    # 发动条件：灵魂50点
    # Summons your avatar to deal unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 25% less for all remaining enemies.
    # Additional Effect: Grants 2 stacks of Soul Reaver
    # Duration: 30s
    # Soul Gauge Cost: 50
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 24393
    names = ['暴食(RPR)', 'Gluttony(RPR)']
    _orig_names = ['暴食', 'Gluttony']
    damage = 500
    # remain metas: {'aoe_reduce': '25%'}


class Action24394(Action):
    # 召唤化身附体并为自身附加最大档数的夜游魂状态
    # 持续时间：30秒
    # 化身附体状态中无法发动召唤化身技能及部分战技
    # 发动条件：魂衣50点
    # Offers your flesh as a vessel to your avatar, gaining maximum stacks of Lemure Shroud.
    # Duration: 30s
    # Certain actions cannot be executed while playing host to your avatar.
    # Shroud Gauge Cost: 50
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863),
    id = 24394
    names = ['夜游魂衣(RPR)', 'Enshroud(RPR)']
    _orig_names = ['Enshroud', '夜游魂衣']


class Action24395(Action):
    # 对目标发动物理攻击
    # 威力：460
    # 虚无收割效果提高中威力：520
    # 追加效果：交错收割效果提高
    # 持续时间：30秒
    # (job==39?(level>=86?追加效果：虚无魂
    # :):)发动条件：夜游魂
    # 该战技有单独计算的复唱时间，不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 460.
    # Enhanced Void Reaping Potency: 520
    # Additional Effect: Grants Enhanced Cross Reaping
    # Duration: 30s
    # (job==39?(level>=86?Additional Effect: Grants Void Shroud
    # :):)Can only be executed while under the effect of Enshrouded.
    # Recast timer cannot be affected by status effects or gear attributes.
    # Lemure Shroud Cost: 1
    # ※This action cannot be assigned to a hotbar.
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863), [虚无收割效果提高(0)](Status2857), [交错收割效果提高(0)](Status2858), [虚无收割效果提高(1)](Status2590), [交错收割效果提高(1)](Status2591),
    id = 24395
    names = ['Void Reaping(RPR)', '虚无收割(RPR)']
    _orig_names = ['Void Reaping', '虚无收割']
    damage = "(虚无收割效果提高?520:460)"


class Action24396(Action):
    # 对目标发动物理攻击
    # 威力：460
    # 交错收割效果提高中威力：520
    # 追加效果：虚无收割效果提高
    # 持续时间：30秒
    # (job==39?(level>=86?追加效果：虚无魂
    # :):)发动条件：夜游魂
    # 该战技有单独计算的复唱时间，不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 460.
    # Enhanced Cross Reaping Potency: 520
    # Additional Effect: Grants Enhanced Void Reaping
    # Duration: 30s
    # (job==39?(level>=86?Additional Effect: Grants Void Shroud
    # :):)Can only be executed while under the effect of Lemure Shroud.
    # Recast timer cannot be affected by status effects or gear attributes.
    # Lemure Shroud Cost: 1
    # ※This action cannot be assigned to a hotbar.
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863), [虚无收割效果提高(0)](Status2857), [交错收割效果提高(0)](Status2858), [虚无收割效果提高(1)](Status2590), [交错收割效果提高(1)](Status2591),
    id = 24396
    names = ['交错收割(RPR)', 'Cross Reaping(RPR)']
    _orig_names = ['交错收割', 'Cross Reaping']
    damage = "(交错收割效果提高?520:460)"


class Action24397(Action):
    # 对目标所在方向发出扇形范围物理攻击
    # 威力：200
    # (job==39?(level>=86?追加效果：虚无魂
    # :):)发动条件：夜游魂
    # 该战技有单独计算的复唱时间，不受装备和状态的影响
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 200 to all enemies in a cone before you.
    # (job==39?(level>=86?Additional Effect: Grants Void Shroud
    # :):)Can only be executed while under the effect of Enshrouded.
    # Recast timer cannot be affected by status effects or gear attributes.
    # Lemure Shroud Cost: 1
    # ※This action cannot be assigned to a hotbar.
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863),
    id = 24397
    names = ['Grim Reaping(RPR)', '阴冷收割(RPR)']
    _orig_names = ['Grim Reaping', '阴冷收割']
    damage = 200


class Action24398(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：1000
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动后夜游魂状态消失
    # 发动条件：夜游魂1档以上
    # Deals unaspected damage to target and all enemies nearby it with a potency of 1,000 for the first enemy, and 60% less for all remaining enemies.
    # Enshrouded effect expires upon execution.
    # Requires at least one stack of Lemure Shroud to execute.
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863),
    id = 24398
    names = ['团契(RPR)', 'Communio(RPR)']
    _orig_names = ['Communio', '团契']
    damage = 1000
    # remain metas: {'aoe_reduce': '60%'}


class Action24399(Action):
    # 对目标发动物理攻击
    # 威力：200
    # 发动条件：虚无魂2档
    # 该战技与夜游魂钐割共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 200.
    # Void Shroud Cost: 2
    # Shares a recast timer with Lemure's Scythe.
    # ※This action cannot be assigned to a hotbar.
    id = 24399
    names = ['夜游魂切割(RPR)', "Lemure's Slice(RPR)"]
    _orig_names = ["Lemure's Slice", '夜游魂切割']
    damage = 200


class Action24400(Action):
    # 对目标所在方向发出扇形范围物理攻击
    # 威力：100
    # 发动条件：虚无魂2档
    # 该战技与夜游魂切割共享复唱时间
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 100 to all enemies in a cone before you.
    # Void Shroud Cost: 2
    # Shares a recast timer with Lemure's Slice.
    # ※This action cannot be assigned to a hotbar.
    id = 24400
    names = ["Lemure's Scythe(RPR)", '夜游魂钐割(RPR)']
    _orig_names = ['夜游魂钐割', "Lemure's Scythe"]
    damage = 100


class Action24401(Action):
    # 迅速移动到自身前方15米处
    # 追加效果：下次发动勾刃不需要咏唱时间
    # 持续时间：15秒
    # (job==39?(level>=74?追加效果：在移动前的地点生成地狱之门，并为自身附加回退预备状态
    # 持续时间：10秒
    # :):)止步状态下无法发动
    # 该战技与地狱出境共享复唱时间
    # Quickly dash 15 yalms forward.
    # Additional Effect: Allows next Harpe to be cast immediately
    # Duration: 15s
    # (job==39?(level>=74?Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
    # Duration: 10s
    # :):)Cannot be executed while bound.
    # Shares a recast timer with Hell's Egress.
    # related: [回退预备(0)](Status2595), [回退预备(1)](Status2860),
    id = 24401
    names = ["Hell's Ingress(RPR)", '地狱入境(RPR)']
    _orig_names = ["Hell's Ingress", '地狱入境']


class Action24402(Action):
    # 迅速移动到自身后方15米处
    # 追加效果：下次发动勾刃不需要咏唱时间
    # 持续时间：15秒
    # (job==39?(level>=74?追加效果：在移动前的地点生成地狱之门，并为自身附加回退预备状态
    # 持续时间：10秒
    # :):)止步状态下无法发动
    # 该战技与地狱入境共享复唱时间
    # Quickly dash 15 yalms backwards.
    # Additional Effect: Allows next Harpe to be cast immediately
    # Duration: 15s
    # (job==39?(level>=74?Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
    # Duration: 10s
    # :):)Cannot be executed while bound.
    # Shares a recast timer with Hell's Ingress.
    # related: [回退预备(0)](Status2595), [回退预备(1)](Status2860),
    id = 24402
    names = ['地狱出境(RPR)', "Hell's Egress(RPR)"]
    _orig_names = ['地狱出境', "Hell's Egress"]


class Action24403(Action):
    # 快速移动到自身留下的地狱之门中心
    # 止步状态下无法发动
    # ※该技能无法设置到热键栏
    # Move instantly to the Hellsgate left behind by you.
    # Can only be executed while under the effect of Threshold.
    # Cannot be executed while bound.
    # ※This action cannot be assigned to a hotbar.
    id = 24403
    names = ['Regress(RPR)', '回退(RPR)']
    _orig_names = ['回退', 'Regress']


class Action24404(Action):
    # 为自身附加能够抵消一定伤害量的防护罩守护纹
    # 该防护罩能够抵消相当于自身最大体力10%的伤害量
    # 持续时间：5秒(job==39?(level>=84?
    # 防护罩因吸收到足够的伤害而消失时，为自身及周围15米以内的队员附加活性纹状态
    # 活性纹效果：持续恢复目标的体力
    # 恢复力：50
    # 持续时间：15秒:):)
    # Grants Crest of Time Borrowed to self, creating a barrier that nullifies damage totaling up to 10% of maximum HP.
    # Duration: 5s(job==39?(level>=84?
    # Grants Crest of Time Returned to self and nearby party members within a radius of 15 yalms when barrier is completely absorbed.
    # Crest of Time Returned Effect: Gradually restores HP
    # Cure Potency: 50
    # Duration: 15s:):)
    id = 24404
    names = ['神秘纹(RPR)', 'Arcane Crest(RPR)']
    _orig_names = ['Arcane Crest', '神秘纹']
    # remain metas: {'shield': '自身最大体力10%'}


class Action24405(Action):
    # 自身及周围队员发动攻击造成的伤害提高3%
    # 持续时间：20秒(job==39?(level>=88?
    # 追加效果：为自身及周围队员附加祭祀环状态
    # 持续时间：5秒
    # 祭祀环效果：持续时间内受自身祭祀环影响的目标发动战技或魔法攻击命中时，自身获得1档死亡祭品
    # 最大档数：8档
    # 持续时间：30秒
    # 追加效果：死亡祭祀
    # 持续时间：6秒
    # 死亡祭祀效果：从受到自身祭祀环影响的目标身上获得死亡祭品:):)
    # Increases damage dealt by self and nearby party members by 3%.
    # Duration: 20s(job==39?(level>=88?
    # Additional Effect: Grants Circle of Sacrifice to self and nearby party members
    # Duration: 5s
    # Additional Effect: Grants Bloodsown Circle to self
    # Duration: 6s
    # Circle of Sacrifice Effect: When you or party members under this effect successfully land a weaponskill or cast a spell, the reaper who applied it may be granted a stack of Immortal Sacrifice, up to a maximum of 8
    # Duration: 30s
    # Bloodsown Circle Effect: Allows you to accumulate stacks of Immortal Sacrifice from party members under the effect of your Circle of Sacrifice:):)
    # related: [神秘环](Status2599),
    id = 24405
    names = ['神秘环(RPR)', 'Arcane Circle(RPR)']
    _orig_names = ['神秘环', 'Arcane Circle']
    # remain metas: {'dmg_increase': '3%'}


class Action27795(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 追加效果：获得10点灵魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: Increases Soul Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 27795
    names = ['Slice(pvp)(RPR)', '切割(pvp)(RPR)']
    _orig_names = ['Slice(pvp)', '切割(pvp)']
    damage = 1200


class Action27796(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：切割
    # 连击成功：获得10点灵魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Slice
    # Combo Potency: 1,400
    # Combo Bonus: Increases Soul Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 27796
    names = ['增盈切割(pvp)(RPR)', 'Waxing Slice(pvp)(RPR)']
    _orig_names = ['Waxing Slice(pvp)', '增盈切割(pvp)']
    combo_action = 27795
    combo_damage = 1400


class Action27797(Action):
    # 对目标发动物理攻击
    # 连击中威力：1600
    # 连击条件：增盈切割
    # 连击成功：获得10点灵魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Waxing Slice
    # Combo Potency: 1,600
    # Combo Bonus: Increases Soul Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 27797
    names = ['地狱切割(pvp)(RPR)', 'Infernal Slice(pvp)(RPR)']
    _orig_names = ['Infernal Slice(pvp)', '地狱切割(pvp)']
    combo_action = 27796
    combo_damage = 1600


class Action27798(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 绞决效果提高中威力：2200
    # 追加效果：缢杀效果提高
    # 持续时间：30秒
    # 持续时间内隐匿挥割变为缢杀爪
    # 追加效果：获得20点魂衣
    # 发动条件：妖异之镰
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,800.
    # Enhanced Gibbet Potency: 2,200
    # Additional Effect: Grants Enhanced Gallows
    # Duration: 30s
    # The action Blood Stalk changes to Unveiled Gallows while under the effect of Enhanced Gallows.
    # Additional Effect: Increases Shroud Gauge by 20
    # Can only be executed while under the effect of Soul Reaver.
    # ※This action cannot be assigned to a hotbar.
    # related: [缢杀效果提高(0)](Status2856), [绞决效果提高(1)](Status2588), [缢杀效果提高(1)](Status2589), [绞决效果提高(0)](Status2855),
    id = 27798
    names = ['Gibbet(pvp)(RPR)', '绞决(pvp)(RPR)']
    _orig_names = ['绞决(pvp)', 'Gibbet(pvp)']
    damage = "(绞决效果提高?2200:1800)"


class Action27799(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 缢杀效果提高中威力：2200
    # 追加效果：绞决效果提高
    # 持续时间“30秒
    # 持续时间内隐匿挥割变为绞决爪
    # 追加效果：获得20点魂衣
    # 发动条件：妖异之镰且缢杀效果提高状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,800.
    # Enhanced Gallows Potency: 2,200
    # Additional Effect: Grants Enhanced Gibbet
    # Duration: 30s
    # The action Blood Stalk changes to Unveiled Gibbet while under the effect of Enhanced Gibbet.
    # Additional Effect: Increases Shroud Gauge by 20
    # Can only be executed while under the effect of Soul Reaver and Enhanced Gallows.
    # ※This action cannot be assigned to a hotbar.
    # related: [缢杀效果提高(0)](Status2856), [绞决效果提高(1)](Status2588), [缢杀效果提高(1)](Status2589), [绞决效果提高(0)](Status2855),
    id = 27799
    names = ['Gallows(pvp)(RPR)', '缢杀(pvp)(RPR)']
    _orig_names = ['Gallows(pvp)', '缢杀(pvp)']
    damage = "(缢杀效果提高?2200:1800)"


class Action27800(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 虚无收割效果提高中威力：2200
    # 追加效果：交错收割效果提高
    # 持续时间：30秒
    # 追加效果：虚无魂
    # 发动条件：夜游魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,800.
    # Enhanced Void Reaping Potency: 2,200
    # Additional Effect: Grants Enhanced Cross Reaping
    # Duration: 30s
    # Additional Effect: Grants Void Shroud
    # Lemure Shroud Cost: 1
    # Can only be executed while under the effect of Enshrouded.
    # ※This action cannot be assigned to a hotbar.
    # related: [虚无收割效果提高(0)](Status2857), [交错收割效果提高(0)](Status2858), [虚无收割效果提高(1)](Status2590), [交错收割效果提高(1)](Status2591),
    id = 27800
    names = ['虚无收割(pvp)(RPR)', 'Void Reaping(pvp)(RPR)']
    _orig_names = ['虚无收割(pvp)', 'Void Reaping(pvp)']
    damage = "(虚无收割效果提高?2200:1800)"


class Action27801(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 交错收割效果提高中威力：2200
    # 追加效果：虚无收割效果提高
    # 持续时间：30秒
    # 追加效果：虚无魂
    # 发动条件：夜游魂且交错收割效果提高状态中
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,800.
    # Enhanced Cross Reaping Potency: 2,200
    # Additional Effect: Grants Enhanced Void Reaping
    # Duration: 30s
    # Additional Effect: Grants Void Shroud
    # Lemure Shroud Cost: 1
    # Can only be executed while under the effect of Enshrouded and Enhanced Cross Reaping.
    # ※This action cannot be assigned to a hotbar.
    # related: [虚无收割效果提高(0)](Status2857), [交错收割效果提高(0)](Status2858), [虚无收割效果提高(1)](Status2590), [交错收割效果提高(1)](Status2591),
    id = 27801
    names = ['Cross Reaping(pvp)(RPR)', '交错收割(pvp)(RPR)']
    _orig_names = ['交错收割(pvp)', 'Cross Reaping(pvp)']
    damage = "(交错收割效果提高?2200:1800)"


class Action27802(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：800
    # 追加效果：获得10点灵魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 800 to all nearby enemies.
    # Additional Effect: Increases Soul Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 27802
    names = ['旋转钐割(pvp)(RPR)', 'Spinning Scythe(pvp)(RPR)']
    _orig_names = ['旋转钐割(pvp)', 'Spinning Scythe(pvp)']
    damage = 800


class Action27803(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 连击中威力：1000
    # 连击条件：旋转钐割
    # 连击成功：获得10点灵魂
    # ※该技能无法设置到热键栏
    # Delivers an attack to all nearby enemies.
    # Combo Action: Spinning Scythe
    # Combo Potency: 1,000
    # Combo Bonus: Increases Soul Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 27803
    names = ['噩梦钐割(pvp)(RPR)', 'Nightmare Scythe(pvp)(RPR)']
    _orig_names = ['噩梦钐割(pvp)', 'Nightmare Scythe(pvp)']
    combo_action = 27802
    combo_damage = 1000


class Action27804(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1200
    # 追加效果：获得20点魂衣
    # 发动条件：妖异之镰
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200 to all enemies in a cone before you.
    # Additional Effect: Increases Shroud Gauge by 20
    # Can only be executed while under the effect of Soul Reaver.
    # ※This action cannot be assigned to a hotbar.
    id = 27804
    names = ['断首(pvp)(RPR)', 'Guillotine(pvp)(RPR)']
    _orig_names = ['断首(pvp)', 'Guillotine(pvp)']
    damage = 1200


class Action27805(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1200
    # 追加效果：虚无魂
    # 发动条件：夜游魂
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,200 to all enemies in a cone before you.
    # Additional Effect: Grants Void Shroud
    # Lemure Shroud Cost: 1
    # Can only be executed while under the effect of Enshrouded.
    # ※This action cannot be assigned to a hotbar.
    id = 27805
    names = ['Grim Reaping(pvp)(RPR)', '阴冷收割(pvp)(RPR)']
    _orig_names = ['阴冷收割(pvp)', 'Grim Reaping(pvp)']
    damage = 1200


class Action27806(Action):
    # 对目标发动魔法攻击
    # 威力：1400
    # Deals unaspected damage with a potency of 1,400.
    # ※Action changes to Communio while under the effect of Enshrouded.
    id = 27806
    names = ['Harpe(pvp)(RPR)', '勾刃(pvp)(RPR)']
    _orig_names = ['Harpe(pvp)', '勾刃(pvp)']
    damage = 1400


class Action27807(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：2400
    # 发动后夜游魂状态消失
    # 发动条件：夜游魂1档以上
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 2,400 to target and all enemies nearby it.
    # Enshrouded effect expires upon execution.
    # Requires at least one stack of Lemure Shroud to execute.
    # ※This action cannot be assigned to a hotbar.
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863),
    id = 27807
    names = ['团契(pvp)(RPR)', 'Communio(pvp)(RPR)']
    _orig_names = ['Communio(pvp)', '团契(pvp)']
    damage = 2400


class Action27808(Action):
    # 对目标发动物理攻击
    # 威力：1600
    # 追加效果：获得50点灵魂
    # 积蓄次数：2
    # 该战技不仅有单独计算的复唱时间，还会与灵魂钐割共享复唱时间
    # Delivers an attack with a potency of 1,600.
    # Additional Effect: Increases Soul Gauge by 50
    # Maximum Charges: 2
    # Shares a recast timer with Soul Scythe.
    id = 27808
    names = ['Soul Slice(pvp)(RPR)', '灵魂切割(pvp)(RPR)']
    _orig_names = ['灵魂切割(pvp)', 'Soul Slice(pvp)']
    damage = 1600


class Action27809(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：1000
    # 追加效果：每命中一个目标都会获得20点灵魂
    # 积蓄次数：2
    # 该战技不仅有单独计算的复唱时间，还会与灵魂切割共享复唱时间
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Increases Soul Gauge by 20 for each enemy hit
    # Maximum Charges: 2
    # Shares a recast timer with Soul Slice.
    id = 27809
    names = ['Soul Scythe(pvp)(RPR)', '灵魂钐割(pvp)(RPR)']
    _orig_names = ['Soul Scythe(pvp)', '灵魂钐割(pvp)']
    damage = 1000


class Action27810(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：1600
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：10秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    #
    # Summons your avatar to deliver an attack with a potency of 1,600.
    # Additional Effect: Grants Soul Reaver
    # Duration: 10s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Shares a recast timer with all avatar attacks except Gluttony.(job==39?(level>=86?
    # ※Action changes to Lemure's Slice while under the effect of Enshrouded.:):)
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 27810
    names = ['隐匿挥割(pvp)(RPR)', 'Blood Stalk(pvp)(RPR)']
    _orig_names = ['隐匿挥割(pvp)', 'Blood Stalk(pvp)']
    damage = 1600


class Action27811(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：1600
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：10秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：绞决效果提高状态中且灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # ※该技能无法设置到热键栏
    # Summons your avatar to deliver an attack with a potency of 1,600.
    # Additional Effect: Grants Soul Reaver
    # Duration: 10s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Can only be executed while under the effect of Enhanced Gibbet.
    # Shares a recast timer with all avatar attacks except Gluttony.
    # ※This action cannot be assigned to a hotbar.
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 27811
    names = ['绞决爪(pvp)(RPR)', 'Unveiled Gibbet(pvp)(RPR)']
    _orig_names = ['Unveiled Gibbet(pvp)', '绞决爪(pvp)']
    damage = 1600


class Action27812(Action):
    # 召唤化身对目标发动物理攻击
    # 威力：1600
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：10秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：缢杀效果提高状态中且灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # ※该技能无法设置到热键栏
    # Summons your avatar to deliver an attack with a potency of 1,600.
    # Additional Effect: Grants Soul Reaver
    # Duration: 10s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Can only be executed while under the effect of Enhanced Gallows.
    # Shares a recast timer with all avatar attacks except Gluttony.
    # ※This action cannot be assigned to a hotbar.
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 27812
    names = ['Unveiled Gallows(pvp)(RPR)', '缢杀爪(pvp)(RPR)']
    _orig_names = ['缢杀爪(pvp)', 'Unveiled Gallows(pvp)']
    damage = 1600


class Action27813(Action):
    # 召唤化身对目标所在方向发出扇形范围物理攻击
    # 威力：1000
    # 追加效果：为自身附加1档妖异之镰状态
    # 持续时间：10秒
    # 若自身已附加妖异之镰状态，则档数刷新为1档
    # 发动条件：灵魂50点
    # 该技能与暴食之外的化身技能共享复唱时间
    # Summons your avatar to deliver an attack with a potency of 1,000 to all enemies in a cone before you.
    # Additional Effect: Grants Soul Reaver
    # Duration: 10s
    # Stack count will be reduced to 1 when already under the effect of Soul Reaver.
    # Soul Gauge Cost: 50
    # Shares a recast timer with all avatar attacks except Gluttony.(job==39?(level>=86?
    # ※Action changes to Lemure's Scythe while under the effect of Enshrouded.:):)
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 27813
    names = ['Grim Swathe(pvp)(RPR)', '束缚挥割(pvp)(RPR)']
    _orig_names = ['束缚挥割(pvp)', 'Grim Swathe(pvp)']
    damage = 1000


class Action27814(Action):
    # 召唤化身对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：2000
    # 追加效果：为自身附加2档妖异之镰
    # 持续时间：10秒
    # 发动条件：灵魂50点
    # Summons your avatar to deal unaspected damage with a potency of 2,000 to target and all enemies nearby it.
    # Additional Effect: Grants 2 stacks of Soul Reaver
    # Duration: 10s
    # Soul Gauge Cost: 50
    # related: [妖异之镰(1)](Status2587), [妖异之镰(0)](Status2854),
    id = 27814
    names = ['Gluttony(pvp)(RPR)', '暴食(pvp)(RPR)']
    _orig_names = ['暴食(pvp)', 'Gluttony(pvp)']
    damage = 2000


class Action27815(Action):
    # 对目标发动物理攻击
    # 威力：1600
    # 发动条件：虚无魂2档
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,600.
    # Void Shroud Cost: 2
    # ※This action cannot be assigned to a hotbar.
    id = 27815
    names = ['夜游魂切割(pvp)(RPR)', "Lemure's Slice(pvp)(RPR)"]
    _orig_names = ["Lemure's Slice(pvp)", '夜游魂切割(pvp)']
    damage = 1600


class Action27816(Action):
    # 对目标所在方向发出扇形范围物理攻击
    # 威力：1000
    # 发动条件：虚无魂2档
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000 to all enemies in a cone before you.
    # Void Shroud Cost: 2
    # ※This action cannot be assigned to a hotbar.
    id = 27816
    names = ['夜游魂钐割(pvp)(RPR)', "Lemure's Scythe(pvp)(RPR)"]
    _orig_names = ['夜游魂钐割(pvp)', "Lemure's Scythe(pvp)"]
    damage = 1000


class Action27817(Action):
    # 迅速移动到自身前方15米处
    # 追加效果：下次发动勾刃不需要咏唱时间
    # 持续时间：10秒
    # 追加效果：在移动前的地点生成地狱之门，并为自身附加回退预备状态
    # 持续时间：10秒
    # 止步状态下无法发动
    # 该战技与地狱出境共享复唱时间
    # Quickly dash 15 yalms forward.
    # Additional Effect: Allows next Harpe to be cast immediately
    # Duration: 10s
    # Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
    # Duration: 10s
    # Cannot be executed while bound.
    # Shares a recast timer with Hell's Egress.
    # related: [回退预备(0)](Status2595), [回退预备(1)](Status2860),
    id = 27817
    names = ["Hell's Ingress(pvp)(RPR)", '地狱入境(pvp)(RPR)']
    _orig_names = ['地狱入境(pvp)', "Hell's Ingress(pvp)"]


class Action27818(Action):
    # 迅速移动到自身后方15米处
    # 追加效果：下次发动勾刃不需要咏唱时间
    # 持续时间：10秒
    # 追加效果：在移动前的地点生成地狱之门，并为自身附加回退预备状态
    # 持续时间：10秒
    # 止步状态下无法发动
    # 该战技与地狱入境共享复唱时间
    # Quickly dash 15 yalms backwards.
    # Additional Effect: Allows next Harpe to be cast immediately
    # Duration: 10s
    # Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
    # Duration: 10s
    # Cannot be executed while bound.
    # Shares a recast timer with Hell's Ingress.
    # related: [回退预备(0)](Status2595), [回退预备(1)](Status2860),
    id = 27818
    names = ["Hell's Egress(pvp)(RPR)", '地狱出境(pvp)(RPR)']
    _orig_names = ['地狱出境(pvp)', "Hell's Egress(pvp)"]


class Action27819(Action):
    # 快速移动到自身留下的地狱之门中心
    # 止步状态下无法发动
    # ※该技能无法设置到热键栏
    # Move instantly to the Hellsgate left behind by you.
    # Can only be executed while under the effect of Threshold.
    # Cannot be executed while bound.
    # ※This action cannot be assigned to a hotbar.
    id = 27819
    names = ['Regress(pvp)(RPR)', '回退(pvp)(RPR)']
    _orig_names = ['Regress(pvp)', '回退(pvp)']


class Action27820(Action):
    # 为自身附加能够抵消一定伤害量的防护罩守护纹
    # 该防护罩能够抵消相当于2500恢复力的伤害量
    # 持续时间：5秒
    # 防护罩因吸收到足够的伤害而消失时，为自身及周围15米以内的队员附加活性纹状态
    # 活性纹效果：持续恢复目标的体力
    # 恢复力：500
    # 持续时间：15秒
    # Grants Crest of Time Borrowed to self, creating a barrier that nullifies damage equivalent to a heal of 2,500 potency.
    # Duration: 5s
    # Grants the Crest of Time Returned to self and nearby party members within a radius of 15 yalms when barrier is completely absorbed.
    # Crest of Time Returned Effect: Gradually restores HP
    # Cure Potency: 500
    # Duration: 15s
    # related: [活性纹(0)](Status2862), [活性纹(1)](Status2598),
    id = 27820
    names = ['Arcane Crest(pvp)(RPR)', '神秘纹(pvp)(RPR)']
    _orig_names = ['神秘纹(pvp)', 'Arcane Crest(pvp)']
    # remain metas: {'shield': '2500恢复力', 'heal_ot': '500'}


class Action27821(Action):
    # 召唤化身附体并为自身附加最大档数的夜游魂状态
    # 持续时间：15秒
    # 化身附体状态中无法发动召唤化身技能及部分战技
    # 发动条件：魂衣50点
    # Offers your flesh as a vessel to your avatar, gaining maximum stacks of Lemure Shroud.
    # Duration: 15s
    # Certain actions cannot be executed while playing host to your avatar.
    # Shroud Gauge Cost: 50
    # related: [夜游魂(0)](Status2593), [夜游魂(1)](Status2863),
    id = 27821
    names = ['夜游魂衣(pvp)(RPR)', 'Enshroud(pvp)(RPR)']
    _orig_names = ['Enshroud(pvp)', '夜游魂衣(pvp)']
