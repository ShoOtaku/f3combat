from ._base import *


class Status855(Status):
    # 物理攻击所造成的伤害提高
    # Physical damage dealt is increased.
    # related: [热弹(MCH)](Action2872), 
    id = 855
    names = ['热弹', 'Hot Shot']


class Status851(Status):
    # 下次发动的战技必定打出暴击和直击
    # Next weaponskill will result in a critical direct hit.
    # related: [整备(MCH)](Action2876), 
    id = 851
    names = ['整备', 'Reassembled']


class Status1946(Status):
    # 对敌人附加了“野火”
    # Currently afflicting an enemy with Wildfire.
    # related: [野火(MCH)](Action2878), [空包弹(pvp)(MCH)](Action8853), [野火(pvp)(MCH)](Action8855), [起爆(MCH)](Action16766), 
    id = 1946
    names = ['野火(0)', 'Wildfire(0)']


class Status1323(Status):
    # 效果时间中积攒自身所造成的部分伤害
    # A portion of damage dealt is being stored.
    # related: [野火(MCH)](Action2878), [空包弹(pvp)(MCH)](Action8853), [野火(pvp)(MCH)](Action8855), [起爆(MCH)](Action16766), 
    id = 1323
    names = ['野火(1)', 'Wildfire(1)']


class Status861(Status):
    # 若受到了来自附加这一状态的机工士发动的战技攻击的话，效果时间结束时会受到伤害
    # Damage is being accumulated with each weaponskill landed by the machinist who applied the effect.
    # related: [野火(MCH)](Action2878), [空包弹(pvp)(MCH)](Action8853), [野火(pvp)(MCH)](Action8855), [起爆(MCH)](Action16766), 
    id = 861
    names = ['野火(2)', 'Wildfire(2)']


class Status1458(Status):
    # 受到持续伤害
    # Taking damage over time.
    # related: [火焰喷射器(MCH)](Action7418), 
    id = 1458
    names = ['火焰喷射器(0)', 'Flamethrower Flames']


class Status1205(Status):
    # 对前方扇形范围内的敌人持续造成伤害
    # Emitting a gout of searing flames in a cone before you, dealing damage over time.
    # related: [火焰喷射器(MCH)](Action7418), 
    id = 1205
    names = ['火焰喷射器(1)', 'Flamethrower(0)']


class Status1455(Status):
    # 对前方扇形范围内的敌人持续造成伤害
    # Emitting a gout of searing flames in a cone, dealing damage over time.
    # related: [火焰喷射器(MCH)](Action7418), 
    id = 1455
    names = ['火焰喷射器(2)', 'Flamethrower(1)']


class Status1866(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [毒菌冲击(MCH)](Action16499), [毒菌冲击(pvp)(MCH)](Action17752), 
    id = 1866
    names = ['毒菌冲击(0)', 'Bioblaster(0)']


class Status2019(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [毒菌冲击(MCH)](Action16499), [毒菌冲击(pvp)(MCH)](Action17752), 
    id = 2019
    names = ['毒菌冲击(1)', 'Bioblaster(1)']


class Status688(Status):
    # 浮空炮塔系技能有所强化
    # Battle turret is overcharged.
    # related: [超荷(MCH)](Action17209), [超荷(pvp)(MCH)](Action17754), 
    id = 688
    names = ['超荷', 'Hypercharge']


class Action2864(Action):
    # 设置车式浮空炮塔进行支援射击
    # 车式浮空炮塔的运转时间随发动该技能时消耗的电能而变动
    # 最长运转时间：15秒
    # 车式浮空炮塔可以通过齐射进行自动攻击
    # 对目标发动物理攻击
    # 威力：70
    # 运转时间结束后，或发动超档车式炮塔后，车式浮空炮塔会被回收
    # 发动条件：电能50点以上
    # 与超档车式炮塔共享复唱时间
    # Deploys a single-target battle turret which attacks using Volley Fire, dealing damage with a potency of 70.
    # Battery Gauge Cost: 50
    # Duration increases as Battery Gauge exceeds required cost at time of deployment, up to a maximum of 15 seconds.
    # Consumes Battery Gauge upon execution.
    # Shuts down when time expires or upon execution of Rook Overdrive.
    # Shares a recast timer with Rook Overdrive.
    id = 2864
    names = ['车式浮空炮塔(MCH)', 'Rook Autoturret(MCH)']
    _orig_names = ['车式浮空炮塔', 'Rook Autoturret']
    damage = 70


class Action2866(Action):
    # 对目标发动物理攻击
    # 威力：140(job==31?(level>=30?
    # 追加效果：获得5点枪管热度:):)
    # Delivers an attack with a potency of 140.(job==31?(level>=30?
    # Additional Effect: Increases Heat Gauge by 5:):)
    id = 2866
    names = ['分裂弹(MCH)', 'Split Shot(MCH)']
    _orig_names = ['Split Shot', '分裂弹']
    damage = 140


class Action2868(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：分裂弹或热分裂弹
    # 连击中威力：210(job==31?(level>=30?
    # 连击成功：获得5点枪管热度:):)
    # Delivers an attack with a potency of 100.
    # Combo Action: Split Shot or Heated Split Shot
    # Combo Potency: 210(job==31?(level>=30?
    # Combo Bonus: Increases Heat Gauge by 5:):)
    id = 2868
    names = ['Slug Shot(MCH)', '独头弹(MCH)']
    _orig_names = ['独头弹', 'Slug Shot']
    combo_action = 2866
    damage = 100
    combo_damage = 210


class Action2870(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：140(job==31?(level>=30?
    # 追加效果：获得5点枪管热度:):)
    # Delivers an attack with a potency of 140 to all enemies in a cone before you.(job==31?(level>=30?
    # Additional Effect: Increases Heat Gauge by 5:):)
    id = 2870
    names = ['散射(MCH)', 'Spread Shot(MCH)']
    _orig_names = ['散射', 'Spread Shot']
    damage = 140


class Action2872(Action):
    # 对目标发动物理攻击
    # 威力：240
    # (job==31?(level>=40?追加效果：获得20点电能
    # :):)该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 240.(job==31?(level>=40?
    # Additional Effect: Increases Battery Gauge by 20:):)
    # This weaponskill does not share a recast timer with any other actions.
    # related: [热弹](Status855), 
    id = 2872
    names = ['热弹(MCH)', 'Hot Shot(MCH)']
    _orig_names = ['热弹', 'Hot Shot']
    damage = 240


class Action2873(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 连击条件：独头弹或热独头弹
    # 连击中威力：270(job==31?(level>=30?
    # 连击成功：获得5点枪管热度:):)(job==31?(level>=40?
    # 连击成功：获得10点电能:):)
    # Delivers an attack with a potency of 100.
    # Combo Action: Slug Shot or Heated Slug Shot
    # Combo Potency: 270(job==31?(level>=30?
    # Combo Bonus: Increases Heat Gauge by 5:):)(job==31?(level>=40?
    # Combo Bonus: Increases Battery Gauge by 10:):)
    id = 2873
    names = ['狙击弹(MCH)', 'Clean Shot(MCH)']
    _orig_names = ['Clean Shot', '狙击弹']
    combo_action = 2868
    damage = 100
    combo_damage = 270


class Action2874(Action):
    # 对目标发动物理攻击
    # 威力：120
    # 积蓄次数：(job==31?(level>=74?3:2):2)
    # Delivers an attack with a potency of 120.
    # Maximum Charges: (job==31?(level>=74?3:2):2)
    id = 2874
    names = ['Gauss Round(MCH)', '虹吸弹(MCH)']
    _orig_names = ['Gauss Round', '虹吸弹']
    damage = 120


class Action2876(Action):
    # 效果时间内，自身发动的1次战技必定打出暴击并且直击
    # 该效果不适用于持续伤害等状态
    # 持续时间：5秒(job==31?(level>=84?
    # 积蓄次数：2:):)
    # Guarantees that next weaponskill is a critical direct hit.
    # Duration: 5s
    # This action does not affect damage over time effects.(job==31?(level>=84?
    # Maximum Charges: 2:):)
    # related: [整备](Status851), 
    id = 2876
    names = ['整备(MCH)', 'Reassemble(MCH)']
    _orig_names = ['整备', 'Reassemble']


class Action2878(Action):
    # 对目标附加野火状态，同时该技能变为起爆
    # 持续时间结束或发动起爆，可以对目标造成伤害
    # 该技能的威力随自身在持续时间内对目标命中的战技次数而变化
    # 每命中1次战技的威力：(job==31?(level>=78?150:100):100)
    # 持续时间：10秒
    # Covers target's body in a slow-burning pitch. Action is changed to Detonator for the duration of the effect.
    # Deals damage when time expires or upon executing Detonator.
    # Potency is increased by (job==31?(level>=78?150:100):100) for each of your own weaponskills you land prior to the end of the effect.
    # Duration: 10s
    # related: [野火(0)](Status1946), [野火(1)](Status1323), [野火(2)](Status861), 
    id = 2878
    names = ['野火(MCH)', 'Wildfire(MCH)']
    _orig_names = ['Wildfire', '野火']
    # remain metas: {'dmg_ot': '(每命?(job==31?(lv>=78?150:100):100):-)'}


class Action2890(Action):
    # 对目标及其周围的敌人发动范围物理攻击
    # 威力：120
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 积蓄次数：(job==31?(level>=74?3:2):2)
    # Deals damage to all nearby enemies with a potency of 120 for the first enemy, and 50% less for all remaining enemies.
    # Maximum Charges: (job==31?(level>=74?3:2):2)
    id = 2890
    names = ['弹射(MCH)', 'Ricochet(MCH)']
    _orig_names = ['Ricochet', '弹射']
    damage = 120
    # remain metas: {'aoe_reduce': '50%'}


class Action7410(Action):
    # 对目标发动物理攻击
    # 威力：170
    # 追加效果：虹吸弹和弹射的复唱时间缩短15秒
    # 发动条件：过热状态
    # 该战技有单独计算的复唱时间，不受装备和状态的影响
    # Delivers an attack with a potency of 170.
    # Additional Effect: Reduces the recast time of both Gauss Round and Ricochet by 15s
    # Can only be executed when firearm is Overheated.
    # Recast timer cannot be affected by status effects or gear attributes.
    id = 7410
    names = ['Heat Blast(MCH)', '热冲击(MCH)']
    _orig_names = ['热冲击', 'Heat Blast']
    damage = 170


class Action7411(Action):
    # 对目标发动物理攻击
    # 威力：(job==31?(level>=84?200:180):180)(job==31?(level>=30?
    # 追加效果：获得5点枪管热度:):)
    # Delivers an attack with a potency of (job==31?(level>=84?200:180):180).(job==31?(level>=30?
    # Additional Effect: Increases Heat Gauge by 5:):)
    id = 7411
    names = ['热分裂弹(MCH)', 'Heated Split Shot(MCH)']
    _orig_names = ['热分裂弹', 'Heated Split Shot']
    damage = "(job==31?(lv>=84?200:180):180)"


class Action7412(Action):
    # 对目标发动物理攻击
    # 威力：(job==31?(level>=84?120:100):100)
    # 连击条件：热分裂弹
    # 连击中威力：(job==31?(level>=84?280:260):260)(job==31?(level>=30?
    # 连击成功：获得5点枪管热度:):)
    # Delivers an attack with a potency of (job==31?(level>=84?120:100):100).
    # Combo Action: Heated Split Shot
    # Combo Potency: (job==31?(level>=84?280:260):260)(job==31?(level>=30?
    # Combo Bonus: Increases Heat Gauge by 5:):)
    id = 7412
    names = ['Heated Slug Shot(MCH)', '热独头弹(MCH)']
    _orig_names = ['热独头弹', 'Heated Slug Shot']
    combo_action = 2866
    damage = "(job==31?(lv>=84?120:100):100)"
    combo_damage = "(job==31?(lv>=84?280:260):260)"


class Action7413(Action):
    # 对目标发动物理攻击
    # 威力：(job==31?(level>=84?110:100):100)
    # 连击条件：热独头弹
    # 连击中威力：(job==31?(level>=84?360:350):350)(job==31?(level>=30?
    # 连击成功：获得5点枪管热度:):)(job==31?(level>=40?
    # 连击成功：获得10点电能:):)
    # Delivers an attack with a potency of (job==31?(level>=84?110:100):100).
    # Combo Action: Heated Slug Shot
    # Combo Potency: (job==31?(level>=84?360:350):350)(job==31?(level>=30?
    # Combo Bonus: Increases Heat Gauge by 5:):)(job==31?(level>=40?
    # Combo Bonus: Increases Battery Gauge by 10:):)
    id = 7413
    names = ['Heated Clean Shot(MCH)', '热狙击弹(MCH)']
    _orig_names = ['Heated Clean Shot', '热狙击弹']
    combo_action = 2868
    damage = "(job==31?(lv>=84?110:100):100)"
    combo_damage = "(job==31?(lv>=84?360:350):350)"


class Action7414(Action):
    # 获得50点枪管热度
    # 发动条件：自身处于战斗状态
    # Increases Heat Gauge by 50.
    # Can only be executed while in combat.
    id = 7414
    names = ['枪管加热(MCH)', 'Barrel Stabilizer(MCH)']
    _orig_names = ['枪管加热', 'Barrel Stabilizer']


class Action7415(Action):
    # 命令设置的车式浮空炮塔发动超负荷车式炮塔
    # 对目标发动物理攻击
    # 威力：320
    # 该技能的威力受设置车式浮空炮塔时消耗的电能影响
    # 发动后车式浮空炮塔消失
    # 所有者使用超档车式炮塔或车式浮空炮塔的运转时间结束时，车式浮空炮塔会自动执行该技能
    # 发动条件：车式浮空炮塔处于设置状态
    # 与车式浮空炮塔共享复唱时间
    # Orders the rook autoturret to use Rook Overload.
    # Rook Overload Potency: 320
    # Potency increases as Battery Gauge exceeds required cost at time of deployment.
    # The rook autoturret shuts down after execution. If this action is not used manually while the rook autoturret is active, it will be triggered automatically immediately before shutting down.
    # Shares a recast timer with Rook Autoturret.
    id = 7415
    names = ['超档车式炮塔(MCH)', 'Rook Overdrive(MCH)']
    _orig_names = ['超档车式炮塔', 'Rook Overdrive']
    damage = 320


class Action7416(Action):
    # 对目标发动物理攻击
    # 威力：320
    # 该技能的威力受设置车式浮空炮塔时消耗的电能影响
    # 发动后车式浮空炮塔消失
    # 所有者使用超档车式炮塔或车式浮空炮塔的运转时间结束时，车式浮空炮塔会自动执行该技能
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 320.
    # Potency increases as Battery Gauge exceeds required cost at time of deployment.
    # The rook autoturret shuts down after execution. If this action is not used manually while the rook autoturret is active, it will be triggered automatically immediately before shutting down.
    # ※This action cannot be assigned to a hotbar.
    id = 7416
    names = ['Rook Overload(MCH)', '超负荷车式炮塔(MCH)']
    _orig_names = ['超负荷车式炮塔', 'Rook Overload']
    damage = 320


class Action7418(Action):
    # 持续向自身前方发出扇形范围攻击
    # 每秒对范围内的敌人造成伤害
    # 威力：80
    # 持续时间：10秒
    # 效果时间内发动技能或进行移动、转身都会立即解除火焰喷射器
    # 发动之后会停止自动攻击
    # 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间
    # Delivers damage over time to all enemies in a cone before you.
    # Potency: 80
    # Duration: 10s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
    # related: [火焰喷射器(0)](Status1458), [火焰喷射器(1)](Status1205), [火焰喷射器(2)](Status1455), 
    id = 7418
    names = ['火焰喷射器(MCH)', 'Flamethrower(MCH)']
    _orig_names = ['火焰喷射器', 'Flamethrower']
    # remain metas: {'dmg_ot': '80'}


class Action8848(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：获得10点枪管热度
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # Additional Effect: Increases Heat Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8848
    names = ['Heated Split Shot(pvp)(MCH)', '热分裂弹(pvp)(MCH)']
    _orig_names = ['热分裂弹(pvp)', 'Heated Split Shot(pvp)']
    damage = 1000


class Action8849(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 连击条件：热分裂弹
    # 追加效果：获得10点枪管热度
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Heated Split Shot
    # Combo Potency: 1,200
    # Additional Effect: Increases Heat Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8849
    names = ['热独头弹(pvp)(MCH)', 'Heated Slug Shot(pvp)(MCH)']
    _orig_names = ['Heated Slug Shot(pvp)', '热独头弹(pvp)']
    combo_action = 8848
    damage = 1200


class Action8850(Action):
    # 对目标发动物理攻击
    # 威力：1400
    # 连击条件：热独头弹
    # 追加效果：获得10点枪管热度
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Heated Slug Shot
    # Combo Potency: 1,400
    # Additional Effect: Increases Heat Gauge by 10
    # ※This action cannot be assigned to a hotbar.
    id = 8850
    names = ['Heated Clean Shot(pvp)(MCH)', '热狙击弹(pvp)(MCH)']
    _orig_names = ['热狙击弹(pvp)', 'Heated Clean Shot(pvp)']
    combo_action = 8849
    damage = 1400


class Action8851(Action):
    # 对目标发动物理攻击
    # 威力：1400
    # 追加效果：虹吸弹和弹射的复唱时间缩短7.5秒
    # 发动条件：过热状态
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,400.
    # Additional Effect: Reduces the recast time of both Gauss Round and Ricochet by 7.5s
    # Can only be executed when firearm is Overheated.
    # ※This action cannot be assigned to a hotbar.
    id = 8851
    names = ['Heat Blast(pvp)(MCH)', '热冲击(pvp)(MCH)']
    _orig_names = ['Heat Blast(pvp)', '热冲击(pvp)']
    damage = 1400


class Action8853(Action):
    # 对目标发动物理攻击
    # 威力：800
    # 目标身上有自身附加的野火状态时威力变为3倍
    # 追加效果：将目标击退15米
    # Delivers an attack with a potency of 800.
    # Additional Effect: If target is suffering from a Wildfire effect inflicted by you, Blank potency is tripled
    # Additional Effect: 15-yalm knockback
    # related: [野火(0)](Status1946), [野火(1)](Status1323), [野火(2)](Status861), 
    id = 8853
    names = ['空包弹(pvp)(MCH)', 'Blank(pvp)(MCH)']
    _orig_names = ['Blank(pvp)', '空包弹(pvp)']
    damage = 800


class Action8855(Action):
    # 在目标身上放置一枚定时炸弹
    # 效果时间内自身对目标造成伤害量的33%会暂时累积，在效果结束时一并造成伤害
    # 该累积效果对部分攻击无效
    # 持续时间：6秒
    # Covers target's body in a slow-burning pitch. For the next 6 seconds, 33% of most damage you inflict upon the target is compiled, then dealt at the end of the effect's duration.
    # related: [野火(0)](Status1946), [野火(1)](Status1323), [野火(2)](Status861), 
    id = 8855
    names = ['Wildfire(pvp)(MCH)', '野火(pvp)(MCH)']
    _orig_names = ['Wildfire(pvp)', '野火(pvp)']


class Action16497(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：140
    # 发动条件：过热状态
    # 该战技有单独计算的复唱时间，不受装备和状态的影响
    # Delivers an attack with a potency of 140 to all enemies in a cone before you.
    # Can only be executed when firearm is Overheated.
    # Recast timer cannot be affected by status effects or gear attributes.
    id = 16497
    names = ['自动弩(MCH)', 'Auto Crossbow(MCH)']
    _orig_names = ['自动弩', 'Auto Crossbow']
    damage = 140


class Action16498(Action):
    # 对目标发动物理攻击
    # 威力：570
    # (job==31?(level>=72?该战技不仅有单独计算的复唱时间，还会与毒菌冲击共享复唱时间:该战技有单独计算的复唱时间):该战技有单独计算的复唱时间)
    # Delivers an attack with a potency of 570.
    # (job==31?(level>=72?Shares a recast timer with Bioblaster.:This weaponskill does not share a recast timer with any other actions.):This weaponskill does not share a recast timer with any other actions.)
    id = 16498
    names = ['Drill(MCH)', '钻头(MCH)']
    _orig_names = ['Drill', '钻头']
    damage = 570


class Action16499(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：50
    # 追加效果：持续伤害
    # 威力：50
    # 持续时间：15秒
    # 该战技不仅有单独计算的复唱时间，还会与钻头共享复唱时间
    # Delivers an attack with a potency of 50 to all enemies in a cone before you.
    # Additional Effect: Damage over time
    # Potency: 50
    # Duration: 15s
    # Shares a recast timer with Drill.
    # related: [毒菌冲击(0)](Status1866), [毒菌冲击(1)](Status2019), 
    id = 16499
    names = ['Bioblaster(MCH)', '毒菌冲击(MCH)']
    _orig_names = ['毒菌冲击', 'Bioblaster']
    damage = 50
    # remain metas: {'dmg_ot': '50'}


class Action16500(Action):
    # 对目标发动物理攻击
    # 威力：570
    # 追加效果：获得20点电能
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 570.
    # Additional Effect: Increases Battery Gauge by 20
    # This weaponskill does not share a recast timer with any other actions.
    id = 16500
    names = ['Air Anchor(MCH)', '空气锚(MCH)']
    _orig_names = ['空气锚', 'Air Anchor']
    damage = 570


class Action16501(Action):
    # 启动后式自走人偶
    # 后式自走人偶的运转时间随发动该技能时消耗的电能而变动
    # 最长运转时间：20秒
    # 运转时间结束后，或发动超档后式人偶后，后式自走人偶会被回收
    # 发动条件：电能50点以上
    # 与超档后式人偶共享复唱时间
    # Deploys an Automaton Queen to fight at your side.
    # Battery Gauge Cost: 50
    # Duration increases as Battery Gauge exceeds minimum cost at time of deployment, up to a maximum of 20 seconds.
    # Consumes Battery Gauge upon execution.
    # Shuts down when time expires or upon execution of Queen Overdrive.
    # Shares a recast timer with Queen Overdrive.
    id = 16501
    names = ['Automaton Queen(MCH)', '后式自走人偶(MCH)']
    _orig_names = ['Automaton Queen', '后式自走人偶']


class Action16502(Action):
    # 命令设置的后式自走人偶发动打桩枪
    # 对目标发动物理攻击
    # 威力：650
    # 该技能的威力受设置后式自走人偶时消耗的电能影响
    # 发动后后式自走人偶消失
    # 所有者使用超档后式人偶或后式自走人偶的运转时间结束时，后式自走人偶会自动执行该技能
    # 发动条件：后式自走人偶处于设置状态
    # 与后式自走人偶共享复唱时间
    # Orders the Automaton Queen to use Pile Bunker.
    # Pile Bunker Potency: 650
    # Potency increases as Battery Gauge exceeds required cost at time of deployment.
    # The Automaton Queen shuts down after execution. If this action is not used manually while the Automaton Queen is active, it will be triggered automatically immediately before shutting down.
    # Shares a recast timer with Automaton Queen.
    id = 16502
    names = ['超档后式人偶(MCH)', 'Queen Overdrive(MCH)']
    _orig_names = ['Queen Overdrive', '超档后式人偶']
    damage = 650


class Action16503(Action):
    # 对目标发动物理攻击
    # 威力：650
    # 该技能的威力受设置后式自走人偶时消耗的电能影响
    # (job==31?(level>=86?:发动后后式自走人偶消失
    # ):发动后后式自走人偶消失
    # )所有者使用超档后式人偶或后式自走人偶的运转时间结束时，后式自走人偶会自动执行该技能
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 650.
    # Potency increases as Battery Gauge exceeds required cost at time of deployment.
    # (job==31?(level>=86?:The Automaton Queen shuts down after execution. ):The Automaton Queen shuts down after execution. )If this action is not used manually while the Automaton Queen is active, it will be triggered automatically immediately before shutting down.
    # ※This action cannot be assigned to a hotbar.
    id = 16503
    names = ['Pile Bunker(MCH)', '打桩枪(MCH)']
    _orig_names = ['打桩枪', 'Pile Bunker']
    damage = 650


class Action16504(Action):
    # 对目标发动物理攻击
    # 威力：120
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 120.
    # ※This action cannot be assigned to a hotbar.
    id = 16504
    names = ['Arm Punch(MCH)', '铁臂拳(MCH)']
    _orig_names = ['Arm Punch', '铁臂拳']
    damage = 120


class Action16766(Action):
    # 令敌人附加的野火状态结束，对敌人造成伤害
    # ※该技能无法设置到热键栏
    # Ends the effect of Wildfire, dealing damage to the target.
    # ※This action cannot be assigned to a hotbar.
    # related: [野火(0)](Status1946), [野火(1)](Status1323), [野火(2)](Status861), 
    id = 16766
    names = ['Detonator(MCH)', '起爆(MCH)']
    _orig_names = ['起爆', 'Detonator']


class Action16889(Action):
    # 一定时间内，令自身和周围队员所受到的伤害减轻10%
    # 持续时间：15秒
    # 无法与吟游诗人的行吟、舞者的防守之桑巴效果共存
    # Reduces damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # Effect cannot be stacked with bard's Troubadour or dancer's Shield Samba.
    # related: [策动(0)](Status2177), [防守之桑巴](Status1826), [策动(1)](Status1197), [行吟](Status1934), [策动(2)](Status1951), 
    id = 16889
    names = ['策动(MCH)', 'Tactician(MCH)']
    _orig_names = ['Tactician', '策动']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action17206(Action):
    # 冲向目标并发动物理攻击
    # 威力：240
    # ※该技能无法设置到热键栏
    # Rushes target and delivers an attack with a potency of 240.
    # ※This action cannot be assigned to a hotbar.
    id = 17206
    names = ['Roller Dash(MCH)', '滚轮冲(MCH)']
    _orig_names = ['Roller Dash', '滚轮冲']
    damage = 240


class Action17209(Action):
    # 进入过热状态
    # 效果时间内，自身发动的单体战技威力提高20
    # 持续时间：8秒
    # 仅对机工士特职技能有效
    # 发动条件：枪管热度50点
    # Releases the energy building in your firearm, causing it to become Overheated, increasing the potency of single-target weaponskills by 20.
    # Duration: 8s
    # Heat Gauge Cost: 50
    # Overheated effect only applicable to machinist job actions.
    # related: [超荷](Status688), 
    id = 17209
    names = ['Hypercharge(MCH)', '超荷(MCH)']
    _orig_names = ['Hypercharge', '超荷']


class Action17749(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 2,000.
    # This action does not share a recast timer with any other actions.
    id = 17749
    names = ['钻头(pvp)(MCH)', 'Drill(pvp)(MCH)']
    _orig_names = ['钻头(pvp)', 'Drill(pvp)']
    damage = 2000


class Action17750(Action):
    # 对目标发动物理攻击
    # 威力：2000
    # 追加效果：获得20点枪管热度
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 2,000.
    # Additional Effect: Increases Heat Gauge by 20
    # This action does not share a recast timer with any other actions.
    id = 17750
    names = ['空气锚(pvp)(MCH)', 'Air Anchor(pvp)(MCH)']
    _orig_names = ['空气锚(pvp)', 'Air Anchor(pvp)']
    damage = 2000


class Action17751(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1600
    # 发动条件：过热状态
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,600 to all enemies in a cone before you.
    # Can only be executed when firearm is Overheated.
    # ※This action cannot be assigned to a hotbar.
    id = 17751
    names = ['Auto Crossbow(pvp)(MCH)', '自动弩(pvp)(MCH)']
    _orig_names = ['自动弩(pvp)', 'Auto Crossbow(pvp)']
    damage = 1600


class Action17752(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：1600
    # 追加效果：令目标受到的伤害提高10%
    # 持续时间：10秒
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 1,600 to all enemies in a cone before you.
    # Additional Effect: Increases target's damage taken by 10%
    # Duration: 10s
    # This action does not share a recast timer with any other actions.
    # related: [毒菌冲击(0)](Status1866), [毒菌冲击(1)](Status2019), 
    id = 17752
    names = ['Bioblaster(pvp)(MCH)', '毒菌冲击(pvp)(MCH)']
    _orig_names = ['Bioblaster(pvp)', '毒菌冲击(pvp)']
    damage = 1600
    # remain metas: {'taken_dmg_increase': '10%'}


class Action17753(Action):
    # 对目标及其周围的敌人发动范围物理攻击
    # 威力：800
    # 积蓄次数：3
    # Delivers an attack with a potency of 800 to target and all enemies nearby it.
    # Maximum Charges: 3
    id = 17753
    names = ['Ricochet(pvp)(MCH)', '弹射(pvp)(MCH)']
    _orig_names = ['弹射(pvp)', 'Ricochet(pvp)']
    damage = 800


class Action17754(Action):
    # 进入过热状态
    # 持续时间：5秒
    # 若自身已处于过热状态，则将持续时间延长5秒
    # 最多可延长至10秒
    # 发动条件：枪管热度50点
    # Release the energy building in your firearm, causing it to become Overheated.
    # Duration: 5s
    # Extends Overheated duration by 5s to a maximum of 10s.
    # Heat Gauge Cost: 50
    # related: [超荷](Status688), 
    id = 17754
    names = ['超荷(pvp)(MCH)', 'Hypercharge(pvp)(MCH)']
    _orig_names = ['超荷(pvp)', 'Hypercharge(pvp)']


class Action18932(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：800
    # 追加效果：每命中一个目标获得5点枪管热度
    # ※“过热”状态中该技能变为“自动弩”
    # Delivers an attack with a potency of 800 to all enemies in a cone before you.
    # Additional Effect: Increases Heat Gauge by 5 for each enemy hit
    # ※Action changes to Auto Crossbow when firearm is Overheated.
    id = 18932
    names = ['Spread Shot(pvp)(MCH)', '散射(pvp)(MCH)']
    _orig_names = ['Spread Shot(pvp)', '散射(pvp)']
    damage = 800


class Action18933(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 积蓄次数：3
    # Delivers an attack with a potency of 1,200.
    # Maximum Charges: 3
    id = 18933
    names = ['Gauss Round(pvp)(MCH)', '虹吸弹(pvp)(MCH)']
    _orig_names = ['Gauss Round(pvp)', '虹吸弹(pvp)']
    damage = 1200


class Action18934(Action):
    # 一定时间内令自己与周围队员受到的伤害减轻10%
    # 持续时间：15秒
    # Reduces damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # related: [策动(0)](Status2177), [策动(1)](Status1197), [策动(2)](Status1951), 
    id = 18934
    names = ['Tactician(pvp)(MCH)', '策动(pvp)(MCH)']
    _orig_names = ['Tactician(pvp)', '策动(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action25786(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：150
    # 追加效果：获得10点枪管热度
    # Delivers an attack with a potency of 150 to all enemies in a cone before you.
    # Additional Effect: Increases Heat Gauge by 10
    id = 25786
    names = ['霰弹枪(MCH)', 'Scattergun(MCH)']
    _orig_names = ['Scattergun', '霰弹枪']
    damage = 150


class Action25787(Action):
    # 对目标发动物理攻击
    # 威力：750
    # 该技能的威力受设置后式自走人偶时消耗的电能影响
    # 发动后后式自走人偶消失
    # 所有者使用超档后式人偶或后式自走人偶的运转时间结束时，后式自走人偶会自动执行该技能
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 750.
    # Potency increases as Battery Gauge exceeds required cost at time of deployment.
    # The Automaton Queen shuts down after execution. If this action is not used manually while the Automaton Queen is active, it will be triggered automatically immediately before shutting down.
    # ※This action cannot be assigned to a hotbar.
    id = 25787
    names = ['王室对撞机(MCH)', 'Crowned Collider(MCH)']
    _orig_names = ['王室对撞机', 'Crowned Collider']
    damage = 750


class Action25788(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：570
    # 攻击复数敌人时，对目标之外的敌人威力降低65%
    # 追加效果：获得20点电能
    # 该战技有单独计算的复唱时间
    # Delivers an attack to all enemies in a straight line before you with a potency of 570 for the first enemy, and 65% less for all remaining enemies.
    # Additional Effect: Increases Battery Gauge by 20
    # This weaponskill does not share a recast timer with any other actions.
    id = 25788
    names = ['Chain Saw(MCH)', '回转飞锯(MCH)']
    _orig_names = ['Chain Saw', '回转飞锯']
    damage = 570
    # remain metas: {'aoe_reduce': '65%'}


