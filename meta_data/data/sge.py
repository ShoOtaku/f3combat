from ._base import *


class Status2872(Status):
    # 为自身附加此效果的贤者发动攻击魔法时，自身体力恢复
    # Triggers a healing effect when the sage who applied this status casts attack magic.
    # related: [注药(SGE)](Action24283), [心关(SGE)](Action24285), [发炎(SGE)](Action24289), [均衡注药(SGE)](Action24293), [拯救(SGE)](Action24294), [失衡(SGE)](Action24297), [箭毒(SGE)](Action24304), [注药II(SGE)](Action24306), [发炎II(SGE)](Action24307), [均衡注药II(SGE)](Action24308), [注药III(SGE)](Action24312), [发炎III(SGE)](Action24313), [均衡注药III(SGE)](Action24314), [失衡II(SGE)](Action24315), [箭毒II(SGE)](Action24316), [魂灵风息(SGE)](Action24318), [注药III(pvp)(SGE)](Action27822), [均衡注药III(pvp)(SGE)](Action27823), [发炎III(pvp)(SGE)](Action27829), [魂灵风息(pvp)(SGE)](Action27830), [心关(pvp)(SGE)](Action27835), 
    id = 2872
    names = ['关心(0)', 'Kardion(0)']


class Status2605(Status):
    # 为自身附加此效果的贤者发动攻击魔法时，自身体力恢复
    # Triggers a healing effect when the sage who applied this status casts attack magic.
    # related: [注药(SGE)](Action24283), [心关(SGE)](Action24285), [发炎(SGE)](Action24289), [均衡注药(SGE)](Action24293), [拯救(SGE)](Action24294), [失衡(SGE)](Action24297), [箭毒(SGE)](Action24304), [注药II(SGE)](Action24306), [发炎II(SGE)](Action24307), [均衡注药II(SGE)](Action24308), [注药III(SGE)](Action24312), [发炎III(SGE)](Action24313), [均衡注药III(SGE)](Action24314), [失衡II(SGE)](Action24315), [箭毒II(SGE)](Action24316), [魂灵风息(SGE)](Action24318), [注药III(pvp)(SGE)](Action27822), [均衡注药III(pvp)(SGE)](Action27823), [发炎III(pvp)(SGE)](Action27829), [魂灵风息(pvp)(SGE)](Action27830), [心关(pvp)(SGE)](Action27835), 
    id = 2605
    names = ['关心(1)', 'Kardion(1)']


class Status2871(Status):
    # 发动攻击魔法时令指定的队员恢复体力
    # Triggers a healing effect on a player under the effect of Kardion granted by you when casting attack magic.
    # related: [心关(SGE)](Action24285), [心关(pvp)(SGE)](Action27835), 
    id = 2871
    names = ['心关(0)', 'Kardia(0)']


class Status2604(Status):
    # 发动攻击魔法时令指定的队员恢复体力
    # Triggers a healing effect on a player under the effect of Kardion granted by you when casting attack magic.
    # related: [心关(SGE)](Action24285), [心关(pvp)(SGE)](Action27835), 
    id = 2604
    names = ['心关(1)', 'Kardia(1)']


class Status2617(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [自生(SGE)](Action24288), 
    id = 2617
    names = ['自生', 'Physis']


class Status2867(Status):
    # 令自身的部分技能发生变化
    # Certain actions are being augmented.
    # related: [均衡(SGE)](Action24290), [均衡(pvp)(SGE)](Action27828), 
    id = 2867
    names = ['均衡(0)', 'Eukrasia(0)']


class Status2606(Status):
    # 令自身的部分技能发生变化
    # Certain actions are being augmented.
    # related: [均衡(SGE)](Action24290), [均衡(pvp)(SGE)](Action27828), 
    id = 2606
    names = ['均衡(1)', 'Eukrasia(1)']


class Status2608(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [均衡诊断(SGE)](Action24291), 
    id = 2608
    names = ['齐衡诊断', 'Differential Diagnosis']


class Status2865(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [均衡诊断(SGE)](Action24291), [消化(SGE)](Action24301), [均衡诊断(pvp)(SGE)](Action27825), [均衡预后(pvp)(SGE)](Action27827), 
    id = 2865
    names = ['均衡诊断(0)', 'Eukrasian Diagnosis(0)']


class Status2607(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [均衡诊断(SGE)](Action24291), [消化(SGE)](Action24301), [均衡诊断(pvp)(SGE)](Action27825), [均衡预后(pvp)(SGE)](Action27827), 
    id = 2607
    names = ['均衡诊断(1)', 'Eukrasian Diagnosis(1)']


class Status2614(Status):
    # 体力逐渐减少
    # Sustaining unaspected damage over time.
    # related: [均衡注药(SGE)](Action24293), 
    id = 2614
    names = ['均衡注药', 'Eukrasian Dosis']


class Status2610(Status):
    # 令带有关心状态的目标恢复体力的治疗量提高
    # The healing potency of Kardia is increased.
    # related: [拯救(SGE)](Action24294), 
    id = 2610
    names = ['拯救', 'Soteria']


class Status2618(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [坚角清汁(SGE)](Action24298), [白牛清汁(SGE)](Action24303), 
    id = 2618
    names = ['坚角清汁', 'Kerachole']


class Status2619(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [坚角清汁(SGE)](Action24298), [白牛清汁(SGE)](Action24303), 
    id = 2619
    names = ['白牛清汁', 'Taurochole']


class Status2611(Status):
    # 下次发动治疗魔法时，治疗量提高
    # Healing magic potency of next spell cast is increased.
    # related: [活化(SGE)](Action24300), 
    id = 2611
    names = ['活化', 'Zoe']


class Status2620(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [自生II(SGE)](Action24302), 
    id = 2620
    names = ['自生II', 'Physis II']


class Status2642(Status):
    # 输血状态消失后消耗血印档数重新附加输血状态，持续时间结束后根据血印剩余档数恢复自身体力
    # Stacks are consumed to restore the Haima barrier each time it is absorbed. Grants a healing effect when duration expires, its potency based on the number of remaining stacks.
    # related: [输血(SGE)](Action24305), [输血(pvp)(SGE)](Action27833), 
    id = 2642
    names = ['血印(0)', 'Haimatinon(0)']


class Status2612(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [输血(SGE)](Action24305), [输血(pvp)(SGE)](Action27833), 
    id = 2612
    names = ['输血(0)', 'Haima(0)']


class Status2869(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [输血(SGE)](Action24305), [输血(pvp)(SGE)](Action27833), 
    id = 2869
    names = ['输血(1)', 'Haima(1)']


class Status2870(Status):
    # 输血状态消失后消耗血印档数重新附加输血状态，持续时间结束后根据血印剩余档数恢复自身体力
    # Stacks are consumed to restore the Haima barrier each time it is absorbed. Grants a healing effect when duration expires, its potency based on the number of remaining stacks.
    # related: [输血(SGE)](Action24305), [输血(pvp)(SGE)](Action27833), 
    id = 2870
    names = ['血印(1)', 'Haimatinon(1)']


class Status2615(Status):
    # 体力逐渐减少
    # Sustaining unaspected damage over time.
    # related: [均衡注药II(SGE)](Action24308), 
    id = 2615
    names = ['均衡注药II', 'Eukrasian Dosis II']


class Status3003(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [整体论(SGE)](Action24310), 
    id = 3003
    names = ['整体论', 'Holos']


class Status2643(Status):
    # 泛输血状态消失后消耗血印档数重新附加泛输血状态，持续时间结束后根据泛血印剩余档数恢复自身体力
    # Stacks are consumed to restore the Panhaima barrier each time it is absorbed. Grants a healing effect when duration expires, its potency based on the number of remaining stacks.
    # related: [泛输血(SGE)](Action24311), 
    id = 2643
    names = ['泛血印', 'Panhaimatinon']


class Status2613(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [泛输血(SGE)](Action24311), 
    id = 2613
    names = ['泛输血', 'Panhaima']


class Status2616(Status):
    # 体力逐渐减少
    # Sustaining unaspected damage over time.
    # related: [均衡注药III(SGE)](Action24314), [均衡注药III(pvp)(SGE)](Action27823), 
    id = 2616
    names = ['均衡注药III(0)', 'Eukrasian Dosis III(0)']


class Status2864(Status):
    # 战技与魔法的咏唱及复唱时间延长
    # Weaponskill and spell cast time and recast time are increased.
    # related: [均衡注药III(SGE)](Action24314), [均衡注药III(pvp)(SGE)](Action27823), 
    id = 2864
    names = ['均衡注药III(1)', 'Eukrasian Dosis III(1)']


class Status2622(Status):
    # 自身所受的治疗效果提高
    # HP recovery via healing actions is increased.
    # related: [混合(SGE)](Action24317), 
    id = 2622
    names = ['混合', 'Krasis']


class Status2868(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [魂灵风息(SGE)](Action24318), [魂灵风息(pvp)(SGE)](Action27830), 
    id = 2868
    names = ['魂灵风息(0)', 'Pneuma(0)']


class Status2623(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [魂灵风息(SGE)](Action24318), [魂灵风息(pvp)(SGE)](Action27830), 
    id = 2623
    names = ['魂灵风息(1)', 'Pneuma(1)']


class Action24283(Action):
    # 对目标发动无属性魔法攻击
    # 威力：(job==40?(level>=64?300:(job==40?(level>=54?250:180):180)):(job==40?(level>=54?250:180):180))
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # Deals unaspected damage with a potency of (job==40?(level>=64?300:(job==40?(level>=54?250:180):180)):(job==40?(level>=54?250:180):180)).
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24283
    names = ['Dosis(SGE)', '注药(SGE)']
    _orig_names = ['注药', 'Dosis']
    damage = "(job==40?(lv>=64?300:(job==40?(lv>=54?250:180):180)):(job==40?(lv>=54?250:180):180))"
    heal = "(job==40?(lv>=85?170:130):130)"


class Action24284(Action):
    # 恢复目标的体力
    # 恢复力：(job==40?(level>=85?450:400):400)
    # Restores target's HP.
    # Cure Potency: (job==40?(level>=85?450:400):400)
    id = 24284
    names = ['诊断(SGE)', 'Diagnosis(SGE)']
    _orig_names = ['诊断', 'Diagnosis']
    heal = "(job==40?(lv>=85?450:400):400)"


class Action24285(Action):
    # 指定自身或一名队员为目标，对自身附加心关状态，对目标附加关心状态
    # 该状态下发动特定攻击魔法，令带有关心状态的目标恢复体力
    # 持续时间：永久
    # Grants self the effect of Kardia and a selected party member or self the effect of Kardion, restoring HP after casting certain magic attacks.
    # related: [心关(0)](Status2871), [关心(0)](Status2872), [心关(1)](Status2604), [关心(1)](Status2605), 
    id = 24285
    names = ['心关(SGE)', 'Kardia(SGE)']
    _orig_names = ['心关', 'Kardia']


class Action24286(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：300
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 300
    id = 24286
    names = ['预后(SGE)', 'Prognosis(SGE)']
    _orig_names = ['Prognosis', '预后']
    heal = 300


class Action24287(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43), 
    id = 24287
    names = ['Egeiro(SGE)', '复苏(SGE)']
    _orig_names = ['Egeiro', '复苏']


class Action24288(Action):
    # 持续恢复自身及周围队员的体力
    # 恢复力：100
    # 持续时间：15秒
    # Gradually restores own HP and the HP of all nearby party members.
    # Cure Potency: 100
    # Duration: 15s
    # related: [自生](Status2617), 
    id = 24288
    names = ['Physis(SGE)', '自生(SGE)']
    _orig_names = ['自生', 'Physis']
    # remain metas: {'heal_ot': '100'}


class Action24289(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：(job==40?(level>=64?400:(job==40?(level>=54?330:230):230)):(job==40?(level>=54?330:230):230))
    # 攻击复数敌人时，对目标之外的敌人威力降低30%
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 积蓄次数：2
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to target and all enemies nearby it with a potency of (job==40?(level>=64?400:(job==40?(level>=54?330:230):230)):(job==40?(level>=54?330:230):230)) for the first enemy, and 30% less for all remaining enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # Maximum Charges: 2
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24289
    names = ['发炎(SGE)', 'Phlegma(SGE)']
    _orig_names = ['Phlegma', '发炎']
    damage = "(job==40?(lv>=64?400:(job==40?(lv>=54?330:230):230)):(job==40?(lv>=54?330:230):230))"
    heal = "(job==40?(lv>=85?170:130):130)"
    # remain metas: {'aoe_reduce': '30%'}


class Action24290(Action):
    # 强化特定的攻击及治疗魔法，令其发生变化
    # 持续时间：永久
    # (job==40?(level>=82?注药III变为均衡注药III:(job==40?(level>=72?注药II变为均衡注药II:注药变为均衡注药):注药变为均衡注药)):(job==40?(level>=72?注药II变为均衡注药II:注药变为均衡注药):注药变为均衡注药))
    # 诊断变为均衡诊断
    # 预后变为均衡预后
    # 变化后的魔法发动后该效果解除
    # 该魔法有单独计算的复唱时间，不受装备和状态的影响
    # Augments certain offensive and healing magic actions.
    # (job==40?(level>=82?Dosis III is upgraded to Eukrasian Dosis III:(job==40?(level>=72?Dosis II is upgraded to Eukrasian Dosis II:Dosis is upgraded to Eukrasian Dosis):Dosis is upgraded to Eukrasian Dosis)):(job==40?(level>=72?Dosis II is upgraded to Eukrasian Dosis II:Dosis is upgraded to Eukrasian Dosis):Dosis is upgraded to Eukrasian Dosis)).
    # Diagnosis is upgraded to Eukrasian Diagnosis.
    # Prognosis is upgraded to Eukrasian Prognosis.
    # Recast timer cannot be affected by status effects or gear attributes.
    # related: [均衡(0)](Status2867), [均衡(1)](Status2606), 
    id = 24290
    names = ['均衡(SGE)', 'Eukrasia(SGE)']
    _orig_names = ['均衡', 'Eukrasia']


class Action24291(Action):
    # 恢复目标的体力
    # 恢复力：300
    # 追加效果：为目标附加能够抵御一定伤害的防护罩均衡诊断
    # 均衡诊断效果：抵消相当于恢复力(job==40?(level>=85?180:125):125)%的伤害量
    # 持续时间：30秒
    # 无法与均衡诊断及学者的鼓舞效果共存
    # 追加效果（暴击时）：为目标附加能够抵御一定伤害的防护罩齐衡诊断
    # 齐衡诊断效果：抵消相当于恢复力(job==40?(level>=85?180:125):125)%的伤害量
    # 持续时间：30秒
    # ※该技能无法设置到热键栏
    # Restores target's HP.
    # Cure Potency: 300
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling (job==40?(level>=85?180:125):125)％ of the amount of HP restored. When critical HP is restored, also grants Differential Diagnosis, nullifying damage equaling (job==40?(level>=85?180:125):125)% the amount of HP restored.
    # Duration: 30s
    # Effect cannot be stacked with Eukrasian Prognosis or scholar's Galvanize.
    # ※This action cannot be assigned to a hotbar.
    # related: [齐衡诊断](Status2608), [均衡诊断(0)](Status2865), [鼓舞(1)](Status1331), [鼓舞(0)](Status297), [均衡诊断(1)](Status2607), 
    id = 24291
    names = ['均衡诊断(SGE)', 'Eukrasian Diagnosis(SGE)']
    _orig_names = ['均衡诊断', 'Eukrasian Diagnosis']
    heal = 300
    # remain metas: {'shield': '恢复力(job==40?(lv>=85?180:125):125)%'}


class Action24292(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：100
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量(job==40?(level>=85?320:230):230)%的伤害
    # 持续时间：30秒
    # 无法与均衡诊断及学者的鼓舞效果共存
    # ※该技能无法设置到热键栏
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 100
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling (job==40?(level>=85?320:230):230)% of the amount of HP restored
    # Duration: 30s
    # Effect cannot be stacked with those of Eukrasian Diagnosis or scholar's Galvanize.
    # ※This action cannot be assigned to a hotbar.
    # related: [均衡预后(0)](Status2609), [均衡预后(1)](Status2866), [鼓舞(1)](Status1331), [鼓舞(0)](Status297), 
    id = 24292
    names = ['均衡预后(SGE)', 'Eukrasian Prognosis(SGE)']
    _orig_names = ['Eukrasian Prognosis', '均衡预后']
    heal = 100
    # remain metas: {'shield': '治疗量(job==40?(lv>=85?320:230):230)%'}


class Action24293(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：(job==40?(level>=64?40:(job==40?(level>=54?35:30):30)):(job==40?(level>=54?35:30):30))
    # 持续时间：30秒
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # ※该技能无法设置到热键栏
    # Deals unaspected damage over time.
    # Potency: (job==40?(level>=64?40:(job==40?(level>=54?35:30):30)):(job==40?(level>=54?35:30):30))
    # Duration: 30s
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # ※This action cannot be assigned to a hotbar.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), [均衡注药](Status2614), 
    id = 24293
    names = ['均衡注药(SGE)', 'Eukrasian Dosis(SGE)']
    _orig_names = ['均衡注药', 'Eukrasian Dosis']
    # remain metas: {'dmg_ot': '(job==40?(lv>=64?40:(job==40?(lv>=54?35:30):30)):(job==40?(lv>=54?35:30):30))', 'heal_ot': '(job==40?(lv>=85?170:130):130)'}


class Action24294(Action):
    # 一定时间内，发动攻击魔法时令带有关心状态的目标恢复体力的效果提高1.5倍
    # 持续时间：15秒
    # Increases the cure potency of Kardion effects granted by you by 50%.
    # Duration: 15s
    # related: [关心(0)](Status2872), [拯救](Status2610), [关心(1)](Status2605), 
    id = 24294
    names = ['拯救(SGE)', 'Soteria(SGE)']
    _orig_names = ['拯救', 'Soteria']


class Action24295(Action):
    # 指定一名敌人或队员为目标，自身快速移动到目标身边
    # 止步状态下无法发动
    # Rush to a targeted enemy's or party member's location.
    # Unable to cast if bound.
    id = 24295
    names = ['神翼(SGE)', 'Icarus(SGE)']
    _orig_names = ['神翼', 'Icarus']


class Action24296(Action):
    # 恢复目标的体力
    # 恢复力：600
    # 追加效果：恢复自身最大魔力的7%
    # 发动条件：蛇胆
    # Restores target's HP.
    # Cure Potency: 600
    # Additional Effect: Restores 7% of maximum MP
    # Addersgall Cost: 1
    id = 24296
    names = ['灵橡清汁(SGE)', 'Druochole(SGE)']
    _orig_names = ['灵橡清汁', 'Druochole']
    heal = 600


class Action24297(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：160
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # Deals unaspected damage with a potency of 160 to all nearby enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24297
    names = ['失衡(SGE)', 'Dyskrasia(SGE)']
    _orig_names = ['Dyskrasia', '失衡']
    damage = 160
    heal = "(job==40?(lv>=85?170:130):130)"


class Action24298(Action):
    # 一定时间内令自己与周围队员受到的伤害减轻10%
    # 持续时间：15秒
    # 无法与白牛清汁效果共存
    # (job==40?(level>=78?追加效果：持续恢复目标的体力
    # 恢复力：100
    # 持续时间：15秒
    # :):)追加效果：恢复自身最大魔力的7%
    # 发动条件：蛇胆
    # Reduces damage taken by self and nearby party members by 10%.
    # Duration: 15s
    # Effect cannot be stacked with Taurochole.
    # (job==40?(level>=78?Additional Effect: Regen
    # Cure Potency: 100
    # Duration: 15s
    # :):)Additional Effect: Restores 7% of maximum MP
    # Addersgall Cost: 1
    # related: [坚角清汁](Status2618), [白牛清汁](Status2619), 
    id = 24298
    names = ['坚角清汁(SGE)', 'Kerachole(SGE)']
    _orig_names = ['坚角清汁', 'Kerachole']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action24299(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：400
    # 追加效果：恢复自身最大魔力的7%
    # 发动条件：蛇胆
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 400
    # Additional Effect: Restores 7% of maximum MP
    # Addersgall Cost: 1
    id = 24299
    names = ['寄生清汁(SGE)', 'Ixochole(SGE)']
    _orig_names = ['寄生清汁', 'Ixochole']
    heal = 400


class Action24300(Action):
    # 持续时间内，发动1次治疗魔法的治疗量提高1.5倍
    # 持续时间：30秒
    # Increases healing magic potency of your next healing spell by 50%.
    # Duration: 30s
    # related: [活化](Status2611), 
    id = 24300
    names = ['Zoe(SGE)', '活化(SGE)']
    _orig_names = ['Zoe', '活化']


class Action24301(Action):
    # 以自身及周围队员为目标
    # 解除自身附加的均衡诊断或均衡预后，恢复目标的体力
    # 均衡诊断状态中恢复力：450
    # 均衡预后状态中恢复力：350
    # 自身未对目标附加均衡诊断或均衡预后状态时该技能无效
    # Restores own HP and the HP of nearby party members by removing Eukrasian Diagnosis and Eukrasian Prognosis effects granted by you.
    # Eukrasian Diagnosis Cure Potency: 450
    # Eukrasian Prognosis Cure Potency: 350
    # Targets not under the effect of Eukrasian Diagnosis or Eukrasian Prognosis will not be healed.
    # related: [均衡预后(0)](Status2609), [均衡预后(1)](Status2866), [均衡诊断(1)](Status2607), [均衡诊断(0)](Status2865), 
    id = 24301
    names = ['消化(SGE)', 'Pepsis(SGE)']
    _orig_names = ['Pepsis', '消化']
    heal = "(均衡预后状态?350:(均衡诊断状态?450:-))"


class Action24302(Action):
    # 持续恢复自身及周围队员的体力
    # 恢复力：130
    # 持续时间：15秒
    # 追加效果：令目标所受的体力恢复效果提高10%
    # 持续时间：10秒
    # Gradually restores own HP and the HP of all nearby party members.
    # Cure Potency: 130
    # Duration: 15s
    # Additional Effect: Increases HP recovered by healing actions by 10%
    # Duration: 10s
    # related: [自生II](Status2620), 
    id = 24302
    names = ['自生II(SGE)', 'Physis II(SGE)']
    _orig_names = ['自生II', 'Physis II']
    # remain metas: {'heal_ot': '130'}


class Action24303(Action):
    # 恢复自身或一名队员的体力
    # 恢复力：700
    # 追加效果：目标所受伤害减轻10%
    # 持续时间：15秒
    # 无法与坚角清汁效果共存
    # 追加效果：恢复自身最大魔力的7%
    # 发动条件：蛇胆
    # Restores own or target party member's HP.
    # Cure Potency: 700
    # Additional Effect: Reduces target's damage taken by 10%
    # Duration: 15s
    # Effect cannot be stacked with Kerachole.
    # Additional Effect: Restores 7% of maximum MP
    # Addersgall Cost: 1
    # related: [坚角清汁](Status2618), [白牛清汁](Status2619), 
    id = 24303
    names = ['Taurochole(SGE)', '白牛清汁(SGE)']
    _orig_names = ['白牛清汁', 'Taurochole']
    heal = 700
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action24304(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：(job==40?(level>=72?300:240):240)
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 发动条件：蛇刺
    # Deals unaspected damage to target and all enemies nearby it with a potency of (job==40?(level>=72?300:240):240) for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # Addersting Cost: 1
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24304
    names = ['Toxikon(SGE)', '箭毒(SGE)']
    _orig_names = ['箭毒', 'Toxikon']
    damage = "(job==40?(lv>=72?300:240):240)"
    heal = "(job==40?(lv>=85?170:130):130)"
    # remain metas: {'aoe_reduce': '50%'}


class Action24305(Action):
    # 为自身或一名队员附加能够抵消一定伤害量的防护罩
    # 该防护罩能够抵消相当于300恢复力的伤害量
    # 同时附加5档血印状态
    # 持续时间：15秒
    # 防护罩因吸收到足够的伤害而消失时，消耗1档血印重新为目标附加防护罩
    # 持续时间结束时，根据血印的剩余档数恢复目标的体力
    # 恢复力：150×血印的剩余档数
    # Erects a magicked barrier around self or target party member that absorbs damage equivalent to a heal of 300 potency.
    # Additional Effect: Grants 5 stacks of Haimatinon
    # Duration: 15s
    # When the barrier is completely absorbed, a stack of Haimatinon is consumed and a new barrier is applied.
    # When the effect duration expires, a healing effect is then applied.
    # Cure Potency: 150 per remaining stack of Haimatinon
    # related: [血印(0)](Status2642), [输血(0)](Status2612), [输血(1)](Status2869), [血印(1)](Status2870), 
    id = 24305
    names = ['Haima(SGE)', '输血(SGE)']
    _orig_names = ['输血', 'Haima']
    # remain metas: {'shield': '300恢复力', 'heal_ot': '150×血印的剩余档数'}


class Action24306(Action):
    # 对目标发动无属性魔法攻击
    # 威力：320
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # Deals unaspected damage with a potency of 320.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24306
    names = ['注药II(SGE)', 'Dosis II(SGE)']
    _orig_names = ['Dosis II', '注药II']
    damage = 320
    heal = "(job==40?(lv>=85?170:130):130)"


class Action24307(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：490
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 积蓄次数：2
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to target and all enemies nearby it with a potency of 490 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # Maximum Charges: 2
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24307
    names = ['Phlegma II(SGE)', '发炎II(SGE)']
    _orig_names = ['发炎II', 'Phlegma II']
    damage = 490
    heal = "(job==40?(lv>=85?170:130):130)"
    # remain metas: {'aoe_reduce': '50%'}


class Action24308(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：60
    # 持续时间：30秒
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # ※该技能无法设置到热键栏
    # Deals unaspected damage over time.
    # Potency: 60
    # Duration: 30s
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # ※This action cannot be assigned to a hotbar.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), [均衡注药II](Status2615), 
    id = 24308
    names = ['Eukrasian Dosis II(SGE)', '均衡注药II(SGE)']
    _orig_names = ['Eukrasian Dosis II', '均衡注药II']
    # remain metas: {'dmg_ot': '60', 'heal_ot': '(job==40?(lv>=85?170:130):130)'}


class Action24309(Action):
    # 为自身附加1档蛇胆
    # Grants 1 stack of Addersgall.
    id = 24309
    names = ['根素(SGE)', 'Rhizomata(SGE)']
    _orig_names = ['根素', 'Rhizomata']


class Action24310(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：300
    # 追加效果：自身及周围队员所受伤害减轻10%
    # 持续时间：20秒
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 300
    # Additional Effect: Reduces damage taken by self and nearby party members by 10%
    # Duration: 20s
    # related: [整体论](Status3003), 
    id = 24310
    names = ['整体论(SGE)', 'Holos(SGE)']
    _orig_names = ['Holos', '整体论']
    heal = 300
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action24311(Action):
    # 为自身及周围队员附加能够抵消一定伤害量的防护罩
    # 该防护罩能够抵消相当于200恢复力的伤害量
    # 同时附加5档泛血印状态
    # 持续时间：15秒
    # 防护罩因吸收到足够的伤害而消失时，消耗1档泛血印重新为目标附加防护罩
    # 持续时间结束时，根据泛血印的剩余档数恢复目标的体力
    # 恢复力：150×泛血印的剩余档数
    # Erects a magicked barrier around self and all party members near you that absorbs damage equivalent to a heal of 200 potency.
    # Additional Effect: Grants 5 stacks of Panhaimatinon
    # Duration: 15s
    # When the barrier is completely absorbed, a stack of Panhaimatinon is consumed and a new barrier is applied.
    # When the effect duration expires, a healing effect is then applied.
    # Cure Potency: 100 per remaining stack of Panhaimatinon
    # related: [泛血印](Status2643), [泛输血](Status2613), 
    id = 24311
    names = ['Panhaima(SGE)', '泛输血(SGE)']
    _orig_names = ['Panhaima', '泛输血']
    # remain metas: {'shield': '200恢复力', 'heal_ot': '150×泛血印的剩余档数'}


class Action24312(Action):
    # 对目标发动无属性魔法攻击
    # 威力：330
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # Deals unaspected damage with a potency of 330.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24312
    names = ['Dosis III(SGE)', '注药III(SGE)']
    _orig_names = ['Dosis III', '注药III']
    damage = 330
    heal = "(job==40?(lv>=85?170:130):130)"


class Action24313(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：510
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 积蓄次数：2
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to target and all enemies nearby it with a potency of 510 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # Maximum Charges: 2
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24313
    names = ['Phlegma III(SGE)', '发炎III(SGE)']
    _orig_names = ['Phlegma III', '发炎III']
    damage = 510
    heal = "(job==40?(lv>=85?170:130):130)"
    # remain metas: {'aoe_reduce': '50%'}


class Action24314(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：70
    # 持续时间：30秒
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # ※该技能无法设置到热键栏
    # Deals unaspected damage over time.
    # Potency: 70
    # Duration: 30s
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # ※This action cannot be assigned to a hotbar.
    # related: [均衡注药III(0)](Status2616), [均衡注药III(1)](Status2864), [关心(1)](Status2605), [关心(0)](Status2872), 
    id = 24314
    names = ['Eukrasian Dosis III(SGE)', '均衡注药III(SGE)']
    _orig_names = ['均衡注药III', 'Eukrasian Dosis III']
    # remain metas: {'dmg_ot': '70', 'heal_ot': '(job==40?(lv>=85?170:130):130)'}


class Action24315(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：170
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # Deals unaspected damage with a potency of 170 to all nearby enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24315
    names = ['失衡II(SGE)', 'Dyskrasia II(SGE)']
    _orig_names = ['失衡II', 'Dyskrasia II']
    damage = 170
    heal = "(job==40?(lv>=85?170:130):130)"


class Action24316(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：330
    # 攻击复数敌人时，对目标之外的敌人威力降低50%
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 发动条件：蛇刺
    # Deals unaspected damage to target and all enemies nearby it with a potency of 330 for the first enemy, and 50% less for all remaining enemies.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # Addersting Cost: 1
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 24316
    names = ['箭毒II(SGE)', 'Toxikon II(SGE)']
    _orig_names = ['箭毒II', 'Toxikon II']
    damage = 330
    heal = "(job==40?(lv>=85?170:130):130)"
    # remain metas: {'aoe_reduce': '50%'}


class Action24317(Action):
    # 令自身或其他一名队员所受的体力恢复效果提高20%
    # 持续时间：10秒
    # Increases HP recovery via healing actions for a party member or self by 20%.
    # Duration: 10s
    # related: [混合](Status2622), 
    id = 24317
    names = ['混合(SGE)', 'Krasis(SGE)']
    _orig_names = ['混合', 'Krasis']


class Action24318(Action):
    # 向目标所在方向发出直线无属性范围魔法攻击
    # 威力：330
    # 攻击复数敌人时，对目标之外的敌人威力降低40%
    # 追加效果：令自身及周围20米内的队员恢复体力
    # 恢复力：600
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：(job==40?(level>=85?170:130):130)
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage to all enemies in a straight line before you with a potency of 330 for the first enemy, and 40% less for all remaining enemies.
    # Additional Effect: Restores own HP and the HP of all party members within a radius of 20 yalms
    # Cure Potency: 600
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: (job==40?(level>=85?170:130):130)
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [魂灵风息(0)](Status2868), [关心(1)](Status2605), [魂灵风息(1)](Status2623), 
    id = 24318
    names = ['Pneuma(SGE)', '魂灵风息(SGE)']
    _orig_names = ['Pneuma', '魂灵风息']
    damage = 330
    heal = 600 # TODO: [600, '"(job==40?(lv>=85?170:130):130)"']
    # remain metas: {'aoe_reduce': '40%'}


class Action27822(Action):
    # 对目标发动无属性魔法攻击
    # 威力：1200
    # 追加效果：令带有自身关心状态的目标恢复体力
    # 恢复力：1000
    # Deals unaspected damage with a potency of 1,200.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: 1,000
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 27822
    names = ['注药III(pvp)(SGE)', 'Dosis III(pvp)(SGE)']
    _orig_names = ['注药III(pvp)', 'Dosis III(pvp)']
    damage = 1200
    heal = 1000


class Action27823(Action):
    # 对目标发动魔法攻击
    # 威力：1200
    # 追加效果：自动攻击间隔、战技与魔法的咏唱及复唱时间延长10%
    # 持续时间：15秒
    # 追加效果：令带有自身关心状态的目标恢复体力
    # 恢复力：1000
    # ※该技能无法设置到热键栏
    # Deals unaspected damage with a potency of 1,200.
    # Additional Effect: Lengthens weaponskill cast time and recast time as well as spell cast time and recast time by 10%
    # Duration: 15s
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: 1,000
    # ※This action cannot be assigned to a hotbar.
    # related: [均衡注药III(0)](Status2616), [均衡注药III(1)](Status2864), [关心(1)](Status2605), [关心(0)](Status2872), 
    id = 27823
    names = ['Eukrasian Dosis III(pvp)(SGE)', '均衡注药III(pvp)(SGE)']
    _orig_names = ['Eukrasian Dosis III(pvp)', '均衡注药III(pvp)']
    damage = 1200
    # remain metas: {'heal_ot': '1000'}


class Action27824(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # Restores target's HP.
    # Cure Potency: 2,000
    id = 27824
    names = ['诊断(pvp)(SGE)', 'Diagnosis(pvp)(SGE)']
    _orig_names = ['诊断(pvp)', 'Diagnosis(pvp)']
    heal = 2000


class Action27825(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：10秒
    # 无法与均衡预后效果共存
    # ※该技能无法设置到热键栏
    # Restores target's HP.
    # Cure Potency: 2,000
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling 100％ of the amount of HP restored.
    # Duration: 10s
    # Effect cannot be stacked with Eukrasian Prognosis.
    # ※This action cannot be assigned to a hotbar.
    # related: [均衡诊断(0)](Status2865), [均衡预后(1)](Status2866), [均衡预后(0)](Status2609), [均衡诊断(1)](Status2607), 
    id = 27825
    names = ['均衡诊断(pvp)(SGE)', 'Eukrasian Diagnosis(pvp)(SGE)']
    _orig_names = ['Eukrasian Diagnosis(pvp)', '均衡诊断(pvp)']
    heal = 2000
    # remain metas: {'shield': '治疗量100%'}


class Action27826(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    id = 27826
    names = ['预后(pvp)(SGE)', 'Prognosis(pvp)(SGE)']
    _orig_names = ['预后(pvp)', 'Prognosis(pvp)']
    heal = 2000


class Action27827(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于治疗量100%的伤害
    # 持续时间：10秒
    # 无法与均衡诊断效果共存
    # ※该技能无法设置到热键栏
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling 100% of the amount of HP restored
    # Duration: 10s
    # Effect cannot be stacked with those of Eukrasian Diagnosis.
    # ※This action cannot be assigned to a hotbar.
    # related: [均衡预后(0)](Status2609), [均衡预后(1)](Status2866), [均衡诊断(1)](Status2607), [均衡诊断(0)](Status2865), 
    id = 27827
    names = ['Eukrasian Prognosis(pvp)(SGE)', '均衡预后(pvp)(SGE)']
    _orig_names = ['Eukrasian Prognosis(pvp)', '均衡预后(pvp)']
    heal = 2000
    # remain metas: {'shield': '治疗量100%'}


class Action27828(Action):
    # 强化特定的攻击及治疗魔法，令其发生变化
    # 持续时间：永久
    # 注药III变为均衡注药III
    # 诊断变为均衡诊断
    # 预后变为均衡预后
    # 变化后的魔法发动后该效果解除
    # 
    # Augments certain offensive and healing magic actions.
    # Dosis III is upgraded to Eukrasian Dosis III.
    # Diagnosis is upgraded to Eukrasian Diagnosis.
    # Prognosis is upgraded to Eukrasian Prognosis.
    # related: [均衡(0)](Status2867), [均衡(1)](Status2606), 
    id = 27828
    names = ['Eukrasia(pvp)(SGE)', '均衡(pvp)(SGE)']
    _orig_names = ['均衡(pvp)', 'Eukrasia(pvp)']


class Action27829(Action):
    # 对目标发动魔法攻击
    # 威力：2400
    # 追加效果令带有关心状态的目标恢复体力
    # 恢复力：1000
    # 积蓄次数：2
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage with a potency of 2,400.
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: 1,000
    # Maximum Charges: 2
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [关心(1)](Status2605), 
    id = 27829
    names = ['发炎III(pvp)(SGE)', 'Phlegma III(pvp)(SGE)']
    _orig_names = ['Phlegma III(pvp)', '发炎III(pvp)']
    damage = 2400
    heal = 1000


class Action27830(Action):
    # 向目标所在方向发出直线范围无属性魔法攻击
    # 威力：1500～3000
    # 与目标距离越近威力越大
    # 追加效果：令自身及周围20米内的队员恢复体力，同时受到的伤害减轻10%
    # 恢复力：3000
    # 持续时间：15秒
    # 追加效果：令带有关心状态的目标恢复体力
    # 恢复力：1000
    # 该魔法有单独计算的复唱时间
    # Deals unaspected damage with a potency of 1,500 to all enemies in a straight line before you.
    # Potency increases up to 3,000 based on proximity to enemies.
    # Additional Effect: Restores own HP and the HP of all party members within a radius of 20 yalms, and reduces damage taken by 10%
    # Cure Potency: 3,000
    # Duration: 15s
    # Additional Effect: Restores HP to targets under the effect of Kardion granted by you
    # Cure Potency: 1,000
    # This action does not share a recast timer with any other actions.
    # related: [关心(0)](Status2872), [魂灵风息(0)](Status2868), [关心(1)](Status2605), [魂灵风息(1)](Status2623), 
    id = 27830
    names = ['Pneuma(pvp)(SGE)', '魂灵风息(pvp)(SGE)']
    _orig_names = ['魂灵风息(pvp)', 'Pneuma(pvp)']
    damage = [1500, 3000]
    heal = 3000
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '1000'}


class Action27831(Action):
    # 恢复目标的体力
    # 恢复力：3000
    # 发动条件：蛇胆
    # 蛇胆获得条件：每隔10秒获得1档，当积攒到最大档数时无法继续获得蛇胆
    # Restores target's HP.
    # Cure Potency: 3,000
    # Addersgall Cost: 1
    # Addersgall is granted automatically every 10 seconds.
    id = 27831
    names = ['Druochole(pvp)(SGE)', '灵橡清汁(pvp)(SGE)']
    _orig_names = ['灵橡清汁(pvp)', 'Druochole(pvp)']
    heal = 3000


class Action27832(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：1500
    # 发动条件：蛇胆
    # 蛇胆获得条件：每隔10秒获得1档，当积攒到最大档数时无法继续获得蛇胆
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 1,500
    # Addersgall Cost: 1
    # Addersgall is granted automatically every 10 seconds.
    id = 27832
    names = ['寄生清汁(pvp)(SGE)', 'Ixochole(pvp)(SGE)']
    _orig_names = ['寄生清汁(pvp)', 'Ixochole(pvp)']
    heal = 1500


class Action27833(Action):
    # 为自身或一名队员附加能够抵消一定伤害量的防护罩
    # 该防护罩能够抵消相当于1000恢复力的伤害量
    # 同时附加5档血印状态
    # 持续时间：15秒
    # 防护罩因吸收到足够的伤害而消失时，消耗1档血印重新为目标附加防护罩
    # 持续时间结束时，根据血印的剩余档数恢复目标的体力
    # 恢复力：1000×血印的剩余档数
    # Creates a barrier around self or target party member that absorbs damage equivalent to a heal of 1,000 potency.
    # Additional Effect: Grants 5 stacks of Haimatinon
    # Duration: 15s
    # When the barrier is completely absorbed, a stack of Haimatinon is consumed and a new barrier is applied.
    # When the effect duration expires, a healing effect is then applied.
    # Cure Potency: 1,000 per remaining stack of Haimatinon
    # related: [血印(0)](Status2642), [输血(0)](Status2612), [输血(1)](Status2869), [血印(1)](Status2870), 
    id = 27833
    names = ['Haima(pvp)(SGE)', '输血(pvp)(SGE)']
    _orig_names = ['输血(pvp)', 'Haima(pvp)']
    # remain metas: {'shield': '1000恢复力', 'heal_ot': '1000×血印的剩余档数'}


class Action27834(Action):
    # 指定一名敌人或队员为目标，自身快速移动到目标身边
    # 止步状态下无法发动
    # Rush to a targeted enemy's or party member's location.
    # Unable to cast if bound.
    id = 27834
    names = ['神翼(pvp)(SGE)', 'Icarus(pvp)(SGE)']
    _orig_names = ['神翼(pvp)', 'Icarus(pvp)']


class Action27835(Action):
    # 指定自身或一名队员为目标，对自身附加心关状态，对目标附加关心状态
    # 该状态下发动特定攻击技能，令带有关心状态的目标恢复体力
    # 持续时间：永久
    # Grants self the effect of Kardia and a selected party member or self the effect of Kardion, restoring HP after casting certain magic attacks.
    # related: [心关(0)](Status2871), [关心(0)](Status2872), [心关(1)](Status2604), [关心(1)](Status2605), 
    id = 27835
    names = ['心关(pvp)(SGE)', 'Kardia(pvp)(SGE)']
    _orig_names = ['Kardia(pvp)', '心关(pvp)']


