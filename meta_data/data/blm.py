from ._base import *


class Status176(Status):
    # 灵魂中寄托了灵极性
    # 火属性魔法威力降低，同时消耗的魔力也降低
    # 魔力自然恢复速度增加
    # Aetherial balance of mind and spirit is leaning umbrally. Fire-aspected spells require less MP, but do less damage. MP regeneration has quickened.
    # related: [火炎(BLM)](Action141), [冰结(BLM)](Action142), [烈炎(BLM)](Action147), [爆炎(BLM)](Action152), [玄冰(BLM)](Action159), [冰澈(BLM)](Action3576), [冰结(pvp)(BLM)](Action8859), [天语(pvp)(BLM)](Action8862), [冰澈(pvp)(BLM)](Action8864), [玄冰(pvp)(BLM)](Action8867), [灵极魂(BLM)](Action16506), [高烈炎(BLM)](Action25794), [详述(BLM)](Action25796), [悖论(BLM)](Action25797), 
    id = 176
    names = ['灵极冰', 'Umbral Ice']


class Status173(Status):
    # 灵魂中寄托了星极性
    # 火属性魔法威力提高，同时消耗的魔力也提高
    # 冰属性魔法威力降低，同时消耗的魔力也降低
    # 魔力不会自然恢复
    # Aetherial balance of mind and spirit is leaning astrally. Fire-aspected spells require more MP, but do more damage. Ice-aspected spells require less MP, but do less damage. MP regeneration has stopped.
    # related: [火炎(BLM)](Action141), [冰结(BLM)](Action142), [冰封(BLM)](Action154), [冰澈(BLM)](Action3576), [炽炎(BLM)](Action3577), [火炎(pvp)(BLM)](Action8858), [天语(pvp)(BLM)](Action8862), [炽炎(pvp)(BLM)](Action8863), [核爆(pvp)(BLM)](Action8866), [绝望(BLM)](Action16505), [灵极魂(BLM)](Action16506), [冰冻(BLM)](Action25793), [高烈炎(BLM)](Action25794), [高冰冻(BLM)](Action25795), [悖论(BLM)](Action25797), 
    id = 173
    names = ['星极火', 'Astral Fire']


class Status161(Status):
    # 雷属性持续伤害，体力逐渐流失
    # Sustaining lightning damage over time.
    # related: [闪雷(BLM)](Action144), [闪雷(pvp)(BLM)](Action8860), [暴雷(pvp)(BLM)](Action8861), 
    id = 161
    names = ['闪雷(0)', 'Thunder(0)']


class Status1324(Status):
    # 受到持续伤害
    # Sustaining lightning damage over time.
    # related: [闪雷(BLM)](Action144), [闪雷(pvp)(BLM)](Action8860), [暴雷(pvp)(BLM)](Action8861), 
    id = 1324
    names = ['闪雷(1)', 'Thunder(1)']


class Status163(Status):
    # 雷属性持续伤害，体力逐渐流失
    # Sustaining lightning damage over time.
    # related: [暴雷(BLM)](Action153), [暴雷(pvp)(BLM)](Action8861), 
    id = 163
    names = ['暴雷', 'Thunder III']


class Status737(Status):
    # 在地上产生黑魔纹
    # Naturally occurring ley lines have been connected into a circle of power.
    # related: [黑魔纹(BLM)](Action3573), 
    id = 737
    names = ['黑魔纹', 'Ley Lines']


class Status867(Status):
    # 下次咏唱的崩溃、火炎以及雷系魔法必定触发“崩溃的追加效果”“火苗”“雷云”
    # Next Scathe, Fire, or Thunder spell cast will trigger enhanced status.
    # related: [激情咏唱(BLM)](Action3574), 
    id = 867
    names = ['激情咏唱', 'Sharpcast']

class Status165(Status):

    id = 165
    names = ['火苗']

class Status1211(Status):
    # 咏唱魔法不需要咏唱时间
    # Spells require no time to cast.
    # related: [三连咏唱(BLM)](Action7421), 
    id = 1211
    names = ['三连咏唱', 'Triplecast']


class Status162(Status):
    # 雷属性持续伤害，体力逐渐流失
    # Sustaining lightning damage over time.
    # related: [震雷(BLM)](Action7447), [震雷(pvp)(BLM)](Action18935), [霹雷(pvp)(BLM)](Action18936), 
    id = 162
    names = ['震雷(0)', 'Thunder II(0)']


class Status2075(Status):
    # 受到持续伤害
    # Sustaining lightning damage over time.
    # related: [震雷(BLM)](Action7447), [震雷(pvp)(BLM)](Action18935), [霹雷(pvp)(BLM)](Action18936), 
    id = 2075
    names = ['震雷(1)', 'Thunder II(1)']


class Status164(Status):
    # 下次咏唱的雷系魔法在命中时将持续伤害的伤害量一并爆发出来，并且咏唱时间与消耗魔力均为0
    # Next Thunder spell will add its full damage over time amount to its initial damage, require no time to cast, and cost no MP.
    # related: [闪雷(pvp)(BLM)](Action8860), [暴雷(pvp)(BLM)](Action8861), [震雷(pvp)(BLM)](Action18935), [霹雷(pvp)(BLM)](Action18936), 
    id = 164
    names = ['雷云(0)', 'Thundercloud(0)']


class Status1365(Status):
    # 可以咏唱暴雷或霹雷
    # Able to cast Thunder III or Thunder IV.
    # related: [闪雷(pvp)(BLM)](Action8860), [暴雷(pvp)(BLM)](Action8861), [震雷(pvp)(BLM)](Action18935), [霹雷(pvp)(BLM)](Action18936), 
    id = 1365
    names = ['雷云(1)', 'Thundercloud(1)']


class Status868(Status):
    # 魔法攻击所造成的伤害提高
    # Magic damage dealt is increased.
    # related: [天语(pvp)(BLM)](Action8862), 
    id = 868
    names = ['天语', 'Enochian']


class Status2960(Status):
    # 核爆的威力提高
    # Flare will deal increased damage.
    # related: [高烈炎(BLM)](Action25794), 
    id = 2960
    names = ['核爆效果提高', 'Enhanced Flare']
class Status1210(Status):

    id = 1210
    names = ['霹雷(0)', 'Thunder IV(0)']

class Action141(Action):
    # 对目标发动火属性魔法攻击
    # 威力：180
    # 追加效果：星极火
    # 在处于灵极冰状态时只会解除该状态
    # 持续时间：15秒
    # (level>=42?(job==7?
    # 追加效果（发动几率40%）：下次发动爆炎不消耗魔力，同时也没有咏唱时间
    # 持续时间：30秒:(job==25?
    # 追加效果（发动几率40%）：下次发动爆炎不消耗魔力，同时也没有咏唱时间
    # 持续时间：30秒:)):)
    # Deals fire damage with a potency of 180.
    # Additional Effect: Grants Astral Fire or removes Umbral Ice
    # Duration: 15s(level>=42?(job==7?
    # Additional Effect: 40% chance next Fire III will cost no MP and have no cast time
    # Duration: 30s:(job==25?
    # Additional Effect: 40% chance next Fire III will cost no MP and have no cast time
    # Duration: 30s:)):)
    # related: [灵极冰](Status176), [星极火](Status173), 
    id = 141
    names = ['Fire(BLM)', '火炎(BLM)']
    _orig_names = ['Fire', '火炎']
    damage = 180


class Action142(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：180
    # 追加效果：灵极冰
    # 持续时间：15秒
    # 在处于星极火状态时只会解除该状态
    # 持续时间：15秒
    # Deals ice damage with a potency of 180.
    # Additional Effect: Grants Umbral Ice or removes Astral Fire
    # Duration: 15s
    # related: [灵极冰](Status176), [星极火](Status173), 
    id = 142
    names = ['Blizzard(BLM)', '冰结(BLM)']
    _orig_names = ['冰结', 'Blizzard']
    damage = 180


class Action144(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：30
    # 追加效果：雷属性持续伤害
    # 威力：35
    # 持续时间：21秒
    # 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(level>=28?(job==7?
    # 追加效果（持续伤害每次起效时，发动几率10%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:(job==25?
    # 追加效果（持续伤害每次起效时，发动几率10%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:)):)
    # Deals lightning damage with a potency of 30.
    # Additional Effect: Lightning damage over time
    # Potency: 35
    # Duration: 21s(level>=28?(job==7?
    # Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :(job==25?
    # Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :
    # )):
    # )Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # related: [闪雷(0)](Status161), [闪雷(1)](Status1324), 
    id = 144
    names = ['闪雷(BLM)', 'Thunder(BLM)']
    _orig_names = ['闪雷', 'Thunder']
    damage = 30
    # remain metas: {'dmg_ot': '35'}


class Action147(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：100
    # 追加效果：(level>=35?(job==7?星极火最大档数:(job==25?星极火最大档数:星极火)):星极火)
    # 在处于灵极冰状态时只会解除该状态
    # 持续时间：15秒(job==25?(level>=56?
    # 星极火状态中追加效果：对自身附加核爆效果提高
    # 星极火状态消失时该状态也会同时消失:):)
    # Deals fire damage with a potency of 100 to target and all enemies nearby it.
    # Additional Effect: (level>=35?(job==7?Grants Astral Fire III and removes Umbral Ice:(job==25?Grants Astral Fire III and removes Umbral Ice:Grants Astral Fire or removes Umbral Ice)):Grants Astral Fire or removes Umbral Ice)
    # Duration: 15s(job==25?(level>=56?
    # Astral Fire Bonus: Grants Enhanced Flare
    # Effect is canceled if Astral Fire ends.:):)
    # related: [灵极冰](Status176), 
    id = 147
    names = ['Fire II(BLM)', '烈炎(BLM)']
    _orig_names = ['烈炎', 'Fire II']
    damage = 100


class Action149(Action):
    # 自身处于星极火或灵极冰的状态时迅速切换到另一状态的初级阶段
    # Swaps Astral Fire with a single Umbral Ice, or Umbral Ice with a single Astral Fire.
    id = 149
    names = ['Transpose(BLM)', '星灵移位(BLM)']
    _orig_names = ['星灵移位', 'Transpose']


class Action152(Action):
    # 对目标发动火属性魔法攻击
    # 威力：260
    # 追加效果：星极火最大档数
    # 持续时间：15秒
    # 在处于灵极冰状态时会同时解除该状态
    # Deals fire damage with a potency of 260.
    # Additional Effect: Grants Astral Fire III and removes Umbral Ice
    # Duration: 15s
    # related: [灵极冰](Status176), 
    id = 152
    names = ['爆炎(BLM)', 'Fire III(BLM)']
    _orig_names = ['Fire III', '爆炎']
    damage = 260


class Action153(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：50
    # 追加效果：雷属性持续伤害
    # 威力：35
    # 持续时间：30秒
    # 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(level>=28?(job==7?
    # 追加效果（持续伤害每次起效时，发动几率10%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:(job==25?
    # 追加效果（持续伤害每次起效时，发动几率10%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:)):)
    # Deals lightning damage with a potency of 50.
    # Additional Effect: Lightning damage over time
    # Potency: 35
    # Duration: 30s(level>=28?(job==7?
    # Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :(job==25?
    # Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :
    # )):
    # )Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # related: [暴雷](Status163), 
    id = 153
    names = ['Thunder III(BLM)', '暴雷(BLM)']
    _orig_names = ['暴雷', 'Thunder III']
    damage = 50
    # remain metas: {'dmg_ot': '35'}


class Action154(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：260
    # 追加效果：灵极冰最大档数
    # 持续时间：15秒
    # 在处于星极火状态时会同时解除该状态
    # Deals ice damage with a potency of 260.
    # Additional Effect: Grants Umbral Ice III and removes Astral Fire
    # Duration: 15s
    # related: [星极火](Status173), 
    id = 154
    names = ['冰封(BLM)', 'Blizzard III(BLM)']
    _orig_names = ['Blizzard III', '冰封']
    damage = 260


class Action155(Action):
    # 指定一名队员为目标，自身快速移动到目标身边
    # 止步状态下无法发动
    # Rush to a target party member's side.
    # Unable to cast if bound.
    id = 155
    names = ['Aetherial Manipulation(BLM)', '以太步(BLM)']
    _orig_names = ['以太步', 'Aetherial Manipulation']


class Action156(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 追加效果（发动几率20%）：伤害变为2倍
    # Deals unaspected damage with a potency of 100.
    # Additional Effect: 20% chance potency will double
    id = 156
    names = ['Scathe(BLM)', '崩溃(BLM)']
    _orig_names = ['崩溃', 'Scathe']
    damage = 100


class Action157(Action):
    # 为自身张开一个防护罩，在一定时间内能抵消相当于最大体力30%的伤害量
    # 抵消的伤害量超过上限时防护罩自动消失
    # 持续时间：20秒
    # Creates a barrier that nullifies damage totaling up to 30% of maximum HP.
    # Duration: 20s
    # related: [魔罩(0)](Status168), [魔罩(1)](Status1989), 
    id = 157
    names = ['魔罩(BLM)', 'Manaward(BLM)']
    _orig_names = ['Manaward', '魔罩']
    # remain metas: {'shield': '最大体力30%'}


class Action158(Action):
    # 恢复最大魔力的30%
    # Restores 30% of maximum MP.
    id = 158
    names = ['魔泉(BLM)', 'Manafont(BLM)']
    _orig_names = ['魔泉', 'Manafont']


class Action159(Action):
    # 对目标及其周围的敌人发动冰属性范围魔法攻击
    # 威力：120
    # (job==25?(level>=58?追加效果：3档灵极心
    # 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗
    # 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3
    # :):)发动条件：灵极冰状态中
    # Deals ice damage with a potency of 120 to target and all enemies nearby it.
    # (job==25?(level>=58?Additional Effect: Grants 3 Umbral Hearts
    # Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
    # :):)Can only be executed while under the effect of Umbral Ice.
    # related: [灵极冰](Status176), 
    id = 159
    names = ['Freeze(BLM)', '玄冰(BLM)']
    _orig_names = ['Freeze', '玄冰']
    damage = 120


class Action162(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：220
    # (job==25?(level>=56?核爆效果提高时的威力：280
    # :):)攻击复数敌人时，对目标之外的敌人威力降低40%
    # 追加效果：星极火最大档数
    # 持续时间：15秒
    # 发动条件：灵极火状态中
    # Deals fire damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 40% less for all remaining enemies.
    # (job==25?(level>=56?Enhanced Flare Potency: 280
    # :):)Additional Effect: Grants Astral Fire III
    # Duration: 15s
    # Can only be executed while under the effect of Astral Fire.
    id = 162
    names = ['核爆(BLM)', 'Flare(BLM)']
    _orig_names = ['核爆', 'Flare']
    damage = 220
    # remain metas: {'aoe_reduce': '40%'}


class Action3573(Action):
    # 在自身脚下产生黑魔纹
    # 黑魔纹效果：自身的自动攻击间隔、魔法的咏唱及复唱时间缩短15%
    # 持续时间：30秒
    # Connects naturally occurring ley lines to create a circle of power which, while standing within it, reduces spell cast time and recast time, and auto-attack delay by 15%.
    # Duration: 30s
    # related: [黑魔纹](Status737), 
    id = 3573
    names = ['Ley Lines(BLM)', '黑魔纹(BLM)']
    _orig_names = ['Ley Lines', '黑魔纹']


class Action3574(Action):
    # 效果时间内，自身发动的1次“崩溃”或“火炎”(job==25?(level>=90?或“悖论”:):)或“雷系魔法”必定触发“崩溃的追加效果”“爆炎效果提高”“雷系魔法效果提高”
    # 持续时间：30秒(job==25?(level>=88?
    # 积蓄次数：2:):)
    # Ensures the next Scathe, Fire, (job==25?(level>=90?Paradox, :):)or Thunder spell cast will, for the first hit, trigger Scathe's additional effect, Firestarter, or Thundercloud.
    # Duration: 30s(job==25?(level>=88?
    # Maximum Charges: 2:):)
    # related: [激情咏唱](Status867), 
    id = 3574
    names = ['激情咏唱(BLM)', 'Sharpcast(BLM)']
    _orig_names = ['Sharpcast', '激情咏唱']


class Action3576(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：310
    # 追加效果：3档灵极心
    # 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗(level>=68?(job==25?
    # 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3:):)
    # 发动条件：灵极冰状态中
    # Deals ice damage with a potency of 310.
    # Additional Effect: Grants 3 Umbral Hearts
    # Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
    # Can only be executed while under the effect of Umbral Ice.
    # related: [灵极冰](Status176), [星极火](Status173), 
    id = 3576
    names = ['Blizzard IV(BLM)', '冰澈(BLM)']
    _orig_names = ['冰澈', 'Blizzard IV']
    damage = 310


class Action3577(Action):
    # 对目标发动火属性魔法攻击
    # 威力：310
    # 发动条件：星极火状态中
    # Deals fire damage with a potency of 310.
    # Can only be executed while under the effect of Astral Fire.
    # related: [星极火](Status173), 
    id = 3577
    names = ['炽炎(BLM)', 'Fire IV(BLM)']
    _orig_names = ['Fire IV', '炽炎']
    damage = 310


class Action7419(Action):
    # 快速移动到自身留下的黑魔纹中心
    # 止步状态下无法发动
    # Move instantly to Ley Lines drawn by you.
    # Cannot be executed while bound.
    id = 7419
    names = ['Between the Lines(BLM)', '魔纹步(BLM)']
    _orig_names = ['魔纹步', 'Between the Lines']


class Action7420(Action):
    # 对目标及其周围敌人发动雷属性范围魔法攻击
    # 威力：50
    # 追加效果：雷属性持续伤害
    # 威力：20
    # 持续时间：18秒
    # 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种
    # 追加效果（持续伤害每次起效时，发动几率3%）：下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒
    # Deals lightning damage with a potency of 50 to target and all enemies nearby it.
    # Additional Effect: Lightning damage over time
    # Potency: 20
    # Duration: 18s
    # Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # related: [霹雷](Status1210), 
    id = 7420
    names = ['霹雷(BLM)', 'Thunder IV(BLM)']
    _orig_names = ['霹雷', 'Thunder IV']
    damage = 50
    # remain metas: {'dmg_ot': '20'}


class Action7421(Action):
    # 效果时间内，前3次咏唱的魔法没有任何咏唱时间
    # 持续时间：15秒
    # 积蓄次数：2
    # The next three spells will require no cast time.
    # Duration: 15s
    # Maximum Charges: 2
    # related: [三连咏唱](Status1211), 
    id = 7421
    names = ['三连咏唱(BLM)', 'Triplecast(BLM)']
    _orig_names = ['三连咏唱', 'Triplecast']


class Action7422(Action):
    # 对目标及其周围敌人发动无属性范围魔法攻击
    # 威力：560
    # 攻击复数敌人时，对目标之外的敌人威力降低60%
    # 发动条件：通晓
    # Deals unaspected damage to target and all enemies nearby it with a potency of 560 for the first enemy, and 60% less for all remaining enemies.
    # Polyglot Cost: 1
    id = 7422
    names = ['秽浊(BLM)', 'Foul(BLM)']
    _orig_names = ['秽浊', 'Foul']
    damage = 560
    # remain metas: {'aoe_reduce': '60%'}


class Action7447(Action):
    # 对目标及其周围敌人发动雷属性范围魔法攻击
    # 威力：50
    # 追加效果：雷属性持续伤害
    # 威力：15
    # 持续时间：18秒
    # 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(level>=28?(job==7?
    # 追加效果（持续伤害每次起效时，发动几率3%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:(job==25?
    # 追加效果（持续伤害每次起效时，发动几率3%）：
    # 下次发动的雷系魔法咏唱时间与消耗魔力均为0
    # 且命中时的威力会加算持续伤害的总和
    # 持续时间：40秒:)):)
    # Deals lightning damage with a potency of 50 to target and all enemies nearby it.
    # Additional Effect: Lightning damage over time
    # Potency: 15
    # Duration: 18s(level>=28?(job==7?
    # Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :(job==25?
    # Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
    # Duration: 40s
    # :
    # )):
    # )Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # related: [震雷(0)](Status162), [震雷(1)](Status2075), 
    id = 7447
    names = ['Thunder II(BLM)', '震雷(BLM)']
    _orig_names = ['Thunder II', '震雷']
    damage = 50
    # remain metas: {'dmg_ot': '15'}


class Action8858(Action):
    # 对目标发动魔法攻击
    # 威力：1200
    # 追加效果：星极火
    # “星极火”效果：攻击伤害提高20%
    # 持续时间：15秒
    # Deals fire damage with a potency of 1,200.
    # Additional Effect: Grants Astral Fire, increasing damage dealt by 20%
    # Duration: 15s
    # related: [星极火](Status173), 
    id = 8858
    names = ['Fire(pvp)(BLM)', '火炎(pvp)(BLM)']
    _orig_names = ['Fire(pvp)', '火炎(pvp)']
    damage = 1200
    # remain metas: {'dmg_increase': '20%'}


class Action8859(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：恢复2000点魔力
    # 追加效果：灵极冰
    # “灵极冰”效果：魔法的咏唱及复唱时间缩短20%
    # 持续时间：15秒
    # Deals ice damage with a potency of 800.
    # Additional Effect: Restores 2,000 MP
    # Additional Effect: Grants Umbral Ice, reducing spell cast and recast times by 20%
    # Duration: 15s
    # related: [灵极冰](Status176), 
    id = 8859
    names = ['冰结(pvp)(BLM)', 'Blizzard(pvp)(BLM)']
    _orig_names = ['Blizzard(pvp)', '冰结(pvp)']
    damage = 800


class Action8860(Action):
    # 对目标发动魔法攻击
    # 威力：400
    # 追加效果：持续伤害
    # 威力：400
    # 持续时间：15秒
    # 追加效果：对身中自身附加的闪雷状态的目标造成超过8000点伤害后，目标身上的闪雷状态会消失，同时为自身附加雷云状态
    # 持续时间：10秒
    # ※“雷云”状态中该技能变为“暴雷”
    # Deals lightning damage with a potency of 400.
    # Additional Effect: Lightning damage over time
    # Potency: 400
    # Duration: 15s
    # Additional Effect: Grants Thundercloud if target is dealt over 8,000 points of damage while under the effect of Thunder
    # Duration: 10s
    # Thunder effect is removed from target upon receiving Thundercloud status.
    # Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # ※Action changes to Thunder III while under the effect of Thundercloud.
    # related: [闪雷(0)](Status161), [雷云(0)](Status164), [雷云(1)](Status1365), [闪雷(1)](Status1324), 
    id = 8860
    names = ['闪雷(pvp)(BLM)', 'Thunder(pvp)(BLM)']
    _orig_names = ['Thunder(pvp)', '闪雷(pvp)']
    damage = 400
    # remain metas: {'dmg_ot': '400'}


class Action8861(Action):
    # 对目标发动魔法攻击
    # 威力：2400
    # 追加效果：持续伤害
    # 威力：400
    # 持续时间：15秒
    # 追加效果：对身中自身附加的闪雷状态的目标造成超过8000点伤害后，目标身上的闪雷状态会消失，同时为自身附加雷云状态
    # 持续时间：10秒
    # 发动条件：雷云状态中
    # ※该技能无法设置到热键栏
    # Deals lightning damage with a potency of 2,400.
    # Additional Effect: Lightning damage over time
    # Potency: 400
    # Duration: 15s
    # Additional Effect: Grants Thundercloud if target is dealt over 8,000 points of damage while under the effect of Thunder
    # Duration: 10s
    # Can only be cast while under the effect of Thundercloud.
    # Thunder effect is removed from target upon receiving Thundercloud status.
    # Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # ※This action cannot be assigned to a hotbar.
    # related: [闪雷(0)](Status161), [暴雷](Status163), [雷云(0)](Status164), [雷云(1)](Status1365), [闪雷(1)](Status1324), 
    id = 8861
    names = ['暴雷(pvp)(BLM)', 'Thunder III(pvp)(BLM)']
    _orig_names = ['暴雷(pvp)', 'Thunder III(pvp)']
    damage = 2400
    # remain metas: {'dmg_ot': '400'}


class Action8862(Action):
    # 星极火状态中可以咏唱炽炎，灵极冰状态中可以咏唱冰澈
    # 星极火或灵极冰的状态持续15秒后，对自身附加通晓状态
    # 持续时间：永久
    # ※“星极火”状态中该技能变为“炽炎”
    # ※“灵极冰”状态中该技能变为“冰澈”
    # Allows the casting of Fire IV and Blizzard IV.
    # Additional Effect: Grants Polyglot if Enochian is maintained for 15s
    # Can only be executed while under the effect of Astral Fire or Umbral Ice. Effect is canceled if Astral Fire or Umbral Ice end.
    # ※Action changes to Fire IV while under the effect of Astral Fire.
    # ※Action changes to Blizzard IV while under the effect of Umbral Ice.
    # related: [灵极冰](Status176), [天语](Status868), [星极火](Status173), 
    id = 8862
    names = ['天语(pvp)(BLM)', 'Enochian(pvp)(BLM)']
    _orig_names = ['Enochian(pvp)', '天语(pvp)']


class Action8863(Action):
    # 对目标发动魔法攻击
    # 威力：2400
    # 发动条件：星极火状态中
    # ※该技能无法设置到热键栏
    # Deals fire damage with a potency of 2,400.
    # Can only be cast while under the effect of Astral Fire.
    # ※This action cannot be assigned to a hotbar.
    # related: [星极火](Status173), 
    id = 8863
    names = ['Fire IV(pvp)(BLM)', '炽炎(pvp)(BLM)']
    _orig_names = ['Fire IV(pvp)', '炽炎(pvp)']
    damage = 2400


class Action8864(Action):
    # 对目标发动魔法攻击
    # 威力：1600
    # 追加效果：恢复4000点魔力
    # 发动条件：灵极冰状态中
    # ※该技能无法设置到热键栏
    # Deals ice damage with a potency of 1,600.
    # Additional Effect: Restores 4,000 MP
    # Can only be cast while under the effect of Umbral Ice.
    # ※This action cannot be assigned to a hotbar.
    # related: [灵极冰](Status176), 
    id = 8864
    names = ['Blizzard IV(pvp)(BLM)', '冰澈(pvp)(BLM)']
    _orig_names = ['冰澈(pvp)', 'Blizzard IV(pvp)']
    damage = 1600


class Action8865(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1800
    # 发动条件：通晓状态中
    # 发动后会取消通晓状态
    # Deals unaspected damage with a potency of 1,800 to target and all enemies nearby it.
    # Polyglot Cost: 1
    id = 8865
    names = ['Foul(pvp)(BLM)', '秽浊(pvp)(BLM)']
    _orig_names = ['Foul(pvp)', '秽浊(pvp)']
    damage = 1800


class Action8866(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1800
    # 追加效果：星极火
    # 持续时间：15秒
    # “星极火”效果：攻击伤害提高20%
    # Deals fire damage with a potency of 1,800 to target and all enemies nearby it.
    # Additional Effect: Grants Astral Fire, increasing damage dealt by 20%
    # Duration: 15s
    # related: [星极火](Status173), 
    id = 8866
    names = ['核爆(pvp)(BLM)', 'Flare(pvp)(BLM)']
    _orig_names = ['Flare(pvp)', '核爆(pvp)']
    damage = 1800
    # remain metas: {'dmg_increase': '20%'}


class Action8867(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：1200
    # 追加效果：每命中一个目标都会恢复2000点魔力
    # 追加效果：灵极冰
    # 持续时间：15秒
    # “灵极冰”效果：魔法的咏唱及复唱时间缩短20%
    # Deals ice damage with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Restores 2,000 MP for each enemy hit
    # Additional Effect: Grants Umbral Ice, reducing spell cast and recast time by 20%
    # Duration: 15s
    # related: [灵极冰](Status176), 
    id = 8867
    names = ['Freeze(pvp)(BLM)', '玄冰(pvp)(BLM)']
    _orig_names = ['Freeze(pvp)', '玄冰(pvp)']
    damage = 1200


class Action8869(Action):
    # 指定一名队员为目标，自身快速移动到目标身边
    # 止步状态下无法发动
    # Rush to a target party member's side.
    # Unable to cast if bound.
    id = 8869
    names = ['以太步(pvp)(BLM)', 'Aetherial Manipulation(pvp)(BLM)']
    _orig_names = ['Aetherial Manipulation(pvp)', '以太步(pvp)']


class Action16505(Action):
    # 对目标发动火属性魔法攻击
    # 威力：340
    # 追加效果：星极火最大档数
    # 持续时间：15秒
    # 发动条件：星极火状态中
    # Deals fire damage with a potency of 340.
    # Additional Effect: Grants Astral Fire III
    # Duration: 15s
    # Can only be executed while under the effect of Astral Fire.
    # related: [星极火](Status173), 
    id = 16505
    names = ['Despair(BLM)', '绝望(BLM)']
    _orig_names = ['绝望', 'Despair']
    damage = 340


class Action16506(Action):
    # 对自身附加灵极冰状态及1档灵极心
    # 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗
    # 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3
    # 发动条件：灵极冰状态中
    # Grants Umbral Ice and 1 Umbral Heart.
    # Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
    # Can only be executed while under the effect of Umbral Ice.
    # related: [灵极冰](Status176), [星极火](Status173), 
    id = 16506
    names = ['灵极魂(BLM)', 'Umbral Soul(BLM)']
    _orig_names = ['灵极魂', 'Umbral Soul']


class Action16507(Action):
    # 对目标发动无属性魔法攻击
    # 威力：760
    # 发动条件：通晓
    # Deals unaspected damage with a potency of 760.
    # Polyglot Cost: 1
    id = 16507
    names = ['异言(BLM)', 'Xenoglossy(BLM)']
    _orig_names = ['异言', 'Xenoglossy']
    damage = 760


class Action17774(Action):
    # 对目标发动魔法攻击
    # 威力：2400
    # 发动条件：通晓状态中
    # 发动后会取消通晓状态
    # Deals unaspected damage with a potency of 2,400.
    # Polyglot Cost: 1
    id = 17774
    names = ['异言(pvp)(BLM)', 'Xenoglossy(pvp)(BLM)']
    _orig_names = ['异言(pvp)', 'Xenoglossy(pvp)']
    damage = 2400


class Action17775(Action):
    # 令目标及其周围敌人陷入睡眠状态
    # 持续时间：3秒
    # Puts target and all enemies nearby it to sleep.
    # Duration: 3s
    id = 17775
    names = ['夜翼(pvp)(BLM)', 'Night Wing(pvp)(BLM)']
    _orig_names = ['Night Wing(pvp)', '夜翼(pvp)']


class Action18935(Action):
    # 对目标及其周围敌人发动范围魔法攻击
    # 威力：200
    # 追加效果：持续伤害
    # 威力：200
    # 持续时间：15秒
    # 追加效果：自身对被自身附加震雷状态的目标造成超过4000伤害后，以解除震雷状态为代价为自身附加雷云状态
    # 持续时间：10秒
    # ※“雷云”状态中，该技能变为“霹雷”
    # Deals lightning damage with a potency of 200 to target and all enemies nearby it.
    # Additional Effect: Lightning damage over time
    # Potency: 200
    # Duration: 15s
    # Additional Effect: Grants Thundercloud if target is dealt over 4,000 points of damage while under the effect of Thunder II
    # Duration: 10s
    # Thunder II effect is removed from target upon receiving Thundercloud status.
    # Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # ※Action changes to Thunder IV while under the effect of Thundercloud.
    # related: [震雷(0)](Status162), [雷云(0)](Status164), [雷云(1)](Status1365), [震雷(1)](Status2075), 
    id = 18935
    names = ['Thunder II(pvp)(BLM)', '震雷(pvp)(BLM)']
    _orig_names = ['震雷(pvp)', 'Thunder II(pvp)']
    damage = 200
    # remain metas: {'dmg_ot': '200'}


class Action18936(Action):
    # 对目标及其周围敌人发动范围魔法攻击
    # 威力：1200
    # 追加效果：持续伤害
    # 威力：200
    # 持续时间：15秒
    # 追加效果：自身对被自身附加震雷状态的目标造成超过4000伤害后，以解除震雷状态为代价为自身附加雷云状态
    # 持续时间：10秒
    # 发动条件：雷云
    # ※该技能无法设置到热键栏
    # Deals lightning damage with a potency of 1,200 to target and all enemies nearby it.
    # Additional Effect: Lightning damage over time
    # Potency: 200
    # Duration: 15s
    # Additional Effect: Grants Thundercloud if target is dealt over 4,000 points of damage while under the effect of Thunder II
    # Duration: 10s
    # Can only be cast while under the effect of Thundercloud.
    # Thunder II effect is removed from target upon receiving Thundercloud status.
    # Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    # ※This action cannot be assigned to a hotbar.
    # related: [震雷(0)](Status162), [雷云(0)](Status164), [雷云(1)](Status1365), [霹雷](Status1210), [震雷(1)](Status2075), 
    id = 18936
    names = ['霹雷(pvp)(BLM)', 'Thunder IV(pvp)(BLM)']
    _orig_names = ['霹雷(pvp)', 'Thunder IV(pvp)']
    damage = 1200
    # remain metas: {'dmg_ot': '200'}


class Action25793(Action):
    # 对目标及其周围的敌人发动冰属性范围魔法攻击
    # 威力：100
    # 追加效果：(level>=35?(job==7?灵极冰最大档数:(job==25?灵极冰最大档数:灵极冰)):灵极冰)
    # 在处于星极火状态时会同时解除该状态
    # 持续时间：15秒
    # Deals ice damage with a potency of 100 to target and all enemies nearby it.
    # Additional Effect: (level>=35?(job==7?Grants Umbral Ice III and:(job==25?Grants Umbral Ice III and:Grants Umbral Ice or)):Grants Umbral Ice or) removes Astral Fire
    # Duration: 15s
    # related: [星极火](Status173), 
    id = 25793
    names = ['冰冻(BLM)', 'Blizzard II(BLM)']
    _orig_names = ['Blizzard II', '冰冻']
    damage = 100


class Action25794(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：140
    # 追加效果：星极火最大档数
    # 在处于灵极冰状态时会同时解除该状态
    # 持续时间：15秒
    # 星极火状态中追加效果：核爆效果提高
    # 星极火状态消失时该状态也会同时消失
    # Deals fire damage with a potency of 140 to target and all enemies nearby it.
    # Additional Effect: Grants Astral Fire III and removes Umbral Ice
    # Duration: 15s
    # Astral Fire Bonus: Grants Enhanced Flare
    # Effect is canceled if Astral Fire ends.
    # related: [核爆效果提高](Status2960), [星极火](Status173), [灵极冰](Status176), 
    id = 25794
    names = ['High Fire II(BLM)', '高烈炎(BLM)']
    _orig_names = ['High Fire II', '高烈炎']
    damage = 140


class Action25795(Action):
    # 对目标及其周围的敌人发动冰属性范围魔法攻击
    # 威力：140
    # 追加效果：灵极冰最大档数
    # 在处于星极火状态时会同时解除该状态
    # 持续时间：15秒
    # Deals ice damage with a potency of 140 to target and all enemies nearby it.
    # Additional Effect: Grants Umbral Ice III and removes Astral Fire
    # Duration: 15s
    # related: [星极火](Status173), 
    id = 25795
    names = ['High Blizzard II(BLM)', '高冰冻(BLM)']
    _orig_names = ['High Blizzard II', '高冰冻']
    damage = 140


class Action25796(Action):
    # 为自身附加通晓状态
    # 发动条件：星极火或灵极冰状态中
    # Grants Polyglot.
    # Can only be executed while under the effect of Astral Fire or Umbral Ice.
    # related: [灵极冰](Status176), 
    id = 25796
    names = ['Amplifier(BLM)', '详述(BLM)']
    _orig_names = ['详述', 'Amplifier']


class Action25797(Action):
    # 对目标发动无属性魔法攻击
    # 威力：500
    # 星极火状态中追加效果：星极火
    # 持续时间：15秒
    # 同时有40%的几率下次发动的爆炎咏唱时间与消耗魔力均为0
    # 持续时间：30秒
    # 灵极冰状态中追加效果：灵极冰
    # 持续时间：15秒
    # 该魔法不消耗魔力，也不需要咏唱时间
    # 发动条件：悖论状态中
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 500.
    # Astral Fire Bonus: Refreshes the duration of Astral Fire and 40% chance to grant Firestarter
    # Duration: 15s
    # Firestarter Effect: Next Fire III will require no time to cast and cost no MP
    # Duration: 30s
    # Umbral Ice Bonus: Spell is cast immediately, requires no MP to cast, and refreshes the duration of Umbral Ice
    # Duration: 15s
    # Can only be executed while under the effect of Paradox.
    # ※This action cannot be assigned to a hotbar.
    # related: [灵极冰](Status176), [星极火](Status173), 
    id = 25797
    names = ['Paradox(BLM)', '悖论(BLM)']
    _orig_names = ['悖论', 'Paradox']
    damage = 500


