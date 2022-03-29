from ._base import *


class Status742(Status):
    # 自身的战技及魔法命中时可以恢复魔力
    # 习得暗血II后追加效果：自身的战技及魔法命中时可以获得暗血
    # Absorbing MP upon landing weaponskills or spells.
    # Enhanced Blackblood Effect: Increasing Blood Gauge upon landing weaponskills or spells.
    # related: [嗜血(DRK)](Action3625),
    id = 742
    names = ['嗜血', 'Blood Weapon']


class Status1397(Status):
    # 以攻击力降低为代价减少自身所受到的伤害
    # Damage dealt and taken are reduced.
    # related: [深恶痛绝(DRK)](Action3629),
    id = 1397
    names = ['深恶痛绝', 'Grit']


class Status746(Status):
    # 减轻所受到的魔法伤害
    # Magic damage taken is reduced.
    # related: [弃明投暗(DRK)](Action3634),
    id = 746
    names = ['弃明投暗', 'Dark Mind']


class Status747(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [暗影墙(DRK)](Action3636),
    id = 747
    names = ['暗影墙', 'Shadow Wall']


class Status810(Status):
    # 受到致命伤害时体力减为1，并附加死而不僵状态
    # 但是对部分攻击无效
    # Unable to be KO'd by most attacks. Status changed to Walking Dead in most cases when HP is reduced to 0.
    # related: [行尸走肉(DRK)](Action3638),
    id = 810
    names = ['行尸走肉', 'Living Dead']


class Status811(Status):
    # 除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下，在效果结束前没有得到足够的治疗便会陷入无法战斗状态
    # Most attacks will not reduce HP below 1. The inability to restore 100% of HP before timer runs out will result in KO.
    # related: [行尸走肉(DRK)](Action3638),
    id = 811
    names = ['死而不僵', 'Walking Dead']


class Status749(Status):
    # 在地上产生造成无属性伤害的危险区
    # The ground is rendered void of all life, dealing unaspected damage to any who tread upon it.
    # related: [腐秽大地(DRK)](Action3639), [腐秽黑暗(DRK)](Action25755),
    id = 749
    names = ['腐秽大地', 'Salted Earth']


class Status1972(Status):
    # 不需要消耗暗血就可以发动血溅和寂灭
    # Blackblood cost for Bloodspiller and Quietus is nullified.
    # related: [血乱(DRK)](Action7390), [血乱(pvp)(DRK)](Action17702),
    id = 1972
    names = ['血乱', 'Delirium']


class Status748(Status):
    # 智力降低
    # Intelligence is reduced.
    # related: [血乱(DRK)](Action7390), [血乱(pvp)(DRK)](Action17702),
    id = 748
    names = ['错乱剑', 'Delirium(1)']


# class Status1996(Status):
#     # 不消耗暗血
#     # Blackblood cost is nullified.
#     # related: [血乱(DRK)](Action7390), [血乱(pvp)(DRK)](Action17702),
#     id = 1996
#     names = ['血乱(1)', 'Delirium(2)']


class Status752(Status):
    # 强化下次发动的特定技能
    # Potency of certain dark knight actions is enhanced.
    # related: [至黑之夜(DRK)](Action7393), [至黑之夜(pvp)(DRK)](Action8779),
    id = 752
    names = ['暗技', 'Dark Arts']


class Status1178(Status):
    # 抵消一定伤害
    # An all-encompassing darkness is nullifying damage.
    # related: [至黑之夜(DRK)](Action7393), [至黑之夜(pvp)(DRK)](Action8779),
    id = 1178
    names = ['至黑之夜(0)', 'Blackest Night(0)']


class Status1308(Status):
    # 抵消一定伤害
    # An all-encompassing darkness is nullifying damage.
    # related: [至黑之夜(DRK)](Action7393), [至黑之夜(pvp)(DRK)](Action8779),
    id = 1308
    names = ['至黑之夜(1)', 'Blackest Night(1)']


class Status751(Status):
    # 以战斗中不会自动恢复魔力为代价提高攻击造成的伤害
    # Damage dealt is increased while MP regeneration is stopped.
    # related: [暗黑波动(DRK)](Action16466), [暗黑锋(DRK)](Action16467), [暗影波动(DRK)](Action16469), [暗影锋(DRK)](Action16470), [暗影锋(pvp)(DRK)](Action17701), [暗影波动(pvp)(DRK)](Action18908), [暗影使者(DRK)](Action25757),
    id = 751
    names = ['暗黑', 'Darkside']


class Status2170(Status):
    # 自身所受的体力恢复效果降低
    # HP recovery via healing actions is reduced.
    # related: [暗影波动(DRK)](Action16469), [暗影波动(pvp)(DRK)](Action18908),
    id = 2170
    names = ['暗影波动', 'Flood of Shadow']


class Status2102(Status):
    # 自身所受的体力恢复效果降低
    # HP recovery is reduced.
    # related: [暗影锋(DRK)](Action16470), [暗影锋(pvp)(DRK)](Action17701),
    id = 2102
    names = ['暗影锋', 'Edge of Shadow']


class Status2171(Status):
    # 减轻所受到的伤害，自身所受体力恢复效果提高
    # Damage taken is reduced while HP recovered via healing actions is increased.
    # related: [暗黑布道(DRK)](Action16471), [暗黑布道(pvp)(DRK)](Action18909),
    id = 2171
    names = ['暗黑布道(0)', 'Dark Missionary(0)']


class Status1894(Status):
    # 减轻所受到的魔法伤害
    # Magic damage taken is reduced.
    # related: [暗黑布道(DRK)](Action16471), [暗黑布道(pvp)(DRK)](Action18909),
    id = 1894
    names = ['暗黑布道(1)', 'Dark Missionary(1)']


class Status2682(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [献奉(DRK)](Action25754),
    id = 2682
    names = ['献奉', 'Oblation']


class Action3617(Action):
    # 对目标发动物理攻击
    # 威力：(job==32?(level>=84?170:150):150)
    # Delivers an attack with a potency of (job==32?(level>=84?170:150):150).
    id = 3617
    names = ['重斩(DRK)', 'Hard Slash(DRK)']
    _orig_names = ['Hard Slash', '重斩']
    damage = "(job==32?(lv>=84?170:150):150)"


class Action3621(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：120
    # Deals unaspected damage with a potency of 120 to all nearby enemies.
    id = 3621
    names = ['Unleash(DRK)', '释放(DRK)']
    _orig_names = ['释放', 'Unleash']
    damage = 120


class Action3623(Action):
    # 对目标发动物理攻击
    # 威力：(job==32?(level>=84?120:100):100)
    # 连击条件：重斩
    # 连击中威力：(job==32?(level>=84?260:240):240)
    # 连击成功：恢复自身魔力
    # Delivers an attack with a potency of (job==32?(level>=84?120:100):100).
    # Combo Action: Hard Slash
    # Combo Potency: (job==32?(level>=84?260:240):240)
    # Combo Bonus: Restores MP
    id = 3623
    names = ['吸收斩(DRK)', 'Syphon Strike(DRK)']
    _orig_names = ['Syphon Strike', '吸收斩']
    combo_action = 3617
    damage = "(job==32?(lv>=84?120:100):100)"
    combo_damage = "(job==32?(lv>=84?260:240):240)"


class Action3624(Action):
    # 对目标发动无属性魔法攻击
    # 威力：150
    # 追加效果：提升仇恨(job==32?(level>=84?
    # 追加效果：跳斩的复唱时间缩短5秒:):)
    # Deals unaspected damage with a potency of 150.
    # Additional Effect: Increased enmity(job==32?(level>=84?
    # Additional Effect: Reduces the recast time of Plunge by 5 seconds:):)
    id = 3624
    names = ['Unmend(DRK)', '伤残(DRK)']
    _orig_names = ['伤残', 'Unmend']
    damage = 150


class Action3625(Action):
    # 一定时间内，自身的战技及魔法命中时可以恢复魔力
    # (level>=66?(job==32?同时获得10点暗血
    # :):)当范围攻击命中复数敌人时，效果只发动1次
    # 持续时间：10秒
    # (level>=66?(job==32?Increases Blood Gauge by 10 and restores MP:Restores MP):Restores MP) upon landing weaponskills or spells.
    # Effect does not stack when hitting multiple targets with a single attack.
    # Duration: 10s
    # related: [嗜血](Status742),
    id = 3625
    names = ['嗜血(DRK)', 'Blood Weapon(DRK)']
    _orig_names = ['嗜血', 'Blood Weapon']


class Action3629(Action):
    # 极大幅度增加战斗时获得的仇恨量
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Significantly increases enmity generation.
    # Effect ends upon reuse.
    # related: [深恶痛绝](Status1397),
    id = 3629
    names = ['深恶痛绝(DRK)', 'Grit(DRK)']
    _orig_names = ['Grit', '深恶痛绝']


class Action3632(Action):
    # 对目标发动物理攻击
    # 威力：(job==32?(level>=84?120:100):100)
    # 连击条件：吸收斩
    # 连击中威力：(job==32?(level>=84?340:320):320)
    # 连击成功：恢复自身体力
    # 恢复力：300
    # (level>=62?(job==32?连击成功：获得20点暗血:):)
    # Delivers an attack with a potency of (job==32?(level>=84?120:100):100).
    # Combo Action: Syphon Strike
    # Combo Potency: (job==32?(level>=84?340:320):320)
    # Combo Bonus: Restores own HP
    # Cure Potency: 300(level>=62?(job==32?
    # Combo Bonus: Increases Blood Gauge by 20:):)
    id = 3632
    names = ['Souleater(DRK)', '噬魂斩(DRK)']
    _orig_names = ['噬魂斩', 'Souleater']
    combo_action = 3623
    damage = "(job==32?(lv>=84?120:100):100)"
    combo_damage = "(job==32?(lv>=84?340:320):320)"
    heal = 300


class Action3634(Action):
    # 一定时间内，令自身所受到的魔法伤害减轻20%
    # 持续时间：10秒
    # Reduces magic vulnerability by 20%.
    # Duration: 10s
    # related: [弃明投暗](Status746),
    id = 3634
    names = ['Dark Mind(DRK)', '弃明投暗(DRK)']
    _orig_names = ['Dark Mind', '弃明投暗']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action3636(Action):
    # 一定时间内，自身受到的伤害减轻30%
    # 持续时间：15秒
    # Reduces damage taken by 30%.
    # Duration: 15s
    # related: [暗影墙](Status747),
    id = 3636
    names = ['暗影墙(DRK)', 'Shadow Wall(DRK)']
    _orig_names = ['Shadow Wall', '暗影墙']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action3638(Action):
    # 对自身附加行尸走肉状态
    # 效果中受到致命伤也不会陷入无法战斗状态，代价是自身体力降为1且该状态变为死而不僵状态
    # 持续时间：10秒
    # 死而不僵效果：所有对自身发动的攻击均无法令体力减少到1以下
    # 效果中得到相当于自身最大体力100%的恢复量即可解除该状态
    # 如恢复量不足以解除状态直到持续时间结束，自身将陷入无法战斗状态
    # 持续时间：10秒
    # 以上两种状态均对部分攻击无效
    # Grants the effect of Living Dead. When HP is reduced to 0 while under the effect of Living Dead, instead of becoming KO'd, your status will change to Walking Dead.
    # Living Dead Duration: 10s
    # While under the effect of Walking Dead, most attacks will not lower your HP below 1. If, before the Walking Dead timer runs out, HP is 100% restored, the effect will fade. If 100% is not restored, you will be KO'd.
    # Walking Dead Duration: 10s
    # related: [行尸走肉](Status810), [死而不僵](Status811),
    id = 3638
    names = ['行尸走肉(DRK)', 'Living Dead(DRK)']
    _orig_names = ['行尸走肉', 'Living Dead']


class Action3639(Action):
    # 以自身脚下为中心产生腐秽区域
    # 所有进入该区域的目标都会受到无属性伤害
    # 威力：50
    # 持续时间：15秒(job==32?(level>=86?
    # 该技能发动后变为腐秽黑暗:):)
    # Creates a patch of salted earth at your feet, dealing unaspected damage with a potency of 50 to any enemies who enter.
    # Duration: 15s(job==32?(level>=86?
    # ※Action changes to Salt and Darkness upon execution.:):)
    # related: [腐秽大地](Status749),
    id = 3639
    names = ['腐秽大地(DRK)', 'Salted Earth(DRK)']
    _orig_names = ['Salted Earth', '腐秽大地']
    damage = 50


class Action3640(Action):
    # 跃向目标并发动物理攻击
    # 威力：150
    # (job==32?(level>=78?积蓄次数：2
    # :):)止步状态下无法发动
    # Delivers a jumping attack with a potency of 150.
    # (job==32?(level>=78?Maximum Charges: 2
    # :):)Cannot be executed while bound.
    id = 3640
    names = ['跳斩(DRK)', 'Plunge(DRK)']
    _orig_names = ['Plunge', '跳斩']
    damage = 150


class Action3641(Action):
    # 以目标为中心发动无属性范围魔法攻击
    # 威力：150
    # 追加效果：恢复自身体力
    # 恢复力：200
    # 追加效果：恢复自身魔力
    # 与精雕怒斩共享复唱时间
    # Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
    # Additional Effect: Restores own HP
    # Cure Potency: 200
    # Additional Effect: Restores MP
    # Shares a recast timer with Carve and Spit.
    id = 3641
    names = ['Abyssal Drain(DRK)', '吸血深渊(DRK)']
    _orig_names = ['Abyssal Drain', '吸血深渊']
    damage = 150
    heal = 200


class Action3643(Action):
    # 对目标发动物理攻击
    # 威力：510
    # 追加效果：恢复自身魔力
    # 与吸血深渊共享复唱时间
    # Delivers a threefold attack with a potency of 510.
    # Additional Effect: Restores MP
    # Shares a recast timer with Abyssal Drain.
    id = 3643
    names = ['Carve and Spit(DRK)', '精雕怒斩(DRK)']
    _orig_names = ['Carve and Spit', '精雕怒斩']
    damage = 510


class Action7390(Action):
    # 为自身附加3档血乱状态
    # 持续时间：15秒
    # 血乱效果：一定时间内，不需要消耗暗血就可以发动寂灭和血溅
    # 寂灭和血溅命中时恢复自身魔力
    # Grants 3 stacks of Delirium, each stack allowing the execution of Quietus or Bloodspiller without Blackblood cost, restoring MP when landing either weaponskill.
    # Duration: 15s
    # related: [血乱(0)](Status1972), [错乱剑](Status748), [血乱(1)](Status1996),
    id = 7390
    names = ['血乱(DRK)', 'Delirium(DRK)']
    _orig_names = ['血乱', 'Delirium']


class Action7391(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：200
    # 发动条件：暗血50点
    # Delivers an attack with a potency of 200 to all nearby enemies.
    # Blood Gauge Cost: 50
    id = 7391
    names = ['Quietus(DRK)', '寂灭(DRK)']
    _orig_names = ['Quietus', '寂灭']
    damage = 200


class Action7392(Action):
    # 对目标发动物理攻击
    # 威力：500
    # 发动条件：暗血50点
    # Delivers an attack with a potency of 500.
    # Blood Gauge Cost: 50
    id = 7392
    names = ['Bloodspiller(DRK)', '血溅(DRK)']
    _orig_names = ['Bloodspiller', '血溅']
    damage = 500


class Action7393(Action):
    # 为自身或一名队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力25%的伤害量
    # 持续时间：7秒
    # 防护罩因吸收到足够的伤害而消失时，暗黑骑士自身附加暗技状态
    # 暗技效果：用暗技代替魔力发动(job==32?(level>=74?暗影波动及暗影锋:暗黑波动及暗黑锋):暗黑波动及暗黑锋)
    # Creates a barrier around target that absorbs damage totaling 25% of target's maximum HP.
    # Duration: 7s
    # Grants Dark Arts when barrier is completely absorbed.
    # Dark Arts Effect: Consume Dark Arts instead of MP to execute (job==32?(level>=74?Edge of Shadow or Flood of Shadow:Edge of Darkness or Flood of Darkness):Edge of Darkness or Flood of Darkness)
    # related: [暗技](Status752), [至黑之夜(0)](Status1178), [至黑之夜(1)](Status1308),
    id = 7393
    names = ['The Blackest Night(DRK)', '至黑之夜(DRK)']
    _orig_names = ['The Blackest Night', '至黑之夜']
    # remain metas: {'shield': '目标最大体力25%'}


class Action8769(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # ※该技能无法设置到热键栏
    # Delivers an attack with a potency of 1,000.
    # ※This action cannot be assigned to a hotbar.
    id = 8769
    names = ['重斩(pvp)(DRK)', 'Hard Slash(pvp)(DRK)']
    _orig_names = ['重斩(pvp)', 'Hard Slash(pvp)']
    damage = 1000


class Action8772(Action):
    # 对目标发动物理攻击
    # 连击中威力：1200
    # 连击条件：重斩
    # 连击成功：恢复500点魔力
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Hard Slash
    # Combo Potency: 1,200
    # Combo Bonus: Restores 500 MP
    # ※This action cannot be assigned to a hotbar.
    id = 8772
    names = ['吸收斩(pvp)(DRK)', 'Syphon Strike(pvp)(DRK)']
    _orig_names = ['吸收斩(pvp)', 'Syphon Strike(pvp)']
    combo_action = 8769
    combo_damage = 1200


class Action8773(Action):
    # 对目标发动物理攻击
    # 连击中威力：1400
    # 连击条件：吸收斩
    # 连击成功：恢复伤害量100%的体力
    # 连击成功：获得25点暗血
    # ※该技能无法设置到热键栏
    # Delivers an attack to target.
    # Combo Action: Syphon Strike
    # Combo Potency: 1,400
    # Combo Bonus: Absorbs 100% of damage dealt as HP
    # Combo Bonus: Increases Blood Gauge by 25
    # ※This action cannot be assigned to a hotbar.
    id = 8773
    names = ['噬魂斩(pvp)(DRK)', 'Souleater(pvp)(DRK)']
    _orig_names = ['噬魂斩(pvp)', 'Souleater(pvp)']
    combo_action = 8772
    combo_damage = 1400


class Action8775(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：获得10点暗血
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Increases Blood Gauge by 10
    id = 8775
    names = ['伤残(pvp)(DRK)', 'Unmend(pvp)(DRK)']
    _orig_names = ['Unmend(pvp)', '伤残(pvp)']
    damage = 800


class Action8776(Action):
    # 对目标发动物理攻击
    # 威力：1800
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：恢复500点魔力
    # 发动条件：暗血50点
    # Delivers an attack with a potency of 1,800.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Restores 500 MP
    # Blood Gauge Cost: 50
    id = 8776
    names = ['Bloodspiller(pvp)(DRK)', '血溅(pvp)(DRK)']
    _orig_names = ['Bloodspiller(pvp)', '血溅(pvp)']
    damage = 1800


class Action8777(Action):
    # 冲向目标并发动物理攻击
    # 威力：600
    # 击倒敌人或拿到助攻时重置复唱时间
    # 止步状态下无法发动
    # Rushes target and delivers an attack with a potency of 600.
    # Recast time is reset if Plunge records a KO or an assist.
    # Cannot be executed while bound.
    id = 8777
    names = ['跳斩(pvp)(DRK)', 'Plunge(pvp)(DRK)']
    _orig_names = ['跳斩(pvp)', 'Plunge(pvp)']
    damage = 600


class Action8779(Action):
    # 为自身或目标队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力3000的伤害量
    # 持续时间：6秒
    # 防护罩因吸收到足够的伤害而消失时，暗黑骑士自身附加暗技状态
    # 暗技效果：用暗技代替魔力发动暗影锋及暗影波动
    # Creates a barrier around self or target party member that absorbs damage equivalent to a heal of 3,000 potency.
    # Duration: 6s
    # Grants Dark Arts when barrier is completely absorbed.
    # Dark Arts Effect: Consume Dark Arts instead of MP to execute Edge of Shadow or Flood of Shadow
    # related: [暗技](Status752), [至黑之夜(0)](Status1178), [至黑之夜(1)](Status1308),
    id = 8779
    names = ['The Blackest Night(pvp)(DRK)', '至黑之夜(pvp)(DRK)']
    _orig_names = ['The Blackest Night(pvp)', '至黑之夜(pvp)']
    # remain metas: {'shield': '恢复力3000'}


class Action16466(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：130
    # 追加效果：暗黑
    # 持续时间：30秒
    # 暗黑效果：攻击伤害提高10%
    # 若自身已经附加暗黑状态，则持续时间延长30秒
    # 最多可延长至60秒
    # 与暗黑锋共享复唱时间
    # Deals unaspected damage with a potency of 130 to all enemies in a straight line before you.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Darkside duration by 30s to a maximum of 60s.
    # Shares a recast timer with Edge of Darkness.
    # related: [暗黑](Status751),
    id = 16466
    names = ['暗黑波动(DRK)', 'Flood of Darkness(DRK)']
    _orig_names = ['暗黑波动', 'Flood of Darkness']
    damage = 130
    # remain metas: {'dmg_increase': '10%'}


class Action16467(Action):
    # 对目标发动无属性魔法攻击
    # 威力：300
    # 追加效果：暗黑
    # 持续时间：30秒
    # 暗黑效果：攻击伤害提高10%
    # 若自身已经附加暗黑状态，则持续时间延长30秒
    # 最多可延长至60秒
    # 与暗黑波动共享复唱时间
    # Deals unaspected damage with a potency of 300.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Darkside duration by 30s to a maximum of 60s.
    # Shares a recast timer with Flood of Darkness.
    # related: [暗黑](Status751),
    id = 16467
    names = ['暗黑锋(DRK)', 'Edge of Darkness(DRK)']
    _orig_names = ['Edge of Darkness', '暗黑锋']
    damage = 300
    # remain metas: {'dmg_increase': '10%'}


class Action16468(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：100
    # 连击条件：释放
    # 连击中威力：140
    # 连击成功：恢复自身魔力
    # 连击成功：获得20点暗血
    # Deals unaspected damage with a potency of 100 to all nearby enemies.
    # Combo Action: Unleash
    # Combo Potency: 140
    # Combo Bonus: Restores MP
    # Combo Bonus: Increases Blood Gauge by 20
    id = 16468
    names = ['刚魂(DRK)', 'Stalwart Soul(DRK)']
    _orig_names = ['Stalwart Soul', '刚魂']
    combo_action = 3621
    damage = 100
    combo_damage = 140


class Action16469(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：160
    # 追加效果：暗黑
    # 持续时间：30秒
    # 暗黑效果：攻击伤害提高10%
    # 若自身已经附加暗黑状态，则持续时间延长30秒
    # 最多可延长至60秒
    # 与暗影锋共享复唱时间
    # Deals unaspected damage with a potency of 160 to all enemies in a straight line before you.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Darkside duration by 30s to a maximum of 60s.
    # Shares a recast timer with Edge of Shadow.
    # related: [暗影波动](Status2170), [暗黑](Status751),
    id = 16469
    names = ['Flood of Shadow(DRK)', '暗影波动(DRK)']
    _orig_names = ['Flood of Shadow', '暗影波动']
    damage = 160
    # remain metas: {'dmg_increase': '10%'}


class Action16470(Action):
    # 对目标发动无属性魔法攻击
    # 威力：460
    # 追加效果：暗黑
    # 持续时间：30秒
    # 暗黑效果：攻击伤害提高10%
    # 若自身已经附加暗黑状态，则持续时间延长30秒
    # 最多可延长至60秒
    # 与暗影波动共享复唱时间
    # Deals unaspected damage with a potency of 460.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 30s
    # Extends Darkside duration by 30s to a maximum of 60s.
    # Shares a recast timer with Flood of Shadow.
    # related: [暗影锋](Status2102), [暗黑](Status751),
    id = 16470
    names = ['暗影锋(DRK)', 'Edge of Shadow(DRK)']
    _orig_names = ['暗影锋', 'Edge of Shadow']
    damage = 460
    # remain metas: {'dmg_increase': '10%'}


class Action16471(Action):
    # 一定时间内，令自身和周围队员所受到的魔法伤害减轻10%
    # 持续时间：15秒
    # Reduces magic damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # related: [暗黑布道(0)](Status2171), [暗黑布道(1)](Status1894),
    id = 16471
    names = ['Dark Missionary(DRK)', '暗黑布道(DRK)']
    _orig_names = ['Dark Missionary', '暗黑布道']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action16472(Action):
    # 令“英雄的掠影”变为实体与自身并肩作战
    # 持续时间：24秒
    # 英雄的掠影的攻击威力：(job==32?(level>=88?300:240):240)
    # (job==32?(level>=90?暗影使者的威力固定
    # 英雄的掠影发动暗影使者的威力：450
    # 攻击复数敌人时，对目标之外的敌人威力降低25%
    # :):)发动条件：暗血50点
    # Conjure a simulacrum of your darkside to fight alongside you.
    # Simulacrum Attack Potency: (job==32?(level>=88?300:240):240)
    # Duration: 24s
    # Blood Gauge Cost: 50
    # (job==32?(level>=90?Additional Effect: Simulacrum is able to execute Shadowbringer, delivering an attack to all enemies in a straight line before it with a potency of 450 for the first enemy, and 25% less for all remaining enemies.:):)
    id = 16472
    names = ['掠影示现(DRK)', 'Living Shadow(DRK)']
    _orig_names = ['Living Shadow', '掠影示现']
    # remain metas: {'dmg_ot': '(job==32?(lv>=88?300:240):240)'}


class Action17700(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：1000
    # 追加效果：恢复伤害量100%的体力
    # 追加效果：每命中一个目标都会恢复250点魔力
    # 发动条件：暗血50点
    # Delivers an attack with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Absorbs 100% of damage dealt as HP
    # Additional Effect: Restores 250 MP for each enemy hit
    # Blood Gauge Cost: 50
    id = 17700
    names = ['Quietus(pvp)(DRK)', '寂灭(pvp)(DRK)']
    _orig_names = ['Quietus(pvp)', '寂灭(pvp)']
    damage = 1000


class Action17701(Action):
    # 对目标发动无属性魔法攻击
    # 威力：1000
    # 追加效果：暗黑
    # 持续时间：15秒
    # 暗黑效果：攻击伤害提高10%
    # 追加效果：目标所受到的恢复效果减少10%
    # 持续时间：10秒
    # 暗黑状态中追加效果：暗黑 持续时间延长15秒
    # 最多可延长至30秒
    # Deals unaspected damage with a potency of 1,000.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 15s
    # Additional Effect: Reduces target's HP recovered by healing actions by 10%
    # Duration: 10s
    # Extends Darkside duration by 15s, to a maximum of 30s.
    # related: [暗影锋](Status2102), [暗黑](Status751),
    id = 17701
    names = ['暗影锋(pvp)(DRK)', 'Edge of Shadow(pvp)(DRK)']
    _orig_names = ['暗影锋(pvp)', 'Edge of Shadow(pvp)']
    damage = 1000
    # remain metas: {'dmg_increase': '10%'}


class Action17702(Action):
    # 不需要消耗暗血就可以发动寂灭和血溅
    # 持续时间：6秒
    # Allows the execution of Quietus and Bloodspiller without cost.
    # Duration: 6s
    # related: [血乱(0)](Status1972), [错乱剑](Status748), [血乱(1)](Status1996),
    id = 17702
    names = ['血乱(pvp)(DRK)', 'Delirium(pvp)(DRK)']
    _orig_names = ['血乱(pvp)', 'Delirium(pvp)']


class Action18906(Action):
    # 对自身周围的敌人发动魔法攻击
    # 威力：600
    # 追加效果：每命中一个目标恢复自身魔力250点
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 600 to all nearby enemies.
    # Additional Effect: Restores 250 MP for each enemy hit
    # ※This action cannot be assigned to a hotbar.
    id = 18906
    names = ['Unleash(pvp)(DRK)', '释放(pvp)(DRK)']
    _orig_names = ['释放(pvp)', 'Unleash(pvp)']
    damage = 600


class Action18907(Action):
    # 对自身周围的敌人发动魔法攻击
    # 连击中威力：800
    # 连击条件：释放
    # 连击成功：恢复伤害量100%的体力
    # 连击成功：获得25点暗血
    # ※该技能无法设置到热键栏
    # Deals unaspected damage to all nearby enemies.
    # Combo Action: Unleash
    # Combo Potency: 800
    # Combo Bonus: Absorbs 100% of damage dealt as HP
    # Combo Bonus: Increases Blood Gauge by 25
    # ※This action cannot be assigned to a hotbar.
    id = 18907
    names = ['Stalwart Soul(pvp)(DRK)', '刚魂(pvp)(DRK)']
    _orig_names = ['刚魂(pvp)', 'Stalwart Soul(pvp)']
    combo_action = 18906
    combo_damage = 800


class Action18908(Action):
    # 向目标所在方向发出直线范围魔法攻击
    # 威力：600
    # 追加效果：暗黑
    # 持续时间：15秒
    # 暗黑效果：攻击伤害提高10%
    # 追加效果：目标所受到的恢复效果降低10%
    # 持续时间：10秒
    # 若自身已经附加暗黑状态，则持续时间延长15秒
    # 最多可延长至30秒
    # Deals unaspected damage with a potency of 600 to all enemies in a straight line.
    # Additional Effect: Grants Darkside, increasing damage dealt by 10%
    # Duration: 15s
    # Additional Effect: Reduces target's HP recovered by healing actions by 10%
    # Duration: 10s
    # Extends Darkside duration by 15s, to a maximum of 30s.
    # related: [暗影波动](Status2170), [暗黑](Status751),
    id = 18908
    names = ['Flood of Shadow(pvp)(DRK)', '暗影波动(pvp)(DRK)']
    _orig_names = ['暗影波动(pvp)', 'Flood of Shadow(pvp)']
    damage = 600
    # remain metas: {'dmg_increase': '10%'}


class Action18909(Action):
    # 一定时间内，令自身和周围队员所受到的伤害减轻10%，并且所受的体力恢复效果提高10%
    # 持续时间：10秒
    # Reduces damage taken by self and nearby party members by 10%, while increasing HP recovered via healing actions by 10%.
    # Duration: 10s
    # related: [暗黑布道(0)](Status2171), [暗黑布道(1)](Status1894),
    id = 18909
    names = ['Dark Missionary(pvp)(DRK)', '暗黑布道(pvp)(DRK)']
    _orig_names = ['暗黑布道(pvp)', 'Dark Missionary(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%，并且所受的体力恢复效果提高10%'}


class Action25754(Action):
    # 令自身或一名队员受到的伤害减轻10%
    # 持续时间：10秒
    # 积蓄次数：2
    # Reduces damage taken by a party member or self by 10%.
    # Duration: 10s
    # Maximum Charges: 2
    # related: [献奉](Status2682),
    id = 25754
    names = ['献奉(DRK)', 'Oblation(DRK)']
    _orig_names = ['Oblation', '献奉']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action25755(Action):
    # 在自身设置的腐秽大地效果范围内对敌人发动无属性范围魔法攻击
    # 威力：500
    # 攻击复数敌人时，对第一个之外的敌人威力降低50%
    # 发动条件：腐秽大地状态中
    # ※该技能无法设置到热键栏
    # All enemies standing in the corrupted patch of Salted Earth take additional unaspected damage with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
    # ※This action cannot be assigned to a hotbar.
    # related: [腐秽大地](Status749),
    id = 25755
    names = ['腐秽黑暗(DRK)', 'Salt and Darkness(DRK)']
    _orig_names = ['腐秽黑暗', 'Salt and Darkness']
    damage = 500


class Action25757(Action):
    # 向目标所在方向发出无属性直线范围魔法攻击
    # 威力：600
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 积蓄次数：2
    # 发动条件：暗黑状态中
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
    # Maximum Charges: 2
    # Can only be executed while under the effect of Darkside.
    # related: [暗黑](Status751),
    id = 25757
    names = ['Shadowbringer(DRK)', '暗影使者(DRK)']
    _orig_names = ['Shadowbringer', '暗影使者']
    damage = 600
    # remain metas: {'aoe_reduce': '50%'}


