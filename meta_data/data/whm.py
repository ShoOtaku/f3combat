from ._base import *


class Status143(Status):
    # 风属性持续伤害，体力逐渐流失
    # Sustaining wind damage over time.
    # related: [疾风(WHM)](Action121), 
    id = 143
    names = ['疾风', 'Aero']


class Status1140(Status):
    # 可选择在原地复活
    # Teetering on the brink of consciousness.
    # related: [复活(WHM)](Action125), 
    id = 1140
    names = ['复活(0)', 'Raise(0)']


class Status148(Status):
    # 接受别人发动的复活
    # Teetering on the brink of consciousness.
    # related: [复活(WHM)](Action125), 
    id = 148
    names = ['复活(1)', 'Raise(1)']


class Status144(Status):
    # 风属性持续伤害，体力逐渐流失
    # Sustaining wind damage over time.
    # related: [烈风(WHM)](Action132), 
    id = 144
    names = ['烈风', 'Aero II']


class Status157(Status):
    # 自动攻击间隔时间缩短，魔法的咏唱时间和复唱时间缩短
    # Spell cast times, recast times, and auto-attack delay are reduced.
    # related: [神速咏唱(WHM)](Action136), 
    id = 157
    names = ['神速咏唱', 'Presence of Mind']


class Status897(Status):
    # 連続してＨＰが回復している状態。
    # Regenerating HP over time.
    # related: [再生(WHM)](Action137), 
    id = 897
    names = ['○削除予定', 'Regen(0)']


class Status1330(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [再生(WHM)](Action137), 
    id = 1330
    names = ['再生(0)', 'Regen(1)']


class Status158(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [再生(WHM)](Action137), 
    id = 158
    names = ['再生(1)', 'Regen(2)']


class Status739(Status):
    # 产生能够令范围内队员恢复体力的区域
    # A veil of succor is healing party members in the area.
    # related: [庇护所(WHM)](Action3569), 
    id = 739
    names = ['庇护所(0)', 'Asylum(0)']


class Status1911(Status):
    # 产生能够令范围内队员恢复体力的区域
    # A veil of succor is healing party members in the area.
    # related: [庇护所(WHM)](Action3569), 
    id = 1911
    names = ['庇护所(1)', 'Asylum(1)']


class Status1912(Status):
    # 自身所受的治疗效果提高
    # HP recovery via healing actions is increased.
    # related: [庇护所(WHM)](Action3569), 
    id = 1912
    names = ['庇护所(2)', 'Asylum(2)']


class Status1217(Status):
    # 下一次发动技能时不会消耗魔力
    # Next spell cast consumes no MP.
    # related: [无中生有(WHM)](Action7430), 
    id = 1217
    names = ['无中生有', 'Thin Air']


class Status1218(Status):
    # 抵消一定伤害
    # A holy blessing from the gods is nullifying damage.
    # related: [神祝祷(WHM)](Action7432), 
    id = 1218
    names = ['神祝祷(0)', 'Divine Benison(0)']


class Status1404(Status):
    # 抵消一定伤害
    # A holy blessing from the gods is nullifying damage.
    # related: [神祝祷(WHM)](Action7432), 
    id = 1404
    names = ['神祝祷(1)', 'Divine Benison(1)']


class Status1219(Status):
    # 成为白魔法师全大赦的对象
    # Sins are confessed. Ready for Plenary Indulgence.
    # related: [全大赦(WHM)](Action7433), 
    id = 1219
    names = ['告解', 'Confession']


class Status2036(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [安慰之心(WHM)](Action16531), [安慰之心(pvp)(WHM)](Action17791), 
    id = 2036
    names = ['安慰之心', 'Afflatus Solace']


class Status2035(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [天辉(WHM)](Action16532), [天辉(pvp)(WHM)](Action17790), 
    id = 2035
    names = ['天辉(0)', 'Dia(0)']


class Status1871(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [天辉(WHM)](Action16532), [天辉(pvp)(WHM)](Action17790), 
    id = 1871
    names = ['天辉(1)', 'Dia(1)']


class Status1872(Status):
    # 治疗魔法的治疗量提高，且减少周围队员受到的伤害
    # Healing magic potency is increased while damage taken by nearby party members is reduced.
    # related: [节制(WHM)](Action16536), [节制(pvp)(WHM)](Action17794), 
    id = 1872
    names = ['节制(0)', 'Temperance(0)']


class Status1873(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [节制(WHM)](Action16536), [节制(pvp)(WHM)](Action17794), 
    id = 1873
    names = ['节制(1)', 'Temperance(1)']


class Status2037(Status):
    # 发动攻击所造成的伤害及自身发动的体力恢复效果提高，周围队员所受伤害减轻
    # Damage dealt and potency of all HP restoration actions are increased while damage taken by nearby party members is reduced.
    # related: [节制(WHM)](Action16536), [节制(pvp)(WHM)](Action17794), 
    id = 2037
    names = ['节制(2)', 'Temperance(2)']


class Status2038(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [节制(WHM)](Action16536), [节制(pvp)(WHM)](Action17794), 
    id = 2038
    names = ['节制(3)', 'Temperance(3)']


class Status2708(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [水流幕(WHM)](Action25861), 
    id = 2708
    names = ['水流幕', 'Aquaveil']


class Status2709(Status):
    # 受到伤害或持续时间结束时自动发动恢复效果
    # Triggers a healing effect upon taking damage or when duration expires.
    # related: [礼仪之铃(WHM)](Action25862), 
    id = 2709
    names = ['礼仪之铃', 'Liturgy of the Bell']


class Action119(Action):
    # 对目标发动土属性魔法攻击
    # 威力：140
    # Deals earth damage with a potency of 140.
    id = 119
    names = ['Stone(WHM)', '飞石(WHM)']
    _orig_names = ['Stone', '飞石']
    damage = 140


class Action120(Action):
    # 恢复目标的体力
    # 恢复力：(job==24?(level>=85?500:450):450)(level>=32?(job==6?
    # 追加效果（发动几率15%）：令下次发动的救疗不消耗魔力
    # 持续时间：15秒:(job==24?
    # 追加效果（发动几率15%）：令下次发动的救疗不消耗魔力
    # 持续时间：15秒:)):)
    # Restores target's HP.
    # Cure Potency: (job==24?(level>=85?500:450):450)(level>=32?(job==6?
    # Additional Effect: 15% chance next Cure II will cost no MP
    # Duration: 15s:(job==24?
    # Additional Effect: 15% chance next Cure II will cost no MP
    # Duration: 15s:)):)
    id = 120
    names = ['Cure(WHM)', '治疗(WHM)']
    _orig_names = ['Cure', '治疗']
    heal = "(job==24?(lv>=85?500:450):450)"


class Action121(Action):
    # 对目标发动风属性魔法攻击
    # 威力：50
    # 追加效果：风属性持续伤害
    # 威力：30
    # 持续时间：18秒
    # Deals wind damage with a potency of 50.
    # Additional Effect: Wind damage over time
    # Potency: 30
    # Duration: 18s
    # related: [疾风](Status143), 
    id = 121
    names = ['Aero(WHM)', '疾风(WHM)']
    _orig_names = ['疾风', 'Aero']
    damage = 50
    # remain metas: {'dmg_ot': '30'}


class Action124(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：(job==24?(level>=85?400:300):300)
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: (job==24?(level>=85?400:300):300)
    id = 124
    names = ['Medica(WHM)', '医治(WHM)']
    _orig_names = ['Medica', '医治']
    heal = "(job==24?(lv>=85?400:300):300)"


class Action125(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [复活(0)](Status1140), [衰弱](Status43), [复活(1)](Status148), 
    id = 125
    names = ['复活(WHM)', 'Raise(WHM)']
    _orig_names = ['复活', 'Raise']


class Action127(Action):
    # 对目标发动土属性魔法攻击
    # 威力：190
    # Deals earth damage with a potency of 190.
    id = 127
    names = ['Stone II(WHM)', '坚石(WHM)']
    _orig_names = ['Stone II', '坚石']
    damage = 190


class Action131(Action):
    # 恢复目标及其周围队员的体力
    # 恢复力：(job==24?(level>=85?600:550):550)
    # Restores HP of target and all party members nearby target.
    # Cure Potency: (job==24?(level>=85?600:550):550)
    id = 131
    names = ['愈疗(WHM)', 'Cure III(WHM)']
    _orig_names = ['愈疗', 'Cure III']
    heal = "(job==24?(lv>=85?600:550):550)"


class Action132(Action):
    # 对目标发动风属性魔法攻击
    # 威力：60
    # 追加效果：风属性持续伤害
    # 威力：60
    # 持续时间：18秒
    # Deals wind damage with a potency of 60.
    # Additional Effect: Wind damage over time
    # Potency: 60
    # Duration: 18s
    # related: [烈风](Status144), 
    id = 132
    names = ['烈风(WHM)', 'Aero II(WHM)']
    _orig_names = ['烈风', 'Aero II']
    damage = 60
    # remain metas: {'dmg_ot': '60'}


class Action133(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：(job==24?(level>=85?250:200):200)
    # 追加效果：目标体力持续恢复
    # 恢复力：(job==24?(level>=85?150:100):100)
    # 持续时间：15秒
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: (job==24?(level>=85?250:200):200)
    # Additional Effect: Regen
    # Cure Potency: (job==24?(level>=85?150:100):100)
    # Duration: 15s
    # related: [医济](Status150), 
    id = 133
    names = ['医济(WHM)', 'Medica II(WHM)']
    _orig_names = ['Medica II', '医济']
    heal = "(job==24?(lv>=85?250:200):200)"
    # remain metas: {'heal_ot': '(job==24?(lv>=85?150:100):100)'}


class Action135(Action):
    # 恢复目标的体力
    # 恢复力：(job==24?(level>=85?800:700):700)
    # Restores target's HP.
    # Cure Potency: (job==24?(level>=85?800:700):700)
    id = 135
    names = ['救疗(WHM)', 'Cure II(WHM)']
    _orig_names = ['Cure II', '救疗']
    heal = "(job==24?(lv>=85?800:700):700)"


class Action136(Action):
    # 一定时间内，自身的自动攻击间隔、魔法的咏唱及复唱时间缩短20%
    # 持续时间：15秒
    # Reduces spell cast time and recast time, and auto-attack delay by 20%.
    # Duration: 15s
    # related: [神速咏唱](Status157), 
    id = 136
    names = ['Presence of Mind(WHM)', '神速咏唱(WHM)']
    _orig_names = ['Presence of Mind', '神速咏唱']


class Action137(Action):
    # 令目标体力持续恢复
    # 恢复力：(job==24?(level>=85?250:200):200)
    # 持续时间：18秒
    # Grants healing over time effect to target.
    # Cure Potency: (job==24?(level>=85?250:200):200)
    # Duration: 18s
    # related: [○削除予定](Status897), [再生(0)](Status1330), [再生(1)](Status158), 
    id = 137
    names = ['再生(WHM)', 'Regen(WHM)']
    _orig_names = ['Regen', '再生']
    # remain metas: {'heal_ot': '(job==24?(lv>=85?250:200):200)'}


class Action139(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：140
    # 追加效果：眩晕
    # 持续时间：4秒
    # Deals unaspected damage with a potency of 140 to all nearby enemies.
    # Additional Effect: Stun
    # Duration: 4s
    id = 139
    names = ['神圣(WHM)', 'Holy(WHM)']
    _orig_names = ['神圣', 'Holy']
    damage = 140


class Action140(Action):
    # 令目标体力完全恢复
    # Restores all of a target's HP.
    id = 140
    names = ['天赐祝福(WHM)', 'Benediction(WHM)']
    _orig_names = ['天赐祝福', 'Benediction']


class Action3568(Action):
    # 对目标发动土属性魔法攻击
    # 威力：230
    # Deals earth damage with a potency of 230.
    id = 3568
    names = ['垒石(WHM)', 'Stone III(WHM)']
    _orig_names = ['垒石', 'Stone III']
    damage = 230


class Action3569(Action):
    # 以指定地点为中心产生治疗区域
    # 效果时间内，持续恢复进入该区域的自身及队员的体力
    # 恢复力：100
    # 持续时间：24秒(job==24?(level>=78?
    # 追加效果：区域内的自身和队员所受的体力恢复效果提高10%:):)
    # Envelops a designated area in a veil of succor, granting healing over time to self and any party members who enter.
    # Cure Potency: 100
    # Duration: 24s (job==24?(level>=78?
    # Additional Effect: Increases HP recovery via healing actions on party members in the designated area by 10%:):)
    # related: [庇护所(0)](Status739), [庇护所(1)](Status1911), [庇护所(2)](Status1912), 
    id = 3569
    names = ['Asylum(WHM)', '庇护所(WHM)']
    _orig_names = ['Asylum', '庇护所']
    # remain metas: {'heal_ot': '100'}


class Action3570(Action):
    # 恢复目标的体力
    # 恢复力：700
    # Restores target's HP.
    # Cure Potency: 700
    id = 3570
    names = ['Tetragrammaton(WHM)', '神名(WHM)']
    _orig_names = ['Tetragrammaton', '神名']
    heal = 700


class Action3571(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：400
    # 追加效果：恢复自身及周围队员的体力
    # 恢复力：400
    # 追加效果：恢复自身最大魔力的5%
    # Deals unaspected damage with a potency of 400 to all nearby enemies.
    # Additional Effect: Restores own HP and the HP of nearby party members
    # Cure Potency: 400
    # Additional Effect: Restores 5% of maximum MP
    id = 3571
    names = ['法令(WHM)', 'Assize(WHM)']
    _orig_names = ['法令', 'Assize']
    damage = 400
    heal = 400


class Action7430(Action):
    # 下一次发动技能消耗的魔力降低100%
    # 持续时间：12秒
    # 积蓄次数：2
    # Next action is executed without MP cost.
    # Duration: 12s
    # Maximum Charges: 2
    # related: [无中生有](Status1217), 
    id = 7430
    names = ['Thin Air(WHM)', '无中生有(WHM)']
    _orig_names = ['Thin Air', '无中生有']


class Action7431(Action):
    # 对目标发动土属性魔法攻击
    # 威力：270
    # Deals earth damage with a potency of 270.
    id = 7431
    names = ['崩石(WHM)', 'Stone IV(WHM)']
    _orig_names = ['崩石', 'Stone IV']
    damage = 270


class Action7432(Action):
    # 为自身或一名队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于500恢复力的伤害量
    # 持续时间：15秒(job==24?(level>=88?
    # 积蓄次数：2:):)
    # Creates a barrier around self or target party member that absorbs damage equivalent to a heal of 500 potency.
    # Duration: 15s(job==24?(level>=88?
    # Maximum Charges: 2:):)
    # related: [神祝祷(0)](Status1218), [神祝祷(1)](Status1404), 
    id = 7432
    names = ['Divine Benison(WHM)', '神祝祷(WHM)']
    _orig_names = ['神祝祷', 'Divine Benison']
    # remain metas: {'shield': '500恢复力'}


class Action7433(Action):
    # 为自身与周围队员附加告解状态
    # 持续时间：10秒
    # 在状态中使用医治、愈疗、医济、狂喜之心，会使目标产生额外的恢复效果
    # 恢复力：200
    # Grants Confession to self and nearby party members.
    # Upon receiving HP recovery via Medica, Medica II, Cure III, or Afflatus Rapture cast by self, Confession triggers an additional healing effect.
    # Cure Potency: 200
    # Duration: 10s
    # related: [告解](Status1219), [医济](Status150), 
    id = 7433
    names = ['全大赦(WHM)', 'Plenary Indulgence(WHM)']
    _orig_names = ['全大赦', 'Plenary Indulgence']
    # remain metas: {'heal_ot': '200'}


class Action8895(Action):
    # 恢复目标的体力
    # 恢复力：2000
    # Restores target's HP.
    # Cure Potency: 2,000
    id = 8895
    names = ['治疗(pvp)(WHM)', 'Cure(pvp)(WHM)']
    _orig_names = ['治疗(pvp)', 'Cure(pvp)']
    heal = 2000


class Action8896(Action):
    # 恢复目标的体力
    # 恢复力：4000
    # Restores target's HP.
    # Cure Potency: 4,000
    id = 8896
    names = ['Cure II(pvp)(WHM)', '救疗(pvp)(WHM)']
    _orig_names = ['Cure II(pvp)', '救疗(pvp)']
    heal = 4000


class Action9620(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：1000
    # 追加效果：恢复自身及周围队员的体力
    # 恢复力：2000
    # Deals unaspected damage with a potency of 1,000 to all nearby enemies.
    # Additional Effect: Restores own HP and the HP of nearby party members
    # Cure Potency: 2,000
    id = 9620
    names = ['Assize(pvp)(WHM)', '法令(pvp)(WHM)']
    _orig_names = ['Assize(pvp)', '法令(pvp)']
    damage = 1000
    heal = 2000


class Action13975(Action):
    # 恢复目标的体力
    # 恢复力：4000
    # 积蓄次数：2
    # Restores target's HP.
    # Cure Potency: 4,000
    # Maximum Charges: 2
    id = 13975
    names = ['Tetragrammaton(pvp)(WHM)', '神名(pvp)(WHM)']
    _orig_names = ['Tetragrammaton(pvp)', '神名(pvp)']
    heal = 4000


class Action16531(Action):
    # 恢复目标的体力
    # 恢复力：(job==24?(level>=85?800:700):700)
    # (job==24?(level>=74?追加效果：血百合开放
    # :):)发动条件：治疗百合
    # Restores target's HP.
    # Cure Potency: (job==24?(level>=85?800:700):700)(job==24?(level>=74?
    # Additional Effect: Nourishes the Blood Lily:):)
    # Healing Gauge Cost: 1 Lily
    # related: [安慰之心](Status2036), 
    id = 16531
    names = ['安慰之心(WHM)', 'Afflatus Solace(WHM)']
    _orig_names = ['Afflatus Solace', '安慰之心']
    heal = "(job==24?(lv>=85?800:700):700)"


class Action16532(Action):
    # 对目标发动无属性魔法攻击
    # 威力：60
    # 追加效果：无属性持续伤害
    # 威力：60
    # 持续时间：30秒
    # Deals unaspected damage with a potency of 60.
    # Additional Effect: Unaspected damage over time
    # Potency: 60
    # Duration: 30s
    # related: [天辉(0)](Status2035), [天辉(1)](Status1871), 
    id = 16532
    names = ['Dia(WHM)', '天辉(WHM)']
    _orig_names = ['Dia', '天辉']
    damage = 60
    # remain metas: {'dmg_ot': '60'}


class Action16533(Action):
    # 对目标发动无属性魔法攻击
    # 威力：290
    # Deals unaspected damage with a potency of 290.
    id = 16533
    names = ['闪耀(WHM)', 'Glare(WHM)']
    _orig_names = ['Glare', '闪耀']
    damage = 290


class Action16534(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：(job==24?(level>=85?400:300):300)
    # 追加效果：血百合开放
    # 发动条件：治疗百合
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: (job==24?(level>=85?400:300):300)
    # Additional Effect: Nourishes the Blood Lily
    # Healing Gauge Cost: 1 Lily
    id = 16534
    names = ['狂喜之心(WHM)', 'Afflatus Rapture(WHM)']
    _orig_names = ['Afflatus Rapture', '狂喜之心']
    heal = "(job==24?(lv>=85?400:300):300)"


class Action16535(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：900
    # 攻击复数敌人时，对目标之外的敌人威力降低25%
    # 发动条件：血百合完全开放
    # Deals unaspected damage to target and all enemies nearby it with a potency of 900 for the first enemy, and 25% less for all remaining enemies.
    # Can only be executed when the Blood Lily is in full bloom.
    id = 16535
    names = ['苦难之心(WHM)', 'Afflatus Misery(WHM)']
    _orig_names = ['苦难之心', 'Afflatus Misery']
    damage = 900
    # remain metas: {'aoe_reduce': '25%'}


class Action16536(Action):
    # 一定时间内，自身发动治疗魔法的治疗量提高20%，自身与30米以内的队员受到的伤害减轻10%
    # 持续时间：20秒
    # Increases healing magic potency by 20%, while reducing damage taken by self and all party members within a radius of 30 yalms by 10%.
    # Duration: 20s
    # related: [节制(0)](Status1872), [节制(1)](Status1873), [节制(2)](Status2037), [节制(3)](Status2038), 
    id = 16536
    names = ['Temperance(WHM)', '节制(WHM)']
    _orig_names = ['节制', 'Temperance']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action17789(Action):
    # 对目标发动魔法攻击
    # 威力：1200
    # Deals unaspected damage with a potency of 1,200.
    id = 17789
    names = ['Glare(pvp)(WHM)', '闪耀(pvp)(WHM)']
    _orig_names = ['闪耀(pvp)', 'Glare(pvp)']
    damage = 1200


class Action17790(Action):
    # 对目标发动魔法攻击
    # 威力：800
    # 追加效果：令目标受到的伤害提高10%
    # 持续时间：15秒
    # Deals unaspected damage with a potency of 800.
    # Additional Effect: Increases target's damage taken by 10%
    # Duration: 15s
    # related: [天辉(0)](Status2035), [天辉(1)](Status1871), 
    id = 17790
    names = ['Dia(pvp)(WHM)', '天辉(pvp)(WHM)']
    _orig_names = ['Dia(pvp)', '天辉(pvp)']
    damage = 800
    # remain metas: {'taken_dmg_increase': '10%'}


class Action17791(Action):
    # 恢复目标的体力
    # 恢复力：4000
    # 追加效果：令目标体力持续恢复
    # 恢复力：400
    # 持续时间：15秒
    # 追加效果：血百合开放
    # 发动条件：治疗百合
    # 治疗百合开放条件：自身进入战斗状态后每隔10秒开放一朵
    # 最大档数：3档
    # Restores target's HP.
    # Cure Potency: 4,000
    # Additional Effect: Regen
    # Cure Potency: 400
    # Duration: 15s
    # Additional Effect: Nourishes the Blood Lily
    # Healing Gauge Cost: 1 Lily
    # A Lily is granted every 10 seconds while in combat.
    # related: [安慰之心](Status2036), 
    id = 17791
    names = ['Afflatus Solace(pvp)(WHM)', '安慰之心(pvp)(WHM)']
    _orig_names = ['安慰之心(pvp)', 'Afflatus Solace(pvp)']
    heal = 4000
    # remain metas: {'heal_ot': '400'}


class Action17793(Action):
    # 对目标及其周围的敌人发动范围魔法攻击
    # 威力：2400
    # 发动条件：血百合完全开放
    # Deals unaspected damage with a potency of 2,400 to target and all enemies nearby it.
    # Can only be executed when the Blood Lily is in full bloom.
    id = 17793
    names = ['苦难之心(pvp)(WHM)', 'Afflatus Misery(pvp)(WHM)']
    _orig_names = ['Afflatus Misery(pvp)', '苦难之心(pvp)']
    damage = 2400


class Action17794(Action):
    # 自身攻击造成的伤害与治疗效果提高20%，自身与30米以内的队员受到的伤害减轻10%
    # 持续时间：15秒
    # Increases damage dealt and healing potency by 20%, while reducing damage taken by self and all party members within a radius of 30 yalms by 10%.
    # Duration: 15s
    # related: [节制(0)](Status1872), [节制(1)](Status1873), [节制(2)](Status2037), [节制(3)](Status2038), 
    id = 17794
    names = ['Temperance(pvp)(WHM)', '节制(pvp)(WHM)']
    _orig_names = ['Temperance(pvp)', '节制(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action18945(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    id = 18945
    names = ['医治(pvp)(WHM)', 'Medica(pvp)(WHM)']
    _orig_names = ['医治(pvp)', 'Medica(pvp)']
    heal = 2000


class Action18946(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：2000
    # 追加效果：目标体力持续恢复
    # 恢复力：200
    # 持续时间：15秒
    # 追加效果：血百合
    # 发动条件：治疗百合
    # 治疗百合获得条件：自身进入战斗状态后每隔10秒获得一朵
    # 最大档数：3
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 2,000
    # Additional Effect: Regen
    # Cure Potency: 200
    # Duration: 15s
    # Additional Effect: Nourishes the Blood Lily
    # Healing Gauge Cost: 1 Lily
    # A Lily is granted every 10 seconds while in combat.
    id = 18946
    names = ['Afflatus Rapture(pvp)(WHM)', '狂喜之心(pvp)(WHM)']
    _orig_names = ['Afflatus Rapture(pvp)', '狂喜之心(pvp)']
    heal = 2000
    # remain metas: {'heal_ot': '200'}


class Action25859(Action):
    # 对目标发动无属性魔法攻击
    # 威力：310
    # Deals unaspected damage with a potency of 310.
    id = 25859
    names = ['Glare III(WHM)', '闪灼(WHM)']
    _orig_names = ['闪灼', 'Glare III']
    damage = 310


class Action25860(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：150
    # 追加效果：眩晕
    # 持续时间：4秒
    # Deals unaspected damage with a potency of 150 to all nearby enemies.
    # Additional Effect: Stun
    # Duration: 4s
    id = 25860
    names = ['豪圣(WHM)', 'Holy III(WHM)']
    _orig_names = ['豪圣', 'Holy III']
    damage = 150


class Action25861(Action):
    # 令自身或一名队员受到的伤害减轻15%
    # 持续时间：8秒
    # Reduces damage taken by a party member or self by 15%.
    # Duration: 8s
    # related: [水流幕](Status2708), 
    id = 25861
    names = ['Aquaveil(WHM)', '水流幕(WHM)']
    _orig_names = ['水流幕', 'Aquaveil']
    # remain metas: {'taken_dmg_reduce': '15%'}


class Action25862(Action):
    # 在指定地点设置礼仪之铃，同时为自身附加5档礼仪之铃状态
    # 持续时间：15秒
    # 礼仪之铃的持续时间内自身受到伤害时，消耗1档礼仪之铃状态为自身及礼仪之铃周围20米以内的队员恢复体力
    # 恢复力：400
    # 该效果每秒只能发动一次
    # 礼仪之铃档数全部消耗或持续时间结束后，礼仪之铃消失
    # 礼仪之铃持续时间结束时，消耗剩余礼仪之铃档数恢复目标的体力
    # 恢复力：200×剩余档数
    # Places a healing blossom at the designated location and grants 5 stacks of Liturgy of the Bell to self.
    # Duration: 15s
    # Taking damage will expend 1 stack of Liturgy of the Bell to heal self and all party members within a radius of 20 yalms.
    # Cure Potency: 400
    # The effect of this action can only be triggered once per second.
    # The healing blossom dissipates when all stacks are expended or the effect expires.
    # Any remaining stacks of Liturgy of the Bell when effect expires will trigger an additional healing effect.
    # Cure Potency: 200 for every remaining stack of Liturgy of the Bell
    # This action does not share a recast timer with any other actions.
    # related: [礼仪之铃](Status2709), 
    id = 25862
    names = ['礼仪之铃(WHM)', 'Liturgy of the Bell(WHM)']
    _orig_names = ['Liturgy of the Bell', '礼仪之铃']
    # remain metas: {'heal_ot': ['200×剩余档数', '400']}


