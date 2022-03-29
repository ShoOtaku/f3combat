from ._base import *


class Status826(Status):
    # 抽出一张卡片
    # An arcanum is drawn from the deck.
    # related: [抽卡(AST)](Action3590), [奥秘卡废弃(AST)](Action9629), 
    id = 826
    names = ['抽卡', 'Card Drawn']


class Status2713(Status):
    # 可以发动重抽
    # Able to execute Redraw.
    # related: [重抽(AST)](Action3593), 
    id = 2713
    names = ['重抽预备', 'Clarifying Draw']


class Status835(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [吉星相位(AST)](Action3595), [中间学派(AST)](Action16559), [吉星相位(pvp)(AST)](Action17804), 
    id = 835
    names = ['吉星相位', 'Aspected Benefic']


class Status838(Status):
    # 体力逐渐减少
    # Proximity of a theoretical sun is causing damage over time.
    # related: [烧灼(AST)](Action3599), 
    id = 838
    names = ['烧灼', 'Combust']


class Status841(Status):
    # 魔法的咏唱时间缩短
    # Spell casting time is reduced.
    # related: [光速(AST)](Action3606), 
    id = 841
    names = ['光速(0)', 'Lightspeed(0)']


class Status1403(Status):
    # 咏唱魔法不需要咏唱时间，同时消耗的魔力减半
    # Spell casting time and MP cost are reduced by 100% and 50% respectively.
    # related: [光速(AST)](Action3606), 
    id = 1403
    names = ['光速(1)', 'Lightspeed(1)']


class Status843(Status):
    # 体力逐渐减少
    # Proximity of a theoretical sun is causing damage over time.
    # related: [炽灼(AST)](Action3608), 
    id = 843
    names = ['炽灼', 'Combust II']


class Status845(Status):
    # 对队员发动单体治疗魔法时，额外恢复特定队员的体力
    # An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
    # related: [星位合图(AST)](Action3612), 
    id = 845
    names = ['星位合图(0)', 'Synastry(0)']


class Status846(Status):
    # 附加此效果的占星术士对某一队员发动单体治疗魔法时，身附此效果的队员会恢复额外的体力
    # An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
    # related: [星位合图(AST)](Action3612), 
    id = 846
    names = ['星位合图(1)', 'Synastry(1)']


class Status1336(Status):
    # 对队员发动单体治疗魔法时，额外恢复特定队员的体力
    # An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
    # related: [星位合图(AST)](Action3612), 
    id = 1336
    names = ['星位合图(2)', 'Synastry(2)']


class Status1337(Status):
    # 附加此效果的占星术士对某一队员发动单体治疗魔法时，身附此效果的队员会恢复额外的体力
    # An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
    # related: [星位合图(AST)](Action3612), 
    id = 1337
    names = ['星位合图(3)', 'Synastry(3)']


class Status2283(Status):
    # 产生减轻伤害的防护区域
    # An area of mind attunement is created, reducing damage taken for all who enter.
    # related: [命运之轮(AST)](Action3613), 
    id = 2283
    names = ['命运之轮(0)', 'Collective Unconscious(0)']


class Status847(Status):
    # 产生能够令范围内队员恢复体力的区域
    # An area of mind attunement is healing party members.
    # related: [命运之轮(AST)](Action3613), 
    id = 847
    names = ['命运之轮(1)', 'Collective Unconscious(1)']


class Status848(Status):
    # 产生减轻伤害的防护区域
    # An area of mind attunement is created, reducing damage taken for all who enter.
    # related: [命运之轮(AST)](Action3613), 
    id = 848
    names = ['命运之轮(2)', 'Collective Unconscious(2)']


class Status849(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [命运之轮(AST)](Action3613), 
    id = 849
    names = ['命运之轮(3)', 'Collective Unconscious(3)']


class Status1206(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [命运之轮(AST)](Action3613), 
    id = 1206
    names = ['命运之轮(4)', 'Wheel of Fortune(0)']


class Status956(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [命运之轮(AST)](Action3613), 
    id = 956
    names = ['命运之轮(5)', 'Wheel of Fortune(1)']


class Status1338(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [太阳神之衡(AST)](Action4401), 
    id = 1338
    names = ['太阳神之衡(0)', 'The Balance(0)']


class Status829(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [太阳神之衡(AST)](Action4401), 
    id = 829
    names = ['太阳神之衡(1)', 'The Balance(1)']


class Status1882(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [太阳神之衡(AST)](Action4401), 
    id = 1882
    names = ['太阳神之衡(2)', 'The Balance(2)']


class Status1884(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [放浪神之箭(AST)](Action4402), 
    id = 1884
    names = ['放浪神之箭(0)', 'The Arrow(0)']


class Status831(Status):
    # 自动攻击间隔缩短，同时战技与魔法的咏唱及复唱时间也会缩短
    # Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [放浪神之箭(AST)](Action4402), 
    id = 831
    names = ['放浪神之箭(1)', 'The Arrow(1)']


class Status832(Status):
    # 暴击发动率提高
    # Critical hit rate is increased.
    # related: [战争神之枪(AST)](Action4403), 
    id = 832
    names = ['战争神之枪(0)', 'The Spear(0)']


class Status1885(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [战争神之枪(AST)](Action4403), 
    id = 1885
    names = ['战争神之枪(1)', 'The Spear(1)']


class Status1339(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [世界树之干(AST)](Action4404), 
    id = 1339
    names = ['世界树之干(0)', 'The Bole(0)']


class Status1883(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [世界树之干(AST)](Action4404), 
    id = 1883
    names = ['世界树之干(1)', 'The Bole(1)']


class Status830(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [世界树之干(AST)](Action4404), 
    id = 830
    names = ['世界树之干(2)', 'The Bole(2)']


class Status833(Status):
    # 魔力持续恢复
    # Restoring MP over time.
    # related: [河流神之瓶(AST)](Action4405), 
    id = 833
    names = ['河流神之瓶(0)', 'The Ewer(0)']


class Status1340(Status):
    # 魔力持续恢复
    # Restoring MP over time.
    # related: [河流神之瓶(AST)](Action4405), 
    id = 1340
    names = ['河流神之瓶(1)', 'The Ewer(1)']


class Status1886(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [河流神之瓶(AST)](Action4405), 
    id = 1886
    names = ['河流神之瓶(2)', 'The Ewer(2)']


class Status834(Status):
    # 技力持续恢复
    # Restoring TP over time.
    # related: [建筑神之塔(AST)](Action4406), 
    id = 834
    names = ['建筑神之塔(0)', 'The Spire(0)']


class Status1341(Status):
    # 技力持续恢复
    # Restoring TP over time.
    # related: [建筑神之塔(AST)](Action4406), 
    id = 1341
    names = ['建筑神之塔(1)', 'The Spire(1)']


class Status1887(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [建筑神之塔(AST)](Action4406), 
    id = 1887
    names = ['建筑神之塔(2)', 'The Spire(2)']


class Status1224(Status):
    # 发动了地星
    # An earthly star is in your control.
    # related: [地星(AST)](Action7439), [星体爆轰(AST)](Action8324), 
    id = 1224
    names = ['地星主宰', 'Earthly Dominance']


class Status1248(Status):
    # 发动了地星
    # An earthly star is in your control.
    # related: [地星(AST)](Action7439), [星体爆轰(AST)](Action8324), 
    id = 1248
    names = ['巨星主宰', 'Giant Dominance']


class Status1451(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [王冠之领主(AST)](Action7444), [王冠之领主(pvp)(AST)](Action10028), 
    id = 1451
    names = ['王冠之领主(0)', 'Lord of Crowns(0)']


class Status1876(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [王冠之领主(AST)](Action7444), [王冠之领主(pvp)(AST)](Action10028), 
    id = 1876
    names = ['王冠之领主(1)', 'Lord of Crowns(1)']


class Status1452(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [王冠之贵妇(AST)](Action7445), [王冠之贵妇(pvp)(AST)](Action10029), 
    id = 1452
    names = ['王冠之贵妇(0)', 'Lady of Crowns(0)']


class Status1877(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [王冠之贵妇(AST)](Action7445), [王冠之贵妇(pvp)(AST)](Action10029), 
    id = 1877
    names = ['王冠之贵妇(1)', 'Lady of Crowns(1)']


class Status1921(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [吉星(pvp)(AST)](Action8913), [中间学派(AST)](Action16559), [吉星相位(pvp)(AST)](Action17804), [中间学派(pvp)(AST)](Action17809), [阳星(pvp)(AST)](Action18950), 
    id = 1921
    names = ['中间学派(0)', 'Neutral Sect(0)']


class Status1892(Status):
    # 发动治疗魔法的治疗量提高
    # Healing magic potency is increased.
    # related: [吉星(pvp)(AST)](Action8913), [中间学派(AST)](Action16559), [吉星相位(pvp)(AST)](Action17804), [中间学派(pvp)(AST)](Action17809), [阳星(pvp)(AST)](Action18950), 
    id = 1892
    names = ['中间学派(1)', 'Neutral Sect(1)']


class Status2044(Status):
    # 魔法的咏唱时间和复唱时间缩短
    # Spell cast and recast times are reduced.
    # Helios is upgraded to Aspected Helios, while Benefic is upgraded to Aspected Benefic.
    # related: [吉星(pvp)(AST)](Action8913), [中间学派(AST)](Action16559), [吉星相位(pvp)(AST)](Action17804), [中间学派(pvp)(AST)](Action17809), [阳星(pvp)(AST)](Action18950), 
    id = 2044
    names = ['中间学派(2)', 'Neutral Sect(2)']


class Status2034(Status):
    # 攻击所造成的伤害提升
    # 受到攻击的伤害减少
    # Damage dealt is increased while damage taken is reduced.
    # related: [占卜(AST)](Action16552), [占卜(pvp)(AST)](Action18941), 
    id = 2034
    names = ['占卜(0)', 'Divination(0)']


class Status1878(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [占卜(AST)](Action16552), [占卜(pvp)(AST)](Action18941), 
    id = 1878
    names = ['占卜(1)', 'Divination(1)']


class Status1879(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [天星冲日(AST)](Action16553), [天星冲日(pvp)(AST)](Action17991), 
    id = 1879
    names = ['天星冲日', 'Opposition']


class Status1881(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [焚灼(AST)](Action16554), [焚灼(pvp)(AST)](Action17806), 
    id = 1881
    names = ['焚灼(0)', 'Combust III(0)']


class Status2041(Status):
    # 发动攻击所造成的伤害及自身发动的体力恢复效果降低
    # Damage dealt and potency of all HP restoration actions are reduced.
    # related: [焚灼(AST)](Action16554), [焚灼(pvp)(AST)](Action17806), 
    id = 2041
    names = ['焚灼(1)', 'Combust III(1)']


class Status1889(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [天星交错(AST)](Action16556), 
    id = 1889
    names = ['天星交错', 'Intersection']


class Status1890(Status):
    # 可以受到天宫图带来的治疗效果
    # Primed to receive the healing effects of Horoscope.
    # related: [天宫图(AST)(0)](Action16557), [天宫图(AST)(1)](Action16558), 
    id = 1890
    names = ['天宫图', 'Horoscope']


class Status1891(Status):
    # 可以受到天宫图带来的治疗效果
    # Primed to receive the healing effects of Horoscope.
    # related: [天宫图(AST)(0)](Action16557), [天宫图(AST)(1)](Action16558), 
    id = 1891
    names = ['阳星天宫图', 'Horoscope Helios']


class Status2714(Status):
    # 魔力持续恢复
    # Restoring MP over time.
    # related: [星力(AST)](Action25870), 
    id = 2714
    names = ['魂魄之座', 'Harmony of Spirit']


class Status2715(Status):
    # 自动攻击间隔缩短，同时战技与魔法的咏唱及复唱时间也会缩短
    # Spell cast time and recast time, and auto-attack delay are reduced.
    # related: [星力(AST)](Action25870), 
    id = 2715
    names = ['身体之座', 'Harmony of Body']


class Status2716(Status):
    # 自身攻击造成的伤害与治疗效果提高
    # Damage dealt and potency of HP restoration actions are increased.
    # related: [星力(AST)](Action25870), 
    id = 2716
    names = ['精神之座', 'Harmony of Mind']


class Status2717(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [擢升(AST)](Action25873), 
    id = 2717
    names = ['擢升', 'Exaltation']


class Status2718(Status):
    # 持续时间结束或附加此效果的占星术士发动小宇宙时恢复自身体力，恢复效果量根据附加大宇宙效果后受到的伤害量而变化
    # Restores HP when effect duration expires or the astrologian who granted this effect executes Microcosmos. Healing potency is based on damage taken and compiled over the duration of the effect.
    # related: [大宇宙(AST)](Action25874), [小宇宙(AST)](Action25875), 
    id = 2718
    names = ['大宇宙', 'Macrocosmos']


class Action3590(Action):
    # 抽取一张奥秘卡
    # 出卡会变为抽到的奥秘卡技能
    # 追加效果：恢复自身最大魔力的5%
    # (job==33?(level>=40?追加效果：重抽预备
    # 持续时间：永久
    # :):)积蓄次数：2
    # Draws a card (arcanum) from your divining deck. Only one arcanum can be drawn at a time.
    # Arcanum effect can be triggered using the action Play.
    # Additional Effect: Restores 5% of maximum MP
    # (job==33?(level>=40?Additional Effect: Grants Clarifying Draw, allowing the execution of Redraw
    # :):)Maximum Charges: 2
    # related: [抽卡](Status826), 
    id = 3590
    names = ['抽卡(AST)', 'Draw(AST)']
    _orig_names = ['Draw', '抽卡']


class Action3593(Action):
    # 重新抽取一张与现有卡不同的奥秘卡
    # 发动条件：重抽预备状态中
    # Draws a different arcanum from your deck.
    # Can only be executed while under the effect of Clarifying Draw.
    # related: [重抽预备](Status2713), 
    id = 3593
    names = ['重抽(AST)', 'Redraw(AST)']
    _orig_names = ['重抽', 'Redraw']


class Action3594(Action):
    # 恢复目标的体力
    # 恢复力：(job==33?(level>=85?500:450):450)(level>=36?(job==33?
    # 追加效果（发动几率15%）：下次福星必定暴击
    # 持续时间：15秒:):)
    # Restores target's HP.
    # Cure Potency: (job==33?(level>=85?500:450):450)(level>=36?(job==33?
    # Additional Effect: 15% chance next Benefic II will restore critical HP
    # Duration: 15s:):)
    id = 3594
    names = ['Benefic(AST)', '吉星(AST)']
    _orig_names = ['Benefic', '吉星']
    heal = "(job==33?(lv>=85?500:450):450)"


class Action3595(Action):
    # 恢复目标的体力
    # 恢复力：(job==33?(level>=85?250:200):200)
    # 追加效果：令目标体力持续恢复
    # 恢复力：(job==33?(level>=85?250:200):200)
    # 持续时间：15秒
    # 
    # Restores target's HP.
    # Cure Potency: (job==33?(level>=85?250:200):200)
    # Additional Effect: Regen
    # Cure Potency: (job==33?(level>=85?250:200):200)
    # Duration: 15s
    # related: [吉星相位](Status835), 
    id = 3595
    names = ['吉星相位(AST)', 'Aspected Benefic(AST)']
    _orig_names = ['Aspected Benefic', '吉星相位']
    heal = "(job==33?(lv>=85?250:200):200)"
    # remain metas: {'heal_ot': '(job==33?(lv>=85?250:200):200)'}


class Action3596(Action):
    # 对目标发动无属性魔法攻击
    # 威力：150
    # Deals unaspected damage with a potency of 150.
    id = 3596
    names = ['凶星(AST)', 'Malefic(AST)']
    _orig_names = ['凶星', 'Malefic']
    damage = 150


class Action3598(Action):
    # 对目标发动无属性魔法攻击
    # 威力：160
    # Deals unaspected damage with a potency of 160.
    id = 3598
    names = ['Malefic II(AST)', '灾星(AST)']
    _orig_names = ['灾星', 'Malefic II']
    damage = 160


class Action3599(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：40
    # 持续时间：18秒
    # Deals unaspected damage over time.
    # Potency: 40
    # Duration: 18s
    # related: [烧灼](Status838), 
    id = 3599
    names = ['烧灼(AST)', 'Combust(AST)']
    _orig_names = ['Combust', '烧灼']
    # remain metas: {'dmg_ot': '40'}


class Action3600(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：(job==33?(level>=85?400:330):330)
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: (job==33?(level>=85?400:330):330)
    id = 3600
    names = ['Helios(AST)', '阳星(AST)']
    _orig_names = ['Helios', '阳星']
    heal = "(job==33?(lv>=85?400:330):330)"


class Action3601(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：(job==33?(level>=85?250:200):200)
    # 追加效果：令目标体力持续恢复
    # 恢复力：(job==33?(level>=85?150:100):100)
    # 持续时间：15秒
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: (job==33?(level>=85?250:200):200)
    # Additional Effect: Regen
    # Cure Potency: (job==33?(level>=85?150:100):100)
    # Duration: 15s
    # related: [阳星相位](Status836), 
    id = 3601
    names = ['阳星相位(AST)', 'Aspected Helios(AST)']
    _orig_names = ['阳星相位', 'Aspected Helios']
    heal = "(job==33?(lv>=85?250:200):200)"
    # remain metas: {'heal_ot': '(job==33?(lv>=85?150:100):100)'}


class Action3603(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43), 
    id = 3603
    names = ['生辰(AST)', 'Ascend(AST)']
    _orig_names = ['生辰', 'Ascend']


class Action3606(Action):
    # 一定时间内，自身的魔法咏唱时间缩短2.5秒
    # 持续时间：15秒
    # Reduces cast times for spells by 2.5 seconds.
    # Duration: 15s
    # related: [光速(0)](Status841), [光速(1)](Status1403), 
    id = 3606
    names = ['光速(AST)', 'Lightspeed(AST)']
    _orig_names = ['Lightspeed', '光速']


class Action3608(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：50
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 50
    # Duration: 30s
    # related: [炽灼](Status843), 
    id = 3608
    names = ['炽灼(AST)', 'Combust II(AST)']
    _orig_names = ['炽灼', 'Combust II']
    # remain metas: {'dmg_ot': '50'}


class Action3610(Action):
    # 恢复目标的体力
    # 恢复力：(job==33?(level>=85?800:700):700)
    # Restores target's HP.
    # Cure Potency: (job==33?(level>=85?800:700):700)
    id = 3610
    names = ['Benefic II(AST)', '福星(AST)']
    _orig_names = ['Benefic II', '福星']
    heal = "(job==33?(lv>=85?800:700):700)"


class Action3612(Action):
    # 指定一名队员为配对目标，在对自身或队员咏唱单体治疗魔法时，配对目标也会恢复治疗量40%的体力
    # 持续时间：20秒
    # Generate an aetheric bond with target party member. Each time you cast a single-target healing spell on yourself or a party member, the party member with whom you have the bond will also recover HP equaling 40% of the original spell.
    # Duration: 20s
    # related: [星位合图(0)](Status845), [星位合图(1)](Status846), [星位合图(2)](Status1336), [星位合图(3)](Status1337), 
    id = 3612
    names = ['Synastry(AST)', '星位合图(AST)']
    _orig_names = ['星位合图', 'Synastry']


class Action3613(Action):
    # 以自身为中心产生命运之轮
    # 范围内的自身及队员所受到的伤害减轻10%
    # 持续时间：18秒
    # 同时，范围内的自身及队员还会附加体力持续恢复的效果
    # 恢复力：100
    # 持续时间：15秒
    # 效果时间内发动技能或进行移动、转身都会使命运之轮立即消失
    # 发动之后会停止自动攻击
    # Creates a celestial ring around the caster.
    # Additional Effect: Reduces damage taken by 10% and applies Wheel of Fortune to self and any party members who enter
    # Duration: 18s
    # Wheel of Fortune Effect: Regen
    # Cure Potency: 100
    # Duration: 15s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # related: [命运之轮(0)](Status2283), [命运之轮(1)](Status847), [命运之轮(2)](Status848), [命运之轮(3)](Status849), [命运之轮(4)](Status1206), [命运之轮(5)](Status956), 
    id = 3613
    names = ['Collective Unconscious(AST)', '命运之轮(AST)']
    _orig_names = ['Collective Unconscious', '命运之轮']
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '100'}


class Action3614(Action):
    # 恢复目标的体力
    # 恢复力：400～900
    # 目标剩余体力越少恢复力越高，30%以下恢复力最高(job==33?(level>=78?
    # 积蓄次数：2:):)
    # Restores target's HP.
    # Cure Potency: 400
    # Potency increases up to 900 as the target's HP decreases, reaching its maximum value when the target has 30% HP or less.(job==33?(level>=78?
    # Maximum Charges: 2:):)
    id = 3614
    names = ['Essential Dignity(AST)', '先天禀赋(AST)']
    _orig_names = ['Essential Dignity', '先天禀赋']
    heal = [400, 900]


class Action3615(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：120
    # Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
    id = 3615
    names = ['Gravity(AST)', '重力(AST)']
    _orig_names = ['重力', 'Gravity']
    damage = 120


class Action4401(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以近身攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加日之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Solar Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [太阳神之衡(0)](Status1338), [太阳神之衡(1)](Status829), [太阳神之衡(2)](Status1882), 
    id = 4401
    names = ['太阳神之衡(AST)', 'the Balance(AST)']
    _orig_names = ['太阳神之衡', 'the Balance']
    # remain metas: {'dmg_increase': ''}


class Action4402(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以近身攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加月之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Lunar Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [放浪神之箭(0)](Status1884), [放浪神之箭(1)](Status831), 
    id = 4402
    names = ['the Arrow(AST)', '放浪神之箭(AST)']
    _orig_names = ['the Arrow', '放浪神之箭']
    # remain metas: {'dmg_increase': ''}


class Action4403(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以近身攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加星之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Celestial Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [战争神之枪(0)](Status832), [战争神之枪(1)](Status1885), 
    id = 4403
    names = ['战争神之枪(AST)', 'the Spear(AST)']
    _orig_names = ['the Spear', '战争神之枪']
    # remain metas: {'dmg_increase': ''}


class Action4404(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以远程攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加日之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Solar Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [世界树之干(0)](Status1339), [世界树之干(1)](Status1883), [世界树之干(2)](Status830), 
    id = 4404
    names = ['the Bole(AST)', '世界树之干(AST)']
    _orig_names = ['世界树之干', 'the Bole']
    # remain metas: {'dmg_increase': ''}


class Action4405(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以远程攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加月之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Lunar Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [河流神之瓶(0)](Status833), [河流神之瓶(1)](Status1340), [河流神之瓶(2)](Status1886), 
    id = 4405
    names = ['the Ewer(AST)', '河流神之瓶(AST)']
    _orig_names = ['河流神之瓶', 'the Ewer']
    # remain metas: {'dmg_increase': ''}


class Action4406(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高
    # 持续时间：15秒
    # 以远程攻击为主的职业提高6%，其他职业提高3%
    # (job==33?(level>=50?追加效果：若自身处于战斗状态，则在星标中附加星之标识
    # :):)奥秘卡的效果只能同时附加1种
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
    # Duration: 15s
    # (job==33?(level>=50?Additional Effect: Grants a Celestial Sign when used in combat
    # :):)Only one arcanum effect can be applied to a target at a time.
    # ※This action cannot be assigned to a hotbar.
    # related: [建筑神之塔(0)](Status834), [建筑神之塔(1)](Status1341), [建筑神之塔(2)](Status1887), 
    id = 4406
    names = ['the Spire(AST)', '建筑神之塔(AST)']
    _orig_names = ['建筑神之塔', 'the Spire']
    # remain metas: {'dmg_increase': ''}


class Action7439(Action):
    # 在指定地点设置地星，并为自身附加地星主宰状态
    # 持续时间：10秒
    # 地星主宰持续时间内再次使用此技能，则会发动星体破裂，对范围内的敌人进行无属性魔法攻击
    # 威力：205
    # 追加效果：恢复范围内自身与队员的体力
    # 恢复力：540
    # 持续时间结束后，地星获得强化，并为自身附加巨星主宰状态
    # 持续时间：10秒
    # 巨星主宰的持续时间结束时，或时间内再次使用此技能，则会发动星体爆炸，对范围内的敌人进行无属性魔法攻击
    # 威力：310
    # 追加效果：恢复范围内自身与队员的体力
    # 恢复力：720
    # Deploys an Earthly Star in the designated area and grants the effect of Earthly Dominance.
    # Duration: 10s
    # Executing Stellar Detonation while under the effect of Earthly Dominance creates a Stellar Burst dealing unaspected damage with a potency of 205 to all nearby enemies. Also restores own HP and the HP of all nearby party members.
    # Cure Potency: 540
    # After 10s, Earthly Dominance effect is changed to Giant Dominance.
    # Duration: 10s
    # Waiting 10s or executing Stellar Detonation while under the effect of Giant Dominance creates a Stellar Explosion dealing unaspected damage with a potency of 310 to all nearby enemies. Also restores own HP and the HP of all nearby party members.
    # Cure Potency: 720
    # related: [地星主宰](Status1224), [巨星主宰](Status1248), 
    id = 7439
    names = ['地星(AST)', 'Earthly Star(AST)']
    _orig_names = ['Earthly Star', '地星']
    heal = 540 # TODO: [540, 720]
    # remain metas: {'dmg_ot': ['310', '205']}


class Action7442(Action):
    # 对目标发动无属性魔法攻击
    # 威力：190
    # Deals unaspected damage with a potency of 190.
    id = 7442
    names = ['Malefic III(AST)', '祸星(AST)']
    _orig_names = ['祸星', 'Malefic III']
    damage = 190


class Action7443(Action):
    # 抽取王冠之领主或王冠之贵妇奥秘卡
    # 发动该技能后，出王冠卡变为抽到的小奥秘卡技能
    # 发动条件：自身处于战斗状态
    # Draws either the Lord of Crowns or the Lady of Crowns from your divining deck.
    # Arcanum effect can be triggered using the action Crown Play.
    # Can only be executed while in combat.
    id = 7443
    names = ['Minor Arcana(AST)', '小奥秘卡(AST)']
    _orig_names = ['Minor Arcana', '小奥秘卡']


class Action7444(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：250
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 250 to all nearby enemies.
    # ※This action cannot be assigned to a hotbar.
    # related: [王冠之领主(0)](Status1451), [王冠之领主(1)](Status1876), 
    id = 7444
    names = ['王冠之领主(AST)', 'Lord of Crowns(AST)']
    _orig_names = ['Lord of Crowns', '王冠之领主']
    damage = 250


class Action7445(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：400
    # ※该技能无法设置到热键栏
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 400
    # ※This action cannot be assigned to a hotbar.
    # related: [王冠之贵妇(0)](Status1452), [王冠之贵妇(1)](Status1877), 
    id = 7445
    names = ['Lady of Crowns(AST)', '王冠之贵妇(AST)']
    _orig_names = ['Lady of Crowns', '王冠之贵妇']
    heal = 400


class Action8324(Action):
    # 发动设置在地面的地星
    # “地星主宰”状态中：对范围内的敌人发动无属性魔法攻击
    # 威力：205
    # 追加效果：恢复范围内自身与队员的体力
    # 恢复力：540
    # “巨星主宰”状态中：对范围内的敌人发动无属性魔法攻击
    # 威力：310
    # 追加效果：恢复范围内自身与队员的体力
    # 恢复力：720
    # While under the effect of Earthly Dominance, detonates the currently deployed Earthly Star, creating a Stellar Burst that deals unaspected damage with a potency of 205 to all nearby enemies.
    # Additional Effect: Restores own HP and the HP of all nearby party members
    # Cure Potency: 540
    # While under the effect of Giant Dominance, detonates the currently deployed Earthly Star, creating a Stellar Explosion that deals unaspected damage with a potency of 310 to all nearby enemies.
    # Additional Effect: Restores own HP and the HP of all nearby party members
    # Cure Potency: 720
    # related: [地星主宰](Status1224), [巨星主宰](Status1248), 
    id = 8324
    names = ['Stellar Detonation(AST)', '星体爆轰(AST)']
    _orig_names = ['Stellar Detonation', '星体爆轰']
    damage = 310 # TODO: [310, 205]
    heal = 540 # TODO: [540, 720]


class Action8913(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # 正常咏唱时追加效果：下次咏唱的魔法没有任何咏唱时间
    # 持续时间：10秒
    # ※该技能在“中间学派”状态中会变为“吉星相位”
    # Restores target's HP.
    # Cure Potency: 2,000
    # Additional Effect: Grants Abridged when spell is cast with a cast time
    # Duration: 10s
    # Abridged Effect: Next spell is cast immediately
    # ※Action changes to Aspected Benefic while under the effect of Neutral Sect.
    # related: [中间学派(0)](Status1921), [中间学派(1)](Status1892), [中间学派(2)](Status2044), 
    id = 8913
    names = ['Benefic(pvp)(AST)', '吉星(pvp)(AST)']
    _orig_names = ['Benefic(pvp)', '吉星(pvp)']
    heal = 2000


class Action8914(Action):
    # 恢复目标的体力
    # 恢复力：4000
    # Restores target's HP.
    # Cure Potency: 4,000
    id = 8914
    names = ['Benefic II(pvp)(AST)', '福星(pvp)(AST)']
    _orig_names = ['Benefic II(pvp)', '福星(pvp)']
    heal = 4000


class Action8916(Action):
    # 恢复目标的体力
    # 恢复力：2500～5000
    # 目标剩余体力越少恢复力越高
    # 积蓄次数：2
    # Restores target's HP.
    # Cure Potency: 2,500
    # Potency increases up to 5,000 as the target's HP decreases.
    # Maximum Charges: 2
    id = 8916
    names = ['Essential Dignity(pvp)(AST)', '先天禀赋(pvp)(AST)']
    _orig_names = ['先天禀赋(pvp)', 'Essential Dignity(pvp)']
    heal = [2500, 5000]


class Action9629(Action):
    # 将抽到的奥秘卡废弃
    # 发动条件：奥秘卡抽卡状态中
    # Returns the currently drawn arcanum back to your deck.
    # related: [抽卡](Status826), 
    id = 9629
    names = ['Undraw(AST)', '奥秘卡废弃(AST)']
    _orig_names = ['奥秘卡废弃', 'Undraw']


class Action10027(Action):
    # 抽取王冠之领主或王冠之贵妇
    # Draws either Lord of Crowns or Lady of Crowns.
    # Shares a recast timer with Lord of Crowns and Lady of Crowns.
    id = 10027
    names = ['小奥秘卡(pvp)(AST)', 'Minor Arcana(pvp)(AST)']
    _orig_names = ['小奥秘卡(pvp)', 'Minor Arcana(pvp)']


class Action10028(Action):
    # 令自身或其他一名队员发动攻击造成的伤害提高20%
    # 持续时间：15秒
    # ※该技能无法设置到热键栏
    # Increases damage dealt by a party member or self by 20%.
    # Duration: 15s
    # Shares a recast timer with Minor Arcana.
    # ※This action cannot be assigned to a hotbar.
    # related: [王冠之领主(0)](Status1451), [王冠之领主(1)](Status1876), 
    id = 10028
    names = ['Lord of Crowns(pvp)(AST)', '王冠之领主(pvp)(AST)']
    _orig_names = ['Lord of Crowns(pvp)', '王冠之领主(pvp)']
    # remain metas: {'dmg_increase': '20%'}


class Action10029(Action):
    # 令自身或其他一名队员所受到的伤害减轻20%
    # 持续时间：15秒
    # ※该技能无法设置到热键栏
    # Reduces damage taken by a party member or self by 20%.
    # Duration: 15s
    # Shares a recast timer with Minor Arcana.
    # ※This action cannot be assigned to a hotbar.
    # related: [王冠之贵妇(0)](Status1452), [王冠之贵妇(1)](Status1877), 
    id = 10029
    names = ['王冠之贵妇(pvp)(AST)', 'Lady of Crowns(pvp)(AST)']
    _orig_names = ['王冠之贵妇(pvp)', 'Lady of Crowns(pvp)']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action16552(Action):
    # 令自身与周围队员发动攻击造成的伤害提高6%
    # 持续时间：15秒
    # Increases damage dealt by self and nearby party members by 6%.
    # Duration: 15s
    # related: [占卜(0)](Status2034), [占卜(1)](Status1878), 
    id = 16552
    names = ['Divination(AST)', '占卜(AST)']
    _orig_names = ['Divination', '占卜']
    # remain metas: {'dmg_increase': '6%'}


class Action16553(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：200
    # 追加效果：目标体力持续恢复
    # 恢复力：100
    # 持续时间：15秒
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 200
    # Additional Effect: Regen
    # Cure Potency: 100
    # Duration: 15s
    # related: [天星冲日](Status1879), 
    id = 16553
    names = ['天星冲日(AST)', 'Celestial Opposition(AST)']
    _orig_names = ['天星冲日', 'Celestial Opposition']
    heal = 200
    # remain metas: {'heal_ot': '100'}


class Action16554(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：55
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 55
    # Duration: 30s
    # related: [焚灼(0)](Status1881), [焚灼(1)](Status2041), 
    id = 16554
    names = ['焚灼(AST)', 'Combust III(AST)']
    _orig_names = ['Combust III', '焚灼']
    # remain metas: {'dmg_ot': '55'}


class Action16555(Action):
    # 对目标发动无属性魔法攻击
    # 威力：230
    # Deals unaspected damage with a potency of 230.
    id = 16555
    names = ['煞星(AST)', 'Malefic IV(AST)']
    _orig_names = ['煞星', 'Malefic IV']
    damage = 230


class Action16556(Action):
    # 恢复自身或一名队员的体力
    # 恢复力：200
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量200%的伤害
    # 持续时间：30秒(job==33?(level>=88?
    # 积蓄次数：2:):)
    # Restores own or target party member's HP.
    # Cure Potency: 200
    # Additional Sect Effect: Erects a magicked barrier which nullifies damage equaling 200% of the amount of HP restored
    # Duration: 30s(job==33?(level>=88?
    # Maximum Charges: 2:):)
    # related: [天星交错](Status1889), 
    id = 16556
    names = ['Celestial Intersection(AST)', '天星交错(AST)']
    _orig_names = ['Celestial Intersection', '天星交错']
    heal = 200
    # remain metas: {'shield': '治疗量200%'}


class Action16557(Action):
    # 对自身和周围队员附加天宫图状态
    # 持续时间：10秒
    # 天宫图持续时间内受到自身发动的阳星或阳星相位时，天宫图状态变为阳星天宫图状态
    # 持续时间：30秒
    # 天宫图及阳星天宫图状态的持续时间结束或持续时间内再次使用此技能，会恢复附加了天宫图及阳星天宫图状态的自身及周围队员的体力
    # 天宫图状态恢复力：200
    # 阳星天宫图状态恢复力：400
    # Reads your fortune and those of nearby party members, granting them Horoscope.
    # Duration: 10s
    # Effect upgraded to Horoscope Helios upon receiving the effects of Helios or Aspected Helios.
    # Duration: 30s
    # Restores the HP of those under either effect when the cards are read a second time or the effect expires.
    # Horoscope Cure Potency: 200
    # Horoscope Helios Cure Potency: 400
    # related: [天宫图](Status1890), [阳星天宫图](Status1891), 
    id = 16557
    names = ['Horoscope(AST)(0)', '天宫图(AST)(0)']
    _orig_names = ['Horoscope', '天宫图']
    heal = 400
    # remain metas: {'heal_ot': '200'}


class Action16558(Action):
    # 恢复自身及周围队员的体力
    # 该技能的恢复力受目标附加的状态影响
    # 天宫图状态恢复力：200
    # 阳星天宫图状态恢复力：400
    # 发动后会取消天宫图及阳星天宫图状态
    # Restores own HP and the HP of all nearby party members.
    # Potency is determined by the Horoscope effect of party members. Effect expires upon execution.
    # Horoscope Potency: 200
    # Horoscope Helios Potency: 400
    # related: [天宫图](Status1890), [阳星天宫图](Status1891), 
    id = 16558
    names = ['Horoscope(AST)(1)', '天宫图(AST)(1)']
    _orig_names = ['Horoscope', '天宫图']
    heal = 200 # TODO: [200, 400]


class Action16559(Action):
    # 一定时间内，自身发动治疗魔法的治疗量提高20%
    # 持续时间：20秒
    # 追加效果：使用吉星相位及阳星相位时，附加能够抵御一定伤害的防护罩
    # 吉星相位效果量：抵消相当于治疗量250%的伤害
    # 阳性相位效果量：抵消相当于治疗量125%的伤害
    # 持续时间：30秒
    # Increases healing magic potency by 20%.
    # Duration: 20s
    # Additional Effect: When casting Aspected Benefic or Aspected Helios, erects a magicked barrier which nullifies damage
    # Aspected Benefic Effect: Nullifies damage equaling 250% of the amount of HP restored
    # Aspected Helios Effect: Nullifies damage equaling 125% of the amount of HP restored
    # Duration: 30s
    # related: [中间学派(0)](Status1921), [吉星相位](Status835), [中间学派(1)](Status1892), [中间学派(2)](Status2044), 
    id = 16559
    names = ['Neutral Sect(AST)', '中间学派(AST)']
    _orig_names = ['Neutral Sect', '中间学派']
    # remain metas: {'shield': ['治疗量250%', '治疗量125%']}


class Action17055(Action):
    # 抽卡后，此技能变为抽到的奥秘卡技能
    # Triggers the effect of your drawn arcanum.
    id = 17055
    names = ['出卡(AST)', 'Play(AST)']
    _orig_names = ['Play', '出卡']


class Action17804(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # 追加效果：目标体力持续恢复
    # 恢复力：800
    # 持续时间：15秒
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：10秒
    # 正常咏唱时追加效果：下次咏唱的魔法没有任何咏唱时间
    # 持续时间：10秒
    # 发动条件：中间学派状态中
    # ※该技能无法设置到热键栏
    # Restores target's HP.
    # Cure Potency: 2,000
    # Additional Effect: Regen
    # Cure Potency: 800
    # Duration: 15s
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling HP restored
    # Duration: 10s
    # Additional Effect: Grants Abridged when spell is cast with a cast time
    # Duration: 10s
    # Abridged Effect: Next spell is cast immediately
    # Can only be executed while under the effect of Neutral Sect.
    # ※This action cannot be assigned to a hotbar.
    # related: [中间学派(0)](Status1921), [吉星相位](Status835), [中间学派(1)](Status1892), [中间学派(2)](Status2044), 
    id = 17804
    names = ['Aspected Benefic(pvp)(AST)', '吉星相位(pvp)(AST)']
    _orig_names = ['吉星相位(pvp)', 'Aspected Benefic(pvp)']
    heal = 2000
    # remain metas: {'heal_ot': '800', 'shield': '治疗量100%'}


class Action17805(Action):
    # 对目标发动魔法攻击
    # 威力：1200
    # 正常咏唱时追加效果：下次咏唱的魔法没有任何咏唱时间
    # 持续时间：10秒
    # Deals unaspected damage with a potency of 1,200.
    # Additional Effect: Grants Abridged when spell is cast with a cast time
    # Duration: 10s
    # Abridged Effect: Next spell is cast immediately
    id = 17805
    names = ['Malefic IV(pvp)(AST)', '煞星(pvp)(AST)']
    _orig_names = ['煞星(pvp)', 'Malefic IV(pvp)']
    damage = 1200


class Action17806(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：令目标攻击造成的伤害、恢复效果降低10%
    # 持续时间：15秒
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Reduces target's damage dealt and healing potency by 10%
    # Duration: 15s
    # related: [焚灼(0)](Status1881), [焚灼(1)](Status2041), 
    id = 17806
    names = ['Combust III(pvp)(AST)', '焚灼(pvp)(AST)']
    _orig_names = ['Combust III(pvp)', '焚灼(pvp)']
    damage = 800


class Action17807(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1600～3200
    # 目标剩余的体力越多威力越大
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage with a potency of 1,600 to target and all enemies nearby it. Potency increases up to 3,200 as target's HP nears maximum.
    # This action does not share a recast timer with any other actions.
    id = 17807
    names = ['Gravity(pvp)(AST)', '重力(pvp)(AST)']
    _orig_names = ['重力(pvp)', 'Gravity(pvp)']
    damage = [1600, 3200]


class Action17809(Action):
    # 令自身魔法的咏唱时间与复唱时间缩短10%
    # 持续时间：15秒
    # Reduces spell cast time and recast time by 10%
    # Duration: 15s
    # related: [中间学派(0)](Status1921), [中间学派(1)](Status1892), [中间学派(2)](Status2044), 
    id = 17809
    names = ['Neutral Sect(pvp)(AST)', '中间学派(pvp)(AST)']
    _orig_names = ['中间学派(pvp)', 'Neutral Sect(pvp)']


class Action17991(Action):
    # 解除自身周围敌人身上所有的持续恢复效果及防护罩
    # 同时对自身及周围的队员附加以下状态
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于恢复力2000的伤害
    # 持续时间：10秒
    # 追加效果：令目标体力持续恢复
    # 恢复力：800
    # 持续时间：15秒
    # Removes all Regen and barrier effects from nearby enemies.
    # Additional Effect: Grants Regen to self and nearby party members
    # Cure Potency: 800
    # Duration: 15s
    # Additional Effect: Creates a barrier around self and nearby party members that absorbs damage equivalent to a heal of 2,000 potency
    # Duration: 10s
    # related: [天星冲日](Status1879), 
    id = 17991
    names = ['Celestial Opposition(pvp)(AST)', '天星冲日(pvp)(AST)']
    _orig_names = ['Celestial Opposition(pvp)', '天星冲日(pvp)']
    # remain metas: {'shield': '恢复力2000', 'heal_ot': '800'}


class Action18941(Action):
    # 令自身与周围队员发动攻击造成的伤害提高10%，受到攻击的伤害减轻10%
    # 持续时间：15秒
    # Increases damage dealt by self and nearby party members by 10%, while reducing damage taken by 10%.
    # Duration: 15s
    # related: [占卜(0)](Status2034), [占卜(1)](Status1878), 
    id = 18941
    names = ['Divination(pvp)(AST)', '占卜(pvp)(AST)']
    _orig_names = ['Divination(pvp)', '占卜(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%', 'dmg_increase': '10%，受到攻击的伤害减轻10%'}


class Action18950(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # ※“中间学派”状态中，该技能变为“阳星相位”
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    # ※Action changes to Aspected Helios while under the effect of Neutral Sect.
    # related: [中间学派(0)](Status1921), [中间学派(1)](Status1892), [中间学派(2)](Status2044), 
    id = 18950
    names = ['Helios(pvp)(AST)', '阳星(pvp)(AST)']
    _orig_names = ['Helios(pvp)', '阳星(pvp)']
    heal = 2000


class Action18951(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # 追加效果：目标体力持续恢复
    # 恢复力：400
    # 持续时间：15秒
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量50%的伤害
    # 持续时间：10秒
    # 发动条件：中间学派
    # ※该技能无法设置到热键栏
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    # Additional Effect: Regen
    # Cure Potency: 400
    # Duration: 15s
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling 50% of HP restored
    # Duration: 10s
    # Can only be cast while under the effect of Neutral Sect.
    # ※This action cannot be assigned to a hotbar.
    # related: [阳星相位](Status836), 
    id = 18951
    names = ['Aspected Helios(pvp)(AST)', '阳星相位(pvp)(AST)']
    _orig_names = ['阳星相位(pvp)', 'Aspected Helios(pvp)']
    heal = 2000
    # remain metas: {'heal_ot': '400', 'shield': '治疗量50%'}


class Action25869(Action):
    # 发动小奥秘卡后，此技能变为抽到的奥秘卡技能
    # Triggers the effect of your drawn arcanum.
    id = 25869
    names = ['Crown Play(AST)', '出王冠卡(AST)']
    _orig_names = ['Crown Play', '出王冠卡']


class Action25870(Action):
    # 该技能的效果根据自身附加的日、月、星的星标种类发生变化
    # 1种星标：为自身附加魂魄之座状态
    # 2种星标：为自身附加魂魄之座与身体之座状态
    # 3种星标：魂魄之座与身体之座与精神之座状态
    # 持续时间：15秒
    # 魂魄之座效果：持续恢复自身魔力
    # 效果量：50
    # 身体之座效果：令自身的自动攻击间隔与魔法的咏唱及复唱时间缩短10%
    # 精神之座效果：自身攻击造成的伤害与治疗效果提高5%
    # 发动条件：星标3档
    # Grants an effect using the astrosigns read from your divining deck.
    # Can only be executed after reading three astrosigns.
    # Effects granted are determined by the number of different types of astrosigns read.
    # 1 Sign Type: Grants Harmony of Spirit
    # 2 Sign Types: Grants Harmony of Spirit and Harmony of Body
    # 3 Sign Types: Grants Harmony of Spirit, Harmony of Body, and Harmony of Mind
    # Duration: 15s
    # Harmony of Spirit Effect: Gradually restores own MP
    # Potency: 50
    # Harmony of Body Effect: Reduces spell cast time and recast time, and auto-attack delay by 10%
    # Harmony of Mind Effect: Increases damage dealt and healing potency by 5%
    # related: [魂魄之座](Status2714), [身体之座](Status2715), [精神之座](Status2716), 
    id = 25870
    names = ['星力(AST)', 'Astrodyne(AST)']
    _orig_names = ['星力', 'Astrodyne']


class Action25871(Action):
    # 对目标发动无属性魔法攻击
    # 威力：250
    # Deals unaspected damage with a potency of 250.
    id = 25871
    names = ['落陷凶星(AST)', 'Fall Malefic(AST)']
    _orig_names = ['Fall Malefic', '落陷凶星']
    damage = 250


class Action25872(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：130
    # Deals unaspected damage with a potency of 130 to target and all enemies nearby it.
    id = 25872
    names = ['中重力(AST)', 'Gravity II(AST)']
    _orig_names = ['中重力', 'Gravity II']
    damage = 130


class Action25873(Action):
    # 令自身或一名队员受到的伤害减轻10%
    # 持续时间：8秒
    # 持续时间结束后恢复目标的体力
    # 恢复力：500
    # Reduces damage taken by self or target party member by 10%.
    # Duration: 8s
    # Additional Effect: Restores HP at the end of the effect's duration
    # Cure Potency: 500
    # related: [擢升](Status2717), 
    id = 25873
    names = ['擢升(AST)', 'Exaltation(AST)']
    _orig_names = ['Exaltation', '擢升']
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '500'}


class Action25874(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：250
    # 攻击复数敌人时，对第一个之外的敌人威力降低40%
    # 追加效果：为自身及周围队员附加大宇宙状态
    # 发动后该技能变为小宇宙
    # 持续时间：15秒
    # 持续时间内积蓄目标所受的伤害
    # 持续时间结束或发动小宇宙后，恢复目标的体力
    # 恢复量：恢复力200＋积蓄所受伤害的50%
    # 恢复量不会超过目标的最大体力
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to all nearby enemies with a potency of 250 for the first enemy, and 40% less for all remaining enemies.
    # Additional Effect: Grants Macrocosmos to self and all nearby party members
    # Duration: 15s
    # Action changes to Microcosmos upon execution.
    # For the effect's duration, 50% of damage taken is compiled.
    # Restores HP equal to a cure of 200 potency plus compiled damage when the effect expires or upon execution of Microcosmos.
    # Amount restored cannot exceed the target's maximum HP.
    # This action does not share a recast timer with any other actions.
    # related: [大宇宙](Status2718), 
    id = 25874
    names = ['Macrocosmos(AST)', '大宇宙(AST)']
    _orig_names = ['大宇宙', 'Macrocosmos']
    damage = 250


class Action25875(Action):
    # 结束自身附加的大宇宙状态，恢复目标的体力
    # 恢复量：恢复力200＋积蓄所受伤害的50%
    # 恢复量不会超过目标的最大体力
    # Triggers the healing effect of Macrocosmos, restoring HP equal to a cure of 200 potency plus 50% of compiled damage.
    # Amount restored cannot exceed the target's maximum HP.
    # related: [大宇宙](Status2718), 
    id = 25875
    names = ['Microcosmos(AST)', '小宇宙(AST)']
    _orig_names = ['小宇宙', 'Microcosmos']


