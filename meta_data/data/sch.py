from ._base import *


class Status1918(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [鼓舞激励之策(SCH)](Action185), [应急战术(SCH)](Action3586), 
    id = 1918
    names = ['激励', 'Catalyze']


class Status166(Status):
    # 下次咏唱士气高扬之策时不会消耗魔力
    # Next Succor will cost no MP.
    # related: [士气高扬之策(SCH)](Action186), [士气高扬之策(pvp)(SCH)](Action18947), 
    id = 166
    names = ['士气高扬之策效果提高', 'Succor']


class Status298(Status):
    # 产生减轻伤害的防护区域
    # An area of land has been sanctified, reducing damage taken for all who enter.
    # related: [野战治疗阵(SCH)](Action188), 
    id = 298
    names = ['野战治疗阵(0)', 'Sacred Soil(0)']


class Status299(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [野战治疗阵(SCH)](Action188), 
    id = 299
    names = ['野战治疗阵(1)', 'Sacred Soil(1)']


class Status2637(Status):
    # 减轻范围内队员所受伤害，产生能够恢复体力的区域
    # A circle of sanctified earth is healing party members and reducing damage taken within its bounds.
    # related: [野战治疗阵(SCH)](Action188), 
    id = 2637
    names = ['野战治疗阵(2)', 'Sacred Soil(2)']


class Status2638(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [野战治疗阵(SCH)](Action188), 
    id = 2638
    names = ['野战治疗阵(3)', 'Sacred Soil(3)']


class Status1944(Status):
    # 减轻范围内队员所受伤害，产生能够恢复体力的区域
    # A circle of sanctified earth is healing party members and reducing damage taken within its bounds.
    # related: [野战治疗阵(SCH)](Action188), 
    id = 1944
    names = ['野战治疗阵(4)', 'Sacred Soil(4)']


class Status315(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [仙光的低语(SCH)(0)](Action803), [仙光的低语(SCH)(1)](Action16537), 
    id = 315
    names = ['仙光的低语', 'Whispering Dawn']


class Status1875(Status):
    # 发动治疗魔法的治疗量提高，且受到魔法攻击的伤害减少
    # Magic defense and healing magic potency are increased.
    # related: [异想的幻光(SCH)(0)](Action805), [异想的幻光(SCH)(1)](Action16538), [炽天的幻光(SCH)](Action16551), 
    id = 1875
    names = ['炽天的幻光', 'Seraphic Illumination']


class Status317(Status):
    # 发动治疗魔法的治疗量提高，且受到魔法攻击的伤害减少
    # Magic defense and healing magic potency are increased.
    # related: [异想的幻光(SCH)(0)](Action805), [异想的幻光(SCH)(1)](Action16538), [炽天的幻光(SCH)](Action16551), 
    id = 317
    names = ['异想的幻光', 'Fey Illumination']


class Status792(Status):
    # 下次咏唱附有鼓舞效果及激励效果的治疗魔法时，将其中的防护罩效果转化为治疗效果
    # The next Galvanize and Catalyze statuses are transformed into HP recovery equaling the amount of damage reduction intended for their barriers.
    # related: [应急战术(SCH)](Action3586), 
    id = 792
    names = ['应急战术', 'Emergency Tactics']


class Status2069(Status):
    # 攻击所造成的伤害提高，自身发动的体力恢复效果恢复量提高
    # Damage dealt and potency of all HP restoration actions are increased.
    # related: [转化(SCH)](Action3587), [转化(pvp)(SCH)](Action17990), 
    id = 2069
    names = ['转化(0)', 'Dissipation(0)']


class Status791(Status):
    # 发动治疗魔法的治疗量提高
    # Healing magic potency is increased.
    # related: [转化(SCH)](Action3587), [转化(pvp)(SCH)](Action17990), 
    id = 791
    names = ['转化(1)', 'Dissipation(1)']


class Status1220(Status):
    # 体力降低到一定比例或持续时间结束时自动发动恢复效果
    # HP will be restored automatically upon falling below a certain level or expiration of effect duration.
    # related: [深谋远虑之策(SCH)](Action7434), [深谋远虑之策(pvp)(SCH)](Action18949), 
    id = 1220
    names = ['深谋远虑之策(0)', 'Excogitation(0)']


class Status2182(Status):
    # 体力降低到一定比例或持续时间结束时自动发动恢复效果
    # HP will be restored automatically upon falling below a certain level or expiration of effect duration.
    # related: [深谋远虑之策(SCH)](Action7434), [深谋远虑之策(pvp)(SCH)](Action18949), 
    id = 2182
    names = ['深谋远虑之策(1)', 'Excogitation(1)']


class Status1221(Status):
    # 受到暴击的几率提高
    # Rate at which critical hits are taken is increased.
    # related: [连环计(SCH)](Action7436), 
    id = 1221
    names = ['连环计(0)', 'Chain Stratagem(0)']


class Status1406(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [连环计(SCH)](Action7436), 
    id = 1406
    names = ['连环计(1)', 'Chain Stratagem(1)']


class Status1222(Status):
    # 发动持续恢复体力效果
    # Allowing regeneration of HP over time.
    # related: [异想的融光(SCH)](Action7438), [融光解除(SCH)](Action7869), 
    id = 1222
    names = ['异想的融光(0)', 'Fey Union(0)']


class Status1223(Status):
    # 受到持续恢复体力效果
    # Regenerating HP over time.
    # related: [异想的融光(SCH)](Action7438), [融光解除(SCH)](Action7869), 
    id = 1223
    names = ['异想的融光(1)', 'Fey Union(1)']


class Status2039(Status):
    # 自身所受的体力恢复效果降低
    # Rapid decomposition of the flesh is reducing HP recovery.
    # related: [蛊毒法(SCH)](Action16540), [蛊毒法(pvp)(SCH)](Action17796), 
    id = 2039
    names = ['蛊毒法(0)', 'Biolysis(0)']


class Status1895(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [蛊毒法(SCH)](Action16540), [蛊毒法(pvp)(SCH)](Action17796), 
    id = 1895
    names = ['蛊毒法(1)', 'Biolysis(1)']


class Status1896(Status):
    # 下一次发动的鼓舞激励之策、士气高扬之策、不屈不挠之策、深谋远虑之策，无需消耗魔力和以太超流，并且必定暴击
    # The next Adloquium, Succor, Indomitability, or Excogitation executed will cost no MP or Aetherflow stacks and will restore critical HP.
    # related: [秘策(SCH)](Action16542), 
    id = 1896
    names = ['秘策', 'Recitation']


class Status2040(Status):
    # 抵消一定伤害
    # An aetherial barrier is preventing damage.
    # related: [炽天的幕帘(SCH)](Action16548), 
    id = 2040
    names = ['炽天的幕帘(0)', 'Seraphic Veil(0)']


class Status1917(Status):
    # 抵消一定伤害
    # A holy barrier is nullifying damage.
    # related: [炽天的幕帘(SCH)](Action16548), 
    id = 1917
    names = ['炽天的幕帘(1)', 'Seraphic Veil(1)']


class Status1874(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [天使的低语(SCH)](Action16550), 
    id = 1874
    names = ['天使的低语', "Angel's Whisper"]


class Status179(Status):
    # 体力逐渐减少
    # Contagions are spreading, causing damage over time.
    # related: [毒菌(SCH)](Action17864), 
    id = 179
    names = ['毒菌', 'Bio']


class Status189(Status):
    # 体力逐渐减少
    # Lungs are failing, causing damage over time.
    # related: [猛毒菌(SCH)](Action17865), 
    id = 189
    names = ['猛毒菌', 'Bio II']


class Status2072(Status):
    # 自身所受体力恢复效果提高
    # HP recovery via healing actions is increased.
    # related: [精神统一之策(pvp)(SCH)](Action18940), 
    id = 2072
    names = ['精神统一之策', 'Focalization']


class Status2710(Status):
    # 体力最大值提高，同时自身所受体力恢复效果提高
    # Maximum HP is increased and HP recovery via healing actions is increased.
    # related: [生命回生法(SCH)](Action25867), 
    id = 2710
    names = ['生命回生法', 'Protraction']


class Status2712(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [疾风怒涛之计(SCH)](Action25868), 
    id = 2712
    names = ['疾风之计', 'Expedience']


class Status2711(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [疾风怒涛之计(SCH)](Action25868), 
    id = 2711
    names = ['怒涛之计', 'Desperate Measures']


class Action166(Action):
    # 恢复自身最大魔力的20%
    # 追加效果：最大档数的以太超流
    # 最大档数：3档
    # 持续时间：永久
    # 发动条件：自身处于战斗状态
    # Restores 20% of maximum MP.
    # Additional Effect: Aetherflow III
    # Can only be executed while in combat.
    # related: [以太超流](Status304), 
    id = 166
    names = ['以太超流(SCH)', 'Aetherflow(SCH)']
    _orig_names = ['Aetherflow', '以太超流']


class Action167(Action):
    # 对目标发动无属性魔法攻击
    # 威力：100
    # 追加效果：恢复伤害量一定比例的体力
    # (level>=70?(job==28?追加效果：获得10点异想以太
    # :):)发动条件：以太超流
    # Deals unaspected damage with a potency of 100.
    # Additional Effect: Absorbs a portion of damage dealt as HP
    # (level>=70?(job==28?Additional Effect: Increases Faerie Gauge by 10
    # :):)Aetherflow Gauge Cost: 1
    # related: [以太超流](Status304), 
    id = 167
    names = ['Energy Drain(SCH)', '能量吸收(SCH)']
    _orig_names = ['Energy Drain', '能量吸收']
    damage = 100


class Action185(Action):
    # 恢复目标的体力
    # 恢复力：300
    # 追加效果：为目标附加能够抵御一定伤害的防护罩鼓舞
    # 鼓舞效果：抵消相当于治疗量(job==28?(level>=85?180:125):125)%的伤害
    # 持续时间：30秒
    # 无法与贤者的部分护盾效果共存
    # 追加效果（暴击时）：为目标附加能够抵御一定伤害的防护罩激励
    # 激励效果：抵消相当于治疗量(job==28?(level>=85?180:125):125)%的伤害
    # 持续时间：30秒
    # Restores target's HP.
    # Cure Potency: 300
    # Additional Effect: Grants Galvanize to target, nullifying damage equaling (job==28?(level>=85?180:125):125)% of the amount of HP restored. When critical HP is restored, also grants Catalyze, nullifying damage equaling (job==28?(level>=85?180:125):125)% the amount of HP restored.
    # Duration: 30s
    # Effect cannot be stacked with certain sage barrier effects.
    # related: [护盾(0)](Status417), [护盾(1)](Status2053), [护盾(2)](Status1415), [鼓舞(0)](Status297), [护盾(3)](Status146), [鼓舞(1)](Status1331), [护盾(4)](Status147), [激励](Status1918), 
    id = 185
    names = ['鼓舞激励之策(SCH)', 'Adloquium(SCH)']
    _orig_names = ['Adloquium', '鼓舞激励之策']
    heal = 300
    # remain metas: {'shield': '治疗量(job==28?(lv>=85?180:125):125)%'}


class Action186(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：200
    # 追加效果：附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量(job==28?(level>=85?160:115):115)%的伤害
    # 持续时间：30秒
    # 无法与贤者的部分护盾效果共存
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 200
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling (job==28?(level>=85?160:115):115)% of the amount of HP restored
    # Duration: 30s
    # Effect cannot be stacked with certain sage barrier effects.
    # related: [护盾(0)](Status417), [护盾(3)](Status146), [护盾(4)](Status147), [护盾(1)](Status2053), [士气高扬之策效果提高](Status166), [护盾(2)](Status1415), 
    id = 186
    names = ['士气高扬之策(SCH)', 'Succor(SCH)']
    _orig_names = ['Succor', '士气高扬之策']
    heal = 200
    # remain metas: {'shield': '治疗量(job==28?(lv>=85?160:115):115)%'}


class Action188(Action):
    # 以指定地点为中心产生减轻伤害的防护区域
    # (job==28?(level>=78?区域内的队员所受到的伤害会减轻10%，同时持续恢复队员体力
    # 恢复力：100
    # 持续时间：15秒
    # :区域内的队员所受到的伤害会减轻10%
    # 持续时间：15秒
    # ):区域内的队员所受到的伤害会减轻10%
    # 持续时间：15秒
    # )(level>=70?(job==28?追加效果：获得10点异想以太
    # :):)发动条件：以太超流
    # Creates a designated area in which party members will only suffer 90% of all damage inflicted.
    # Duration: 15s
    # (job==28?(level>=78?Additional Effect: Regen
    # Cure Potency: 100
    # :):)(level>=70?(job==28?Additional Effect: Increases Faerie Gauge by 10
    # :):)Aetherflow Gauge Cost: 1
    # related: [野战治疗阵(0)](Status298), [野战治疗阵(1)](Status299), [野战治疗阵(2)](Status2637), [野战治疗阵(3)](Status2638), [以太超流](Status304), [野战治疗阵(4)](Status1944), 
    id = 188
    names = ['野战治疗阵(SCH)', 'Sacred Soil(SCH)']
    _orig_names = ['Sacred Soil', '野战治疗阵']


class Action189(Action):
    # 恢复目标的体力
    # 恢复力：600
    # (level>=70?(job==28?追加效果：获得10点异想以太
    # :):)发动条件：以太超流
    # Restores target's HP.
    # Cure Potency: 600
    # (level>=70?(job==28?Additional Effect: Increases Faerie Gauge by 10
    # :):)Aetherflow Gauge Cost: 1
    # related: [以太超流](Status304), 
    id = 189
    names = ['生命活性法(SCH)', 'Lustrate(SCH)']
    _orig_names = ['生命活性法', 'Lustrate']
    heal = 600


class Action190(Action):
    # 恢复目标的体力
    # 恢复力：(job==28?(level>=85?450:400):400)
    # Restores target's HP.
    # Cure Potency: (job==28?(level>=85?450:400):400)
    id = 190
    names = ['医术(SCH)', 'Physick(SCH)']
    _orig_names = ['Physick', '医术']
    heal = "(job==28?(lv>=85?450:400):400)"


class Action802(Action):
    # 恢复目标的体力
    # 恢复力：(job==28?(level>=85?180:150):150)
    # ※该技能无法设置到热键栏
    # Restores target's HP.
    # Cure Potency: (job==28?(level>=85?180:150):150)
    # ※This action cannot be assigned to a hotbar.
    id = 802
    names = ['Embrace(SCH)', '仙光的拥抱(SCH)']
    _orig_names = ['仙光的拥抱', 'Embrace']
    heal = "(job==28?(lv>=85?180:150):150)"


class Action803(Action):
    # 持续恢复周围队员的体力
    # 恢复力：80
    # 持续时间：21秒
    # ※该技能无法设置到热键栏
    # Gradually restores the HP of all nearby party members.
    # Cure Potency: 80
    # Duration: 21s
    # ※This action cannot be assigned to a hotbar.
    # related: [仙光的低语](Status315), 
    id = 803
    names = ['仙光的低语(SCH)(0)', 'Whispering Dawn(SCH)(0)']
    _orig_names = ['Whispering Dawn', '仙光的低语']
    # remain metas: {'heal_ot': '80'}


class Action805(Action):
    # 一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5%
    # 持续时间：20秒
    # 无法与炽天使的炽天的幻光效果共存
    # ※该技能无法设置到热键栏
    # Increases healing magic potency of all nearby party members by 10%, while reducing magic damage taken by all nearby party members by 5%.
    # Duration: 20s
    # Effect cannot be stacked with Seraphic Illumination.
    # ※This action cannot be assigned to a hotbar.
    # related: [炽天的幻光](Status1875), [异想的幻光](Status317), 
    id = 805
    names = ['Fey Illumination(SCH)(0)', '异想的幻光(SCH)(0)']
    _orig_names = ['Fey Illumination', '异想的幻光']
    # remain metas: {'taken_dmg_reduce': '5%'}


class Action3583(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：400
    # (level>=70?(job==28?追加效果：获得10点异想以太
    # :):)发动条件：以太超流
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 400
    # (level>=70?(job==28?Additional Effect: Increases Faerie Gauge by 10
    # :):)Aetherflow Gauge Cost: 1
    # related: [以太超流](Status304), 
    id = 3583
    names = ['Indomitability(SCH)', '不屈不挠之策(SCH)']
    _orig_names = ['不屈不挠之策', 'Indomitability']
    heal = 400


class Action3584(Action):
    # 对目标发动无属性魔法攻击
    # 威力：220
    # Deals unaspected damage with a potency of 220.
    id = 3584
    names = ['气炎法(SCH)', 'Broil(SCH)']
    _orig_names = ['Broil', '气炎法']
    damage = 220


class Action3585(Action):
    # 令自身或目标所带的鼓舞状态向周围队员身上扩散
    # 持续时间：扩散时状态的剩余持续时间
    # 自身没有对目标附加鼓舞状态时无效
    # Extends Galvanize effect cast on self or target to nearby party members.
    # Duration: Time remaining on original effect
    # No effect when target is not under the effect of Galvanize.
    # related: [鼓舞(0)](Status297), [鼓舞(1)](Status1331), 
    id = 3585
    names = ['Deployment Tactics(SCH)', '展开战术(SCH)']
    _orig_names = ['Deployment Tactics', '展开战术']


class Action3586(Action):
    # 效果时间内自身发动1次带有鼓舞及激励状态的治疗魔法时，将鼓舞及激励效果转化为同等数值的体力恢复效果
    # 持续时间：15秒
    # Transforms the next Galvanize and Catalyze statuses into HP recovery equaling the amount of damage reduction intended for the barrier.
    # Duration: 15s
    # related: [应急战术](Status792), [激励](Status1918), 
    id = 3586
    names = ['应急战术(SCH)', 'Emergency Tactics(SCH)']
    _orig_names = ['Emergency Tactics', '应急战术']


class Action3587(Action):
    # 回收小仙女的同时为自身附加最大档数的以太超流状态
    # 并且自身发动治疗魔法的治疗量提高20%
    # 持续时间：30秒
    # 但是效果时间内无法咏唱朝日召唤及夕月召唤
    # 效果时间结束后小仙女会重新被召唤出来
    # 发动条件：自身处于战斗状态且小仙女处于同行状态
    # Orders your faerie away while granting you a full Aetherflow stack. Also increases healing magic potency by 20%.
    # Duration: 30s
    # Current faerie will return once the effect expires.
    # Summon Eos or Summon Selene cannot be executed while under the effect of Dissipation.
    # Can only be executed while in combat.
    # related: [以太超流](Status304), [转化(0)](Status2069), [转化(1)](Status791), 
    id = 3587
    names = ['Dissipation(SCH)', '转化(SCH)']
    _orig_names = ['Dissipation', '转化']


class Action7434(Action):
    # 为自身或一名队员附加“体力低于50%时或持续时间结束后自动恢复”状态
    # 恢复力：800
    # 持续时间：45秒
    # (level>=70?(job==28?追加效果：获得10点异想以太
    # :):)发动条件：以太超流
    # Grants self or target party member the effect of Excogitation, restoring HP when member's HP falls below 50% or upon effect duration expiration.
    # Cure Potency: 800
    # Duration: 45s
    # (level>=70?(job==28?Additional Effect: Increases Faerie Gauge by 10
    # :):)Aetherflow Gauge Cost: 1
    # related: [以太超流](Status304), [深谋远虑之策(0)](Status1220), [深谋远虑之策(1)](Status2182), 
    id = 7434
    names = ['深谋远虑之策(SCH)', 'Excogitation(SCH)']
    _orig_names = ['深谋远虑之策', 'Excogitation']
    # remain metas: {'heal_ot': '800'}


class Action7435(Action):
    # 对目标发动无属性魔法攻击
    # 威力：240
    # Deals unaspected damage with a potency of 240.
    id = 7435
    names = ['魔炎法(SCH)', 'Broil II(SCH)']
    _orig_names = ['Broil II', '魔炎法']
    damage = 240


class Action7436(Action):
    # 一定时间内，目标被暴击率提高10%
    # 持续时间：15秒
    # Increases rate at which target takes critical hits by 10%.
    # Duration: 15s
    # related: [连环计(0)](Status1221), [连环计(1)](Status1406), 
    id = 7436
    names = ['Chain Stratagem(SCH)', '连环计(SCH)']
    _orig_names = ['连环计', 'Chain Stratagem']


class Action7437(Action):
    # 命令召唤出的小仙女对自身或一名队员发动异想的融光
    # 再次发动时则取消该状态
    # 发动条件：异想以太10点
    # 异想以太获得条件：自身处于战斗状态，(job==28?(level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态，消耗以太超流的技能成功生效
    # Orders faerie to execute Fey Union with target party member. Effect ends upon reuse.
    # Faerie Gauge Cost: 10
    # The Faerie Gauge increases when (job==28?(level>=80?a faerie or Seraph:a faerie):a faerie) is summoned and an Aetherflow action is successfully executed while in combat.
    id = 7437
    names = ['以太契约(SCH)', 'Aetherpact(SCH)']
    _orig_names = ['以太契约', 'Aetherpact']


class Action7438(Action):
    # 持续恢复目标的体力
    # 恢复力：300
    # 发动后持续消耗异想以太
    # 且小仙女无法进行其他行动
    # 效果发动条件：与目标的距离不超过30米
    # ※该技能无法设置到热键栏
    # Gradually restores HP of party member with which faerie has a Fey Union.
    # Cure Potency: 300
    # Faerie Gauge is depleted while HP is restored. Fey Union effect fades upon execution of other faerie actions. Party member must be within 30 yalms.
    # ※This action cannot be assigned to a hotbar.
    # related: [异想的融光(0)](Status1222), [异想的融光(1)](Status1223), 
    id = 7438
    names = ['异想的融光(SCH)', 'Fey Union(SCH)']
    _orig_names = ['异想的融光', 'Fey Union']
    # remain metas: {'heal_ot': '300'}


class Action7869(Action):
    # 将异想的融光状态解除
    # Dissolves current Fey Union.
    # related: [异想的融光(0)](Status1222), [异想的融光(1)](Status1223), 
    id = 7869
    names = ['融光解除(SCH)', 'Dissolve Union(SCH)']
    _orig_names = ['融光解除', 'Dissolve Union']


class Action8904(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # 追加效果：获得10点异想以太
    # 追加效果发动条件：在战斗状态下为体力减少的目标恢复体力
    # Restores target's HP.
    # Cure Potency: 2,000
    # Additional Effect: Increases Faerie Gauge by 10 when used to restore HP of self or a party member while in combat
    id = 8904
    names = ['医术(pvp)(SCH)', 'Physick(pvp)(SCH)']
    _orig_names = ['医术(pvp)', 'Physick(pvp)']
    heal = 2000


class Action8905(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：10秒
    # 追加效果：获得10点异想以太
    # 追加效果发动条件：在战斗状态下为体力减少的目标恢复体力
    # Restores target's HP.
    # Cure Potency: 2,000
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
    # Duration: 10s
    # Additional Effect: Increases Faerie Gauge by 10 when used to restore HP of self or a party member while in combat
    id = 8905
    names = ['鼓舞激励之策(pvp)(SCH)', 'Adloquium(pvp)(SCH)']
    _orig_names = ['Adloquium(pvp)', '鼓舞激励之策(pvp)']
    heal = 2000
    # remain metas: {'shield': '治疗量100%'}


class Action8909(Action):
    # 恢复目标的体力
    # 恢复力：3000
    # 积蓄次数：3
    # 与不屈不挠之策共享复唱时间
    # Restores target's HP.
    # Cure Potency: 3,000
    # Maximum Charges: 3
    # Shares a recast timer with Indomitability.
    id = 8909
    names = ['Lustrate(pvp)(SCH)', '生命活性法(pvp)(SCH)']
    _orig_names = ['Lustrate(pvp)', '生命活性法(pvp)']
    heal = 3000


class Action16537(Action):
    # 命令小仙女发动仙光的低语
    # (job==28?(level>=80?炽天使同行时，命令炽天使发动天使的低语
    # :):)
    # 持续恢复周围队员的体力
    # 恢复力：80
    # 持续时间：21秒
    # 发动条件：(job==28?(level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态
    # Orders faerie to execute Whispering Dawn.(job==28?(level>=80? If Seraph is summoned, orders her to execute Angel's Whisper.:):)
    # Whispering Dawn(job==28?(level>=80?/Angel's Whisper:):) Effect: Gradually restores the HP of all nearby party members
    # Cure Potency: 80
    # Duration: 21s
    # related: [仙光的低语](Status315), 
    id = 16537
    names = ['仙光的低语(SCH)(1)', 'Whispering Dawn(SCH)(1)']
    _orig_names = ['Whispering Dawn', '仙光的低语']
    # remain metas: {'heal_ot': '80'}


class Action16538(Action):
    # 命令小仙女发动异想的幻光
    # (job==28?(level>=80?炽天使同行时，命令炽天使发动炽天的幻光
    # :):)
    # 一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5%
    # 持续时间：20秒
    # 小仙女的异想的幻光无法与炽天使的炽天的幻光效果共存
    # 发动条件：(job==28?(level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态
    # Orders faerie to execute Fey Illumination.(job==28?(level>=80? If Seraph is summoned, orders her to execute Seraphic Illumination.:):)
    # Fey Illumination(job==28?(level>=80?/Seraphic Illumination:):) Effect: Increases healing magic potency of all nearby party members by 10%, while reducing magic damage taken by all nearby party members by 5%
    # Duration: 20s(job==28?(level>=80?
    # Effect cannot be stacked with Seraphic Illumination.:):)
    # related: [炽天的幻光](Status1875), [异想的幻光](Status317), 
    id = 16538
    names = ['异想的幻光(SCH)(1)', 'Fey Illumination(SCH)(1)']
    _orig_names = ['Fey Illumination', '异想的幻光']
    # remain metas: {'taken_dmg_reduce': '5%'}


class Action16539(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：(job==28?(level>=54?165:150):150)
    # Deals unaspected damage with a potency of (job==28?(level>=54?165:150):150) to all nearby enemies.
    id = 16539
    names = ['破阵法(SCH)', 'Art of War(SCH)']
    _orig_names = ['破阵法', 'Art of War']
    damage = "(job==28?(lv>=54?165:150):150)"


class Action16540(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：70
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 70
    # Duration: 30s
    # related: [蛊毒法(0)](Status2039), [蛊毒法(1)](Status1895), 
    id = 16540
    names = ['蛊毒法(SCH)', 'Biolysis(SCH)']
    _orig_names = ['Biolysis', '蛊毒法']
    # remain metas: {'dmg_ot': '70'}


class Action16541(Action):
    # 对目标发动无属性魔法攻击
    # 威力：255
    # Deals unaspected damage with a potency of 255.
    id = 16541
    names = ['Broil III(SCH)', '死炎法(SCH)']
    _orig_names = ['死炎法', 'Broil III']
    damage = 255


class Action16542(Action):
    # 效果时间内，自身发动的1次鼓舞激励之策、士气高扬之策、不屈不挠之策、深谋远虑之策可以不消耗魔力及以太超流，并且必定暴击
    # 持续时间：15秒
    # Allows the execution of Adloquium, Succor, Indomitability, or Excogitation without consuming resources while also ensuring critical HP is restored.
    # Duration: 15s
    # related: [秘策](Status1896), 
    id = 16542
    names = ['秘策(SCH)', 'Recitation(SCH)']
    _orig_names = ['秘策', 'Recitation']


class Action16543(Action):
    # 命令小仙女发动异想的祥光
    # 恢复自身及周围队员的体力
    # 恢复力：320
    # 发动条件：小仙女处于同行状态
    # Orders faerie to execute Fey Blessing.
    # Fey Blessing Effect: Restores the HP of all nearby party members
    # Cure Potency: 320
    id = 16543
    names = ['Fey Blessing(SCH)(0)', '异想的祥光(SCH)(0)']
    _orig_names = ['Fey Blessing', '异想的祥光']
    heal = 320


class Action16544(Action):
    # 恢复周围队员的体力
    # 恢复力：320
    # ※该技能无法设置到热键栏
    # Restores the HP of all nearby party members.
    # Cure Potency: 320
    # ※This action cannot be assigned to a hotbar.
    id = 16544
    names = ['Fey Blessing(SCH)(1)', '异想的祥光(SCH)(1)']
    _orig_names = ['Fey Blessing', '异想的祥光']
    heal = 320


class Action16545(Action):
    # 回收小仙女，召唤炽天使
    # 召唤时间：22秒
    # 炽天使在截击状态下，会对体力减少的队员使用炽天的幕帘
    # 炽天使消失后，小仙女会重新被召唤出来
    # 发动条件：小仙女处于同行状态
    # 发动后该技能变为慰藉
    # Summons Seraph to fight at your side. When set to guard, automatically casts Seraphic Veil on party members who suffer damage.
    # Cannot summon Seraph unless a pet is already summoned. Current pet will leave the battlefield while Seraph is present, and return once gone.
    # Duration: 22s
    # ※Action changes to Consolation upon execution.
    id = 16545
    names = ['Summon Seraph(SCH)', '炽天召唤(SCH)']
    _orig_names = ['炽天召唤', 'Summon Seraph']


class Action16546(Action):
    # 命令炽天使发动慰藉
    # 恢复周围队员的体力
    # 恢复力：250
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：30秒
    # 积蓄次数：2
    # 发动条件：炽天使处于同行状态
    # ※该技能无法设置到热键栏
    # Orders Seraph to execute Consolation.
    # Consolation Effect: Restores the HP of all nearby party members
    # Cure Potency: 250
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
    # Duration: 30s
    # Maximum Charges: 2
    # ※This action cannot be assigned to a hotbar.
    id = 16546
    names = ['慰藉(SCH)(0)', 'Consolation(SCH)(0)']
    _orig_names = ['Consolation', '慰藉']
    heal = 250
    # remain metas: {'shield': '治疗量100%'}


class Action16547(Action):
    # 恢复周围队员的体力
    # 恢复力：250
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：30秒
    # ※该技能无法设置到热键栏
    # Restores the HP of all nearby party members.
    # Cure Potency: 250
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
    # Duration: 30s
    # ※This action cannot be assigned to a hotbar.
    id = 16547
    names = ['慰藉(SCH)(1)', 'Consolation(SCH)(1)']
    _orig_names = ['Consolation', '慰藉']
    heal = 250
    # remain metas: {'shield': '治疗量100%'}


class Action16548(Action):
    # 恢复目标的体力
    # 恢复力：(job==28?(level>=85?180:150):150)
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：30秒
    # ※该技能无法设置到热键栏
    # Restores target's HP.
    # Cure Potency: (job==28?(level>=85?180:150):150)
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
    # Duration: 30s
    # ※This action cannot be assigned to a hotbar.
    # related: [炽天的幕帘(0)](Status2040), [炽天的幕帘(1)](Status1917), 
    id = 16548
    names = ['Seraphic Veil(SCH)', '炽天的幕帘(SCH)']
    _orig_names = ['Seraphic Veil', '炽天的幕帘']
    heal = "(job==28?(lv>=85?180:150):150)"
    # remain metas: {'shield': '治疗量100%'}


class Action16550(Action):
    # 持续恢复周围队员的体力
    # 恢复力：80
    # 持续时间：21秒
    # ※该技能无法设置到热键栏
    # Gradually restores the HP of all nearby party members.
    # Cure Potency: 80
    # Duration: 21s
    # ※This action cannot be assigned to a hotbar.
    # related: [天使的低语](Status1874), 
    id = 16550
    names = ['天使的低语(SCH)', "Angel's Whisper(SCH)"]
    _orig_names = ['天使的低语', "Angel's Whisper"]
    # remain metas: {'heal_ot': '80'}


class Action16551(Action):
    # 一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5%
    # 持续时间：20秒
    # 无法与小仙女的异想的幻光效果共存
    # ※该技能无法设置到热键栏
    # Increases healing magic potency of nearby party members by 10%, while reducing magic damage taken by nearby party members by 5%.
    # Duration: 20s
    # Effect cannot be stacked with Fey Illumination.
    # ※This action cannot be assigned to a hotbar.
    # related: [炽天的幻光](Status1875), [异想的幻光](Status317), 
    id = 16551
    names = ['Seraphic Illumination(SCH)', '炽天的幻光(SCH)']
    _orig_names = ['炽天的幻光', 'Seraphic Illumination']
    # remain metas: {'taken_dmg_reduce': '5%'}


class Action17215(Action):
    # 召唤朝日小仙女
    # 朝日小仙女在截击状态下，会对体力减少的队员使用仙光的拥抱
    # Summons the faerie Eos to fight at your side. When set to guard, automatically casts Embrace on party members who suffer damage.
    id = 17215
    names = ['Summon Eos(SCH)', '朝日召唤(SCH)']
    _orig_names = ['朝日召唤', 'Summon Eos']


class Action17216(Action):
    # 召唤夕月小仙女
    # 夕月小仙女在截击状态下，会对体力减少的队员使用仙光的拥抱
    # Summons the faerie Selene to fight at your side. When set to guard, automatically casts Embrace on party members who suffer damage.
    id = 17216
    names = ['夕月召唤(SCH)', 'Summon Selene(SCH)']
    _orig_names = ['Summon Selene', '夕月召唤']


class Action17795(Action):
    # 对目标发动魔法攻击
    # 威力：1200
    # 追加效果：获得20点异想以太
    # Deals unaspected damage with a potency of 1,200.
    # Additional Effect: Increases Faerie Gauge by 20
    id = 17795
    names = ['死炎法(pvp)(SCH)', 'Broil III(pvp)(SCH)']
    _orig_names = ['Broil III(pvp)', '死炎法(pvp)']
    damage = 1200


class Action17796(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：目标所受到的恢复效果减少10%
    # 持续时间：15秒
    # 追加效果：获得20点异想以太
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Reduces target's HP recovered by healing actions by 10%
    # Duration: 15s
    # Additional Effect: Increases Faerie Gauge by 20
    # related: [蛊毒法(0)](Status2039), [蛊毒法(1)](Status1895), 
    id = 17796
    names = ['蛊毒法(pvp)(SCH)', 'Biolysis(pvp)(SCH)']
    _orig_names = ['蛊毒法(pvp)', 'Biolysis(pvp)']
    damage = 800


class Action17797(Action):
    # 对自身周围的敌人发动魔法攻击
    # 威力：2000
    # 追加效果：每命中一个目标都会获得10点异想以太
    # Deals unaspected damage with a potency of 2,000 to all nearby enemies.
    # Additional Effect: Increases Faerie Gauge by 10 for each enemy hit
    id = 17797
    names = ['Aura Blast(pvp)(SCH)', '生命波动法(pvp)(SCH)']
    _orig_names = ['Aura Blast(pvp)', '生命波动法(pvp)']
    damage = 2000


class Action17864(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：20
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 20
    # Duration: 30s
    # related: [毒菌](Status179), 
    id = 17864
    names = ['毒菌(SCH)', 'Bio(SCH)']
    _orig_names = ['Bio', '毒菌']
    # remain metas: {'dmg_ot': '20'}


class Action17865(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：40
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 40
    # Duration: 30s
    # related: [猛毒菌](Status189), 
    id = 17865
    names = ['猛毒菌(SCH)', 'Bio II(SCH)']
    _orig_names = ['猛毒菌', 'Bio II']
    # remain metas: {'dmg_ot': '40'}


class Action17869(Action):
    # 对目标发动无属性魔法攻击
    # 威力：150
    # Deals unaspected damage with a potency of 150.
    id = 17869
    names = ['毁灭(SCH)', 'Ruin(SCH)']
    _orig_names = ['毁灭', 'Ruin']
    damage = 150


class Action17870(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==28?(level>=82?220:(job==28?(level>=72?200:(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140))):(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140)))):(job==28?(level>=72?200:(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140))):(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140))))
    # Deals unaspected damage with a potency of (job==28?(level>=82?220:(job==28?(level>=72?200:(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140))):(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140)))):(job==28?(level>=72?200:(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140))):(job==28?(level>=64?180:(job==28?(level>=54?160:140):140)):(job==28?(level>=54?160:140):140)))).
    id = 17870
    names = ['Ruin II(SCH)', '毁坏(SCH)']
    _orig_names = ['毁坏', 'Ruin II']
    damage = "(job==28?(lv>=82?220:(job==28?(lv>=72?200:(job==28?(lv>=64?180:(job==28?(lv>=54?160:140):140)):(job==28?(lv>=54?160:140):140))):(job==28?(lv>=64?180:(job==28?(lv>=54?160:140):140)):(job==28?(lv>=54?160:140):140)))):(job==28?(lv>=72?200:(job==28?(lv>=64?180:(job==28?(lv>=54?160:140):140)):(job==28?(lv>=54?160:140):140))):(job==28?(lv>=64?180:(job==28?(lv>=54?160:140):140)):(job==28?(lv>=54?160:140):140))))"


class Action17990(Action):
    # 自身攻击造成的伤害与治疗效果提高25%
    # 持续时间：10秒
    # 追加效果：生命活性法和不屈不挠之策的复唱时间缩短15秒
    # 发动条件：异想以太50点
    # Increases damage dealt and healing potency by 25%.
    # Duration: 10s
    # Additional Effect: Reduces the recast time of both Lustrate and Indomitability by 15s
    # Faerie Gauge Cost: 50
    # related: [转化(0)](Status2069), [转化(1)](Status791), 
    id = 17990
    names = ['转化(pvp)(SCH)', 'Dissipation(pvp)(SCH)']
    _orig_names = ['Dissipation(pvp)', '转化(pvp)']


class Action18940(Action):
    # 令自身与周围队员受到的恢复效果提高20%
    # 持续时间：15秒
    # Increases HP recovered by healing actions for self and nearby party members by 20%.
    # Duration: 15s
    # related: [精神统一之策](Status2072), 
    id = 18940
    names = ['精神统一之策(pvp)(SCH)', 'Focalization(pvp)(SCH)']
    _orig_names = ['Focalization(pvp)', '精神统一之策(pvp)']


class Action18947(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：1000
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：10秒
    # 追加效果：获得10点异想以太
    # 追加效果发动条件：在战斗状态下为体力减少的目标恢复体力
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 1,000
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
    # Duration: 10s
    # Additional Effect: Increases Faerie Gauge by 10 when used to restore HP of self or a party member while in combat
    # related: [士气高扬之策效果提高](Status166), 
    id = 18947
    names = ['Succor(pvp)(SCH)', '士气高扬之策(pvp)(SCH)']
    _orig_names = ['士气高扬之策(pvp)', 'Succor(pvp)']
    heal = 1000
    # remain metas: {'shield': '治疗量100%'}


class Action18948(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：1500
    # 积蓄次数：3
    # 与生命活性法共享复唱时间
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 1,500
    # Maximum Charges: 3
    # Shares a recast timer with Lustrate.
    id = 18948
    names = ['不屈不挠之策(pvp)(SCH)', 'Indomitability(pvp)(SCH)']
    _orig_names = ['Indomitability(pvp)', '不屈不挠之策(pvp)']
    heal = 1500


class Action18949(Action):
    # 为自身或一名队员附加“体力低于50%时或持续时间结束后自动恢复”状态
    # 恢复力：4000
    # 持续时间：15秒
    # 积蓄次数：2
    # Grants self or target party member the effect of Excogitation, restoring HP when member's HP falls below 50% or upon effect duration expiration.
    # Cure Potency: 4,000
    # Duration: 15s
    # Maximum Charges: 2
    # related: [深谋远虑之策(0)](Status1220), [深谋远虑之策(1)](Status2182), 
    id = 18949
    names = ['深谋远虑之策(pvp)(SCH)', 'Excogitation(pvp)(SCH)']
    _orig_names = ['Excogitation(pvp)', '深谋远虑之策(pvp)']
    # remain metas: {'heal_ot': '4000'}


class Action25865(Action):
    # 对目标发动无属性魔法攻击
    # 威力：295
    # Deals unaspected damage with a potency of 295.
    id = 25865
    names = ['Broil IV(SCH)', '极炎法(SCH)']
    _orig_names = ['Broil IV', '极炎法']
    damage = 295


class Action25866(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：180
    # Deals unaspected damage with a potency of 180 to all nearby enemies.
    id = 25866
    names = ['裂阵法(SCH)', 'Art of War II(SCH)']
    _orig_names = ['Art of War II', '裂阵法']
    damage = 180


class Action25867(Action):
    # 令自身或其他一名队员所受的体力恢复效果提高10%
    # 发动时恢复最大体力的10%
    # 持续时间：10秒
    # Increases maximum HP of a party member or self by 10% and restores the amount increased.
    # Additional Effect: Increases HP recovery via healing actions by 10%
    # Duration: 10s
    # related: [生命回生法](Status2710), 
    id = 25867
    names = ['生命回生法(SCH)', 'Protraction(SCH)']
    _orig_names = ['生命回生法', 'Protraction']


class Action25868(Action):
    # 一定时间内，为自身及周围队员附加疾风之计与怒涛之计状态
    # 持续时间：20秒
    # 疾风之计效果：提高目标的移动速度
    # 怒涛之计效果：受到的伤害减轻10%
    # Grants Expedience and Desperate Measures to all nearby party members.
    # Expedience Effect: Increases movement speed
    # Desperate Measures Effect: Reduces damage taken by 10%
    # Duration: 20s
    # related: [疾风之计](Status2712), [怒涛之计](Status2711), 
    id = 25868
    names = ['Expedient(SCH)', '疾风怒涛之计(SCH)']
    _orig_names = ['Expedient', '疾风怒涛之计']
    # remain metas: {'taken_dmg_reduce': '10%'}


