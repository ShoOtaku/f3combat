from ._base import *


class Status148(Status):
    # 接受别人发动的复活
    # Teetering on the brink of consciousness.
    id = 148
    names = ['Raise', '复活']


class Status76(Status):
    # 物理攻击所造成的伤害提高
    # Physical damage dealt is increased.
    # related: [战逃反应(PLD)](Action20), [战逃反应(CMN)(0)](Action15870), [战逃反应(CMN)(1)](Action26252),
    id = 76
    names = ['战逃反应', 'Fight or Flight']


class Status1191(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [干预(pvp)(PLD)](Action19085), [摆脱(pvp)(WAR)](Action17699), [铁壁(CMN)(0)](Action7531), [铁壁(pvp)(CMN)](Action17672), [铁壁(CMN)(1)](Action26253),
    id = 1191
    names = ['铁壁(0)', 'Rampart(0)']


class Status71(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [干预(pvp)(PLD)](Action19085), [摆脱(pvp)(WAR)](Action17699), [铁壁(CMN)(0)](Action7531), [铁壁(pvp)(CMN)](Action17672), [铁壁(CMN)(1)](Action26253),
    id = 71
    names = ['铁壁(1)', 'Rampart(1)']


class Status1978(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [干预(PLD)](Action7382), [干预(pvp)(PLD)](Action19085), [摆脱(pvp)(WAR)](Action17699), [铁壁(CMN)(0)](Action7531), [铁壁(pvp)(CMN)](Action17672), [铁壁(CMN)(1)](Action26253),
    id = 1978
    names = ['铁壁(2)', 'Rampart(2)']


class Status2176(Status):
    # 不断增强剑压
    # Deep in contemplation.
    # related: [斗气(MNK)](Action3546), [默想(SAM)](Action7497), [天下五剑(pvp)(SAM)](Action8830), [纷乱雪月花(pvp)(SAM)](Action8831), [回返五剑(pvp)(SAM)](Action17742), [回返雪月花(pvp)(SAM)](Action17743), [奥义斩浪(SAM)](Action25781),
    id = 2176
    names = ['剑压(0)', 'Meditation(0)']


class Status1865(Status):
    # 不断增强剑压
    # Deep in contemplation.
    # related: [斗气(MNK)](Action3546), [默想(SAM)](Action7497), [天下五剑(pvp)(SAM)](Action8830), [纷乱雪月花(pvp)(SAM)](Action8831), [回返五剑(pvp)(SAM)](Action17742), [回返雪月花(pvp)(SAM)](Action17743), [奥义斩浪(SAM)](Action25781),
    id = 1865
    names = ['剑压(1)', 'Meditation(1)']


class Status1304(Status):
    # 无法自由移动，受到伤害也不会解除
    # 另外，除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下
    # Unable to move until effect fades. Most attacks cannot reduce your HP to less than 1.
    # related: [死斗(WAR)](Action43), [死斗(pvp)(WAR)](Action8767), [回避跳跃(pvp)(DRG)](Action8803), [营救(pvp)(CMN)](Action17688), [自愈(pvp)(CMN)](Action18928),
    id = 1304
    names = ['死斗(0)', 'Holmgang(0)']


class Status1305(Status):
    # 无法自由移动，受到伤害也不会解除
    # Unable to move until effect fades.
    # related: [死斗(WAR)](Action43), [死斗(pvp)(WAR)](Action8767), [回避跳跃(pvp)(DRG)](Action8803), [营救(pvp)(CMN)](Action17688), [自愈(pvp)(CMN)](Action18928),
    id = 1305
    names = ['死斗(1)', 'Holmgang(1)']


class Status88(Status):
    # 无法自由移动，受到伤害也不会解除
    # Unable to move until effect fades.
    # related: [死斗(WAR)](Action43), [死斗(pvp)(WAR)](Action8767), [回避跳跃(pvp)(DRG)](Action8803), [营救(pvp)(CMN)](Action17688), [自愈(pvp)(CMN)](Action18928),
    id = 88
    names = ['死斗(2)', 'Holmgang(2)']


class Status409(Status):
    # 除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下
    # Most attacks cannot reduce your HP to less than 1.
    # related: [死斗(WAR)](Action43), [死斗(pvp)(WAR)](Action8767), [回避跳跃(pvp)(DRG)](Action8803), [营救(pvp)(CMN)](Action17688), [自愈(pvp)(CMN)](Action18928),
    id = 409
    names = ['死斗(3)', 'Holmgang(3)']


class Status801(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 801
    names = ['中毒(0)', 'Poison(0)']


class Status2089(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 2089
    names = ['中毒(1)', 'Poison(1)']


class Status686(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 686
    names = ['中毒(2)', 'Poison(2)']


class Status559(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 559
    names = ['中毒(3)', 'Poison(3)']


class Status560(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 560
    names = ['中毒(4)', 'Poison(4)']


class Status18(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 18
    names = ['中毒(5)', 'Poison(5)']


class Status275(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 275
    names = ['中毒(6)', 'Poison +1']


class Status2104(Status):
    # 毒素会导致体力逐渐减少
    # Toxins are causing damage over time.
    # related: [毒咬箭(BRD)](Action100), [烈毒咬箭(BRD)](Action7406), [臭气(BLU)](Action11388), [酸咬箭(CMN)](Action17122),
    id = 2104
    names = ['中毒(7)', 'Poison(6)']


class Status2177(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [行吟(BRD)](Action7405), [策动(MCH)](Action16889), [策动(pvp)(MCH)](Action18934), [防守之桑巴(DNC)](Action16012),
    id = 2177
    names = ['策动(0)', 'Tactician(0)']


class Status1826(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [行吟(BRD)](Action7405), [策动(MCH)](Action16889), [防守之桑巴(DNC)](Action16012),
    id = 1826
    names = ['防守之桑巴', 'Shield Samba']


class Status1197(Status):
    # 技力持续恢复
    # Gradually regenerating TP.
    # related: [行吟(BRD)](Action7405), [策动(MCH)](Action16889), [策动(pvp)(MCH)](Action18934), [防守之桑巴(DNC)](Action16012),
    id = 1197
    names = ['策动(1)', 'Tactician(1)']


class Status1934(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [行吟(BRD)](Action7405), [策动(MCH)](Action16889), [防守之桑巴(DNC)](Action16012),
    id = 1934
    names = ['行吟', 'Troubadour']


class Status1951(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [行吟(BRD)](Action7405), [策动(MCH)](Action16889), [策动(pvp)(MCH)](Action18934), [防守之桑巴(DNC)](Action16012),
    id = 1951
    names = ['策动(2)', 'Tactician(2)']


class Status43(Status):
    # 身体很虚弱，力量、灵巧、智力、精神均降低25%
    # Strength, dexterity, intelligence, and mind are reduced by 25%.
    # related: [复活(WHM)](Action125), [生辰(AST)](Action3603), [赤复活(RDM)](Action7523), [天使低语(BLU)](Action18317), [复苏(SGE)](Action24287), [复生(CMN)](Action173), [文理复活(CMN)](Action12996), [失传完全复活(CMN)](Action20730), [义军不死鸟之尾(CMN)](Action20735), [失传卓异(CMN)](Action23919),
    id = 43
    names = ['衰弱', 'Weakness']


class Status150(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [医济(WHM)](Action133), [全大赦(WHM)](Action7433), [医济(CMN)](Action21888),
    id = 150
    names = ['医济', 'Medica II']


class Status168(Status):
    # 抵消一定伤害
    # An aetherial barrier is preventing damage.
    # related: [魔罩(BLM)](Action157), [魔罩(pvp)(CMN)](Action17687),
    id = 168
    names = ['魔罩(0)', 'Manaward(0)']


class Status1989(Status):
    # 抵消一定伤害
    # An aetherial barrier is preventing damage.
    # related: [魔罩(BLM)](Action157), [魔罩(pvp)(CMN)](Action17687),
    id = 1989
    names = ['魔罩(1)', 'Manaward(1)']


class Status1210(Status):
    # 雷属性持续伤害，体力逐渐流失
    # Sustaining lightning damage over time.
    # related: [霹雷(BLM)](Action7420), [霹雷(pvp)(BLM)](Action18936), [霹雷(CMN)](Action21884),
    id = 1210
    names = ['霹雷', 'Thunder IV']


class Status304(Status):
    # 体内的以太流动逐渐活化
    # Aether is gathering in the body.
    # related: [能量吸收(SMN)](Action16508), [能量抽取(SMN)](Action16510), [能量吸收(pvp)(SMN)](Action17777), [三重灾祸(pvp)(SMN)](Action18953), [以太超流(SCH)](Action166), [能量吸收(SCH)](Action167), [野战治疗阵(SCH)](Action188), [生命活性法(SCH)](Action189), [不屈不挠之策(SCH)](Action3583), [转化(SCH)](Action3587), [深谋远虑之策(SCH)](Action7434),
    id = 304
    names = ['以太超流', 'Aetherflow']


class Status417(Status):
    # 物理防御力及魔法防御力增强
    # Defense and magic defense are enhanced.
    # related: [鼓舞激励之策(SCH)](Action185), [士气高扬之策(SCH)](Action186), [护盾(pvp)(CMN)](Action17832),
    id = 417
    names = ['护盾(0)', 'Protect(0)']


class Status2053(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [鼓舞激励之策(SCH)](Action185), [士气高扬之策(SCH)](Action186), [护盾(pvp)(CMN)](Action17832),
    id = 2053
    names = ['护盾(1)', 'Protect(1)']


class Status1415(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [鼓舞激励之策(SCH)](Action185), [士气高扬之策(SCH)](Action186), [护盾(pvp)(CMN)](Action17832),
    id = 1415
    names = ['护盾(2)', 'Protect(2)']


class Status297(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [鼓舞激励之策(SCH)](Action185), [展开战术(SCH)](Action3585), [哥布防御(BLU)](Action18304), [均衡诊断(SGE)](Action24291), [均衡预后(SGE)](Action24292),
    id = 297
    names = ['鼓舞(0)', 'Galvanize(0)']


class Status146(Status):
    # 物理防御力及魔法防御力增强
    # Both physical and magic defense are enhanced.
    # related: [鼓舞激励之策(SCH)](Action185), [士气高扬之策(SCH)](Action186), [护盾(pvp)(CMN)](Action17832),
    id = 146
    names = ['护盾(3)', 'Protect(3)']


class Status1331(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [鼓舞激励之策(SCH)](Action185), [展开战术(SCH)](Action3585), [哥布防御(BLU)](Action18304), [均衡诊断(SGE)](Action24291), [均衡预后(SGE)](Action24292),
    id = 1331
    names = ['鼓舞(1)', 'Galvanize(1)']


class Status147(Status):
    # 物理防御力及魔法防御力增强
    # Both physical and magic defense are enhanced.
    # related: [鼓舞激励之策(SCH)](Action185), [士气高扬之策(SCH)](Action186), [护盾(pvp)(CMN)](Action17832),
    id = 147
    names = ['护盾(4)', 'Protect(4)']


class Status1347(Status):
    # 无法发动技能
    # A stifling magic is preventing the use of any actions.
    # related: [尘卷(pvp)(NIN)](Action18987), [净化(pvp)(CMN)](Action1584), [天降甘霖(pvp)(CMN)](Action3362), [隔离罩(pvp)(CMN)](Action17677), [伤头(pvp)(CMN)](Action17680),
    id = 1347
    names = ['沉默(0)', 'Silence(0)']


class Status1060(Status):
    # 无法咏唱魔法
    # A stifling magic is preventing casts.
    # related: [尘卷(pvp)(NIN)](Action18987), [净化(pvp)(CMN)](Action1584), [天降甘霖(pvp)(CMN)](Action3362), [隔离罩(pvp)(CMN)](Action17677), [伤头(pvp)(CMN)](Action17680),
    id = 1060
    names = ['沉默(1)', 'Silence(1)']


class Status7(Status):
    # 无法咏唱魔法
    # A stifling magic is preventing casts.
    # related: [尘卷(pvp)(NIN)](Action18987), [净化(pvp)(CMN)](Action1584), [天降甘霖(pvp)(CMN)](Action3362), [隔离罩(pvp)(CMN)](Action17677), [伤头(pvp)(CMN)](Action17680),
    id = 7
    names = ['沉默(2)', 'Silence(2)']


class Status836(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [阳星相位(AST)](Action3601), [阳星相位(pvp)(AST)](Action18951), [阳星相位(CMN)](Action21609),
    id = 836
    names = ['阳星相位', 'Aspected Helios']


class Status1297(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [鼓励(RDM)](Action7520), [鼓励(pvp)(RDM)](Action20106), [鼓励(CMN)](Action26225),
    id = 1297
    names = ['鼓励(队伍)', 'Embolden(party)']


class Status1239(Status):
    # 魔法攻击所造成的伤害提高
    # Magic damage dealt is increased.
    # related: [鼓励(RDM)](Action7520), [鼓励(pvp)(RDM)](Action20106), [鼓励(CMN)](Action26225),
    id = 1239
    names = ['鼓励(自己)', 'Embolden(self)']


# class Status2282(Status):
#     # 攻击所造成的伤害提高
#     # Damage dealt is increased.
#     # related: [鼓励(RDM)](Action7520), [鼓励(pvp)(RDM)](Action20106), [鼓励(CMN)](Action26225),
#     id = 2282
#     names = ['鼓励(2)', 'Embolden(2)']


class Status1721(Status):
    # 受到魔法攻击的伤害增加
    # Magic damage taken is increased.
    # related: [惊奇光(BLU)](Action11421), [惊奇光(CMN)(0)](Action20030), [惊奇光(CMN)(1)](Action20031),
    id = 1721
    names = ['惊奇光', 'Peculiar Light']


class Status2529(Status):
    # 被吸引，无法跳跃或发动技能，会朝着特定方向移动
    # Inexorably pulled in one direction. Unable to jump or execute actions.
    # related: [超硬化(BLU)](Action11424), [亲疏自行(CMN)](Action7548), [沉稳咏唱(CMN)](Action7559), [吸引(CMN)(0)](Action10013), [吸引(CMN)(1)](Action10014), [失传坚壁(CMN)](Action20703),
    id = 2529
    names = ['吸引(0)', 'Sucked In(0)']


class Status2486(Status):
    # 被吸引，无法跳跃或发动技能，会朝着特定方向移动
    # Inexorably pulled in one direction. Unable to jump or execute actions.
    # related: [超硬化(BLU)](Action11424), [亲疏自行(CMN)](Action7548), [沉稳咏唱(CMN)](Action7559), [吸引(CMN)(0)](Action10013), [吸引(CMN)(1)](Action10014), [失传坚壁(CMN)](Action20703),
    id = 2486
    names = ['吸引(1)', 'Sucked In(1)']


class Status2609(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [哥布防御(BLU)](Action18304), [均衡预后(SGE)](Action24292), [消化(SGE)](Action24301), [均衡诊断(pvp)(SGE)](Action27825), [均衡预后(pvp)(SGE)](Action27827),
    id = 2609
    names = ['均衡预后(0)', 'Eukrasian Prognosis(0)']


class Status2866(Status):
    # 抵消一定伤害
    # A magicked barrier is nullifying damage.
    # related: [哥布防御(BLU)](Action18304), [均衡预后(SGE)](Action24292), [消化(SGE)](Action24301), [均衡诊断(pvp)(SGE)](Action27825), [均衡预后(pvp)(SGE)](Action27827),
    id = 2866
    names = ['均衡预后(1)', 'Eukrasian Prognosis(1)']


class Status2448(Status):
    # 积攒力量，下一次发动的技能威力上升
    # Storing power. Potency of next action is increased.
    # related: [口笛(BLU)](Action18309), [文理蓄力(CMN)](Action12972), [失传蓄力(CMN)](Action20714),
    id = 2448
    names = ['蓄力(0)', 'Boosted']


class Status1716(Status):
    # 下次发动魔法攻击的威力提高
    # Potency of next offensive spell is increased.
    # related: [口笛(BLU)](Action18309), [文理蓄力(CMN)](Action12972), [失传蓄力(CMN)](Action20714),
    id = 1716
    names = ['蓄力(1)', 'Boost(0)']


class Status1656(Status):
    # 提升下次战技的攻击力
    # Attack power of next weaponskill is increased.
    # related: [口笛(BLU)](Action18309), [文理蓄力(CMN)](Action12972), [失传蓄力(CMN)](Action20714),
    id = 1656
    names = ['蓄力(2)', 'Boost(1)']


class Status203(Status):
    # 提升下次战技的攻击力
    # Attack power on next special technique is increased.
    # related: [口笛(BLU)](Action18309), [文理蓄力(CMN)](Action12972), [失传蓄力(CMN)](Action20714),
    id = 203
    names = ['蓄力(3)', 'Boost(2)']


class Status1834(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [星云(GNB)](Action16148), [星云(CMN)(0)](Action17839), [星云(CMN)(1)](Action27430),
    id = 1834
    names = ['星云', 'Nebula']


class Status2452(Status):
    # 受到时魔法回返的影响，会在时空中留下痕迹
    # 倒计时结束时会陷入眩晕，并强制移动至留有痕迹的位置
    # Aetherially entwined with the temporal manifold. You will be stunned and drawn back to your aetherial trace when this effect expires.
    # related: [返回(CMN)(0)](Action6), [返回(CMN)(1)](Action10061),
    id = 2452
    names = ['回返', 'Return']


class Status194(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [铜墙铁盾(CMN)](Action197),
    id = 194
    names = ['铜墙铁盾', 'Shield Wall']


class Status195(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [坚守要塞(CMN)](Action198),
    id = 195
    names = ['坚守要塞', 'Stronghold']


class Status196(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [终极堡垒(CMN)](Action199),
    id = 196
    names = ['终极堡垒', 'Last Bastion']


class Status655(Status):
    # 受到攻击的伤害减少
    # Damage taken is reduced.
    # related: [圣盾之恩(pvp)(CMN)](Action3359),
    id = 655
    names = ['圣盾之恩', 'Aegis Boon']


class Status1408(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [微型陨石(pvp)(CMN)](Action3361),
    id = 1408
    names = ['微型陨石', 'Cometeor']


class Status345(Status):
    # 攻击所造成的伤害提高，同时自动攻击间隔缩短，战技与魔法的咏唱及复唱时间也会缩短
    # Damage dealt is increased, while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [充电(CMN)(0)](Action4067), [充电(CMN)(1)](Action4917),
    id = 345
    names = ['魔力供给', 'Recharge']


class Status1409(Status):
    # 自身所受的体力恢复效果降低
    # HP recovery is reduced.
    # related: [终端速度(pvp)(CMN)](Action4249),
    id = 1409
    names = ['终端速度', 'Terminal Velocity']


class Status753(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [雪仇(CMN)](Action7535), [雪仇(pvp)(CMN)](Action17866),
    id = 753
    names = ['雪仇剑(0)', 'Reprisal(0)']


class Status1193(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [雪仇(CMN)](Action7535), [雪仇(pvp)(CMN)](Action17866),
    id = 1193
    names = ['雪仇', 'Reprisal(1)']


class Status2101(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [雪仇(CMN)](Action7535), [雪仇(pvp)(CMN)](Action17866),
    id = 2101
    names = ['雪仇剑(1)', 'Reprisal(2)']


class Status84(Status):
    # 物理攻击附带吸收体力的效果
    # Physical attacks generate HP equal to a portion of damage dealt.
    # related: [浴血(CMN)](Action7542), [浴血(pvp)(CMN)](Action17676),
    id = 84
    names = ['浴血(0)', 'Bloodbath(0)']


class Status1982(Status):
    # 物理攻击附带吸收体力的效果
    # Attacks generate HP equal to the amount of physical damage dealt.
    # related: [浴血(CMN)](Action7542), [浴血(pvp)(CMN)](Action17676),
    id = 1982
    names = ['浴血(1)', 'Bloodbath(1)']


class Status1250(Status):
    # 无视自身技能的方向要求
    # All action direction requirements are nullified.
    # related: [真北(CMN)](Action7546),
    id = 1250
    names = ['真北', 'True North']


class Status1984(Status):
    # 受到攻击的伤害减少，并且可以防御下次的眩晕、睡眠、止步、加重、减速、沉默、击退、吸引的效果
    # Damage taken is reduced. Impervious to the next stun, sleep, bind, heavy, silence, knockback, or draw-in effect.
    # related: [亲疏自行(CMN)](Action7548), [亲疏自行(pvp)(CMN)](Action17681),
    id = 1984
    names = ['亲疏自行(0)', "Arm's Length(0)"]


class Status2181(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [亲疏自行(CMN)](Action7548), [亲疏自行(pvp)(CMN)](Action17681),
    id = 2181
    names = ['亲疏自行(1)', "Arm's Length(1)"]


class Status1209(Status):
    # 除特定攻击之外击退与吸引无效
    # 受到攻击时对攻击者附加减速状态
    # Slowing enemies when attacked. Immune to most knockback and draw-in effects.
    # related: [亲疏自行(CMN)](Action7548), [亲疏自行(pvp)(CMN)](Action17681),
    id = 1209
    names = ['亲疏自行(2)', "Arm's Length(2)"]


class Status2172(Status):
    # 受到攻击时对攻击方附加状态，令其发动攻击时造成的伤害降低
    # Weakening enemies when attacked. Damage taken is reduced.
    # related: [亲疏自行(CMN)](Action7548), [亲疏自行(pvp)(CMN)](Action17681),
    id = 2172
    names = ['亲疏自行(3)', "Arm's Length(3)"]


class Status2185(Status):
    # 被为你附加此效果的玩家攻击时所受伤害增加
    # Sustaining increased damage from target who executed Feint.
    # related: [牵制(CMN)](Action7549), [牵制(pvp)(CMN)](Action18954),
    id = 2185
    names = ['牵制(0)', 'Feint(0)']


class Status1195(Status):
    # 物理攻击和魔法攻击所造成的伤害降低
    # Physical and magic damage are reduced.
    # related: [牵制(CMN)](Action7549), [牵制(pvp)(CMN)](Action18954),
    id = 1195
    names = ['牵制(1)', 'Feint(1)']


class Status1985(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [速行(CMN)](Action7557), [速行(pvp)(CMN)](Action17682),
    id = 1985
    names = ['速行(0)', 'Peloton(0)']


class Status1199(Status):
    # 移动速度提高，进入战斗状态后效果消失
    # Movement speed is increased. Effect ends upon entering battle.
    # related: [速行(CMN)](Action7557), [速行(pvp)(CMN)](Action17682),
    id = 1199
    names = ['速行(1)', 'Peloton(1)']


class Status160(Status):
    # 下次魔法咏唱不会被攻击打断
    # Spells cannot be interrupted by taking damage.
    # related: [沉稳咏唱(CMN)](Action7559),
    id = 160
    names = ['沉稳咏唱', 'Surecast']


class Status1203(Status):
    # 物理攻击和魔法攻击所造成的伤害降低
    # Physical and magic damage are reduced.
    # related: [昏乱(CMN)](Action7560), [昏乱(pvp)(CMN)](Action17686),
    id = 1203
    names = ['昏乱(0)', 'Addle(0)']


class Status1988(Status):
    # 攻击所造成的伤害降低
    # Damage dealt is reduced.
    # related: [昏乱(CMN)](Action7560), [昏乱(pvp)(CMN)](Action17686),
    id = 1988
    names = ['昏乱(1)', 'Addle(1)']


class Status1987(Status):
    # 下次咏唱的魔法没有任何咏唱时间
    # The next spell will be cast immediately.
    # related: [即刻咏唱(CMN)](Action7561), [即刻咏唱(pvp)(CMN)](Action17685),
    id = 1987
    names = ['即刻咏唱(0)', 'Swiftcast(0)']


class Status167(Status):
    # 下次咏唱魔法不需要咏唱时间
    # Next spell will require no time to cast.
    # related: [即刻咏唱(CMN)](Action7561), [即刻咏唱(pvp)(CMN)](Action17685),
    id = 167
    names = ['即刻咏唱', 'Swiftcast']


class Status1325(Status):
    # 下次咏唱魔法不需要咏唱时间
    # Next spell will require no time to cast.
    # related: [即刻咏唱(CMN)](Action7561), [即刻咏唱(pvp)(CMN)](Action17685),
    id = 1325
    names = ['即刻咏唱(2)', 'Swiftcast(2)']


class Status1204(Status):
    # 魔力持续恢复
    # Restoring MP over time.
    # related: [醒梦(CMN)](Action7562),
    id = 1204
    names = ['醒梦', 'Lucid Dreaming']


class Status789(Status):
    # 抑制仇恨上升
    # Enmity generation is reduced.
    # related: [烟雾弹(CMN)](Action7816),
    id = 789
    names = ['烟雾弹', 'Smoke Screen']


class Status1290(Status):
    # 燃烧沐浴到的吉祥天女的以太
    # 受到特定攻击时所受伤害减轻，或转变为治疗魔法效果
    # Damage taken by certain attacks is reduced or converted in to HP.
    # related: [元气(CMN)(0)](Action8517), [元气(CMN)(1)](Action9345),
    id = 1290
    names = ['元气', 'Vril']


class Status2401(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2401
    names = ['火伤(0)', 'Burns(0)']


class Status2082(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2082
    names = ['火伤(1)', 'Burns(1)']


class Status2945(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2945
    names = ['火伤(2)', 'Burns(2)']


class Status2916(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2916
    names = ['火伤(3)', 'Burns(3)']


class Status1577(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 1577
    names = ['火伤(4)', 'Burns(4)']


class Status267(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 267
    names = ['火伤(5)', 'Burns(5)']


class Status619(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 619
    names = ['火伤(6)', 'Burns(6)']


class Status530(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 530
    names = ['火伤(7)', 'Burns(7)']


class Status2194(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2194
    names = ['火伤(8)', 'Burns(8)']


class Status503(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 503
    names = ['火伤(9)', 'Burns(9)']


class Status2199(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 2199
    names = ['火伤(10)', 'Burns(10)']


class Status250(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 250
    names = ['火伤(11)', 'Burns(11)']


class Status1787(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 1787
    names = ['火伤(12)', 'Burns(12)']


class Status284(Status):
    # 火属性持续伤害，体力逐渐流失
    # Sustaining fire damage over time.
    # related: [大火炎放射(pvp)(CMN)](Action9978),
    id = 284
    names = ['火伤(13)', 'Burns(13)']


class Status1470(Status):
    # 持有红色颜料的状态
    # Carrying a pot of red paint.
    # related: [红色陆行鸟之笔(CMN)](Action10262),
    id = 1470
    names = ['红色的颜料', 'Red Paint']


class Status1467(Status):
    # 持有黄色颜料的状态
    # Carrying a pot of yellow paint.
    # related: [黄色陆行鸟之笔(CMN)](Action10263),
    id = 1467
    names = ['黄色的颜料', 'Yellow Paint']


class Status1469(Status):
    # 持有黑色颜料的状态
    # Carrying a pot of black paint.
    # related: [黑色陆行鸟之笔(CMN)(0)](Action10264), [黑色陆行鸟之笔(CMN)(1)](Action20304),
    id = 1469
    names = ['黑色的颜料', 'Black Paint']


class Status1468(Status):
    # 持有蓝色颜料的状态
    # Carrying a pot of light blue paint.
    # related: [蓝色陆行鸟之笔(CMN)](Action10265),
    id = 1468
    names = ['蓝色的颜料', 'Blue Paint']


class Status1494(Status):
    # 观看公演的状态
    # Participating in a live performance.
    # related: [离场(CMN)](Action11063),
    id = 1494
    names = ['公演观众', 'Face in the Crowd']


class Status962(Status):
    # 攻击力有所提高
    # ATK is increased.
    # related: [声援(CMN)](Action12578),
    id = 962
    names = ['攻击力提高', 'ATK Up']


class Status1112(Status):
    # 移动的速度有所提高
    # Movement speed is increased.
    # related: [盗贼的记忆(CMN)](Action12967), [盗贼的秘药(CMN)](Action20752), [盗贼的灵药(CMN)](Action20767),
    id = 1112
    names = ['移动速度提高(0)', 'Movement Speed Up(0)']


class Status669(Status):
    # 移动的速度有所提高
    # Movement speed is increased.
    # related: [盗贼的记忆(CMN)](Action12967), [盗贼的秘药(CMN)](Action20752), [盗贼的灵药(CMN)](Action20767),
    id = 669
    names = ['移动速度提高(1)', 'Movement Speed Up(1)']


class Status1641(Status):
    # 体力最大值提高，命中率提高，陷入无法战斗状态时有几率自动复活
    # Maximum HP and accuracy are increased. Chance of automatic revival upon KO.
    # related: [英杰的加护(CMN)](Action12968),
    id = 1641
    names = ['英杰的加护', 'Spirit of the Remembered']


class Status1642(Status):
    # 物理防御力增强
    # Physical defense is increased.
    # related: [文理护盾(CMN)](Action12969),
    id = 1642
    names = ['文理护盾', 'Protect L']


class Status1643(Status):
    # 魔法防御力增强
    # Magic defense is increased.
    # related: [文理魔盾(CMN)](Action12970),
    id = 1643
    names = ['文理魔盾', 'Shell L']


class Status1644(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [文理敏捷(CMN)](Action12975),
    id = 1644
    names = ['文理敏捷', 'Swift L']


class Status1654(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [文理精神镖(CMN)](Action12977),
    id = 1654
    names = ['文理精神镖', 'Spirit Dart L']


class Status1677(Status):
    # 攻击附带吸收体力的效果
    # Attacks generate HP equal to a portion of damage dealt.
    # related: [文理浴血(CMN)](Action12985),
    id = 1677
    names = ['文理浴血', 'Bloodbath L']


class Status1657(Status):
    # 自身吸引的仇恨增加
    # Enmity is increased.
    # related: [文理激怒(CMN)](Action12995),
    id = 1657
    names = ['文理激怒', 'Incense L']


class Status1646(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [文理勇气(CMN)](Action12997),
    id = 1646
    names = ['文理勇气', 'Bravery L']


class Status1649(Status):
    # 自身受到的魔法将被反射给对方
    # Reflecting magic back on its caster.
    # related: [文理反射(CMN)](Action13000),
    id = 1649
    names = ['文理反射', 'Reflect L']


class Status1651(Status):
    # 魔素以太恢复量提高
    # Magia aether regeneration is increased.
    # related: [文理醒神(CMN)](Action13002),
    id = 1651
    names = ['文理醒神', 'Refresh L']


class Status1655(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [文理放逐(CMN)](Action13003),
    id = 1655
    names = ['文理放逐', 'Banish L']


class Status1653(Status):
    # 以体力不断降低为代价提高物理攻击所造成的伤害
    # Physical damage dealt is increasing, while you are sustaining damage over time.
    # related: [文理双刃剑(CMN)](Action13006),
    id = 1653
    names = ['文理双刃剑', 'Double Edge L']


class Status705(Status):
    # 变成了其他形态
    # Corporeal form has been altered.
    # related: [解除变身(CMN)](Action13266),
    id = 705
    names = ['变身(0)', 'Transfiguration(0)']


class Status2727(Status):
    # 变身成了其他形态，无法发动任何技能，不会受到特定敌人的攻击
    # Corporeal form has been altered, inhibiting use of actions while allowing you to go undetected by certain enemies.
    # related: [解除变身(CMN)](Action13266),
    id = 2727
    names = ['变身(1)', 'Transfiguration(1)']


class Status1448(Status):
    # 变成了其他形态
    # Corporeal form has been altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1448
    names = ['变身(2)', 'Transfiguration(2)']


class Status1608(Status):
    # 变成了其他形态
    # Corporeal form has been altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1608
    names = ['变身(3)', 'Transfiguration(3)']


class Status1609(Status):
    # 变成了其他形态
    # Corporeal form has been altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1609
    names = ['变身(4)', 'Transfiguration(4)']


class Status1423(Status):
    # 变成了其他形态，失去了自我
    # Spiritual and corporeal forms are drastically altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1423
    names = ['变身(5)', 'Transfiguration(5)']


class Status1459(Status):
    # 变成了其他形态，失去了自我
    # Spiritual and corporeal forms are drastically altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1459
    names = ['变身(6)', 'Transfiguration(6)']


class Status2548(Status):
    # 变成了其他形态
    # Corporeal form has been altered.
    # related: [解除变身(CMN)](Action13266),
    id = 2548
    names = ['变身(7)', 'Transfiguration(7)']


class Status565(Status):
    # 变身成了其他形态，无法发动任何技能
    # Corporeal form has been altered, inhibiting use of actions.
    # related: [解除变身(CMN)](Action13266),
    id = 565
    names = ['变身(8)', 'Transfiguration(8)']


class Status1433(Status):
    # 变成了其他形态
    # Corporeal form is altered.
    # related: [解除变身(CMN)](Action13266),
    id = 1433
    names = ['变身(9)', 'Transfiguration(9)']


class Status1735(Status):
    # 利用圣盾进行防御。受到特定技能攻击的伤害减少
    # Protected by an ethereal shield. Damage taken from certain attacks is reduced.
    # related: [圣盾防御(CMN)](Action14415),
    id = 1735
    names = ['圣盾防御', 'Heavenly Shield']


class Status1743(Status):
    # 倒计时为0时会陷入无法战斗状态
    # Certain death when counter reaches zero.
    # related: [文理献祭(CMN)](Action14481), [失传献祭(CMN)](Action22345),
    id = 1743
    names = ['献祭', 'Sacrifice']


class Status1779(Status):
    # 体力逐渐减少
    # Fine cuts are causing damage over time.
    # related: [紫阳花(CMN)](Action14841),
    id = 1779
    names = ['紫阳花', 'Ajisai']


class Status1906(Status):
    # 绞锁自身命脉，完全切断气息。对自身附加“命脉负荷”状态
    # Having severely restricted the flow of life-sustaining aether, your presence is concealed but you are subject to the effect of Fading Fast.
    # related: [完美隐形(CMN)](Action16438),
    id = 1906
    names = ['完美隐形', 'Perfect Deception']


class Status1859(Status):
    # 消除气息的秘技给命脉带来了负荷，不解除会陷入无法战斗状态
    # Reduction of life-sustaining aether by concealment techniques is placing strain on the body. Failure to remove this effect will result in KO.
    # related: [完美隐形(CMN)](Action16438), [绝脉隐形(CMN)](Action17291),
    id = 1859
    names = ['命脉负荷', 'Fading Fast']


class Status2073(Status):
    # 身中剧毒，体力会逐渐减少
    # Toxins are causing damage over time.
    # related: [酸咬箭(CMN)](Action17122),
    id = 2073
    names = ['酸咬箭', 'Acidic Bite']


class Status1956(Status):
    # 暂时绞锁自身命脉，完全切断气息。对自身附加“命脉负荷”和“生命活动停滞”状态
    # Having severed the flow of life-sustaining aether, your presence is completely concealed but you are subject to the effects of Fading Fast and Vital Sign.
    # related: [绝脉隐形(CMN)](Action17291),
    id = 1956
    names = ['绝脉隐形', 'Souldeep Invisibility']


class Status1860(Status):
    # 命脉断绝对生命活动造成了巨大的负面影响，移动速度大幅降低
    # Severing the flow of life-sustaining aether in order to avoid detection has damaged the body's vital functions. Movement speed is severely decreased.
    # related: [绝脉隐形(CMN)](Action17291),
    id = 1860
    names = ['生命活动停滞', 'Vital Sign']


class Status1977(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [全力挥打(pvp)(CMN)](Action17671),
    id = 1977
    names = ['全力挥打', 'Full Swing']


class Status1983(Status):
    # 不受眩晕、睡眠、止步、加重、沉默、击退、吸引的效果影响
    # All Stun, Sleep, Bind, Heavy, Silence, knockback, and draw-in effects are nullified.
    # related: [隔离罩(pvp)(CMN)](Action17677),
    id = 1983
    names = ['隔离罩', 'Fetter Ward']


class Status519(Status):
    # 所有物理攻击都会反弹到发动者身上
    # All physical attacks are reflected back at the dealer.
    # related: [亲疏自行(pvp)(CMN)](Action17681),
    id = 519
    names = ['反击', 'Counter']


class Status1986(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [幻影弹(pvp)(CMN)](Action17684),
    id = 1986
    names = ['幻影弹', 'Phantom Dart']


class Status1990(Status):
    # 受到的伤害大幅降低的同时无法行动
    # Damage taken is significantly reduced. Unable to act.
    # related: [平衡(pvp)(CMN)](Action17689),
    id = 1990
    names = ['平衡', 'Attunement']


class Status2068(Status):
    # 攻击所造成的伤害和命中力提高
    # Accuracy and damage dealt are increased.
    # related: [折服(CMN)](Action17901),
    id = 2068
    names = ['折服', 'Smackdown']


class Status1342(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [疾跑(pvp)(CMN)](Action18942),
    id = 1342
    names = ['疾跑', 'Bolt']


class Status2186(Status):
    # 下次发动战技造成的伤害提高
    # Next weaponskill will deal increased damage.
    # related: [集中(pvp)(CMN)](Action18955),
    id = 2186
    names = ['集中(pvp)', 'Concentrate(pvp)']


class Status396(Status):
    # 免受1次异常状态效果
    # Next enfeeblement received is nullified.
    # related: [集中(pvp)(CMN)](Action18955),
    id = 396
    names = ['集中(1)', 'Concentration']


class Status2187(Status):
    # 战技与魔法的咏唱及复唱时间延长
    # Weaponskill and spell cast time and recast time are increased.
    # related: [以太爆发(pvp)(CMN)](Action18956),
    id = 2187
    names = ['以太爆发', 'Aetheric Burst']


class Status2188(Status):
    # 自身发动的体力恢复效果恢复量提高
    # Potency of all HP restoration actions is increased.
    # related: [慈爱(pvp)(CMN)](Action18957),
    id = 2188
    names = ['慈爱(0)', 'Largesse(0)']


class Status1207(Status):
    # 发动治疗魔法的治疗量提高
    # HP restoration via healing magic is increased.
    # related: [慈爱(pvp)(CMN)](Action18957),
    id = 1207
    names = ['慈爱(1)', 'Largesse(1)']


class Status2184(Status):
    # 受到攻击时会对攻击者造成反击伤害
    # Delivering counter damage every time an attack is suffered.
    # related: [还击(pvp)(CMN)](Action18990),
    id = 2184
    names = ['还击', 'Retaliation']


class Status2265(Status):
    # 调整好姿势，准备抵御冲击
    # Unbowed even by relentless onslaught.
    # related: [抵御冲击(CMN)](Action19994),
    id = 2265
    names = ['抵御冲击', 'Standing Firm']


class Status401(Status):
    # 被抓住，无法行动，体力逐渐减少
    # Held in a vicelike grip and cannot act. Taking damage over time.
    # related: [抓捕(CMN)](Action19997),
    id = 401
    names = ['抓捕(0)', 'Seized(0)']


class Status961(Status):
    # 被抓住，无法行动，体力逐渐减少
    # Held in a vicelike grip and cannot act. Taking damage over time.
    # related: [抓捕(CMN)](Action19997),
    id = 961
    names = ['抓捕(1)', 'Seized(1)']


class Status609(Status):
    # 被抓住，无法行动，体力逐渐减少
    # Held in a vicelike grip and cannot act. Taking damage over time.
    # related: [抓捕(CMN)](Action19997),
    id = 609
    names = ['抓捕(2)', 'Seized(2)']


class Status1287(Status):
    # 被抓住，无法行动，体力逐渐减少
    # Held in a vicelike grip and cannot act. Taking damage over time.
    # related: [抓捕(CMN)](Action19997),
    id = 1287
    names = ['抓捕(3)', 'Seized(3)']


class Status2340(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [失传强放逐(CMN)](Action20702),
    id = 2340
    names = ['失传强放逐', 'Lost Banish']


class Status2345(Status):
    # 令自身所受到的伤害减少，同时除特定攻击之外其他所有击退与吸引无效
    # Damage taken is reduced and immune to most knockback and draw-in effects.
    # related: [失传坚壁(CMN)](Action20703),
    id = 2345
    names = ['失传坚壁', 'Lost Manawall']


class Status2338(Status):
    # 自身发动的所有攻击均视为魔法攻击
    # All attacks deal magic damage.
    # related: [失传铸魔(CMN)](Action20706), [失传钢刺(CMN)](Action20707),
    id = 2338
    names = ['失传铸魔', 'Lost Spellforge']


class Status2339(Status):
    # 自身发动的所有攻击均视为物理攻击
    # All attacks deal physical damage.
    # related: [失传铸魔(CMN)](Action20706), [失传钢刺(CMN)](Action20707),
    id = 2339
    names = ['失传钢刺', 'Lost Steelsting']


class Status2322(Status):
    # 移动速度提高，回避率提高，中毒耐性提高
    # Evasion, movement speed, and poison resistance are increased.
    # related: [失传敏捷(CMN)](Action20708), [义军恢复药箱(CMN)](Action20737), [义军以太药箱(CMN)](Action20738), [失传推进(CMN)](Action23918), [失传痊愈(CMN)](Action23920),
    id = 2322
    names = ['盗贼的药', 'Spirit of the Breathtaker']


class Status2319(Status):
    # 以最大体力值降低为代价提高回避率
    # Evasion is increased while maximum HP is reduced.
    # related: [失传敏捷(CMN)](Action20708), [失传连锁咏唱(CMN)](Action23913), [失传推进(CMN)](Action23918),
    id = 2319
    names = ['斥候的药', 'Spirit of the Watcher']


class Status1645(Status):
    # 缩短下次能力类技能的复唱时间
    # Recast time of next ability is reduced.
    # related: [失传敏捷(CMN)](Action20708), [失传推进(CMN)](Action23918),
    id = 1645
    names = ['高速复唱', 'Rapid Recast']


class Status2335(Status):
    # 移动速度提高
    # Movement speed is increased.
    # related: [失传敏捷(CMN)](Action20708), [失传推进(CMN)](Action23918),
    id = 2335
    names = ['失传敏捷', 'Lost Swift']


class Status2333(Status):
    # 减轻所受到的物理伤害
    # Physical damage taken is reduced.
    # related: [失传护盾(CMN)](Action20709),
    id = 2333
    names = ['失传护盾', 'Lost Protect']


class Status2334(Status):
    # 减轻所受到的魔法伤害
    # Magic damage taken is reduced.
    # related: [失传魔盾(CMN)](Action20710),
    id = 2334
    names = ['失传魔盾', 'Lost Shell']


class Status2337(Status):
    # 自身受到的魔法将被反射给对方
    # Reflecting magic back on its caster.
    # related: [失传反射(CMN)](Action20711), [光之幕帘(CMN)](Action23911),
    id = 2337
    names = ['失传反射', 'Lost Reflect']


class Status2316(Status):
    # 体力最大值提高，防御力增强
    # Maximum HP and defense are increased.
    # related: [失传反射(CMN)](Action20711),
    id = 2316
    names = ['守护者的药', 'Spirit of the Guardian']


class Status2341(Status):
    # 攻击所造成的伤害提高
    # Damage dealt is increased.
    # related: [失传勇气(CMN)](Action20713),
    id = 2341
    names = ['失传勇气', 'Lost Bravery']


class Status1648(Status):
    # 受到魔法攻击的伤害减少
    # Magic damage taken is reduced.
    # related: [失传魔泉(CMN)](Action20715),
    id = 1648
    names = ['魔法盾', 'Spell Shield']


class Status2314(Status):
    # 体力最大值提高，防御力增强
    # Maximum HP and defense are increased.
    # related: [失传魔泉(CMN)](Action20715),
    id = 2314
    names = ['魔战士的药', 'Spirit of the Veteran']


class Status2332(Status):
    # 以一定时间内持续消耗魔力为代价提高攻击所造成的伤害
    # Increasing damage dealt while draining own MP.
    # related: [失传魔泉(CMN)](Action20715),
    id = 2332
    names = ['失传魔泉', 'Lost Font of Magic']


class Status2321(Status):
    # 以受到攻击的伤害增加、最大体力值降低为代价提高攻击所造成的伤害
    # Damage dealt and taken is increased while maximum HP is reduced.
    # related: [失传力泉(CMN)](Action20717),
    id = 2321
    names = ['狂战士的药', 'Spirit of the Irregular']


class Status2346(Status):
    # 攻击所造成的伤害提高，暴击发动率提高
    # Damage dealt and critical hit rate are increased.
    # related: [失传力泉(CMN)](Action20717), [失传暗杀(CMN)](Action23914),
    id = 2346
    names = ['失传力泉', 'Lost Font of Power']


class Status2315(Status):
    # 体力最大值提高，防御力增强
    # Maximum HP and defense are increased.
    # related: [失传力泉(CMN)](Action20717),
    id = 2315
    names = ['重骑兵的药', 'Spirit of the Platebearer']


class Status1647(Status):
    # 受到物理攻击的伤害减少
    # Physical damage taken is reduced.
    # related: [失传力泉(CMN)](Action20717),
    id = 1647
    names = ['物理盾', 'Solid Shield']


class Status2317(Status):
    # 魔力最大值提高，自身发动的体力恢复效果恢复量提高，攻击所造成的伤害提高
    # Maximum MP, damage dealt, and potency of all HP restoration actions are increased.
    # related: [失传即死(CMN)](Action20719), [失传连锁咏唱(CMN)](Action23913),
    id = 2317
    names = ['祭司的药', 'Spirit of the Ordained']


class Status2326(Status):
    # 以自身受到除特定技能之外的体力恢复效果恢复量降低为代价提高攻击所造成的伤害
    # HP recovered via most healing actions is nullified, but damage dealt is increased.
    # related: [背水境地(CMN)](Action20720),
    id = 2326
    names = ['背水境地', 'Banner of Noble Ends']


class Status2327(Status):
    # 以体力逐渐流失为代价提高攻击所造成的伤害
    # Sustaining damage over time in exchange for dealing increased damage.
    # related: [舍身境地(CMN)](Action20721),
    id = 2327
    names = ['舍身境地', 'Banner of Honored Sacrifice']


class Status2328(Status):
    # 受到攻击的伤害增加，每次受到攻击会增加档数，档数最大时变为铁壁境地
    # 铁壁境地的效果：受到攻击的伤害减少
    # Damage taken is increased, but your conviction is strengthened with each attack received. At maximum stacks, take up the Banner of Unyielding Defense.
    # Banner of Unyielding Defense Effect: Damage taken is reduced.
    # related: [忍耐境地(CMN)](Action20722),
    id = 2328
    names = ['忍耐境地', 'Banner of Tireless Conviction']


class Status2329(Status):
    # 攻击所造成的伤害减少，每次受到攻击会增加档数，档数最大时变为铁壁境地
    # 铁壁境地的效果：受到攻击的伤害减少
    # Damage dealt is reduced, but your resolve is strengthened with each attack received. At maximum stacks, take up the Banner of Unyielding Defense.
    # Banner of Unyielding Defense Effect: Damage taken is reduced.
    # related: [坚守境地(CMN)](Action20723),
    id = 2329
    names = ['坚守境地', 'Banner of Firm Resolve']


class Status2330(Status):
    # 随时间经过增加档数，档数最大时变为无我境地，任何行动都会解除冥想境地
    # 无我境地的效果：减少魔力消耗，同时提高自身发动的体力恢复效果恢复量
    # You take a moment to still your mind, gaining clarity as time passes. At maximum stacks, take up the Banner of Limitless Grace.
    # Banner of Limitless Grace Effect: Potency of HP restoration actions is increased while MP cost is reduced.
    # related: [冥想境地(CMN)](Action20724),
    id = 2330
    names = ['冥想境地', 'Banner of Solemn Clarity']


class Status2331(Status):
    # 受到攻击的伤害增加，每次回避攻击会增加档数，档数最大时变为神速境地
    # 神速境地的效果：直击发动率提高，同时自动攻击间隔缩短，战技与魔法的咏唱及复唱时间也会缩短
    # Damage taken is increased, but your senses sharpen with each attack evaded. At maximum stacks, take up the Banner of Transcendent Finesse.
    # Banner of Transcendent Finesse Effect: Critical hit rate is increased while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [敏锐境地(CMN)](Action20725),
    id = 2331
    names = ['敏锐境地', 'Banner of Honed Acuity']


class Status2313(Status):
    # 自身发动的体力恢复效果恢复量提高
    # Potency of all HP restoration actions is increased.
    # related: [失传救疗(CMN)](Action20727), [失传圣疗(CMN)](Action20729),
    id = 2313
    names = ['治愈者的药', 'Spirit of the Savior']


class Status2356(Status):
    # 自身吸引的仇恨增加，同时受到攻击的伤害减少
    # Enmity is increased and damage taken is reduced.
    # related: [失传激怒(CMN)](Action20731),
    id = 2356
    names = ['失传激怒', 'Lost Incense']


class Status1056(Status):
    # 自身前方的陆行鸟使用道具或能力时，发动与之相同的效果
    # Repeating any ability or item used by forerunning chocobos.
    # related: [模仿(CMN)](Action20733),
    id = 1056
    names = ['模仿(0)', 'Mimic']


class Status2450(Status):
    # 模仿对手的行动，对于物理攻击将进行物理反击，对于魔法攻击将进行魔法反击
    # Mimicking the actions of opponents. Physical attacks are answered with physical attacks, magical attacks with magical attacks.
    # related: [模仿(CMN)](Action20733),
    id = 2450
    names = ['模仿(1)', 'Mimicry']


class Status2342(Status):
    # 体力低于50%时自动恢复，发动恢复效果后有50%的几率解除该状态，盗贼的药状态中解除几率变为10%
    # Recover HP automatically when HP falls below 50%. When triggered, there is a 50% chance the effect will end. While enlivened by the Spirit of the Breathtaker, this chance is reduced to 10%.
    # related: [义军恢复药箱(CMN)](Action20737), [失传痊愈(CMN)](Action23920),
    id = 2342
    names = ['自动恢复药', 'Auto-potion']


class Status2343(Status):
    # 魔力低于20%时自动恢复，发动恢复效果后有50%的几率解除该状态，盗贼的药状态中解除几率变为10%
    # Recover MP automatically when MP falls below 20%. When triggered, there is a 50% chance the effect will end. While enlivened by the Spirit of the Breathtaker, this chance is reduced to 10%.
    # related: [义军以太药箱(CMN)](Action20738), [失传痊愈(CMN)](Action23920),
    id = 2343
    names = ['自动以太药', 'Auto-ether']


class Status2640(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [不动宫(CMN)](Action21611),
    id = 2640
    names = ['不动宫(0)', 'Fixed Sign(0)']


class Status2641(Status):
    # 体力会随时间逐渐恢复
    # Regenerating HP over time.
    # related: [不动宫(CMN)](Action21611),
    id = 2641
    names = ['不动宫(1)', 'Fixed Sign(1)']


class Status2639(Status):
    # 产生减轻伤害的防护区域
    # An area of land has been granted protection, reducing damage taken for all who enter.
    # related: [不动宫(CMN)](Action21611),
    id = 2639
    names = ['不动宫(2)', 'Fixed Sign(2)']


class Status1(Status):
    # 手足被石化，无法做出任何行动
    # Stone-like rigidity is preventing the execution of actions.
    # related: [石化(CMN)](Action21921),
    id = 1
    names = ['石化(0)', 'Petrification(0)']


class Status610(Status):
    # 手足被石化，无法做出任何行动
    # Stone-like rigidity is preventing the execution of actions.
    # related: [石化(CMN)](Action21921),
    id = 610
    names = ['石化(1)', 'Petrification(1)']


class Status1511(Status):
    # 手足被石化，无法做出任何行动
    # Stone-like rigidity is preventing the execution of actions.
    # related: [石化(CMN)](Action21921),
    id = 1511
    names = ['石化(2)', 'Petrification(2)']


class Status2573(Status):
    # 行动遭到严重妨碍的状态
    # Activity is severely impeded.
    # related: [石化(CMN)](Action21921),
    id = 2573
    names = ['石化(3)', 'Break']


class Status2440(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [失传耀星(CMN)](Action22352),
    id = 2440
    names = ['失传耀星', 'Lost Flare Star']


class Status2441(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [失传破甲(CMN)](Action22353),
    id = 2441
    names = ['失传破甲', 'Lost Rend Armor']


class Status145(Status):
    # 魔法攻击所造成的伤害提高
    # Magic damage dealt is increased.
    # related: [失传炽天强袭(CMN)](Action22354),
    id = 145
    names = ['战姿(0)', 'Cleric Stance(0)']


class Status2484(Status):
    # 以自身发动的体力恢复效果恢复量降低为代价提高攻击所造成的伤害
    # Healing potency is reduced while damage dealt is increased.
    # related: [失传炽天强袭(CMN)](Action22354),
    id = 2484
    names = ['战姿(1)', 'Cleric Stance(1)']


class Status2443(Status):
    # 减轻所受到的伤害
    # Damage taken is reduced.
    # related: [失传以太之盾(CMN)](Action22355),
    id = 2443
    names = ['失传以太之盾', 'Lost Aethershield']


class Status2444(Status):
    # 攻击所造成的伤害提高，暴击发动率提高，自动攻击间隔缩短，同时战技与魔法的咏唱及复唱时间也会缩短
    # Critical hit rate and damage dealt are increased, while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
    # related: [失传速度之星(CMN)](Action22356),
    id = 2444
    names = ['失传速度之星', 'Lost Dervish']


class Status2558(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [失传磁暴(CMN)](Action23909),
    id = 2558
    names = ['失传磁暴', 'Lost Burst']


class Status2559(Status):
    # 受到攻击的伤害增加
    # Damage taken is increased.
    # related: [失传暴怒(CMN)](Action23910),
    id = 2559
    names = ['失传暴怒', 'Lost Rampage']


class Status2355(Status):
    # 陷入无法战斗状态时有几率自动复活
    # Chance of automatic revival upon KO.
    # related: [失传重生(CMN)](Action23912),
    id = 2355
    names = ['重生', 'Reraise']


class Status2560(Status):
    # 咏唱魔法不需要咏唱时间
    # Spells require no time to cast.
    # related: [失传连锁咏唱(CMN)](Action23913),
    id = 2560
    names = ['失传连锁咏唱', 'Lost Chainspell']


class Status1652(Status):
    # 以自身发动技能时消耗的魔力增加为代价提高魔法类技能攻击时造成的伤害
    # Damage dealt by spells and MP cost of spells is increased.
    # related: [失传连锁咏唱(CMN)](Action23913),
    id = 1652
    names = ['魔法爆发', 'Magic Burst']


class Status2324(Status):
    # 体力最大值提高，防御力增强，附带吸收体力的效果
    # Maximum HP and defense are increased, and attacks generate HP equal to a portion of damage dealt.
    # related: [失传暗杀(CMN)](Action23914),
    id = 2324
    names = ['狼人的药', 'Spirit of the Beast']


class Status2561(Status):
    # 减轻所受到的物理伤害
    # Physical damage taken is reduced.
    # related: [失传护盾II(CMN)](Action23915),
    id = 2561
    names = ['失传护盾II', 'Lost Protect II']


class Status2562(Status):
    # 减轻所受到的魔法伤害
    # Magic damage taken is reduced.
    # related: [失传魔盾II(CMN)](Action23916),
    id = 2562
    names = ['失传魔盾II', 'Lost Shell II']


class Status2563(Status):
    # 体力最大值提高
    # Maximum HP is increased.
    # related: [失传生机(CMN)](Action23917),
    id = 2563
    names = ['失传生机', 'Lost Bubble']


class Status2738(Status):
    # 濒临死亡。凭自身意志保持意识清醒，但无法站起来
    # Gravely wounded and unable to stand, but still clinging to consciousness.
    # related: [失传卓异(CMN)](Action23919),
    id = 2738
    names = ['濒死(0)', "At Death's Door"]


class Status2564(Status):
    # 除特定攻击之外其他所有攻击均无效化，攻击目标时造成的伤害提高
    # Impervious to most attacks. Damage dealt is increased.
    # related: [失传卓异(CMN)](Action23919),
    id = 2564
    names = ['失传卓异', 'Lost Excellence']


class Status2565(Status):
    # 攻击所造成的伤害提高，受到攻击的伤害减少
    # Damage dealt is increased, while damage taken is decreased.
    # related: [失传卓异(CMN)](Action23919),
    id = 2565
    names = ['英杰', 'Memorable']


class Status44(Status):
    # 身体很虚弱，力量、灵巧、智力、精神均降低50%
    # Strength, dexterity, intelligence, and mind are reduced by 50%.
    # related: [失传卓异(CMN)](Action23919),
    id = 44
    names = ['濒死(1)', 'Brink of Death']


class Status2566(Status):
    # 攻击所造成的伤害提高，受到攻击的伤害减少
    # Damage dealt is increased, while damage taken is decreased.
    # related: [失传血怒(CMN)](Action23921),
    id = 2566
    names = ['失传血怒', 'Lost Blood Rage']


class Status2567(Status):
    # 攻击所造成的伤害提高，体力和魔力会随时间逐渐恢复，缩短下次能力类技能的复唱时间
    # Gradually recovering HP and MP. Damage dealt is increased and ability recast time is reduced.
    # related: [失传血怒(CMN)](Action23921),
    id = 2567
    names = ['血怒觉醒', 'Blood Rush']


class Status3(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 3
    names = ['睡眠(0)', 'Sleep(0)']


class Status1348(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 1348
    names = ['睡眠(1)', 'Sleep(1)']


class Status1510(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 1510
    names = ['睡眠(2)', 'Sleep(2)']


class Status2983(Status):
    #
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 2983
    names = ['(1)', 'Sleep(3)']


class Status1363(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 1363
    names = ['睡眠(3)', 'Sleep(4)']


class Status1947(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 1947
    names = ['睡眠(4)', 'Sleep(5)']


class Status1596(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 1596
    names = ['睡眠(5)', 'Sleep(6)']


class Status926(Status):
    # 陷入沉睡，无法做出任何行动
    # Overwhelming drowsiness is preventing the execution of actions.
    # related: [催眠(CMN)](Action25880),
    id = 926
    names = ['睡眠(6)', 'Sleep(7)']


class Status2957(Status):
    # 完全切断自身的气息，移动速度提高
    # Unable to be detected by sight, and movement speed is increased.
    # related: [疾隐(CMN)](Action27432), [终招(CMN)](Action27433),
    id = 2957
    names = ['疾隐', 'Swift Deception']


class Status2650(Status):
    # 体力逐渐减少
    # Sustaining damage over time.
    # related: [莱韦耶勒尔注药III(CMN)](Action28439),
    id = 2650
    names = ['莱韦耶勒尔注药III', 'Leveilleur Dosis III']


class Action6(Action):
    # 传送到上一次所记录的返回点。
    # Instantly return to your current home point.
    # related: [回返](Status2452),
    id = 6
    names = ['返回(CMN)(0)', 'Return(CMN)(0)']
    _orig_names = ['Return', '返回']


class Action173(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43),
    id = 173
    names = ['复生(CMN)', 'Resurrection(CMN)']
    _orig_names = ['Resurrection', '复生']


class Action197(Action):
    # 一定时间内，小队全员受到的伤害减轻20%
    # 持续时间：10秒
    # Reduces damage taken by all party members by 20%.
    # Duration: 10s
    # related: [铜墙铁盾](Status194),
    id = 197
    names = ['铜墙铁盾(CMN)', 'Shield Wall(CMN)']
    _orig_names = ['Shield Wall', '铜墙铁盾']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action198(Action):
    # 一定时间内，小队全员受到的伤害减轻40%
    # 持续时间：15秒
    # Reduces damage taken by all party members by 40%.
    # Duration: 15s
    # related: [坚守要塞](Status195),
    id = 198
    names = ['坚守要塞(CMN)', 'Stronghold(CMN)']
    _orig_names = ['Stronghold', '坚守要塞']
    # remain metas: {'taken_dmg_reduce': '40%'}


class Action199(Action):
    # 一定时间内，小队全员受到的伤害减轻80%
    # 持续时间：12秒
    # Reduces damage taken by all party members by 80%.
    # Duration: 12s
    # related: [终极堡垒](Status196),
    id = 199
    names = ['终极堡垒(CMN)', 'Last Bastion(CMN)']
    _orig_names = ['终极堡垒', 'Last Bastion']
    # remain metas: {'taken_dmg_reduce': '80%'}


class Action200(Action):
    # 对目标发动物理攻击
    # 威力：2400
    # Delivers an attack with a potency of 2,400.
    id = 200
    names = ['Braver(CMN)', '勇猛烈斩(CMN)']
    _orig_names = ['勇猛烈斩', 'Braver']
    damage = 2400


class Action201(Action):
    # 对目标发动物理攻击
    # 威力：5250
    # Delivers an attack with a potency of 5,250.
    id = 201
    names = ['Bladedance(CMN)', '刀光剑舞(CMN)']
    _orig_names = ['刀光剑舞', 'Bladedance']
    damage = 5250


class Action202(Action):
    # 对目标发动物理攻击
    # 威力：9000
    # Delivers an attack with a potency of 9,000.
    id = 202
    names = ['最终天堂(CMN)', 'Final Heaven(CMN)']
    _orig_names = ['Final Heaven', '最终天堂']
    damage = 9000


class Action203(Action):
    # 对指定地点发动范围无属性魔法攻击
    # 威力：1650
    # Deals unaspected damage with a potency of 1,650 to all enemies near point of impact.
    id = 203
    names = ['Skyshard(CMN)', '苍穹破碎(CMN)']
    _orig_names = ['Skyshard', '苍穹破碎']
    damage = 1650


class Action204(Action):
    # 对指定地点发动范围无属性魔法攻击
    # 威力：3600
    # Deals unaspected damage with a potency of 3,600 to all enemies near point of impact.
    id = 204
    names = ['星体风暴(CMN)(0)', 'Starstorm(CMN)(0)']
    _orig_names = ['Starstorm', '星体风暴']
    damage = 3600


class Action205(Action):
    # 对指定地点发动范围无属性魔法攻击
    # 威力：6150
    # Deals unaspected damage with a potency of 6,150 to all enemies near point of impact.
    id = 205
    names = ['陨石流星(CMN)', 'Meteor(CMN)']
    _orig_names = ['陨石流星', 'Meteor']
    damage = 6150


class Action206(Action):
    # 恢复自身及周围队员最大体力的25%
    # Restores 25% of own HP and the HP of all nearby party members.
    id = 206
    names = ['Healing Wind(CMN)', '治愈微风(CMN)']
    _orig_names = ['Healing Wind', '治愈微风']


class Action207(Action):
    # 恢复自身及周围队员最大体力的60%
    # Restores 60% of own HP and the HP of all nearby party members.
    id = 207
    names = ['Breath of the Earth(CMN)', '大地气息(CMN)']
    _orig_names = ['大地气息', 'Breath of the Earth']


class Action208(Action):
    # 恢复自身及周围队员全部体力，无法战斗的队员也会复活
    # Restores 100% of own HP and the HP of all nearby party members, including ones KO'd.
    id = 208
    names = ['Pulse of Life(CMN)', '生命鼓动(CMN)']
    _orig_names = ['Pulse of Life', '生命鼓动']


class Action1128(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 1128
    names = ['魔导加农炮(CMN)(0)', 'Magitek Cannon(CMN)(0)']
    _orig_names = ['Magitek Cannon', '魔导加农炮']


class Action1129(Action):
    # 向自身前方发动直线范围攻击
    # Fires a short-range burst of energy in a straight line before you.
    id = 1129
    names = ['魔导光子炮(CMN)(0)', 'Photon Stream(CMN)(0)']
    _orig_names = ['Photon Stream', '魔导光子炮']


class Action1134(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 1134
    names = ['Cannonfire(CMN)(0)', '炮击(CMN)(0)']
    _orig_names = ['Cannonfire', '炮击']


class Action1437(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 1437
    names = ['Cannonfire(CMN)(1)', '炮击(CMN)(1)']
    _orig_names = ['Cannonfire', '炮击']


class Action1584(Action):
    # 解除自身或一名队员的眩晕、睡眠、止步、加重、沉默状态，同时恢复体力
    # 恢复力：2000
    # 成功解除异常状态时，恢复力变为2倍
    # 即使自身处于异常状态下也可以发动该技能
    # Restores own or target party member's HP while also removing Stun, Sleep, Bind, Heavy, and Silence.
    # Cure Potency: 2,000
    # Cure potency is doubled when a status affliction is removed. Can be used regardless of own status affliction.
    # related: [沉默(0)](Status1347), [沉默(1)](Status1060), [沉默(2)](Status7),
    id = 1584
    names = ['Purify(pvp)(CMN)', '净化(pvp)(CMN)']
    _orig_names = ['净化(pvp)', 'Purify(pvp)']
    heal = 2000


class Action1764(Action):
    # 喷出火属性的猛烈吐息
    # Emits a stream of white-hot flames.
    id = 1764
    names = ['Fiery Breath(CMN)(0)', '烈火吐息(CMN)(0)']
    _orig_names = ['Fiery Breath', '烈火吐息']


class Action1765(Action):
    # 打出声音巨大的喷嚏
    # Discharges a shower of lukewarm spittle onto an unfortunate target.
    id = 1765
    names = ['喷嚏(CMN)(0)', 'Big Sneeze(CMN)']
    _orig_names = ['Big Sneeze', '喷嚏']


class Action2237(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 2237
    names = ['炮击(CMN)(2)', 'Iron Kiss(CMN)(0)']
    _orig_names = ['Iron Kiss', '炮击']


class Action2238(Action):
    # 向指定地点附近开炮射击
    # 追加效果：眩晕
    # 持续时间：1秒
    # Fires a lightning-aspected projectile at the designated area.
    # Additional Effect: Stun
    # Duration: 1s
    id = 2238
    names = ['Spindly Finger(CMN)(0)', '雷弹(CMN)(0)']
    _orig_names = ['Spindly Finger', '雷弹']


class Action2360(Action):
    # 对指定地点施加魔咒
    # Casts a minor spell upon the designated location.
    id = 2360
    names = ['Festal Cant(CMN)', '魔咒(CMN)']
    _orig_names = ['Festal Cant', '魔咒']


class Action2434(Action):
    # 向指定地点附近开炮射击
    # 演出技能，没有任何实际效果
    # Fires an explosive projectile at the designated area.
    # ※Has no effect in battle.
    id = 2434
    names = ['Magitek Cannon(CMN)(1)', '魔导加农炮(CMN)(1)']
    _orig_names = ['Magitek Cannon', '魔导加农炮']


class Action2435(Action):
    # 向自身前方发动直线范围攻击
    # 演出技能，没有任何实际效果
    # Fires a short-range burst of energy in a straight line before you.
    # ※Has no effect in battle.
    id = 2435
    names = ['魔导光子炮(CMN)(1)', 'Photon Stream(CMN)(1)']
    _orig_names = ['Photon Stream', '魔导光子炮']


class Action2436(Action):
    # 喷出火属性的猛烈吐息
    # 演出技能，没有任何实际效果
    # Emits a stream of white-hot flames.
    # ※Has no effect in battle.
    id = 2436
    names = ['Fiery Breath(CMN)(1)', '烈火吐息(CMN)(1)']
    _orig_names = ['Fiery Breath', '烈火吐息']


class Action2437(Action):
    # 打出声音巨大的喷嚏
    # 演出技能，没有任何实际效果
    # Discharges a shower of lukewarm spittle onto an unfortunate target.
    # ※Has no effect in battle.
    id = 2437
    names = ['Sneeze(CMN)', '喷嚏(CMN)(1)']
    _orig_names = ['Sneeze', '喷嚏']


class Action2620(Action):
    # 喷射出冰冷的水流
    # Sprays tepid water over target.
    id = 2620
    names = ['喷水(CMN)(0)', 'Saturate(CMN)(0)']
    _orig_names = ['喷水', 'Saturate']


class Action2630(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 2630
    names = ['Cannonfire(CMN)(2)', '炮击(CMN)(3)']
    _orig_names = ['Cannonfire', '炮击']


class Action3139(Action):
    # 对目标发动物理攻击
    # 特定条件下会打消“湿润”的状态
    # Delivers an impotent attack. In certain cases, may remove the Wet Plate status.
    id = 3139
    names = ['河童拳(CMN)(0)', 'Imp Punch(CMN)(0)']
    _orig_names = ['河童拳', 'Imp Punch']


class Action3359(Action):
    # 一定时间内令自己与周围队员受到的伤害减轻25%
    # 持续时间：10秒
    # 发动条件：奋战槽最大
    # Reduces damage taken by self and nearby party members by 25%.
    # Duration: 10s
    # Can only be executed while the Adrenaline Gauge is full.
    # related: [圣盾之恩](Status655),
    id = 3359
    names = ['圣盾之恩(pvp)(CMN)', 'Aegis Boon(pvp)(CMN)']
    _orig_names = ['圣盾之恩(pvp)', 'Aegis Boon(pvp)']
    # remain metas: {'taken_dmg_reduce': '25%'}


class Action3360(Action):
    # 对目标发动物理攻击
    # 威力：10000
    # 发动条件：奋战槽最大
    # 此技能造成的伤害不受来自玩家的伤害变化效果影响
    # Delivers an attack with a potency of 10,000.
    # Damage dealt is not affected by increased or decreased damage effects applied by players.
    # Can only be executed while the Adrenaline Gauge is full.
    id = 3360
    names = ['Raw Destruction(pvp)(CMN)', '毁灭痛击(pvp)(CMN)']
    _orig_names = ['Raw Destruction(pvp)', '毁灭痛击(pvp)']
    damage = 10000


class Action3361(Action):
    # 对指定地点发动范围魔法攻击
    # 威力：4000
    # 追加效果：目标所受伤害提高25%
    # 持续时间：10秒
    # 发动条件：奋战槽最大
    # 此技能造成的伤害不受来自玩家的伤害变化效果影响
    # Deals magic damage to enemies near point of impact with a potency of 4,000.
    # Additional Effect: Increases target's damage taken by 25%
    # Duration: 10s
    # Damage dealt is not affected by increased or decreased damage effects applied by players.
    # Can only be executed while the Adrenaline Gauge is full.
    # related: [微型陨石](Status1408),
    id = 3361
    names = ['微型陨石(pvp)(CMN)', 'Cometeor(pvp)(CMN)']
    _orig_names = ['微型陨石(pvp)', 'Cometeor(pvp)']
    damage = 4000
    # remain metas: {'taken_dmg_increase': '25%'}


class Action3362(Action):
    # 恢复自身及周围队员最大体力的50%
    # 追加效果：解除目标受到的眩晕、睡眠、止步、加重、沉默状态
    # 发动条件：奋战槽最大
    # Restores 50% of own HP and the HP of all nearby party members.
    # Additional Effect: Removes Stun, Sleep, Bind, Heavy, and Silence
    # Can only be executed while the Adrenaline Gauge is full.
    # related: [沉默(0)](Status1347), [沉默(1)](Status1060), [沉默(2)](Status7),
    id = 3362
    names = ['天降甘霖(pvp)(CMN)', 'Empyrean Rain(pvp)(CMN)']
    _orig_names = ['天降甘霖(pvp)', 'Empyrean Rain(pvp)']


class Action3377(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 3377
    names = ['炮击(CMN)(4)', 'Iron Kiss(CMN)(1)']
    _orig_names = ['Iron Kiss', '炮击']


class Action3378(Action):
    # 向指定地点附近开炮射击
    # 追加效果：眩晕
    # 持续时间：1秒
    # Fires a lightning-aspected projectile at the designated area.
    # Additional Effect: Stun
    # Duration: 1s
    id = 3378
    names = ['雷弹(CMN)(1)', 'Spindly Finger(CMN)(1)']
    _orig_names = ['Spindly Finger', '雷弹']


class Action3379(Action):
    # 以指定地点为中心产生粘着区域
    # 会降低所有范围内目标的移动速度
    # Coats the ground with a viscid sap, slowing the movement speed of any who enter.
    id = 3379
    names = ['Pitch Bomb(CMN)', '粘着弹(CMN)']
    _orig_names = ['粘着弹', 'Pitch Bomb']


class Action3504(Action):
    # 对目标发动远距离物理攻击
    # Delivers a ranged attack.
    id = 3504
    names = ['Quickchant(CMN)', '怒喊(CMN)']
    _orig_names = ['Quickchant', '怒喊']


class Action3506(Action):
    # 向周围发出强烈的电流
    # 演出技能，没有任何实际效果
    # Emits a bright, harmless charge.
    id = 3506
    names = ['低压电流(CMN)', 'Low Voltage(CMN)']
    _orig_names = ['Low Voltage', '低压电流']


class Action4062(Action):
    # 能使敌人加重的特殊弹，对大型兵器无效
    # Fires a pressurized round of ammunition. Has no effect against oversized targets.
    id = 4062
    names = ['重压弹(CMN)(0)', 'Heavydoom(CMN)(0)']
    _orig_names = ['重压弹', 'Heavydoom']


class Action4063(Action):
    # 能使生物感电的特殊弹，对机械兵器无效
    # Fires a hypercharged round of ammunition capable of electrocuting living targets. Has no effect on machina.
    id = 4063
    names = ['Cracklyplume(CMN)(0)', '电压弹(CMN)(0)']
    _orig_names = ['电压弹', 'Cracklyplume']


class Action4064(Action):
    # 能溶解敌人装甲的特殊弹
    # Fires a round of armor-piercing ammunition.
    id = 4064
    names = ['Meltyspume(CMN)(0)', '强酸弹(CMN)(0)']
    _orig_names = ['强酸弹', 'Meltyspume']


class Action4065(Action):
    # 能把敌人吸引到身边的特殊武装
    # Activates electromagnets capable of drawing in a target.
    id = 4065
    names = ['Stickyloom(CMN)(0)', '电磁石(CMN)(0)']
    _orig_names = ['电磁石', 'Stickyloom']


class Action4067(Action):
    # 吸取敌机电力，给自机充电
    # Saps a target of its electrical charge.
    # related: [魔力供给](Status345),
    id = 4067
    names = ['Recharge(CMN)(0)', '充电(CMN)(0)']
    _orig_names = ['充电', 'Recharge']


class Action4249(Action):
    # 向目标所在方向发出直线范围物理攻击
    # 威力：6000
    # 追加效果：目标所受到的恢复效果减少25%
    # 持续时间：10秒
    # 发动条件：奋战槽最大
    # 此技能造成的伤害不受来自玩家的伤害变化效果影响
    # Delivers an attack with a potency of 6,000 to all enemies in a straight line before you.
    # Additional Effect: Reduces target's HP recovered by healing actions by 25%
    # Duration: 10s
    # Damage dealt is not affected by increased or decreased damage effects applied by players.
    # Can only be executed while the Adrenaline Gauge is full.
    # related: [终端速度](Status1409),
    id = 4249
    names = ['Terminal Velocity(pvp)(CMN)', '终端速度(pvp)(CMN)']
    _orig_names = ['Terminal Velocity(pvp)', '终端速度(pvp)']
    damage = 6000


class Action4583(Action):
    # 用巨大的翅膀扇风
    # Commands your griffin to flap its wings.
    id = 4583
    names = ['Buffet(CMN)(0)', '突风(CMN)(0)']
    _orig_names = ['突风', 'Buffet']


class Action4584(Action):
    # 用巨大的翅膀扇风
    # 演出技能，没有任何实际效果
    # Commands your griffin to flap its wings.
    # ※Has no effect in battle.
    id = 4584
    names = ['Buffet(CMN)(1)', '突风(CMN)(1)']
    _orig_names = ['突风', 'Buffet']


class Action4585(Action):
    # 用力踩地面
    # Commands your marid to stomp the earth.
    id = 4585
    names = ['Trample(CMN)(0)', '踩踏(CMN)(0)']
    _orig_names = ['踩踏', 'Trample']


class Action4586(Action):
    # 用力踩地面
    # 演出技能，没有任何实际效果
    # Commands your marid to stomp the earth.
    # ※Has no effect in battle.
    id = 4586
    names = ['Trample(CMN)(1)', '踩踏(CMN)(1)']
    _orig_names = ['踩踏', 'Trample']


class Action4592(Action):
    # 令变身魔法失效的魔咒
    # 演出技能，没有任何实际效果
    # Casts a minor spell to prevent curses of transfiguration.
    # ※Has no effect in battle.
    id = 4592
    names = ['Silencing Cant(CMN)(0)', '清扫魔咒(CMN)(0)']
    _orig_names = ['Silencing Cant', '清扫魔咒']


class Action4800(Action):
    # 自机进行自爆
    # Initiate self-detonation.
    id = 4800
    names = ['Self-detonate(CMN)', '雾散爆发(CMN)']
    _orig_names = ['雾散爆发', 'Self-detonate']


class Action4913(Action):
    # 能使敌人加重的特殊弹，对大型兵器无效
    # Fires a pressurized round of ammunition. Has no effect against oversized targets.
    id = 4913
    names = ['Heavydoom(CMN)(1)', '重压弹(CMN)(1)']
    _orig_names = ['重压弹', 'Heavydoom']


class Action4914(Action):
    # 能使生物感电的特殊弹，对机械兵器无效
    # Fires a hypercharged round of ammunition capable of electrocuting living targets. Has no effect on machina.
    id = 4914
    names = ['电压弹(CMN)(1)', 'Cracklyplume(CMN)(1)']
    _orig_names = ['电压弹', 'Cracklyplume']


class Action4915(Action):
    # 能溶解敌人装甲的特殊弹
    # Fires a round of armor-piercing ammunition.
    id = 4915
    names = ['强酸弹(CMN)(1)', 'Meltyspume(CMN)(1)']
    _orig_names = ['强酸弹', 'Meltyspume']


class Action4916(Action):
    # 能把敌人吸引到身边的特殊武装
    # Activates electromagnets capable of drawing in a target.
    id = 4916
    names = ['电磁石(CMN)(1)', 'Stickyloom(CMN)(1)']
    _orig_names = ['电磁石', 'Stickyloom']


class Action4917(Action):
    # 吸取敌机电力，给自机充电
    # Saps a target of its electrical charge.
    # related: [魔力供给](Status345),
    id = 4917
    names = ['Recharge(CMN)(1)', '充电(CMN)(1)']
    _orig_names = ['充电', 'Recharge']


class Action4930(Action):
    # 可以清扫变身的诅咒，使变身魔法失效
    # Casts a minor spell to prevent curses of transfiguration.
    id = 4930
    names = ['清扫魔咒(CMN)(1)', 'Silencing Cant(CMN)(1)']
    _orig_names = ['Silencing Cant', '清扫魔咒']


class Action4931(Action):
    # 将积攒在肺里的空气一口气全喷出来
    # Fills lungs with air then releases it in a single powerful gust.
    id = 4931
    names = ['Buffet(CMN)(2)', '突风(CMN)(2)']
    _orig_names = ['突风', 'Buffet']


class Action4976(Action):
    # 在飞行中做出各种飞行特技
    # 演出技能，没有任何实际效果
    # Do a barrel roll!
    # ※Has no effect in battle.
    id = 4976
    names = ['空战机动(CMN)', 'Air Combat Maneuver(CMN)']
    _orig_names = ['Air Combat Maneuver', '空战机动']


class Action5872(Action):
    # 从香炉中喷出烟雾四面散播
    # Evenly distributes the Vath solution in a fine mist.
    id = 5872
    names = ['Fumigate(CMN)(0)', '散播(CMN)(0)']
    _orig_names = ['散播', 'Fumigate']


class Action6143(Action):
    # 喷射出冰冷的水流
    # Sprays tepid water over target.
    id = 6143
    names = ['喷水(CMN)(1)', 'Saturate(CMN)(1)']
    _orig_names = ['喷水', 'Saturate']


class Action6273(Action):
    # 对目标造成伤害
    # Deals damage to a target.
    id = 6273
    names = ['Pummel(CMN)', '殴打(CMN)']
    _orig_names = ['Pummel', '殴打']


class Action6274(Action):
    # 对目标及其周围的敌人造成伤害，并附加受伤加重状态
    # Deals damage to nearby enemies while increasing vulnerability.
    id = 6274
    names = ['虚空烈炎(CMN)', 'Void Fire II(CMN)']
    _orig_names = ['虚空烈炎', 'Void Fire II']


class Action6293(Action):
    # 发出蕴含魔力的龙啸
    # Emits a deafening roar charged with arcane dragon magicks.
    id = 6293
    names = ['咆哮(CMN)', 'Roar(CMN)']
    _orig_names = ['咆哮', 'Roar']


class Action6294(Action):
    # 散播治愈莫古力族的绒毛
    # Disperses countless moogle-soothing cloud mallow seeds into the air.
    id = 6294
    names = ['绒毛散播(CMN)(0)', 'Seed(CMN)(0)']
    _orig_names = ['绒毛散播', 'Seed']


class Action6295(Action):
    # 将积攒在肺里的空气一口气全喷出来
    # 演出技能，没有任何实际效果
    # Fills lungs with air then releases it in a single powerful gust.
    # ※Has no effect in battle.
    id = 6295
    names = ['突风(CMN)(3)', 'Buffet(CMN)(3)']
    _orig_names = ['突风', 'Buffet']


class Action6296(Action):
    # 从香炉中喷出烟雾四面散播
    # 演出技能，没有任何实际效果
    # Evenly distributes Vath solution in a fine mist.
    # ※Has no effect in battle.
    id = 6296
    names = ['散播(CMN)(1)', 'Fumigate(CMN)(1)']
    _orig_names = ['散播', 'Fumigate']


class Action6297(Action):
    # 散播治愈莫古力族的绒毛
    # 演出技能，没有任何实际效果
    # Disperses countless moogle-soothing cloud mallow seeds into the air.
    # ※Has no effect in battle.
    id = 6297
    names = ['Seed(CMN)(1)', '绒毛散播(CMN)(1)']
    _orig_names = ['绒毛散播', 'Seed']


class Action6324(Action):
    # 随行的莫古力族开始在周围转圈
    # 演出技能，没有任何实际效果
    # Dance! Dance I say!
    # ※Has no effect in battle.
    id = 6324
    names = ['莫古莫古回旋(CMN)', 'Mogatory Mog Dance(CMN)']
    _orig_names = ['莫古莫古回旋', 'Mogatory Mog Dance']


class Action6871(Action):
    # 召唤圣力攻击范围区域并追加眩晕效果，可对特定的敌人发挥奇效
    # Stuns and deals damage to all nearby targets. Damage increased for certain enemies.
    id = 6871
    names = ['天罚(CMN)', 'Heavenly Judge(CMN)']
    _orig_names = ['Heavenly Judge', '天罚']


class Action7531(Action):
    # 一定时间内，将自身所受的伤害减轻20%
    # 持续时间：20秒
    # Reduces damage taken by 20%.
    # Duration: 20s
    # related: [铁壁(1)](Status71), [铁壁(0)](Status1191), [铁壁(2)](Status1978),
    id = 7531
    names = ['Rampart(CMN)(0)', '铁壁(CMN)(0)']
    _orig_names = ['铁壁', 'Rampart']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action7533(Action):
    # 向目标进行挑衅，令目标对自身的仇恨变为最高后，继续提高自身仇恨
    # Gesture threateningly, placing yourself at the top of a target's enmity list while gaining additional enmity.
    id = 7533
    names = ['Provoke(CMN)', '挑衅(CMN)']
    _orig_names = ['Provoke', '挑衅']


class Action7535(Action):
    # 使自身周围的敌人攻击伤害降低10%
    # 持续时间：10秒
    # Reduces damage dealt by nearby enemies by 10%.
    # Duration: 10s
    # related: [雪仇剑(0)](Status753), [雪仇](Status1193), [雪仇剑(1)](Status2101),
    id = 7535
    names = ['雪仇(CMN)', 'Reprisal(CMN)']
    _orig_names = ['Reprisal', '雪仇']
    # remain metas: {'dmg_reduce': '10%'}


class Action7537(Action):
    # 将自身仇恨的25%转移给目标队员
    # Diverts 25% of enmity to target party member.
    id = 7537
    names = ['退避(CMN)', 'Shirk(CMN)']
    _orig_names = ['Shirk', '退避']


class Action7538(Action):
    # 中断目标的技能咏唱
    # Interrupts the use of a target's action.
    id = 7538
    names = ['Interject(CMN)', '插言(CMN)']
    _orig_names = ['Interject', '插言']


class Action7540(Action):
    # 令目标陷入眩晕状态
    # 持续时间：5秒
    # Stuns target.
    # Duration: 5s
    id = 7540
    names = ['下踢(CMN)', 'Low Blow(CMN)']
    _orig_names = ['下踢', 'Low Blow']


class Action7541(Action):
    # 恢复自身体力
    # 恢复力：500
    # Instantly restores own HP.
    # Cure Potency: 500
    id = 7541
    names = ['内丹(CMN)(0)', 'Second Wind(CMN)(0)']
    _orig_names = ['Second Wind', '内丹']
    heal = 500


class Action7542(Action):
    # 一定时间内，将自身物理攻击所造成伤害的一部分转化为自身的体力
    # 持续时间：20秒
    # Converts a portion of physical damage dealt into HP.
    # Duration: 20s
    # related: [浴血(0)](Status84), [浴血(1)](Status1982),
    id = 7542
    names = ['Bloodbath(CMN)', '浴血(CMN)']
    _orig_names = ['浴血', 'Bloodbath']


class Action7546(Action):
    # 一定时间内无视技能的方向要求
    # 持续时间：10秒
    # 积蓄次数：2
    # Nullifies all action direction requirements.
    # Duration: 10s
    # Maximum Charges: 2
    # related: [真北](Status1250),
    id = 7546
    names = ['True North(CMN)', '真北(CMN)']
    _orig_names = ['真北', 'True North']


class Action7548(Action):
    # 为自身张开一个防护罩，一定时间内令除特定攻击之外其他所有击退与吸引效果失效
    # 持续时间：6秒
    # 防护罩追加效果（受到物理攻击时，发动几率100%）：攻击者减速20%
    # 持续时间：15秒
    # Creates a barrier nullifying most knockback and draw-in effects.
    # Duration: 6s
    # Additional Effect: Slow +20% when barrier is struck
    # Duration: 15s
    # related: [亲疏自行(0)](Status1984), [吸引(0)](Status2529), [亲疏自行(1)](Status2181), [吸引(1)](Status2486), [亲疏自行(2)](Status1209), [亲疏自行(3)](Status2172),
    id = 7548
    names = ["Arm's Length(CMN)", '亲疏自行(CMN)']
    _orig_names = ["Arm's Length", '亲疏自行']


class Action7549(Action):
    # 一定时间内，令目标物理攻击造成的伤害降低10%，魔法攻击造成的伤害降低5%
    # 持续时间：10秒
    # Lowers target's physical damage dealt by 10% and magic damage dealt by 5%.
    # Duration: 10s
    # related: [牵制(0)](Status2185), [牵制(1)](Status1195),
    id = 7549
    names = ['牵制(CMN)', 'Feint(CMN)']
    _orig_names = ['Feint', '牵制']
    # remain metas: {'dmg_reduce': '10%，魔法攻击造成的伤害降低5%'}


class Action7551(Action):
    # 中断目标的技能咏唱
    # Interrupts the use of a target's action.
    id = 7551
    names = ['伤头(CMN)', 'Head Graze(CMN)']
    _orig_names = ['Head Graze', '伤头']


class Action7553(Action):
    # 对目标造成止步效果
    # 持续时间：10秒
    # 发动之后会停止自动攻击
    # Binds target.
    # Duration: 10s
    # Cancels auto-attack upon execution.
    # Target unbound if damage taken.
    id = 7553
    names = ['Foot Graze(CMN)', '伤足(CMN)']
    _orig_names = ['Foot Graze', '伤足']


class Action7554(Action):
    # 令目标陷入40%加重状态
    # 持续时间：10秒
    # Afflicts target with Heavy +40%.
    # Duration: 10s
    id = 7554
    names = ['Leg Graze(CMN)', '伤腿(CMN)']
    _orig_names = ['伤腿', 'Leg Graze']


class Action7557(Action):
    # 提高自身和周围队员的移动速度
    # 进入战斗状态后效果消失，并且战斗状态下也无法重新生效
    # 持续时间：30秒
    # Increases movement speed of self and nearby party members.
    # Duration: 30s
    # Effect ends when enmity is generated. Has no effect in battle.
    # related: [速行(0)](Status1985), [速行(1)](Status1199),
    id = 7557
    names = ['速行(CMN)', 'Peloton(CMN)']
    _orig_names = ['Peloton', '速行']


class Action7559(Action):
    # 一定时间内，咏唱的魔法不会被任何妨碍打断
    # 同时，令除特定攻击之外其他所有击退与吸引效果失效
    # 持续时间：6秒
    # Spells can be cast without interruption.
    # Additional Effect: Nullifies most knockback and draw-in effects
    # Duration: 6s
    # related: [沉稳咏唱](Status160), [吸引(0)](Status2529), [吸引(1)](Status2486),
    id = 7559
    names = ['沉稳咏唱(CMN)', 'Surecast(CMN)']
    _orig_names = ['Surecast', '沉稳咏唱']


class Action7560(Action):
    # 一定时间内，令目标物理攻击造成的伤害降低5%，魔法攻击造成的伤害降低10%
    # 持续时间：10秒
    # Lowers target's physical damage dealt by 5% and magic damage dealt by 10%.
    # Duration: 10s
    # related: [昏乱(0)](Status1203), [昏乱(1)](Status1988),
    id = 7560
    names = ['昏乱(CMN)', 'Addle(CMN)']
    _orig_names = ['Addle', '昏乱']
    # remain metas: {'dmg_reduce': '5%，魔法攻击造成的伤害降低10%'}


class Action7561(Action):
    # 一定时间内，下次咏唱的魔法没有任何咏唱时间
    # 持续时间：10秒
    # Next spell is cast immediately.
    # Duration: 10s
    # related: [即刻咏唱(0)](Status1987), [即刻咏唱(1)](Status167), [即刻咏唱(2)](Status1325),
    id = 7561
    names = ['Swiftcast(CMN)', '即刻咏唱(CMN)']
    _orig_names = ['Swiftcast', '即刻咏唱']


class Action7562(Action):
    # 持续恢复自身魔力
    # 效果量：55
    # 持续时间：21秒
    # Gradually restores own MP.
    # Potency: 55
    # Duration: 21s
    # related: [醒梦](Status1204),
    id = 7562
    names = ['醒梦(CMN)', 'Lucid Dreaming(CMN)']
    _orig_names = ['醒梦', 'Lucid Dreaming']


class Action7568(Action):
    # 解除目标身上部分弱化效果中的一种
    # Removes a single detrimental effect from target.
    id = 7568
    names = ['Esuna(CMN)', '康复(CMN)']
    _orig_names = ['康复', 'Esuna']


class Action7571(Action):
    # 将目标队员吸引到自己身边
    # 目标身中部分弱化效果或处于非战斗状态时无效
    # 发动条件：自身处于战斗状态
    # Instantly draws target party member to your side. Cannot be used outside of combat or when target is suffering from certain enfeeblements.
    id = 7571
    names = ['营救(CMN)', 'Rescue(CMN)']
    _orig_names = ['Rescue', '营救']


class Action7599(Action):
    # 弹出陆行鸟玩偶
    # Releases a shockingly cute chocobo chick.
    id = 7599
    names = ['Shockobo(CMN)(0)', '陆行鸟玩偶(CMN)(0)']
    _orig_names = ['陆行鸟玩偶', 'Shockobo']


class Action7600(Action):
    # 弹出陆行鸟玩偶
    # 演出技能，没有任何实际效果
    # Releases a shockingly cute chocobo chick.
    # ※Has no effect in battle.
    id = 7600
    names = ['Shockobo(CMN)(1)', '陆行鸟玩偶(CMN)(1)']
    _orig_names = ['陆行鸟玩偶', 'Shockobo']


class Action7619(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 7619
    names = ['Magitek Cannon(CMN)(2)', '魔导加农炮(CMN)(2)']
    _orig_names = ['Magitek Cannon', '魔导加农炮']


class Action7620(Action):
    # 向自身前方发动直线范围攻击
    # Fires a short-range burst of energy in a straight line before you.
    id = 7620
    names = ['Photon Stream(CMN)(2)', '魔导光子炮(CMN)(2)']
    _orig_names = ['Photon Stream', '魔导光子炮']


class Action7621(Action):
    # 指定地点附近发射魔导加农散弹炮
    # Fires an explosive projectile at the designated area.
    id = 7621
    names = ['Diffractive Magitek Cannon(CMN)(0)', '魔导加农散弹炮(CMN)(0)']
    _orig_names = ['Diffractive Magitek Cannon', '魔导加农散弹炮']


class Action7622(Action):
    # 向自身前方发射高功率魔导加农炮
    # Fires a concentrated burst of energy in a straight line before you.
    id = 7622
    names = ['High-powered Magitek Cannon(CMN)(0)', '高功率魔导加农炮(CMN)(0)']
    _orig_names = ['High-powered Magitek Cannon', '高功率魔导加农炮']


class Action7816(Action):
    # 扔出烟雾弹中断逮捕并潜行
    # Throw an incendiary device that creates a blanket of smoke temporarily granting you the Stealth status.
    # related: [烟雾弹](Status789),
    id = 7816
    names = ['烟雾弹(CMN)', 'Smoke Screen(CMN)']
    _orig_names = ['烟雾弹', 'Smoke Screen']


class Action7863(Action):
    # 令目标陷入眩晕状态
    # 持续时间：3秒
    # Stuns target.
    # Duration: 3s
    id = 7863
    names = ['扫腿(CMN)', 'Leg Sweep(CMN)']
    _orig_names = ['扫腿', 'Leg Sweep']


class Action7962(Action):
    # 向指定地点附近开炮射击
    # 追加效果：拘束魔导机车大魔
    # 持续时间：4秒
    # Fires an explosive projectile at the designated area.
    # Additional Effect: Binds magna roader
    # Duration: 4s
    id = 7962
    names = ['Magitek Pulse(CMN)(0)', '魔导脉冲弹(CMN)']
    _orig_names = ['Magitek Pulse', '魔导脉冲弹']


class Action8517(Action):
    # 燃烧身上的元气伪装成信徒
    # Use the aetheric residue lingering on your body to temporarily disguise yourself as one of Lakshmi's loyal dreamers.
    # related: [元气](Status1290),
    id = 8517
    names = ['元气(CMN)(0)', 'Vril(CMN)(0)']
    _orig_names = ['元气', 'Vril']


class Action8623(Action):
    # 发射水泡
    # Sprays a jet of bubbly water.
    id = 8623
    names = ['水泡(CMN)', 'Double Bubble(CMN)']
    _orig_names = ['Double Bubble', '水泡']


class Action8624(Action):
    # 向自身前方发动发射魔导脉冲
    # Fires a magitek-powered burst of energy.
    id = 8624
    names = ['魔导脉冲(CMN)', 'Magitek Pulse(CMN)(1)']
    _orig_names = ['Magitek Pulse', '魔导脉冲']


class Action8625(Action):
    # 对指定地点发射魔导闪雷
    # Emits a bolt of magitek-powered lightning.
    id = 8625
    names = ['Magitek Thunder(CMN)', '魔导闪雷(CMN)']
    _orig_names = ['Magitek Thunder', '魔导闪雷']


class Action9035(Action):
    # 对目标发动物理攻击
    # Delivers an impotent attack.
    id = 9035
    names = ['Imp Punch(CMN)(1)', '河童拳(CMN)(1)']
    _orig_names = ['河童拳', 'Imp Punch']


class Action9066(Action):
    # 使用尼禄制造的可疑装置，暂时浮空
    # Simulates the spell Levitate using Nero tol Scaeva's odd contraption.
    id = 9066
    names = ['反重力装置(CMN)(0)', 'Anti-gravity Gimbal(CMN)(0)']
    _orig_names = ['Anti-gravity Gimbal', '反重力装置']


class Action9102(Action):
    # 启动以太干扰器振动目标周围的以太
    # Activates the instrument.
    id = 9102
    names = ['以太干扰器(CMN)', 'Aetheric Siphon(CMN)']
    _orig_names = ['Aetheric Siphon', '以太干扰器']


class Action9345(Action):
    # 燃烧身上的元气伪装成信徒
    # Use the aetheric residue lingering on your body to temporarily disguise yourself as one of Lakshmi's loyal dreamers.
    # related: [元气](Status1290),
    id = 9345
    names = ['Vril(CMN)(1)', '元气(CMN)(1)']
    _orig_names = ['元气', 'Vril']


class Action9483(Action):
    # 使用尼禄制造的可疑装置，暂时浮空
    # Simulates the spell Levitate using Nero tol Scaeva's odd contraption.
    id = 9483
    names = ['Anti-gravity Gimbal(CMN)(1)', '反重力装置(CMN)(1)']
    _orig_names = ['Anti-gravity Gimbal', '反重力装置']


class Action9823(Action):
    # 设置带有魔力的爆炸岩
    # Sets an enchanted trap that triggers upon contact.
    id = 9823
    names = ['爆炸岩(CMN)', 'Shatterstone(CMN)']
    _orig_names = ['Shatterstone', '爆炸岩']


class Action9971(Action):
    # 对指定地点发动范围攻击
    # 对人、对机动兵器威力：7500
    # 对场景物体、对自走人偶威力：750
    # Deals damage with a potency of 7,500 to all opposing players and warmachina near point of impact. 750 when attacking a mammet or object.
    id = 9971
    names = ['制导(pvp)(CMN)', 'Optical Sight(pvp)(CMN)']
    _orig_names = ['制导(pvp)', 'Optical Sight(pvp)']
    damage = 7500  # TODO: [7500, 750]


class Action9973(Action):
    # 向自身前方发出扇形范围攻击
    # 对人、对自走人偶、对场景物体威力：1000
    # 对机动兵器威力：10000
    # Delivers an attack with a potency of 10,000 to all opposing warmachina in a cone before you. 1,000 when attacking a player, mammet, or object.
    id = 9973
    names = ['Spin Crusher(pvp)(CMN)', '回旋碎踢(pvp)(CMN)']
    _orig_names = ['回旋碎踢(pvp)', 'Spin Crusher(pvp)']
    damage = 10000  # TODO: [10000, 1000]


class Action9974(Action):
    # 向自身前方发出扇形范围攻击
    # 对人、对机动兵器威力：12500
    # 对场景物体、对自走人偶威力：1250
    # Delivers an attack with a potency of 12,500 to all opposing players and warmachina in a cone before you. 1,250 when attacking a mammet or object.
    id = 9974
    names = ['Laser X Sword(pvp)(CMN)', '交叉光剑(pvp)(CMN)']
    _orig_names = ['Laser X Sword(pvp)', '交叉光剑(pvp)']
    damage = 1250  # TODO: [1250, 12500]


class Action9975(Action):
    # 对指定地点发动范围攻击
    # 对人、对机动兵器、对自走人偶威力：5000
    # 对场景物体：250000
    # 有效范围30米，离着弹地点越远威力越小
    # Deals damage with a potency of 250,000 to all objects near point of impact. 5,000 to opposing players, warmachina, or mammets.
    # Potency decreases the greater the target's distance from point of impact, to a maximum of 30 yalms.
    id = 9975
    names = ['超大型导弹(pvp)(CMN)', '3000-tonze Missile(pvp)(CMN)']
    _orig_names = ['超大型导弹(pvp)', '3000-tonze Missile(pvp)']
    damage = 5000


class Action9977(Action):
    # 向自身周围发动扇形范围攻击
    # 对人、对机动兵器威力：2500
    # 对场景物体、对自走人偶威力：250
    # 追加效果：将目标击退15米
    # Deals damage to all opposing players and warmachina nearby with a potency of 2,500. 250 when attacking a mammet or object.
    # Additional Effect: 15-yalm knockback
    id = 9977
    names = ['Steam Release(pvp)(CMN)', '喷射蒸汽(pvp)(CMN)']
    _orig_names = ['喷射蒸汽(pvp)', 'Steam Release(pvp)']
    damage = 250  # TODO: [250, 2500]


class Action9978(Action):
    # 向自身前方发动扇形范围魔法攻击
    # 对人、对机动兵器威力：10000
    # 对人、对机动兵器威力追加效果：火伤
    # 威力：2500
    # 持续时间：12秒
    # 对场景物体、对自走人偶威力：1000
    # Deals damage with a potency of 10,000 to all opposing players and warmachina in a cone before you. 1,000 when attacking a mammet or object.
    # Additional Effect: Inflicts Burns on opposing players and warmachina
    # Potency: 2,500
    # Duration: 12s
    # related: [火伤(0)](Status2401), [火伤(1)](Status2082), [火伤(2)](Status2945), [火伤(3)](Status2916), [火伤(4)](Status1577), [火伤(5)](Status267), [火伤(6)](Status619), [火伤(7)](Status530), [火伤(8)](Status2194), [火伤(9)](Status503), [火伤(10)](Status2199), [火伤(11)](Status250), [火伤(12)](Status1787), [火伤(13)](Status284),
    id = 9978
    names = ['大火炎放射(pvp)(CMN)', 'Flarethrower(pvp)(CMN)']
    _orig_names = ['大火炎放射(pvp)', 'Flarethrower(pvp)']
    damage = 2500  # TODO: [2500, 10000]
    # remain metas: {'dmg_ot': '1000'}


class Action9979(Action):
    # 对指定地点发动范围物理攻击
    # 对人、对机动兵器、对自走人偶威力：7500
    # 对场景物体威力：150000
    # 追加效果：眩晕
    # 持续时间：3秒
    # Deals damage with a potency of 150,000 to all objects near point of impact. 7,500 when attacking opposing players, warmachina, or mammets.
    # Additional Effect: Stun
    # Duration: 3s
    id = 9979
    names = ['Double Rocket Punch(pvp)(CMN)', '双重火箭飞拳(pvp)(CMN)']
    _orig_names = ['双重火箭飞拳(pvp)', 'Double Rocket Punch(pvp)']
    damage = 150000  # TODO: [150000, 7500]


class Action9980(Action):
    # 向自身前方发动直线范围攻击
    # 对人、对机动兵器威力：15000
    # 对场景物体、对自走人偶威力：1500
    # 追加效果：将目标击退30米
    # Delivers damage with a potency of 15,000 to all opposing players and warmachina in a straight line before you. 1,500 when attacking a mammet or object.
    # Additional Effect: 30-yalm knockback
    id = 9980
    names = ['巨型光束炮(pvp)(CMN)', 'Mega Beam(pvp)(CMN)']
    _orig_names = ['巨型光束炮(pvp)', 'Mega Beam(pvp)']
    damage = 15000  # TODO: [15000, 1500]


class Action9981(Action):
    # 自身搭乘的机动兵器能量恢复5000点
    # 发动条件：青磷水25点
    # Uses 25 units of ceruleum fuel (CE) to restore 5000 EP to currently mounted warmachina.
    id = 9981
    names = ['装填青磷水(pvp)(CMN)', 'Ceruleum Refill(pvp)(CMN)']
    _orig_names = ['Ceruleum Refill(pvp)', '装填青磷水(pvp)']


class Action9982(Action):
    # 对指定地点发动范围攻击
    # 对人、对机动兵器威力：5000
    # 对场景物体、对自走人偶威力：500
    # Deals damage with a potency of 5,000 to all opposing players and warmachina near point of impact. 500 when attacking a mammet or object.
    id = 9982
    names = ['Cannonfire(pvp)(CMN)', '炮击(pvp)(CMN)']
    _orig_names = ['Cannonfire(pvp)', '炮击(pvp)']
    damage = 500  # TODO: [500, 5000]


class Action10006(Action):
    # 破坏吉祥天女释放的以太晶球
    # Scatters potentially harmful aether.
    id = 10006
    names = ['Deflect(CMN)(0)', '偏折屏障(CMN)(0)']
    _orig_names = ['偏折屏障', 'Deflect']


class Action10013(Action):
    # 用力吸入
    # Orders the manta to draw water into its gaping maw.
    # related: [吸引(0)](Status2529), [吸引(1)](Status2486),
    id = 10013
    names = ['吸引(CMN)(0)', 'Inhale(CMN)(0)']
    _orig_names = ['Inhale', '吸引']


class Action10014(Action):
    # 用力吸入
    # 演出技能，没有任何实际效果
    # Orders the manta to draw water into its gaping maw.
    # ※Has no effect in battle.
    # related: [吸引(0)](Status2529), [吸引(1)](Status2486),
    id = 10014
    names = ['Inhale(CMN)(1)', '吸引(CMN)(1)']
    _orig_names = ['Inhale', '吸引']


class Action10019(Action):
    # 投掷礼花筒
    # Toss a Starburst into the air.
    id = 10019
    names = ['Starburst(CMN)(0)', '礼花筒(CMN)(0)']
    _orig_names = ['Starburst', '礼花筒']


class Action10020(Action):
    # 投掷礼花筒
    # 演出技能，没有任何实际效果
    # Toss a Starburst into the air.
    # ※Has no effect in battle.
    id = 10020
    names = ['Starburst(CMN)(1)', '礼花筒(CMN)(1)']
    _orig_names = ['Starburst', '礼花筒']


class Action10057(Action):
    # 从机动兵器上下来
    # Exit the warmachina.
    id = 10057
    names = ['Dismount(pvp)(CMN)', '降落(pvp)(CMN)']
    _orig_names = ['降落(pvp)', 'Dismount(pvp)']


class Action10061(Action):
    # 传送到我方队伍的初始地点
    # 该技能在对战中也能使用
    # Returns your team to the starting area. Can be used while engaged in battle.
    # related: [回返](Status2452),
    id = 10061
    names = ['返回(CMN)(1)', 'Return(CMN)(1)']
    _orig_names = ['Return', '返回']


class Action10229(Action):
    # 大幅度恢复体力
    # Restores a moderate amount of health.
    id = 10229
    names = ['回复药“大”(CMN)', 'Mega Potion(CMN)']
    _orig_names = ['Mega Potion', '回复药“大”']


class Action10262(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面有红色的颜料
    # Red paint drips from the tip of this massive brush made from Alpha's feathers.
    # related: [红色的颜料](Status1470),
    id = 10262
    names = ['Red Paint(CMN)', '红色陆行鸟之笔(CMN)']
    _orig_names = ['红色陆行鸟之笔', 'Red Paint']


class Action10263(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面有黄色的颜料
    # Yellow paint drips from the tip of this massive brush made from Alpha's feathers.
    # related: [黄色的颜料](Status1467),
    id = 10263
    names = ['Yellow Paint(CMN)', '黄色陆行鸟之笔(CMN)']
    _orig_names = ['黄色陆行鸟之笔', 'Yellow Paint']


class Action10264(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面有黑色的颜料
    # Black paint drips from the tip of this massive brush made from Alpha's feathers.
    # related: [黑色的颜料](Status1469),
    id = 10264
    names = ['黑色陆行鸟之笔(CMN)(0)', 'Black Paint(CMN)(0)']
    _orig_names = ['黑色陆行鸟之笔', 'Black Paint']


class Action10265(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面有蓝色的颜料
    # Blue paint drips from the tip of this massive brush made from Alpha's feathers.
    # related: [蓝色的颜料](Status1468),
    id = 10265
    names = ['蓝色陆行鸟之笔(CMN)', 'Blue Paint(CMN)']
    _orig_names = ['Blue Paint', '蓝色陆行鸟之笔']


class Action10270(Action):
    # 放出比风还强烈的鼻息
    # Emit a sinal blast precisely powerful enough to misdirect the wind itself.
    id = 10270
    names = ['鼻息(CMN)', 'Snort(CMN)']
    _orig_names = ['鼻息', 'Snort']


class Action10401(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面没有附着颜料
    # A brush made from Alpha's feathers.
    id = 10401
    names = ['Chocobo Brush(CMN)', '陆行鸟之笔(CMN)']
    _orig_names = ['Chocobo Brush', '陆行鸟之笔']


class Action10713(Action):
    # 挥舞红色的魔导光棒为乌拉拉声援
    # Might as well use a red light to cheer on your favorite performer.
    id = 10713
    names = ['Cheer Jump(CMN)(0)', '声援小红(CMN)(0)']
    _orig_names = ['声援小红', 'Cheer Jump']


class Action10714(Action):
    # 挥舞黄色的魔导光棒为鸣海声援
    # Use a yellow light to cheer on your favorite performer like you just don't care.
    id = 10714
    names = ['Cheer Wave(CMN)(0)', '声援小黄(CMN)(0)']
    _orig_names = ['Cheer Wave', '声援小黄']


class Action10715(Action):
    # 挥舞蓝色的魔导光棒为马夏·玛卡拉卡声援
    # Use a pair of blue lights to clear your favorite performer for landing.
    id = 10715
    names = ['Cheer On(CMN)(0)', '声援小蓝(CMN)(0)']
    _orig_names = ['Cheer On', '声援小蓝']


class Action10716(Action):
    # 挥舞红色的魔导光棒为乌拉拉声援
    # Might as well use a red light to cheer on your favorite performer.
    id = 10716
    names = ['声援小红(CMN)(1)', 'Cheer Jump(CMN)(1)']
    _orig_names = ['声援小红', 'Cheer Jump']


class Action10717(Action):
    # 挥舞黄色的魔导光棒为鸣海声援
    # Use a yellow light to cheer on your favorite performer like you just don't care.
    id = 10717
    names = ['Cheer Wave(CMN)(1)', '声援小黄(CMN)(1)']
    _orig_names = ['Cheer Wave', '声援小黄']


class Action10718(Action):
    # 挥舞蓝色的魔导光棒为马夏·玛卡拉卡声援
    # Use a pair of blue lights to clear your favorite performer for landing.
    id = 10718
    names = ['声援小蓝(CMN)(1)', 'Cheer On(CMN)(1)']
    _orig_names = ['Cheer On', '声援小蓝']


class Action11063(Action):
    # 解除公演观众状态
    # Removes the “Face in the Crowd” status.
    # related: [公演观众](Status1494),
    id = 11063
    names = ['离场(CMN)', 'Curtain Call(CMN)']
    _orig_names = ['离场', 'Curtain Call']


class Action11191(Action):
    # 对目标发动无属性魔法攻击
    # 威力：200
    # Deals unaspected damage with a potency of 200.
    id = 11191
    names = ['毁荡(CMN)', 'Ruin III(CMN)']
    _orig_names = ['毁荡', 'Ruin III']
    damage = 200


class Action11192(Action):
    # 恢复目标的体力
    # 恢复力：400
    # Restores target's HP.
    # Cure Potency: 400
    id = 11192
    names = ['Physick(CMN)', '医术(CMN)']
    _orig_names = ['Physick', '医术']
    heal = 400


class Action11193(Action):
    # 对指定地点发动范围无属性魔法攻击
    # 威力：3600
    # Deals unaspected damage with a potency of 3,600 to all enemies near point of impact.
    id = 11193
    names = ['Starstorm(CMN)(1)', '星体风暴(CMN)(1)']
    _orig_names = ['Starstorm', '星体风暴']
    damage = 3600


class Action11482(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：30
    # 追加效果：止步
    # 持续时间：20秒
    # Deals unaspected damage with a potency of 30 to target and all enemies nearby it.
    # Additional Effect: Bind
    # Duration: 20s
    id = 11482
    names = ['Tri-shackle(CMN)', '三重惩戒(CMN)']
    _orig_names = ['Tri-shackle', '三重惩戒']
    damage = 30


class Action11499(Action):
    # 文明地喊口号
    # Lead the mikoshi bearers in a rousing display of civilization and enlightenment.
    id = 11499
    names = ['Wasshoi(CMN)(0)', '喊口号(CMN)(0)']
    _orig_names = ['喊口号', 'Wasshoi']


class Action11500(Action):
    # 文明地喊口号
    # 演出技能，没有任何实际效果
    # Lead the mikoshi bearers in a rousing display of civilization and enlightenment.
    # ※Has no effect in battle.
    id = 11500
    names = ['喊口号(CMN)(1)', 'Wasshoi(CMN)(1)']
    _orig_names = ['喊口号', 'Wasshoi']


class Action12257(Action):
    # 向指定地点附近开炮射击
    # Fires an explosive projectile at the designated area.
    id = 12257
    names = ['Cannonfire(CMN)(3)', '炮击(CMN)(5)']
    _orig_names = ['Cannonfire', '炮击']


class Action12577(Action):
    # 向目标所在方向发动直线范围攻击
    # 追加效果：受伤加重
    # Fires a short-range burst of energy in a straight line before you.
    # Additional Effect: Increased damage taken
    id = 12577
    names = ['Mog Heaven(CMN)', '莫古力天堂(CMN)']
    _orig_names = ['莫古力天堂', 'Mog Heaven']


class Action12578(Action):
    # 恢复自身及周围队员的体力并附加体力持续恢复与攻击力提高效果
    # Restores HP and HP of all nearby party members, and grants healing over time as well as increased damage dealt.
    # related: [攻击力提高](Status962),
    id = 12578
    names = ['Bring It Pom(CMN)', '声援(CMN)']
    _orig_names = ['声援', 'Bring It Pom']


class Action12911(Action):
    # 产生高压雷电
    # Emits a pulse of concentrated electromagnetic energy.
    id = 12911
    names = ['Omega Jammer(CMN)', '欧米茄干扰器(CMN)']
    _orig_names = ['欧米茄干扰器', 'Omega Jammer']


class Action12958(Action):
    # 令自身发动魔法攻击造成的伤害提高60%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases magic damage dealt by 60%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12958
    names = ['Wisdom of the Aetherweaver(CMN)', '术士的记忆(CMN)']
    _orig_names = ['Wisdom of the Aetherweaver', '术士的记忆']
    # remain metas: {'dmg_increase': '60%'}


class Action12959(Action):
    # 令自身发动攻击造成的伤害提高40%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases damage dealt by 40%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12959
    names = ['Wisdom of the Martialist(CMN)', '斗士的记忆(CMN)']
    _orig_names = ['Wisdom of the Martialist', '斗士的记忆']
    # remain metas: {'dmg_increase': '40%'}


class Action12960(Action):
    # 令自身防御力提高150%，并且最大体力提高50%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases defense by 150% and maximum HP by 50%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12960
    names = ['重骑兵的记忆(CMN)', 'Wisdom of the Platebearer(CMN)']
    _orig_names = ['重骑兵的记忆', 'Wisdom of the Platebearer']


class Action12961(Action):
    # 自身防御力提高50%，并且最大体力提高10%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases defense by 50% and maximum HP by 10%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12961
    names = ['Wisdom of the Guardian(CMN)', '守护者的记忆(CMN)']
    _orig_names = ['Wisdom of the Guardian', '守护者的记忆']


class Action12962(Action):
    # 令自身最大魔力提高50%，并且发动治疗魔法的治疗量提高25%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases maximum MP by 50% and healing magic potency by 25%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12962
    names = ['祭司的记忆(CMN)', 'Wisdom of the Ordained(CMN)']
    _orig_names = ['Wisdom of the Ordained', '祭司的记忆']


class Action12963(Action):
    # 令自身发动攻击造成的伤害提高20%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases damage dealt by 20%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12963
    names = ['Wisdom of the Skirmisher(CMN)', '武人的记忆(CMN)']
    _orig_names = ['Wisdom of the Skirmisher', '武人的记忆']
    # remain metas: {'dmg_increase': '20%'}


class Action12964(Action):
    # 以自身发动攻击造成的伤害降低5%为代价，令自身的回避率提高25%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases evasion by 25% while reducing damage dealt by 5%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12964
    names = ['Wisdom of the Watcher(CMN)', '斥候的记忆(CMN)']
    _orig_names = ['Wisdom of the Watcher', '斥候的记忆']
    # remain metas: {'dmg_reduce': '5%为代价，令自身的回避率提高25%'}


class Action12965(Action):
    # 以自身发动攻击造成的伤害降低5%为代价，令自身的最大体力提高30%，并且发动治疗魔法的治疗量提高50%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases healing magic potency by 50% and maximum HP by 30%, while reducing damage dealt by 5%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12965
    names = ['Wisdom of the Templar(CMN)', '圣骑士的记忆(CMN)']
    _orig_names = ['Wisdom of the Templar', '圣骑士的记忆']
    # remain metas: {'dmg_reduce': '5%为代价，令自身的最大体力提高30%，并且发动治疗魔法的治疗量提高50%'}


class Action12966(Action):
    # 以令自身魔法防御力降低60%为代价提高30%发动攻击造成的伤害
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases damage dealt by 30% while reducing magic defense by 60%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 12966
    names = ['Wisdom of the Irregular(CMN)', '狂战士的记忆(CMN)']
    _orig_names = ['狂战士的记忆', 'Wisdom of the Irregular']


class Action12967(Action):
    # 令自身回避率提高10%，并且移动速度提高、中毒耐性提高
    # 该移动速度提高效果在骑乘坐骑时有效
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases poison resistance and movement speed, including mount speed, and increases evasion by 10%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    # related: [移动速度提高(0)](Status1112), [移动速度提高(1)](Status669),
    id = 12967
    names = ['Wisdom of the Breathtaker(CMN)', '盗贼的记忆(CMN)']
    _orig_names = ['Wisdom of the Breathtaker', '盗贼的记忆']


class Action12968(Action):
    # 令自身最大体力提高10%，并且命中率提高30%
    # 持续时间内若陷入无法战斗状态，有70%几率自动复活
    # 持续时间：180分
    # Increases maximum HP by 10% and accuracy by 30%.
    # Additional Effect: Grants a 70% chance of automatic revival upon KO
    # Duration: 180m
    # related: [英杰的加护](Status1641),
    id = 12968
    names = ['Spirit of the Remembered(CMN)', '英杰的加护(CMN)']
    _orig_names = ['Spirit of the Remembered', '英杰的加护']


class Action12969(Action):
    # 令目标的物理防御力提高1000
    # 持续时间：30分
    # Increases the physical defense of target by 1,000.
    # Duration: 30m
    # related: [文理护盾](Status1642),
    id = 12969
    names = ['Protect L(CMN)', '文理护盾(CMN)']
    _orig_names = ['文理护盾', 'Protect L']


class Action12970(Action):
    # 令目标的魔法防御力提高1000
    # 持续时间：30分
    # Increases the magic defense of target by 1,000.
    # Duration: 30m
    # related: [文理魔盾](Status1643),
    id = 12970
    names = ['Shell L(CMN)', '文理魔盾(CMN)']
    _orig_names = ['文理魔盾', 'Shell L']


class Action12971(Action):
    # 令目标陷入无法战斗状态
    # 目标剩余体力越少成功率越高
    # KOs target. The less the target's HP, the greater the chance of success.
    id = 12971
    names = ['Death L(CMN)', '文理即死(CMN)']
    _orig_names = ['文理即死', 'Death L']


class Action12972(Action):
    # 对自身附加蓄力状态，最多可以积累16档
    # “蓄力”效果：效果时间内自身发动的1次战技威力提高，效果量为每档提高30%
    # 持续时间：30秒
    # 与战技共享复唱时间
    # Grants a stack of Boost, up to a maximum of 16.
    # Boost Bonus: Increases potency of next weaponskill by 30% per stack
    # Duration: 30s
    # Shares a recast timer with all weaponskills.
    # related: [蓄力(2)](Status1656), [蓄力(3)](Status203), [蓄力(1)](Status1716), [蓄力(0)](Status2448),
    id = 12972
    names = ['Focus L(CMN)', '文理蓄力(CMN)']
    _orig_names = ['Focus L', '文理蓄力']


class Action12973(Action):
    # 令目标陷入麻痹状态
    # 持续时间：60秒
    # Afflicts target with Paralysis.
    # Duration: 60s
    id = 12973
    names = ['文理麻痹(CMN)', 'Paralyze L(CMN)']
    _orig_names = ['文理麻痹', 'Paralyze L']


class Action12974(Action):
    # 令目标及其周围敌人陷入麻痹状态
    # 持续时间：60秒
    # Afflicts target and all neaby enemies with Paralysis.
    # Duration: 60s
    id = 12974
    names = ['Paralyze L III(CMN)', '文理强麻痹(CMN)']
    _orig_names = ['文理强麻痹', 'Paralyze L III']


class Action12975(Action):
    # 令自身的移动速度大幅提高
    # 持续时间：10秒
    # Greatly increases movement speed.
    # Duration: 10s
    # related: [文理敏捷](Status1644),
    id = 12975
    names = ['文理敏捷(CMN)', 'Swift L(CMN)']
    _orig_names = ['文理敏捷', 'Swift L']


class Action12976(Action):
    # 令自身的回避率提高15%
    # 持续时间：45秒
    # Increases evasion by 15%.
    # Duration: 45s
    id = 12976
    names = ['文理飘羽步(CMN)', 'Featherfoot L(CMN)']
    _orig_names = ['文理飘羽步', 'Featherfoot L']


class Action12977(Action):
    # 对目标发动远距离物理攻击
    # 威力：100
    # 追加效果：受伤加重
    # 持续时间：60秒
    # 受伤加重效果：目标所受伤害提高8%
    #
    # Delivers a ranged attack with a potency of 100.
    # Additional Effect: Afflicts target with Spirit Dart L, increasing damage taken by 8%
    # Duration: 60s
    # related: [文理精神镖](Status1654),
    id = 12977
    names = ['文理精神镖(CMN)', 'Spirit Dart L(CMN)']
    _orig_names = ['文理精神镖', 'Spirit Dart L']
    damage = 100
    # remain metas: {'taken_dmg_increase': '8%'}


class Action12978(Action):
    # 对自身周围的敌人发动范围魔法攻击
    # 威力：4000
    # 自身也会受到巨大伤害
    # 对自身威力：999999
    # Deals unaspected damage to all nearby enemies with a potency of 4,000, while dealing damage with a potency of 999,999 to self.
    id = 12978
    names = ['文理天灾(CMN)', 'Catastrophe L(CMN)']
    _orig_names = ['文理天灾', 'Catastrophe L']
    damage = 999999  # TODO: [999999, 4000]


class Action12979(Action):
    # 打消目标身上的一种强化状态
    # Removes one beneficial status from target.
    id = 12979
    names = ['文理驱魔(CMN)', 'Dispel L(CMN)']
    _orig_names = ['Dispel L', '文理驱魔']


class Action12980(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：令目标的回避率降低
    # 持续时间：60秒
    # Delivers an attack with a potency of 100.
    # Additional Effect: Reduces target's evasion
    # Duration: 60s
    id = 12980
    names = ['文理虚枪(CMN)', 'Feint L(CMN)']
    _orig_names = ['Feint L', '文理虚枪']
    damage = 100


class Action12981(Action):
    # 隐藏自己的身形，大多数敌人都无法发现自己
    # 不过移动速度会降低50%
    # 对部分特殊怪物无效
    # 发动除冲刺以外的技能会取消该状态
    # 持续时间：永久
    # 发动条件：自身处于非战斗状态
    # Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 50%. Has no effect on certain enemies with special sight.
    # Cannot be executed while in combat.
    # Effect ends upon use of any action other than Sprint, or upon reuse.
    id = 12981
    names = ['文理潜行(CMN)', 'Stealth L(CMN)']
    _orig_names = ['Stealth L', '文理潜行']


class Action12982(Action):
    # 自身快速移动到目标身边
    # 止步状态下无法发动
    # Rush to a target's side.
    # Unable to cast if bound.
    id = 12982
    names = ['Aetherial Manipulation L(CMN)', '文理以太步(CMN)']
    _orig_names = ['Aetherial Manipulation L', '文理以太步']


class Action12983(Action):
    # 向身后跳出10米距离
    # 止步状态下无法发动
    # Jump 10 yalms back from current position. Cannot be executed while bound.
    id = 12983
    names = ['Backstep L(CMN)', '文理后跳(CMN)']
    _orig_names = ['文理后跳', 'Backstep L']


class Action12984(Action):
    # 令目标陷入眩晕状态
    # 持续时间：8秒
    # Stuns target.
    # Duration: 8s
    id = 12984
    names = ['文理镇定(CMN)', 'Tranquilizer L(CMN)']
    _orig_names = ['Tranquilizer L', '文理镇定']


class Action12985(Action):
    # 一定时间内，将自身攻击所造成伤害的一定比例转化为自身的体力
    # 持续时间：45秒
    # Converts a portion of damage dealt into HP.
    # Duration: 45s
    # related: [文理浴血](Status1677),
    id = 12985
    names = ['文理浴血(CMN)', 'Bloodbath L(CMN)']
    _orig_names = ['文理浴血', 'Bloodbath L']


class Action12986(Action):
    # 恢复自身最大体力与魔力的50%
    # Instantly restores 50% of maximum HP and MP.
    id = 12986
    names = ['Rejuvenate L(CMN)', '文理充能(CMN)']
    _orig_names = ['文理充能', 'Rejuvenate L']


class Action12987(Action):
    # 对目标发动物理攻击
    # 威力：300
    # 追加效果：减速20%
    # 持续时间：30秒
    # 发动条件：回避之后
    # Delivers an attack with a potency of 300.
    # Can only be executed immediately after evading an attack.
    # Additional Effect: Slow +20%
    # Duration: 30s
    id = 12987
    names = ['文理反攻(CMN)', 'Haymaker L(CMN)']
    _orig_names = ['Haymaker L', '文理反攻']
    damage = 300


class Action12988(Action):
    # 效果时间内，自身发动的1次能力类技能复唱时间缩短50%
    # 持续时间：15秒
    # Shortens recast time for next ability used by 50%.
    # Duration: 15s
    id = 12988
    names = ['Rapid Recast L(CMN)', '文理高速复唱(CMN)']
    _orig_names = ['文理高速复唱', 'Rapid Recast L']


class Action12989(Action):
    # 恢复目标的体力
    # 恢复力：9000
    # Restores target's HP.
    # Cure Potency: 9,000
    id = 12989
    names = ['Cure L(CMN)', '文理治疗(CMN)']
    _orig_names = ['文理治疗', 'Cure L']
    heal = 9000


class Action12990(Action):
    # 恢复目标的体力
    # 恢复力：12000
    # Restores target's HP.
    # Cure Potency: 12,000
    id = 12990
    names = ['文理救疗(CMN)', 'Cure L II(CMN)']
    _orig_names = ['Cure L II', '文理救疗']
    heal = 12000


class Action12991(Action):
    # 为目标附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力10%的伤害量
    # 持续时间：30秒
    # Creates a barrier around target that absorbs damage totaling 10% of target's maximum HP.
    # Duration: 30s
    id = 12991
    names = ['Stoneskin L(CMN)', '文理石肤(CMN)']
    _orig_names = ['文理石肤', 'Stoneskin L']
    # remain metas: {'shield': '目标最大体力10%'}


class Action12992(Action):
    # 恢复目标及其周围队员的体力
    # 恢复力：9000
    # Restores HP of target and all party members nearby target.
    # Cure Potency: 9,000
    id = 12992
    names = ['Cure L III(CMN)', '文理愈疗(CMN)']
    _orig_names = ['文理愈疗', 'Cure L III']
    heal = 9000


class Action12993(Action):
    # 令目标体力持续恢复
    # 恢复力：2500
    # 持续时间：21秒
    # Grants Regen to target.
    # Cure Potency: 2,500
    # Duration: 21s
    id = 12993
    names = ['Regen L(CMN)', '文理再生(CMN)']
    _orig_names = ['文理再生', 'Regen L']
    # remain metas: {'heal_ot': '2500'}


class Action12994(Action):
    # 解除目标身上部分弱化效果中的一种
    # Removes a single detrimental effect from target.
    id = 12994
    names = ['文理康复(CMN)', 'Esuna L(CMN)']
    _orig_names = ['文理康复', 'Esuna L']


class Action12995(Action):
    # 向目标进行挑衅，令目标对自身的仇恨变为最高
    # 并且一定时间内提升自身仇恨
    # 持续时间：15秒
    # Gesture threateningly, placing yourself at the top of a target's enmity list and increasing enmity generation.
    # Duration: 15s
    # related: [文理激怒](Status1657),
    id = 12995
    names = ['文理激怒(CMN)', 'Incense L(CMN)']
    _orig_names = ['文理激怒', 'Incense L']


class Action12996(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43),
    id = 12996
    names = ['Raise L(CMN)', '文理复活(CMN)']
    _orig_names = ['Raise L', '文理复活']


class Action12997(Action):
    # 令目标攻击所造成的伤害提高10%
    # 持续时间：300秒
    # Increases target's damage dealt by 10%.
    # Duration: 300s
    # related: [文理勇气](Status1646),
    id = 12997
    names = ['Bravery L(CMN)', '文理勇气(CMN)']
    _orig_names = ['Bravery L', '文理勇气']
    # remain metas: {'dmg_increase': '10%'}


class Action12998(Action):
    # 一定时间内，自身受到的物理伤害减轻99%
    # 持续时间：8秒
    # Reduces physical damage taken by 99%.
    # Duration: 8s
    id = 12998
    names = ['Solid Shield L(CMN)', '文理物理盾(CMN)']
    _orig_names = ['Solid Shield L', '文理物理盾']
    # remain metas: {'taken_dmg_reduce': '99%'}


class Action12999(Action):
    # 一定时间内，自身受到的魔法伤害减轻99%
    # 持续时间：8秒
    # Reduces magic damage taken by 99%.
    # Duration: 8s
    id = 12999
    names = ['文理魔法盾(CMN)', 'Spell Shield L(CMN)']
    _orig_names = ['文理魔法盾', 'Spell Shield L']
    # remain metas: {'taken_dmg_reduce': '99%'}


class Action13000(Action):
    # 为自身或其他一名队员附加能够反射魔法的防护罩
    # 持续时间：10秒
    # Creates a magic-reflecting barrier around self or party member.
    # Duration: 10s
    # related: [文理反射](Status1649),
    id = 13000
    names = ['Reflect L(CMN)', '文理反射(CMN)']
    _orig_names = ['文理反射', 'Reflect L']


class Action13001(Action):
    # 对目标发动物理攻击
    # 威力：1000
    # 追加效果：恢复伤害量一定比例的体力
    # 发动条件：自身体力低于50%
    # Delivers an attack with a potency of 1,000.
    # Can only be executed when your HP is below 50%.
    # Additional Effect: Restores an amount of own HP proportional to damage dealt
    id = 13001
    names = ['文理猛击(CMN)', 'Smite L(CMN)']
    _orig_names = ['Smite L', '文理猛击']
    damage = 1000


class Action13002(Action):
    # 一定时间内，自身与周围队员的魔素以太恢复量提高
    # 持续时间：30秒
    #
    # Increases the amount of magia aether regenerated over time by self and nearby party members.
    # Duration: 30s
    # related: [文理醒神](Status1651),
    id = 13002
    names = ['文理醒神(CMN)', 'Refresh L(CMN)']
    _orig_names = ['Refresh L', '文理醒神']


class Action13003(Action):
    # 对目标发动无属性魔法攻击
    # 威力：200
    # 目标为不死系怪物时发动追加效果
    # 追加效果：目标所受伤害提高25%
    # 持续时间：60秒
    # Deals unaspected damage with a potency of 200.
    # Additional Effect: Afflicts undead targets with Banish L, increasing damage taken by 25%
    # Duration: 60s
    # related: [文理放逐](Status1655),
    id = 13003
    names = ['文理放逐(CMN)', 'Banish L(CMN)']
    _orig_names = ['文理放逐', 'Banish L']
    damage = 200
    # remain metas: {'taken_dmg_increase': '25%'}


class Action13004(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：150
    # 目标为不死系怪物时发动追加效果
    # 追加效果：目标所受伤害提高25%
    # 持续时间：60秒
    # Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
    # Additional Effect: Afflicts undead targets with Banish L, increasing damage taken by 25%
    # Duration: 60s
    id = 13004
    names = ['文理强放逐(CMN)', 'Banish L III(CMN)']
    _orig_names = ['文理强放逐', 'Banish L III']
    damage = 150
    # remain metas: {'taken_dmg_increase': '25%'}


class Action13005(Action):
    # 一定时间内，以自身消耗的魔力增加为代价，令魔法类技能攻击时造成的伤害提高100%
    # 持续时间：20秒
    # Increases spell damage by 100% while increasing MP cost.
    # Duration: 20s
    id = 13005
    names = ['Magic Burst L(CMN)', '文理魔法爆发(CMN)']
    _orig_names = ['文理魔法爆发', 'Magic Burst L']
    # remain metas: {'dmg_increase': '100%'}


class Action13006(Action):
    # 一定时间内，以自身体力逐渐流失为代价，令发动物理攻击造成的伤害提高
    # 持续时间：48秒
    # 该状态每3秒增加1档，最多可以积累16档
    # 每档可以令物理伤害提高15%、令体力流失增加360点
    # Increases physical damage dealt while dealing damage to self over time.
    # Stacks increase every 3 seconds, up to a maximum of 16. For each stack, physical damage dealt is increased by 15%, and potency of damage dealt to self increases by 360.
    # Duration: 48s
    # related: [文理双刃剑](Status1653),
    id = 13006
    names = ['Double Edge L(CMN)', '文理双刃剑(CMN)']
    _orig_names = ['Double Edge L', '文理双刃剑']
    # remain metas: {'dmg_increase': ['', '15%、令体力流失增加360点']}


class Action13007(Action):
    # 对目标发动远距离物理攻击
    # 威力：80
    # 目标剩余体力越低威力越大，最大提升到10倍
    # 该技能拥有高仇恨提升率
    # Delivers a ranged attack with a potency of 80. Potency increases up to 1,000% the lower the target's HP.
    # Generates significant enmity upon use.
    id = 13007
    names = ['文理锐眼追击(CMN)', 'Eagle Eye Shot L(CMN)']
    _orig_names = ['Eagle Eye Shot L', '文理锐眼追击']
    damage = 80


class Action13265(Action):
    # 对指定地点施放魔法吓人
    # Casts a spell that alarms targets within the designated area.
    id = 13265
    names = ['Tricksome Treat(CMN)', '不给糖就捣蛋(CMN)']
    _orig_names = ['不给糖就捣蛋', 'Tricksome Treat']


class Action13266(Action):
    # 解除变身状态
    # Removes the effects of transfiguration.
    # related: [变身(0)](Status705), [变身(1)](Status2727), [变身(2)](Status1448), [变身(3)](Status1608), [变身(4)](Status1609), [变身(5)](Status1423), [变身(6)](Status1459), [变身(7)](Status2548), [变身(8)](Status565), [变身(9)](Status1433),
    id = 13266
    names = ['解除变身(CMN)', 'Unveil(CMN)']
    _orig_names = ['Unveil', '解除变身']


class Action13423(Action):
    # 对目标发动土属性魔法攻击
    # 威力：140
    # Deals earth damage with a potency of 140.
    id = 13423
    names = ['血盟崩石(CMN)', 'Stone IV of the Seventh Dawn(CMN)']
    _orig_names = ['血盟崩石', 'Stone IV of the Seventh Dawn']
    damage = 140


class Action13424(Action):
    # 对目标发动风属性魔法攻击
    # 威力：50
    # 追加效果：风属性持续伤害
    # 威力：30
    # 持续时间：18秒
    # Deals wind damage with a potency of 50.
    # Additional Effect: Wind damage over time
    # Potency: 30
    # Duration: 18s
    id = 13424
    names = ['Aero II of the Seventh Dawn(CMN)', '血盟烈风(CMN)']
    _orig_names = ['血盟烈风', 'Aero II of the Seventh Dawn']
    damage = 50
    # remain metas: {'dmg_ot': '30'}


class Action13425(Action):
    # 恢复目标的体力
    # 恢复力：700
    # Restores target's HP.
    # Cure Potency: 700
    id = 13425
    names = ['血盟救疗(CMN)', 'Cure II of the Seventh Dawn(CMN)']
    _orig_names = ['血盟救疗', 'Cure II of the Seventh Dawn']
    heal = 700


class Action13426(Action):
    # 恢复自身魔力
    # Restores MP.
    id = 13426
    names = ['补魔(CMN)', 'Aetherwell(CMN)']
    _orig_names = ['Aetherwell', '补魔']


class Action14414(Action):
    # 使用幻影圣剑对自身正面发动攻击
    # Wield the ethereal sword to strike forward.
    id = 14414
    names = ['Heavenly Sword(CMN)', '圣剑攻击(CMN)']
    _orig_names = ['圣剑攻击', 'Heavenly Sword']


class Action14415(Action):
    # 使用幻影圣盾对正面攻击进行防御
    # Wield the ethereal shield to defend against frontal attacks.
    # related: [圣盾防御](Status1735),
    id = 14415
    names = ['Heavenly Shield(CMN)', '圣盾防御(CMN)']
    _orig_names = ['Heavenly Shield', '圣盾防御']


class Action14476(Action):
    # 发现自身周围15米内隐藏的陷阱
    # 若周围15米内没有陷阱，则可以获知周围36米内是否存在陷阱
    # 此文理技能仅在迷宫内有效
    # Reveals all traps within a 15-yalm radius. If no traps exist within 15 yalms, detects whether any traps are present within a 36-yalm radius.
    # Only effective within dungeons.
    id = 14476
    names = ['Perception L(CMN)', '文理探景(CMN)']
    _orig_names = ['Perception L', '文理探景']


class Action14477(Action):
    # 令自身发动魔法攻击造成的伤害提高35%，魔法防御力增加1000，并且发动魔法消耗的魔力降低
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases magic damage dealt by 35% and magic defense by 1,000, while decreasing spell MP cost.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 14477
    names = ['Wisdom of the Elder(CMN)', '贤者的记忆(CMN)']
    _orig_names = ['贤者的记忆', 'Wisdom of the Elder']
    # remain metas: {'dmg_increase': '35%，魔法防御力增加1000，并且发动魔法消耗的魔力降低'}


class Action14478(Action):
    # 令自身发动物理攻击造成的伤害提高40%，最大体力增加15%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases physical damage dealt by 40% and maximum HP by 15%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 14478
    names = ['剑豪的记忆(CMN)', 'Wisdom of the Duelist(CMN)']
    _orig_names = ['Wisdom of the Duelist', '剑豪的记忆']
    # remain metas: {'dmg_increase': '40%，最大体力增加15%'}


class Action14479(Action):
    # 令自身的发动物理时造成的伤害提高25%，并且回避率提高25%
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases physical damage dealt by 25% and evasion by 25%.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 14479
    names = ['Wisdom of the Fiendhunter(CMN)', '弓圣的记忆(CMN)']
    _orig_names = ['弓圣的记忆', 'Wisdom of the Fiendhunter']
    # remain metas: {'dmg_increase': '25%，并且回避率提高25%'}


class Action14480(Action):
    # 令自身的防御力提高2000
    # 效果时间内每次受到超过自身最大体力50%以上的单体攻击伤害时，获得1档体力增加
    # 无法与其他“记忆”系技能同时使用
    # 切换任务指令时消失
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Increases defense by 2,000.
    # Grants one stack of HP Boost each time damage equal to or greater than half of maximum HP is taken from a single-target attack.
    # Cannot be used with other Wisdom abilities.
    # Effect ends upon reuse or upon replacement of duty action.
    id = 14480
    names = ['豪杰的记忆(CMN)', 'Wisdom of the Indomitable(CMN)']
    _orig_names = ['Wisdom of the Indomitable', '豪杰的记忆']


class Action14481(Action):
    # 复活目标并恢复其全部体力
    # 追加效果：对自己附加“献祭”
    # 持续时间：10秒
    # 献祭效果：持续时间结束后自身将陷入无法战斗的状态
    # 发动条件：非“献祭”状态中
    # Restores all of a KO'd target's HP.
    # Cannot be executed if currently afflicted with Sacrifice.
    # Additional Effect: Inflicts Sacrifice on self
    # Sacrifice Effect: When effect expires, you will be KO'd
    # Duration: 10s
    # related: [献祭](Status1743),
    id = 14481
    names = ['文理献祭(CMN)', 'Sacrifice L(CMN)']
    _orig_names = ['文理献祭', 'Sacrifice L']


class Action14597(Action):
    # 瞬移接近目标并发动物理攻击
    # 发动时距离目标越远威力越高
    # Move instantly to the target while delivering a physical attack. Potency increases with initial distance from target.
    id = 14597
    names = ['位移破击(CMN)', 'Warp-strike(CMN)']
    _orig_names = ['Warp-strike', '位移破击']


class Action14840(Action):
    # 对目标发动物理攻击
    # 威力：180
    # Delivers an attack with a potency of 180.
    id = 14840
    names = ['Kyokufu(CMN)', '极风(CMN)']
    _orig_names = ['极风', 'Kyokufu']
    damage = 180


class Action14841(Action):
    # 对目标发动物理攻击
    # 威力：100
    # 追加效果：持续伤害
    # 威力：30
    # 持续时间：30秒
    # Delivers an attack with a potency of 100.
    # Additional Effect: Damage over time
    # Potency: 30
    # Duration: 30s
    # related: [紫阳花](Status1779),
    id = 14841
    names = ['紫阳花(CMN)', 'Ajisai(CMN)']
    _orig_names = ['紫阳花', 'Ajisai']
    damage = 100
    # remain metas: {'dmg_ot': '30'}


class Action14842(Action):
    # 冲向目标并发动物理攻击
    # 威力：100
    # Rushes target and delivers an attack with a potency of 100.
    id = 14842
    names = ['必杀剑·晓天(CMN)', 'Hissatsu: Gyoten(CMN)']
    _orig_names = ['必杀剑·晓天', 'Hissatsu: Gyoten']
    damage = 100


class Action15375(Action):
    # 恢复自身体力
    # 恢复力：(level>=32?(job==2?650:(job==20?650:450)):450)
    # 恢复力与当前物理攻击力相关
    # Instantly restores own HP.
    # Cure Potency: 500
    # Cure potency varies with current attack power.
    id = 15375
    names = ['Second Wind(CMN)(1)', '内丹(CMN)(1)']
    _orig_names = ['Second Wind', '内丹']
    heal = "(lv>=32?(job==2?650:(job==20?650:450)):450)"


class Action15537(Action):
    # 中断目标的技能咏唱
    # Interrupts the use of a target's action.
    id = 15537
    names = ['插言(CMN)(1)', 'Interject(CMN)(1)']
    _orig_names = ['Interject(1)', '插言(1)']


class Action15553(Action):
    # 派发装饰彩蛋
    # Present an eggsquisite gift.
    id = 15553
    names = ['发礼物(CMN)', 'Present(CMN)']
    _orig_names = ['发礼物', 'Present']


class Action15870(Action):
    # 一定时间内，自身发动物理攻击造成的伤害提高25%
    # 持续时间：25秒
    # Increases physical damage dealt by 25%.
    # Duration: 25s
    # related: [战逃反应](Status76),
    id = 15870
    names = ['战逃反应(CMN)(0)', 'Fight or Flight(CMN)(0)']
    _orig_names = ['战逃反应(CMN)', 'Fight or Flight(CMN)']
    # remain metas: {'dmg_increase': '25%'}


class Action16436(Action):
    # 产自水晶都的特殊恢复药，可以恢复体力
    # Instantly restores own HP via the consumption of a curious Crystarium concoction.
    id = 16436
    names = ['镇痛恢复药(CMN)', 'Soothing Potion(CMN)']
    _orig_names = ['Soothing Potion', '镇痛恢复药']


class Action16437(Action):
    # 使用敏菲利亚准备的晶壤，对目标释放光之斩击
    # Harnesses the power of one of Minfilia's cartridges to lacerate the target with pure light.
    id = 16437
    names = ['光明之刃(CMN)', 'Shining Blade(CMN)']
    _orig_names = ['Shining Blade', '光明之刃']


class Action16438(Action):
    # 绞锁自身命脉，完全切断气息
    # 对自身附加“命脉负荷”状态
    # Completely conceals own presence by severely restricting the flow of life-sustaining aether.
    # Additional Effect: Fading Fast
    # related: [完美隐形](Status1906), [命脉负荷](Status1859),
    id = 16438
    names = ['完美隐形(CMN)', 'Perfect Deception(CMN)']
    _orig_names = ['Perfect Deception', '完美隐形']


class Action16439(Action):
    # 使用敏菲利亚精心灌注魔力的晶壤释放连续斩击
    # Harnesses the mysterious power of Minfilia's experimental cartridge to deliver a powerful onslaught.
    id = 16439
    names = ['Leap of Faith(CMN)', '晶壤光斩(CMN)']
    _orig_names = ['Leap of Faith', '晶壤光斩']


class Action16560(Action):
    # 令目标陷入睡眠状态
    # 持续时间：30秒
    # 发动之后会停止自动攻击
    # Afflicts target with Sleep.
    # Duration: 30s
    # Cancels auto-attack upon execution.
    id = 16560
    names = ['沉静(CMN)', 'Repose(CMN)']
    _orig_names = ['Repose', '沉静']


class Action16574(Action):
    # 对目标发动火属性魔法攻击
    # 威力：430
    # Deals fire damage with a potency of 430.
    id = 16574
    names = ['隆卡爆炎(CMN)', 'Ronkan Fire III(CMN)']
    _orig_names = ['隆卡爆炎', 'Ronkan Fire III']
    damage = 430


class Action16575(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：240
    # 追加效果：恢复自身魔力
    # Deals ice damage with a potency of 240.
    # Additional Effect: Restores MP
    id = 16575
    names = ['隆卡冰封(CMN)', 'Ronkan Blizzard III(CMN)']
    _orig_names = ['隆卡冰封', 'Ronkan Blizzard III']
    damage = 240


class Action16576(Action):
    # 对目标发动雷属性魔法攻击
    # 威力：200
    # 追加效果：雷属性持续伤害
    # 威力：40
    # 持续时间：24秒
    # Deals lightning damage with a potency of 200.
    # Additional Effect: Lightning damage over time
    # Potency: 40
    # Duration: 24s
    id = 16576
    names = ['Ronkan Thunder III(CMN)', '隆卡暴雷(CMN)']
    _orig_names = ['隆卡暴雷', 'Ronkan Thunder III']
    damage = 200
    # remain metas: {'dmg_ot': '40'}


class Action16577(Action):
    # 对目标及其周围的敌人发动火属性范围魔法攻击
    # 威力：460
    # Deals fire damage with a potency of 460 to target and all enemies nearby it.
    id = 16577
    names = ['Ronkan Flare(CMN)', '隆卡核爆(CMN)']
    _orig_names = ['Ronkan Flare', '隆卡核爆']
    damage = 460


class Action16578(Action):
    # 对指定地点发动范围无属性魔法攻击
    # 威力：1500
    # Deals unaspected damage with a potency of 1,500 to all enemies near point of impact.
    id = 16578
    names = ['坠星(CMN)', 'Falling Star(CMN)']
    _orig_names = ['Falling Star', '坠星']
    damage = 1500


class Action16804(Action):
    # 跃向目标并发动物理攻击
    # 威力：200
    # 积蓄次数：2
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 200.
    # Maximum Charges: 2
    # Cannot be executed while bound.
    id = 16804
    names = ['粗分斩(CMN)', 'Rough Divide(CMN)']
    _orig_names = ['Rough Divide(CMN)', '粗分斩(CMN)']
    damage = 200


class Action17000(Action):
    # 恢复目标的体力
    # 恢复力：1300
    # Restores target's HP.
    # Cure Potency: 1300
    id = 17000
    names = ['Ronkan Cure II(CMN)', '隆卡救疗(CMN)']
    _orig_names = ['隆卡救疗', 'Ronkan Cure II']
    heal = 1300


class Action17001(Action):
    # 恢复自身及周围队员的体力
    # 恢复力：500
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 500
    id = 17001
    names = ['隆卡医治(CMN)', 'Ronkan Medica(CMN)']
    _orig_names = ['Ronkan Medica', '隆卡医治']
    heal = 500


class Action17002(Action):
    # 解除目标身上部分弱化效果中的一种
    # Removes a single detrimental effect from target.
    id = 17002
    names = ['Ronkan Esuna(CMN)', '隆卡康复(CMN)']
    _orig_names = ['隆卡康复', 'Ronkan Esuna']


class Action17003(Action):
    # 对目标发动土属性魔法攻击
    # 威力：200
    # Deals earth damage with a potency of 200.
    id = 17003
    names = ['隆卡坚石(CMN)', 'Ronkan Stone II(CMN)']
    _orig_names = ['Ronkan Stone II', '隆卡坚石']
    damage = 200


class Action17004(Action):
    # 令目标体力完全恢复
    # Restores all of a target's HP.
    id = 17004
    names = ['Ronkan Renew(CMN)', '隆卡痊愈(CMN)']
    _orig_names = ['隆卡痊愈', 'Ronkan Renew']


class Action17122(Action):
    # 对目标发动物理攻击
    # 威力：300
    # 追加效果：中毒
    # 威力：120
    # 持续时间：30秒
    # Delivers an attack with a potency of 300.
    # Additional Effect: Acidic Bite
    # Potency: 120
    # Duration: 30s
    # related: [中毒(0)](Status801), [中毒(1)](Status2089), [中毒(2)](Status686), [中毒(3)](Status559), [中毒(4)](Status560), [中毒(5)](Status18), [中毒(6)](Status275), [中毒(7)](Status2104), [酸咬箭](Status2073),
    id = 17122
    names = ['Acidic Bite(CMN)', '酸咬箭(CMN)']
    _orig_names = ['酸咬箭', 'Acidic Bite']
    damage = 300  # TODO: [300, 120]


class Action17123(Action):
    # 对目标发动物理攻击
    # 威力：550
    # Delivers an attack with a potency of 550.
    id = 17123
    names = ['强力射击(CMN)', 'Heavy Shot(CMN)']
    _orig_names = ['Heavy Shot(CMN)', '强力射击(CMN)']
    damage = 550


class Action17124(Action):
    # 对目标发动物理攻击
    # 威力：1100
    # Delivers an attack with a potency of 1,100.
    id = 17124
    names = ['Radiant Arrow(CMN)', '星光箭(CMN)']
    _orig_names = ['星光箭', 'Radiant Arrow']
    damage = 1100


class Action17125(Action):
    # 中断目标的技能咏唱
    # Interrupts the use of a target's action.
    id = 17125
    names = ['Dulling Arrow(CMN)', '消声箭(CMN)']
    _orig_names = ['Dulling Arrow', '消声箭']


class Action17236(Action):
    # 恢复目标的体力
    # 恢复力：1200
    # 追加效果：对小队队员发动该技能时，自身恢复目标所恢复体力的一半
    # Restores target's HP.
    # Cure Potency: 1200
    # Additional Effect: Restores to self 50% of HP restored to target if target is a party member
    id = 17236
    names = ['Chivalrous Spirit(CMN)', '骑士精神(CMN)']
    _orig_names = ['Chivalrous Spirit', '骑士精神']
    heal = 1200


class Action17291(Action):
    # 暂时断开自身命脉，完全切断气息
    # 对自身附加“命脉负荷”和“生命活动停滞”状态
    # Completely conceals own presence by temporarily severing the flow of life-sustaining aether.
    # Additional Effect: Fading Fast and Vital Sign
    # related: [命脉负荷](Status1859), [绝脉隐形](Status1956), [生命活动停滞](Status1860),
    id = 17291
    names = ['绝脉隐形(CMN)', 'Souldeep Invisibility(CMN)']
    _orig_names = ['Souldeep Invisibility', '绝脉隐形']


class Action17390(Action):
    # 释放有点可怕又不可怕的发光视线
    # Fix your enemies with a gaze that won't quite strike fear into their hearts, but will certainly make them feel uncomfortable.
    id = 17390
    names = ['Sort-of Dread Gaze(CMN)(0)', '恐怖视线？(CMN)(0)']
    _orig_names = ['恐怖视线？', 'Sort-of Dread Gaze']


class Action17391(Action):
    # 释放有点可怕又不可怕的发光视线
    # 演出技能，没有任何实际效果
    # Fix your enemies with a gaze that won't quite strike fear into their hearts, but will certainly make them feel uncomfortable.
    # ※Has no effect in battle.
    id = 17391
    names = ['恐怖视线？(CMN)(1)', 'Sort-of Dread Gaze(CMN)(1)']
    _orig_names = ['恐怖视线？', 'Sort-of Dread Gaze']


class Action17596(Action):
    # 恢复自身体力
    # 恢复力：1000
    # 恢复力与当前物理攻击力相关
    # Restores own HP.
    # Cure Potency: 1,000
    # Cure potency varies with current attack power.
    id = 17596
    names = ["Hunter's Prudence(CMN)", '猎人的智慧(CMN)']
    _orig_names = ["Hunter's Prudence", '猎人的智慧']
    heal = 1000


class Action17669(Action):
    # 对目标发动物理攻击
    # 威力：600
    # 追加效果：眩晕
    # 持续时间：2秒
    # Delivers an attack with a potency of 600.
    # Additional Effect: Stun
    # Duration: 2s
    id = 17669
    names = ['下踢(pvp)(CMN)', 'Low Blow(pvp)(CMN)']
    _orig_names = ['下踢(pvp)', 'Low Blow(pvp)']
    damage = 600


class Action17671(Action):
    # 对目标发动物理攻击
    # 威力：1200
    # 追加效果：将目标击退15米
    # Delivers an attack with a potency of 1,200.
    # Additional Effect: 15-yalm knockback
    # related: [全力挥打](Status1977),
    id = 17671
    names = ['Full Swing(pvp)(CMN)', '全力挥打(pvp)(CMN)']
    _orig_names = ['全力挥打(pvp)', 'Full Swing(pvp)']
    damage = 1200


class Action17672(Action):
    # 将自身所受的伤害减轻20%
    # 持续时间：10秒
    # Reduces damage taken by 20%.
    # Duration: 10s
    # related: [铁壁(1)](Status71), [铁壁(0)](Status1191), [铁壁(2)](Status1978),
    id = 17672
    names = ['Rampart(pvp)(CMN)', '铁壁(pvp)(CMN)']
    _orig_names = ['铁壁(pvp)', 'Rampart(pvp)']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action17674(Action):
    # 向身后跳出10米距离
    # 止步状态下无法发动
    # Jump 10 yalms back from current position.
    # Cannot be executed while bound.
    id = 17674
    names = ['后闪(pvp)(CMN)', 'Backstep(pvp)(CMN)']
    _orig_names = ['后闪(pvp)', 'Backstep(pvp)']


class Action17676(Action):
    # 将物理攻击所造成伤害的100%转化为自身的体力
    # 持续时间：6秒
    # Converts 100% of physical damage dealt into HP.
    # Duration: 6s
    # related: [浴血(0)](Status84), [浴血(1)](Status1982),
    id = 17676
    names = ['Bloodbath(pvp)(CMN)', '浴血(pvp)(CMN)']
    _orig_names = ['浴血(pvp)', 'Bloodbath(pvp)']


class Action17677(Action):
    # 令以自身为目标的眩晕、睡眠、止步、加重、沉默、击退、吸引的效果无效
    # 持续时间：10秒
    # Grants immunity to Stun, Sleep, Bind, Heavy, Silence, and knockback and draw-in effects.
    # Duration: 10s
    # related: [沉默(0)](Status1347), [沉默(1)](Status1060), [沉默(2)](Status7), [隔离罩](Status1983),
    id = 17677
    names = ['隔离罩(pvp)(CMN)', 'Fetter Ward(pvp)(CMN)']
    _orig_names = ['隔离罩(pvp)', 'Fetter Ward(pvp)']


class Action17678(Action):
    # 令目标陷入50%加重状态
    # 持续时间：5秒
    # Afflicts target with Heavy +50%.
    # Duration: 5s
    id = 17678
    names = ['伤腿(pvp)(CMN)', 'Leg Graze(pvp)(CMN)']
    _orig_names = ['伤腿(pvp)', 'Leg Graze(pvp)']


class Action17679(Action):
    # 对目标造成止步效果
    # 持续时间：3秒
    # Binds target.
    # Duration: 3s
    id = 17679
    names = ['伤足(pvp)(CMN)', 'Foot Graze(pvp)(CMN)']
    _orig_names = ['Foot Graze(pvp)', '伤足(pvp)']


class Action17680(Action):
    # 令目标陷入沉默状态
    # 持续时间：2秒
    # Silences target.
    # Duration: 2s
    # related: [沉默(0)](Status1347), [沉默(1)](Status1060), [沉默(2)](Status7),
    id = 17680
    names = ['Head Graze(pvp)(CMN)', '伤头(pvp)(CMN)']
    _orig_names = ['Head Graze(pvp)', '伤头(pvp)']


class Action17681(Action):
    # 令自身所受的伤害减轻10%，并在以自身受到攻击时发动反击
    # 持续时间：6秒
    # 反击效果：使敌人发动攻击所造成的伤害降低10%
    # 持续时间：6秒
    #
    # Reduces damage taken by 10%.
    # Duration: 6s
    # Additional Effect: When you are struck, the striker's damage dealt will be reduced by 10%
    # Duration: 6s
    # related: [亲疏自行(0)](Status1984), [亲疏自行(1)](Status2181), [反击](Status519), [亲疏自行(2)](Status1209), [亲疏自行(3)](Status2172),
    id = 17681
    names = ['亲疏自行(pvp)(CMN)', "Arm's Length(pvp)(CMN)"]
    _orig_names = ["Arm's Length(pvp)", '亲疏自行(pvp)']
    # remain metas: {'taken_dmg_reduce': '10%，并在以自身受到攻击时发动反击', 'dmg_reduce': '10%'}


class Action17682(Action):
    # 提高自身和周围队员的移动速度
    # 持续时间：10秒
    # Increases movement speed of self and nearby party members.
    # Duration: 10s
    # related: [速行(0)](Status1985), [速行(1)](Status1199),
    id = 17682
    names = ['Peloton(pvp)(CMN)', '速行(pvp)(CMN)']
    _orig_names = ['速行(pvp)', 'Peloton(pvp)']


class Action17683(Action):
    # 对目标发动魔法攻击
    # 威力：600～2400
    # 自身剩余体力越少威力越大
    # 追加效果：恢复伤害量2倍的体力
    # Deals unaspected damage with a potency of 600.
    # Potency increases up to 2,400 as your HP decreases.
    # Additional Effect: Absorbs 200% of damage dealt as HP
    id = 17683
    names = ['Drain(pvp)(CMN)', '吸取(pvp)(CMN)']
    _orig_names = ['Drain(pvp)', '吸取(pvp)']
    damage = [600, 2400]


class Action17684(Action):
    # 对目标发动魔法攻击
    # 威力：1000
    # 追加效果：目标所受伤害提高20%
    # 持续时间：6秒
    # Deals unaspected damage with a potency of 1,000.
    # Additional Effect: Increases target's damage taken by 20%
    # Duration: 6s
    # related: [幻影弹](Status1986),
    id = 17684
    names = ['幻影弹(pvp)(CMN)', 'Phantom Dart(pvp)(CMN)']
    _orig_names = ['幻影弹(pvp)', 'Phantom Dart(pvp)']
    damage = 1000
    # remain metas: {'taken_dmg_increase': '20%'}


class Action17685(Action):
    # 下次咏唱的魔法没有任何咏唱时间
    # 持续时间：5秒
    # Next spell is cast immediately.
    # Duration: 5s
    # related: [即刻咏唱(0)](Status1987), [即刻咏唱(1)](Status167), [即刻咏唱(2)](Status1325),
    id = 17685
    names = ['Swiftcast(pvp)(CMN)', '即刻咏唱(pvp)(CMN)']
    _orig_names = ['Swiftcast(pvp)', '即刻咏唱(pvp)']


class Action17686(Action):
    # 目标的攻击伤害降低40%
    # 持续时间：6秒
    # Reduces the potency of target's attacks by 40%.
    # Duration: 6s
    # related: [昏乱(0)](Status1203), [昏乱(1)](Status1988),
    id = 17686
    names = ['Addle(pvp)(CMN)', '昏乱(pvp)(CMN)']
    _orig_names = ['昏乱(pvp)', 'Addle(pvp)']
    # remain metas: {'dmg_reduce': '40%'}


class Action17687(Action):
    # 为自身张开一个防护罩，能抵消相当于恢复力2500的伤害量
    # 持续时间：10秒
    # 防护罩因吸收到足够的伤害而消失时，恢复自身2500点魔力
    # Creates a barrier around self that absorbs damage equivalent to a heal of 2,500 potency.
    # Duration: 10s
    # Additional Effect: Restores 2,500 MP when barrier is completely absorbed
    # related: [魔罩(0)](Status168), [魔罩(1)](Status1989),
    id = 17687
    names = ['魔罩(pvp)(CMN)', 'Manaward(pvp)(CMN)']
    _orig_names = ['Manaward(pvp)', '魔罩(pvp)']
    # remain metas: {'shield': '恢复力2500'}


class Action17688(Action):
    # 将目标队员吸引到自己身边
    # 目标带有击退无效及部分弱化效果时无效
    # 追加效果：解除目标的死斗状态
    # Instantly draws target party member to your side.
    # Additional Effect: Removes Holmgang effect from target
    # Ignores target's knockback resistance.
    # related: [死斗(2)](Status88), [死斗(3)](Status409), [死斗(1)](Status1305), [死斗(0)](Status1304),
    id = 17688
    names = ['Rescue(pvp)(CMN)', '营救(pvp)(CMN)']
    _orig_names = ['营救(pvp)', 'Rescue(pvp)']


class Action17689(Action):
    # 恢复自身体力
    # 恢复力：3000～6000
    # 自身剩余体力越少恢复力越高
    # 追加效果：以无法移动或行动为代价，令自身所受的伤害减轻99%
    # 持续时间：3秒
    # Restores own HP.
    # Cure Potency: 3,000
    # Potency increases up to 6,000 as your HP decreases.
    # Additional Effect: Nullifies 99% of damage taken but prevents movement or use of other actions
    # Duration: 3s
    # related: [平衡](Status1990),
    id = 17689
    names = ['平衡(pvp)(CMN)', 'Attunement(pvp)(CMN)']
    _orig_names = ['平衡(pvp)', 'Attunement(pvp)']
    heal = [3000, 6000]
    # remain metas: {'taken_dmg_reduce': '99%'}


class Action17690(Action):
    # 令目标陷入睡眠状态
    # 持续时间：3秒
    # Afflicts target with Sleep.
    # Duration: 3s
    id = 17690
    names = ['沉静(pvp)(CMN)', 'Repose(pvp)(CMN)']
    _orig_names = ['沉静(pvp)', 'Repose(pvp)']


class Action17832(Action):
    # 令自身或其他一名队员所受到的伤害减轻20%
    # 持续时间：10秒
    # Reduces damage taken by a party member or self by 20%.
    # Duration: 10s
    # related: [护盾(0)](Status417), [护盾(1)](Status2053), [护盾(2)](Status1415), [护盾(3)](Status146), [护盾(4)](Status147),
    id = 17832
    names = ['护盾(pvp)(CMN)', 'Protect(pvp)(CMN)']
    _orig_names = ['Protect(pvp)', '护盾(pvp)']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action17839(Action):
    # 一定时间内，将自身所受的伤害减轻25%
    # 持续时间：10秒
    # Reduces damage taken by 25%.
    # Duration: 10s
    # related: [星云](Status1834),
    id = 17839
    names = ['Nebula(CMN)(0)', '星云(CMN)(0)']
    _orig_names = ['星云', 'Nebula']
    # remain metas: {'taken_dmg_reduce': '25%'}


class Action17866(Action):
    # 使自身周围的敌人攻击伤害降低20%
    # 持续时间：10秒
    # Reduces damage dealt by nearby enemies by 20%.
    # Duration: 10s
    # related: [雪仇剑(0)](Status753), [雪仇](Status1193), [雪仇剑(1)](Status2101),
    id = 17866
    names = ['雪仇(pvp)(CMN)', 'Reprisal(pvp)(CMN)']
    _orig_names = ['Reprisal(pvp)', '雪仇(pvp)']
    # remain metas: {'dmg_reduce': '20%'}


class Action17901(Action):
    # 一定时间内，自身发动攻击造成的伤害提高10%，命中率提高100%
    # 持续时间：10秒
    # Increases damage dealt by 10% and accuracy by 100%.
    # Duration: 10s
    # related: [折服](Status2068),
    id = 17901
    names = ['Smackdown(CMN)', '折服(CMN)']
    _orig_names = ['折服', 'Smackdown']
    # remain metas: {'dmg_increase': '10%，命中率提高100%'}


class Action18187(Action):
    # 用超强的吸力将东西吸入
    # Sucks up any substance with a great huffing snort.
    id = 18187
    names = ['Siphon Snout(CMN)(0)', '鼻吸(CMN)(0)']
    _orig_names = ['鼻吸', 'Siphon Snout']


class Action18188(Action):
    # 用超强的吸力将东西吸入
    # 演出技能，没有任何实际效果
    # Sucks up any substance with a great huffing snort.
    # ※Has no effect in battle.
    id = 18188
    names = ['鼻吸(CMN)(1)', 'Siphon Snout(CMN)(1)']
    _orig_names = ['鼻吸', 'Siphon Snout']


class Action18775(Action):
    # 跳起接近目标并发动火属性范围攻击
    # 威力：800
    # Delivers a jumping fire-based attack with a potency of 800 to target and all enemies nearby it.
    id = 18775
    names = ['苍天龙炎冲(CMN)', 'Skydragon Dive(CMN)']
    _orig_names = ['苍天龙炎冲', 'Skydragon Dive']
    damage = 800


class Action18776(Action):
    # 对目标发动物理攻击
    # 威力：3000
    # 追加效果：恢复伤害量一定比例的体力
    # Delivers an attack with a potency of 3,000.
    # Additional Effect: Absorbs a portion of damage dealt as HP
    id = 18776
    names = ['绝灭(CMN)', 'Ala Morn(CMN)']
    _orig_names = ['绝灭', 'Ala Morn']
    damage = 3000


class Action18777(Action):
    # 对目标发动物理攻击
    # 威力：500
    # 追加效果：持续伤害
    # 持续时间：15秒
    # Delivers an attack with a potency of 500.
    # Additional Effect: Damage over time
    # Duration: 15s
    id = 18777
    names = ['腾龙枪(CMN)', 'Drachenlance(CMN)']
    _orig_names = ['Drachenlance', '腾龙枪']
    damage = 500


class Action18778(Action):
    # 对自身周围的敌人以及敌人周围的敌人发动无属性范围魔法攻击
    # 威力：600
    # 该战技有单独计算的复唱时间
    # Delivers an attack with a potency of 600 to all nearby enemies, as well as enemies in proximity to those initially affected.
    # This action does not share a recast timer with any other actions.
    id = 18778
    names = ['Horrid Roar(CMN)', '恐惧咆哮(CMN)']
    _orig_names = ['恐惧咆哮', 'Horrid Roar']
    damage = 600


class Action18780(Action):
    # 跳起接近目标并发动火属性范围物理攻击
    # 威力：1500
    # 攻击复数敌人时，对目标之外的敌人威力降低30%
    # Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 1,500 for the first enemy, and 30% less for all remaining enemies.
    id = 18780
    names = ['Stardiver(CMN)', '坠星冲(CMN)']
    _orig_names = ['Stardiver', '坠星冲']
    damage = 1500
    # remain metas: {'aoe_reduce': '30%'}


class Action18781(Action):
    # 解放魔枪尼德霍格的力量发动攻击
    # Delivers an attack to target and all enemies nearby it.
    id = 18781
    names = ['Dragonshadow Dive(CMN)', '暗影龙炎冲(CMN)']
    _orig_names = ['暗影龙炎冲', 'Dragonshadow Dive']


class Action18813(Action):
    # 指示艾泽尔二世吸入所选恶梦之雾
    # Direct Ezel II to devour a dream.
    id = 18813
    names = ['鼻吸指示(CMN)', 'Solicit Siphon Snout(CMN)']
    _orig_names = ['Solicit Siphon Snout', '鼻吸指示']


class Action18863(Action):
    # 破坏吉祥天女释放的以太晶球
    # Scatters potentially harmful aether.
    id = 18863
    names = ['偏折屏障(CMN)(1)', 'Deflect(CMN)(1)']
    _orig_names = ['偏折屏障', 'Deflect']


class Action18928(Action):
    # 恢复自身体力
    # 恢复力：3000
    # 追加效果：解除加重、止步、死斗
    # Restores own HP.
    # Cure Potency: 3,000
    # Additional Effect: Removes Heavy, Bind, and Holmgang effects
    # related: [死斗(2)](Status88), [死斗(3)](Status409), [死斗(1)](Status1305), [死斗(0)](Status1304),
    id = 18928
    names = ['自愈(pvp)(CMN)', 'Recuperate(pvp)(CMN)']
    _orig_names = ['Recuperate(pvp)', '自愈(pvp)']
    heal = 3000


class Action18942(Action):
    # 提高自身的移动速度
    # 持续时间：10秒
    # Movement speed is increased.
    # Duration: 10s
    # related: [疾跑](Status1342),
    id = 18942
    names = ['疾跑(pvp)(CMN)', 'Bolt(pvp)(CMN)']
    _orig_names = ['Bolt(pvp)', '疾跑(pvp)']


class Action18943(Action):
    # 恢复自身体力
    # 恢复力：3000～6000
    # 自身剩余体力越少恢复力越高
    # 积蓄次数：3
    # Restores own HP.
    # Cure Potency: 3,000
    # Potency increases up to 6,000 as HP decreases.
    # Maximum Charges: 3
    id = 18943
    names = ['军用恢复药(pvp)(CMN)', 'Medical Kit(pvp)(CMN)']
    _orig_names = ['军用恢复药(pvp)', 'Medical Kit(pvp)']
    heal = [3000, 6000]


class Action18952(Action):
    # 对目标发动远距离物理攻击
    # 威力：400
    # 追加效果：将目标向自己拉10米
    # Delivers a ranged attack with a potency of 400.
    # Additional Effect: 10-yalm draw-in
    id = 18952
    names = ['Weapon Throw(pvp)(CMN)', '武器投掷(pvp)(CMN)']
    _orig_names = ['Weapon Throw(pvp)', '武器投掷(pvp)']
    damage = 400


class Action18954(Action):
    # 一定时间内，令自身对目标造成的伤害提高20%
    # 持续时间：6秒
    # Increases damage you deal target by 20%.
    # Duration: 6s
    # related: [牵制(0)](Status2185), [牵制(1)](Status1195),
    id = 18954
    names = ['Feint(pvp)(CMN)', '牵制(pvp)(CMN)']
    _orig_names = ['Feint(pvp)', '牵制(pvp)']
    # remain metas: {'dmg_increase': '20%'}


class Action18955(Action):
    # 效果时间内，自身发动的1次战技造成的伤害提升50%
    # 持续时间：5秒
    # Increases potency of next weaponskill by 50%.
    # Duration: 5s
    # related: [集中(0)](Status2186), [集中(1)](Status396),
    id = 18955
    names = ['Concentrate(pvp)(CMN)', '集中(pvp)(CMN)']
    _orig_names = ['Concentrate(pvp)', '集中(pvp)']


class Action18956(Action):
    # 对自身周围的敌人发动魔法攻击
    # 威力：1600
    # 追加效果：战技与魔法的咏唱及复唱时间延长20%
    # 持续时间：10秒
    # Deals unaspected damage with a potency of 1,600 to all nearby enemies.
    # Additional Effect: Lengthens weaponskill cast time and recast time as well as spell cast time and recast time by 20%
    # Duration: 10s
    # related: [以太爆发](Status2187),
    id = 18956
    names = ['Aetheric Burst(pvp)(CMN)', '以太爆发(pvp)(CMN)']
    _orig_names = ['Aetheric Burst(pvp)', '以太爆发(pvp)']
    damage = 1600


class Action18957(Action):
    # 一定时间内，自身发动治疗魔法的治疗量提高25%
    # 持续时间：10秒
    # Increases healing potency by 25%.
    # Duration: 10s
    # related: [慈爱(0)](Status2188), [慈爱(1)](Status1207),
    id = 18957
    names = ['Largesse(pvp)(CMN)', '慈爱(pvp)(CMN)']
    _orig_names = ['Largesse(pvp)', '慈爱(pvp)']


class Action18990(Action):
    # 受到攻击时会给予对方反击伤害
    # 威力：800
    # 持续时间：10秒
    # Counters all incoming attacks.
    # Counter Potency: 800
    # Duration: 10s
    # related: [还击](Status2184),
    id = 18990
    names = ['Retaliation(pvp)(CMN)', '还击(pvp)(CMN)']
    _orig_names = ['还击(pvp)', 'Retaliation(pvp)']
    damage = 800


class Action18992(Action):
    # 对目标发动物理攻击
    # 威力：600～3000
    # 目标剩余体力越低威力越高
    # Delivers an attack with a potency of 600.
    # Potency increases up to 3,000 as the target's HP decreases.
    id = 18992
    names = ['Smite(pvp)(CMN)', '猛击(pvp)(CMN)']
    _orig_names = ['Smite(pvp)', '猛击(pvp)']
    damage = [600, 3000]


class Action19218(Action):
    # 恢复自身体力
    # Restores own HP.
    id = 19218
    names = ['Aqua Vitae(CMN)', '生命水(CMN)']
    _orig_names = ['Aqua Vitae', '生命水']


class Action19275(Action):
    # 向自身前方扇形范围内喷吐微微臭气
    # 演出技能，没有任何实际效果
    # Blows breath that is not so horrid as to stop one in their tracks, yet still unmistakably offensive, in a cone before you.
    # ※Has no effect in battle.
    id = 19275
    names = ['微微臭气(CMN)', 'Could-be-worse Breath(CMN)']
    _orig_names = ['Could-be-worse Breath', '微微臭气']


class Action19731(Action):
    # 脱下目前穿着的特殊玩偶装
    # Cease to wear this peculiar garb and return to wearing your usual peculiar garb.
    id = 19731
    names = ['Remove Costume(CMN)', '解除玩偶装(CMN)']
    _orig_names = ['Remove Costume', '解除玩偶装']


class Action19994(Action):
    # 站稳准备承受强烈的冲击
    # Brace yourself to stand against even the most relentless onslaught.
    # related: [抵御冲击](Status2265),
    id = 19994
    names = ['Stand Firm(CMN)', '抵御冲击(CMN)']
    _orig_names = ['Stand Firm', '抵御冲击']


class Action19997(Action):
    # 抛网捉鸡
    # Snare a chicken in your net with a single swift motion.
    # related: [抓捕(0)](Status401), [抓捕(1)](Status961), [抓捕(2)](Status609), [抓捕(3)](Status1287),
    id = 19997
    names = ['抓捕(CMN)', 'Seize(CMN)']
    _orig_names = ['抓捕', 'Seize']


class Action19998(Action):
    # 投掷粘鸟胶，拖慢小鸡的动作
    # Toss a glob of paste to stick overexcited chickens to the ground.
    id = 19998
    names = ['粘鸟胶(CMN)', 'Birdlime(CMN)']
    _orig_names = ['粘鸟胶', 'Birdlime']


class Action20030(Action):
    # 发出具有魔力的不可思议的光线
    # Plumb the depths of the great serpent's power for no particular reason, unleashing an awe-inspiring ray of light. May or may not obliterate nonbelievers.
    # related: [惊奇光](Status1721),
    id = 20030
    names = ['惊奇光(CMN)(0)', 'Peculiar Light(CMN)(0)']
    _orig_names = ['Peculiar Light', '惊奇光']


class Action20031(Action):
    # 发出具有魔力的不可思议的光线
    # 演出技能，没有任何实际效果
    # Plumb the depths of the great serpent's power for no particular reason, unleashing an awe-inspiring ray of light. May or may not obliterate nonbelievers.
    # ※Has no effect in battle.
    # related: [惊奇光](Status1721),
    id = 20031
    names = ['Peculiar Light(CMN)(1)', '惊奇光(CMN)(1)']
    _orig_names = ['Peculiar Light', '惊奇光']


class Action20064(Action):
    # 展示自己美丽的尾羽
    # 演出技能，没有任何实际效果
    # Commands your peacock to proudly display its plumage.
    # ※Has no effect in battle.
    id = 20064
    names = ['Dazzling Display(CMN)', '开屏(CMN)']
    _orig_names = ['Dazzling Display', '开屏']


class Action20121(Action):
    # 发射主炮
    # Solves your problems with excessive explosive force.
    id = 20121
    names = ['Cannonfire(CMN)(4)', '炮击(CMN)(6)']
    _orig_names = ['Cannonfire', '炮击']


class Action20122(Action):
    # 发射主炮
    # 演出技能，没有任何实际效果
    # Solves your problems with excessive explosive force.
    # ※Has no effect in battle.
    id = 20122
    names = ['Cannonfire(CMN)(5)', '炮击(CMN)(7)']
    _orig_names = ['Cannonfire', '炮击']


class Action20304(Action):
    # 用阿尔法的羽毛制作的陆行鸟之笔
    # 上面有黑色的颜料
    # Black paint drips from the tip of this massive brush made from Alpha's feathers.
    # related: [黑色的颜料](Status1469),
    id = 20304
    names = ['黑色陆行鸟之笔(CMN)(1)', 'Black Paint(CMN)(1)']
    _orig_names = ['黑色陆行鸟之笔', 'Black Paint']


class Action20489(Action):
    # 对目标发动无属性魔法攻击
    # 威力：600
    # Deals unaspected damage with a potency of 600.
    id = 20489
    names = ['以太加农炮(CMN)', 'Aether Cannon(CMN)']
    _orig_names = ['以太加农炮', 'Aether Cannon']
    damage = 600


class Action20493(Action):
    # 向目标所在方向发出直线无属性范围魔法攻击
    # 威力：1200
    # 该战技有单独计算的复唱时间，发动后其他战技与魔法会产生与该战技相同的复唱时间
    # Deals unaspected damage with a potency of 1,200 to all enemies in a straight line before you.
    # Triggers the cooldown of weaponskills and spells upon execution.
    id = 20493
    names = ['Ultima Buster(CMN)', '究极破坏炮(CMN)']
    _orig_names = ['究极破坏炮', 'Ultima Buster']
    damage = 1200


class Action20494(Action):
    # 战技与魔法的咏唱及复唱时间缩短25%，令自身移动速度提高25%，作为代价将持续消耗体力
    # 再次发动时则取消该状态
    # 持续时间：永久
    # Reduces cast time and recast time of weaponskills by 25% and increases movement speed by 25%. HP is drained while in use.
    # Effect ends upon reuse.
    id = 20494
    names = ['Pyretic Booster(CMN)', '加速模式(CMN)']
    _orig_names = ['加速模式', 'Pyretic Booster']


class Action20495(Action):
    # 令自身受到的伤害减轻50%，作为代价将持续消耗能量
    # 当能量为0或再次发动时则取消该状态
    # 持续时间：永久
    # Reduces damage taken by 50%. EP is drained while in use.
    # Effect ends upon reuse or when EP is depleted.
    id = 20495
    names = ['Aetherial Aegis(CMN)', '以太屏障(CMN)']
    _orig_names = ['Aetherial Aegis', '以太屏障']
    # remain metas: {'taken_dmg_reduce': '50%，作为代价将持续消耗能量'}


class Action20496(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：300
    # 追加效果：目标所受伤害提高20%
    # 持续时间：60秒
    # 该战技有单独计算的复唱时间
    # Deals unaspected damage with a potency of 300 to target and all enemies nearby it.
    # Additional Effect: Increases target's damage taken by 20%
    # Duration: 60s
    # This action does not share a recast timer with any other actions.
    id = 20496
    names = ['Aether Mine(CMN)', '以太机雷(CMN)']
    _orig_names = ['Aether Mine', '以太机雷']
    damage = 300
    # remain metas: {'taken_dmg_increase': '20%'}


class Action20533(Action):
    # 对周围的敌人发动无属性范围魔法攻击
    # 威力：200
    # Deals unaspected damage with a potency of 200 to all nearby enemies.
    id = 20533
    names = ['Crimson Savior(CMN)(0)', '深红救世(CMN)(0)']
    _orig_names = ['深红救世', 'Crimson Savior']
    damage = 200


class Action20701(Action):
    # 令目标及其周围敌人陷入麻痹状态
    # 持续时间：60秒
    # Afflicts target and all nearby enemies with Paralysis.
    # Duration: 60s
    id = 20701
    names = ['失传强麻痹(CMN)', 'Lost Paralyze III(CMN)']
    _orig_names = ['Lost Paralyze III', '失传强麻痹']


class Action20702(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：200
    # 目标为不死系怪物时发动追加效果
    # 追加效果：目标所受伤害提高25%
    # 持续时间：60秒
    # Deals unaspected damage with a potency of 200 to target and all enemies nearby it.
    # Additional Effect: Increases damage undead enemies take by 25%
    # Duration: 60s
    # related: [失传强放逐](Status2340),
    id = 20702
    names = ['Lost Banish III(CMN)', '失传强放逐(CMN)']
    _orig_names = ['失传强放逐', 'Lost Banish III']
    damage = 200
    # remain metas: {'taken_dmg_increase': '25%'}


class Action20703(Action):
    # 一定时间内，以自身加重为代价，令自身所受的伤害减轻90%，同时除特定攻击之外其他所有击退与吸引效果失效
    # 持续时间：6秒
    # Temporarily applies Heavy to self, while reducing damage taken by 90% and nullifying most knockback and draw-in effects.
    # Duration: 6s
    # related: [失传坚壁](Status2345), [吸引(0)](Status2529), [吸引(1)](Status2486),
    id = 20703
    names = ['失传坚壁(CMN)', 'Lost Manawall(CMN)']
    _orig_names = ['Lost Manawall', '失传坚壁']
    # remain metas: {'taken_dmg_reduce': '90%，同时除特定攻击之外其他所有击退与吸引效果失效'}


class Action20704(Action):
    # 打消目标身上的一种强化状态
    # 发动之后会停止自动攻击
    # Removes one beneficial status from target.
    # Cancels auto-attack upon execution.
    id = 20704
    names = ['失传驱魔(CMN)', 'Lost Dispel(CMN)']
    _orig_names = ['失传驱魔', 'Lost Dispel']


class Action20705(Action):
    # 隐藏自己的身形，大多数敌人都无法发现自己
    # 不过移动速度会降低25%
    # 对部分特殊怪物无效
    # 发动除冲刺以外的技能会取消该状态
    # 持续时间：永久
    # 发动条件：自身处于非战斗状态
    # Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 25%. Has no effect on certain enemies with special sight.
    # Cannot be executed while in combat.
    # Effect ends upon use of any action other than Sprint, or upon reuse.
    id = 20705
    names = ['Lost Stealth(CMN)', '失传潜行(CMN)']
    _orig_names = ['Lost Stealth', '失传潜行']


class Action20706(Action):
    # 对自身或一名队员附加失传铸魔状态
    # 无法与失传钢刺状态共存
    # 失传铸魔效果：一定时间内，所有攻击均视为魔法攻击
    # 不过，伤害提高等效果受技能原本属性影响
    # 持续时间：300秒
    # Grants the effect of Lost Spellforge to self or target ally.
    # Lost Spellforge Effect: All attacks deal magic damage. However, all bonuses to damage dealt are determined by the attack's base damage type.
    # Duration: 300s
    # Effect cannot be stacked with Lost Steelsting.
    # related: [失传铸魔](Status2338), [失传钢刺](Status2339),
    id = 20706
    names = ['失传铸魔(CMN)', 'Lost Spellforge(CMN)']
    _orig_names = ['Lost Spellforge', '失传铸魔']
    # remain metas: {'dmg_increase': '等效果受技能原本属性影响'}


class Action20707(Action):
    # 对自身或一名队员附加失传钢刺状态
    # 无法与失传铸魔状态共存
    # 失传钢刺效果：一定时间内，所有攻击均视为物理攻击
    # 不过，伤害提高等效果受技能原本属性影响
    # 持续时间：300秒
    # Grants the effect of Lost Steelsting to self or target ally.
    # Lost Steelsting Effect: All attacks deal physical damage. However, all bonuses to damage dealt are determined by the attack's base damage type.
    # Duration: 300s
    # Effect cannot be stacked with Lost Spellforge.
    # related: [失传铸魔](Status2338), [失传钢刺](Status2339),
    id = 20707
    names = ['Lost Steelsting(CMN)', '失传钢刺(CMN)']
    _orig_names = ['Lost Steelsting', '失传钢刺']
    # remain metas: {'dmg_increase': '等效果受技能原本属性影响'}


class Action20708(Action):
    # 令自身的移动速度大幅提高
    # 同时附加了其他移动速度提高的效果时，仅能适用其中1种
    # 持续时间：10秒
    # 盗贼的药状态中追加效果：令自身回避率提高30%
    # 持续时间：60秒
    # 斥候的药状态中追加效果：对自身附加高速复唱状态
    # 高速复唱效果：效果时间内，自身发动的1次能力类技能复唱时间缩短60%
    # 持续时间：30秒
    # Greatly increases movement speed.
    # Effect cannot be stacked with other movement speed enhancing abilities.
    # Duration: 10s
    # Spirit of the Breathtaker Effect: Increases evasion by 30%
    # Duration: 60s
    # Spirit of the Watcher Effect: Grants Rapid Recast to self
    # Rapid Recast Effect: Shortens recast time for next ability used by 60%
    # Effect only applies to certain abilities.
    # Duration: 30s
    # related: [盗贼的药](Status2322), [斥候的药](Status2319), [高速复唱](Status1645), [失传敏捷](Status2335),
    id = 20708
    names = ['失传敏捷(CMN)', 'Lost Swift(CMN)']
    _orig_names = ['Lost Swift', '失传敏捷']


class Action20709(Action):
    # 指定自身或其他一名玩家，附加物理伤害减轻10%的防护罩
    # 持续时间：30分
    # Applies a barrier to self or target player reducing physical damage taken by 10%.
    # Duration: 30m
    # related: [失传护盾](Status2333),
    id = 20709
    names = ['Lost Protect(CMN)', '失传护盾(CMN)']
    _orig_names = ['Lost Protect', '失传护盾']
    # remain metas: {'taken_dmg_reduce': '10%的防护罩'}


class Action20710(Action):
    # 指定自身或其他一名玩家，附加魔法伤害减轻10%的防护罩
    # 持续时间：30分
    # Applies a barrier to self or target player reducing magic damage taken by 10%.
    # Duration: 30m
    # related: [失传魔盾](Status2334),
    id = 20710
    names = ['Lost Shell(CMN)', '失传魔盾(CMN)']
    _orig_names = ['Lost Shell', '失传魔盾']
    # remain metas: {'taken_dmg_reduce': '10%的防护罩'}


class Action20711(Action):
    # 为自身或一名队员附加防护罩，在效果时间内能够反射除特定攻击之外的所有魔法
    # 持续时间：10秒
    # 守护者的药状态中追加效果：持续时间变为30秒
    # Creates a barrier around self or party member that reflects most magic attacks.
    # Duration: 10s
    # Spirit of the Guardian Effect: Duration is increased to 30s
    # related: [失传反射](Status2337), [守护者的药](Status2316),
    id = 20711
    names = ['失传反射(CMN)', 'Lost Reflect(CMN)']
    _orig_names = ['失传反射', 'Lost Reflect']


class Action20712(Action):
    # 指定自身或其他一名玩家，附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力15%的伤害量
    # 持续时间：60秒
    # Applies a barrier to self or target player that absorbs damage totaling 15% of target's maximum HP.
    # Duration: 60s
    id = 20712
    names = ['失传石肤(CMN)', 'Lost Stoneskin(CMN)']
    _orig_names = ['Lost Stoneskin', '失传石肤']
    # remain metas: {'shield': '目标最大体力15%'}


class Action20713(Action):
    # 令自身或一名队员攻击造成的伤害提高5%
    # 持续时间：600秒
    # Increases damage dealt by an ally or self by 5%.
    # Duration: 600s
    # related: [失传勇气](Status2341),
    id = 20713
    names = ['Lost Bravery(CMN)', '失传勇气(CMN)']
    _orig_names = ['Lost Bravery', '失传勇气']
    # remain metas: {'dmg_increase': '5%'}


class Action20714(Action):
    # 对自身附加蓄力状态
    # 蓄力效果：效果时间内自身发动的1次战技威力提高，效果量为每档提高15%，继承其他失传技能后取消该状态
    # 最大档数：16档
    # 持续时间：30秒
    # 与战技和魔法共享复唱时间
    # Grants a stack of Boost, up to a maximum of 16.
    # Boost Bonus: Increases potency of next weaponskill by 15% per stack
    # Duration: 30s
    # Effect ends upon using another lost action.
    # Shares a recast timer with all other weaponskills and spells.
    # related: [蓄力(2)](Status1656), [蓄力(3)](Status203), [蓄力(1)](Status1716), [蓄力(0)](Status2448),
    id = 20714
    names = ['失传蓄力(CMN)', 'Lost Focus(CMN)']
    _orig_names = ['失传蓄力', 'Lost Focus']


class Action20715(Action):
    # 一定时间内，自身发动攻击造成的伤害提高70%
    # 效果中会持续消耗魔力，魔力为0时取消该状态
    # 持续时间：30秒
    # 发动条件：自身处于战斗状态
    # 魔战士的药状态中追加效果：对自身附加魔法盾状态
    # 魔法盾效果：受到的魔法伤害减少50%
    # 持续时间：15秒
    # Increases damage dealt by 70%, draining MP while in use.
    # Duration: 30s
    # Spirit of the Veteran Effect: Grants Spell Shield to self
    # Spell Shield Effect: Reduces magic damage taken by 50%
    # Duration: 15s
    # Can only be executed while in combat.
    # related: [魔法盾](Status1648), [魔战士的药](Status2314), [失传魔泉](Status2332),
    id = 20715
    names = ['Lost Font of Magic(CMN)', '失传魔泉(CMN)']
    _orig_names = ['失传魔泉', 'Lost Font of Magic']
    # remain metas: {'dmg_increase': '70%'}


class Action20716(Action):
    # 重置除特定技能之外所有职业技能、特职技能以及职能技能的复唱时间
    # Resets the recast timer for most actions and role actions.
    id = 20716
    names = ['Lost Font of Skill(CMN)', '失传技泉(CMN)']
    _orig_names = ['失传技泉', 'Lost Font of Skill']


class Action20717(Action):
    # 一定时间内，自身发动攻击造成的伤害提高30%，且暴击发动率提高40%
    # 持续时间：30秒
    # 发动条件：自身处于战斗状态
    # 狂战士的药状态中追加效果：攻击造成的伤害提高量变为40%
    # 重骑兵的药状态中追加效果：对自身附加物理盾状态
    # 物理盾效果：受到的物理伤害减少50%
    # 持续时间：15秒
    # Increases damage dealt by 30% and critical hit rate by 40%.
    # Duration: 30s
    # Spirit of the Irregular Effect: Damage bonus effect is increased to 40%
    # Spirit of the Platebearer Effect: Grants Solid Shield to self
    # Solid Shield Effect: Reduces physical damage taken by 50%
    # Duration: 15s
    # Can only be executed while in combat.
    # related: [狂战士的药](Status2321), [失传力泉](Status2346), [重骑兵的药](Status2315), [物理盾](Status1647),
    id = 20717
    names = ['Lost Font of Power(CMN)', '失传力泉(CMN)']
    _orig_names = ['失传力泉', 'Lost Font of Power']
    # remain metas: {'dmg_increase': ['量变为40%', '30%，且暴击发动率提高40%']}


class Action20718(Action):
    # 向目标所在方向发出扇形范围物理攻击
    # 威力：800
    # 追加效果（暴击时）：暴击伤害变为300%
    # 该战技有单独计算的复唱时间，不受其他战技与魔法的复唱时间影响
    # Delivers an attack with a potency of 800 to all enemies in a cone before you. When critical damage is dealt, potency is tripled.
    # This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
    id = 20718
    names = ['Lost Slash(CMN)', '失传斩击(CMN)']
    _orig_names = ['Lost Slash', '失传斩击']
    damage = 800


class Action20719(Action):
    # 令目标陷入无法战斗状态
    # 目标剩余体力越少成功率越高
    # 该战技有单独计算的复唱时间，不受其他战技与魔法的复唱时间影响
    # 祭司的药状态中追加效果：提高成功率
    # KOs target. The less the target's HP, the greater the chance of success.
    # Spirit of the Ordained Effect: Chance of success is increased
    # This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
    # related: [祭司的药](Status2317),
    id = 20719
    names = ['失传即死(CMN)', 'Lost Death(CMN)']
    _orig_names = ['Lost Death', '失传即死']


class Action20720(Action):
    # 一定时间内，以自身所受除特定技能之外的治疗魔法效果降低100%为代价，令攻击造成的伤害提高50%
    # 无法与其他境地系技能同时使用
    # 持续时间：15秒
    # 发动条件：自身处于战斗状态
    # Storm the field under the Banner of Noble Ends, increasing damage dealt by 50% while reducing own HP recovery via most healing actions by 100%.
    # Duration: 15s
    # Can only be executed while in combat.
    # Effect cannot be stacked with other Banner actions.
    # related: [背水境地](Status2326),
    id = 20720
    names = ['Banner of Noble Ends(CMN)', '背水境地(CMN)']
    _orig_names = ['背水境地', 'Banner of Noble Ends']
    # remain metas: {'taken_dmg_increase': '50%'}


class Action20721(Action):
    # 一定时间内，以自身体力逐渐流失为代价，令攻击造成的伤害提高55%
    # 无法与其他境地系技能同时使用
    # 持续时间：15秒
    # 发动条件：自身处于战斗状态
    # Storm the field under the Banner of Honored Sacrifice, increasing damage dealt by 55% while draining your HP.
    # Duration: 15s
    # Can only be executed while in combat.
    # Effect cannot be stacked with other Banner actions.
    # related: [舍身境地](Status2327),
    id = 20721
    names = ['舍身境地(CMN)', 'Banner of Honored Sacrifice(CMN)']
    _orig_names = ['舍身境地', 'Banner of Honored Sacrifice']
    # remain metas: {'dmg_increase': '55%'}


class Action20722(Action):
    # 对自身附加忍耐境地状态
    # 一定时间内，受到伤害会增加忍耐境地的档数
    # 无法与其他境地系技能同时使用
    # 忍耐境地的效果：每档所受伤害提高15%
    # 持续时间：30秒
    # 最大档数：5档
    # 档数最大时忍耐境地会变为铁壁境地
    # 铁壁境地的效果：所受伤害减轻30%
    # 持续时间：180秒
    # Storm the field under the Banner of Tireless Conviction, gaining additional stacks each time damage is taken, up to a maximum of 5.
    # Banner of Tireless Conviction Effect: Increases damage taken by 15% per stack
    # Duration: 30s
    # At maximum stacks, take up the Banner of Unyielding Defense.
    # Banner of Unyielding Defense Effect: Reduces damage taken by 30%
    # Duration: 180s
    # Effect cannot be stacked with other Banner actions.
    # related: [忍耐境地](Status2328),
    id = 20722
    names = ['忍耐境地(CMN)', 'Banner of Tireless Conviction(CMN)']
    _orig_names = ['Banner of Tireless Conviction', '忍耐境地']
    # remain metas: {'taken_dmg_increase': '15%', 'taken_dmg_reduce': '30%'}


class Action20723(Action):
    # 对自身附加坚守境地状态
    # 一定时间内，受到伤害会增加坚守境地的档数
    # 无法与其他境地系技能同时使用
    # 坚守境地的效果：每档攻击造成的伤害减少15%
    # 持续时间：30秒
    # 最大档数：5档
    # 档数最大时坚守境地会变为铁壁境地
    # 铁壁境地的效果：所受伤害减轻30%
    # 持续时间：180秒
    # Storm the field under the Banner of Firm Resolve, gaining additional stacks each time damage is taken, up to a maximum of 5.
    # Banner of Firm Resolve Effect: Reduces damage dealt by 15% per stack
    # Duration: 30s
    # At maximum stacks, take up the Banner of Unyielding Defense.
    # Banner of Unyielding Defense Effect: Reduces damage taken by 30%
    # Duration: 180s
    # Effect cannot be stacked with other Banner actions.
    # related: [坚守境地](Status2329),
    id = 20723
    names = ['坚守境地(CMN)', 'Banner of Firm Resolve(CMN)']
    _orig_names = ['Banner of Firm Resolve', '坚守境地']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action20724(Action):
    # 对自身附加冥想境地状态
    # 每隔一段时间会增加冥想境地的档数
    # 效果时间内发动技能或进行移动、转身都会立即解除冥想境地
    # 发动之后会停止自动攻击
    # 无法与其他境地系技能同时使用
    # 持续时间：30秒
    # 最大档数：4档
    # 发动条件：自身处于战斗状态档数最大时冥想境地会变为无我境地
    # 无我境地的效果： 自身发动的体力恢复效果提高50%，且减少魔力消耗
    # 持续时间：120秒
    # Storm the field under the Banner of Solemn Clarity, periodically gaining additional stacks, up to a maximum of 4.
    # Duration: 30s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # At maximum stacks, take up the Banner of Limitless Grace.
    # Banner of Limitless Grace Effect: Increases healing potency by 50% while reducing MP cost
    # Duration: 120s
    # Can only be executed while in combat.
    # Effect cannot be stacked with other Banner actions.
    # related: [冥想境地](Status2330),
    id = 20724
    names = ['冥想境地(CMN)', 'Banner of Solemn Clarity(CMN)']
    _orig_names = ['Banner of Solemn Clarity', '冥想境地']


class Action20725(Action):
    # 对自身附加敏锐境地状态
    # 一定时间内，回避攻击会增加敏锐境地的档数
    # 无法与其他境地系技能同时使用
    # 敏锐境地的效果：每档所受伤害提高10%
    # 持续时间：120秒
    # 最大档数：3档
    # 发动条件：自身处于战斗状态档数最大时敏锐境地会变为神速境地
    # 神速境地的效果：自身直击发动率提高30%，攻击间隔、战技与魔法的咏唱及复唱时间缩短20%
    # 持续时间：180秒
    # Storm the field under the Banner of Honed Acuity, gaining additional stacks each time an attack is evaded, up to a maximum of 3.
    # Banner of Honed Acuity Effect: Increases damage taken by 10% per stack
    # Duration: 120s
    # At maximum stacks, take up the Banner of Transcendent Finesse.
    # Banner of Transcendent Finesse Effect: Increases critical hit rate by 30% and reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 20%
    # Duration: 180s
    # Can only be executed while in combat.
    # Effect cannot be stacked with other Banner actions.
    # related: [敏锐境地](Status2331),
    id = 20725
    names = ['Banner of Honed Acuity(CMN)', '敏锐境地(CMN)']
    _orig_names = ['敏锐境地', 'Banner of Honed Acuity']
    # remain metas: {'taken_dmg_increase': '10%'}


class Action20726(Action):
    # 恢复目标的体力
    # 恢复力：15000
    # Restores target's HP.
    # Cure Potency: 15,000
    id = 20726
    names = ['Lost Cure(CMN)', '失传治疗(CMN)']
    _orig_names = ['Lost Cure', '失传治疗']
    heal = 15000


class Action20727(Action):
    # 恢复目标的体力
    # 恢复力：21700
    # 治愈者的药状态中追加效果：目标体力持续恢复
    # 恢复力：6000
    # 持续时间：21秒
    # Restores target's HP.
    # Cure Potency: 21,700
    # Spirit of the Savior Effect: Regen
    # Cure Potency: 6,000
    # Duration: 21s
    # related: [治愈者的药](Status2313),
    id = 20727
    names = ['失传救疗(CMN)', 'Lost Cure II(CMN)']
    _orig_names = ['Lost Cure II', '失传救疗']
    heal = 21700
    # remain metas: {'heal_ot': '6000'}


class Action20728(Action):
    # 恢复目标及其周围队员的体力
    # 恢复力：15000
    # Restores HP of target and all party members nearby target.
    # Cure Potency: 15,000
    id = 20728
    names = ['Lost Cure III(CMN)', '失传愈疗(CMN)']
    _orig_names = ['失传愈疗', 'Lost Cure III']
    heal = 15000


class Action20729(Action):
    # 恢复目标及其周围队员的体力
    # 恢复力：21700
    # 治愈者的药状态中追加效果：目标体力持续恢复
    # 恢复力：6000
    # 持续时间：21秒
    # Restores HP of target and all party members nearby target.
    # Cure Potency: 21,700
    # Spirit of the Savior Effect: Regen
    # Cure Potency: 6,000
    # Duration: 21s
    # related: [治愈者的药](Status2313),
    id = 20729
    names = ['失传圣疗(CMN)', 'Lost Cure IV(CMN)']
    _orig_names = ['失传圣疗', 'Lost Cure IV']
    heal = 21700
    # remain metas: {'heal_ot': '6000'}


class Action20730(Action):
    # 复活目标并恢复其全部体力
    # 目标陷入衰弱状态时会解除衰弱复活目标
    # Restores all of a KO'd target's HP.
    # If the target was weakened at the time of Raise, the weakness effect will be removed.
    # related: [衰弱](Status43),
    id = 20730
    names = ['Lost Arise(CMN)', '失传完全复活(CMN)']
    _orig_names = ['失传完全复活', 'Lost Arise']


class Action20731(Action):
    # 向目标进行挑衅，令目标对自身的仇恨变为最高后，继续提高自身仇恨
    # 一定时间内，持续提高自身仇恨且所受的伤害减轻20%
    # 持续时间：20秒
    # Gesture threateningly, placing yourself at the top of a target's enmity list.
    # Additional Effect: Enmity generation is increased and damage taken is reduced by 20%
    # Duration: 20s
    # related: [失传激怒](Status2356),
    id = 20731
    names = ['Lost Incense(CMN)', '失传激怒(CMN)']
    _orig_names = ['失传激怒', 'Lost Incense']
    # remain metas: {'taken_dmg_reduce': '20%'}


class Action20732(Action):
    # 从持有的失传技能中随机选取1个掷向敌人，发动单体攻击
    # 威力：50～1000
    # 会失去掷出的失传技能
    # 掷出的失传技能体积越大威力越大
    # 该战技有单独计算的复唱时间，不受其他战技与魔法的复唱时间影响
    # Through sheer force of will, restore a random technique of the lost to physical form and throw it at a single target, dealing damage with a potency of 50.
    # Potency increases up to 1,000 based on the weight of the lost action.
    # The lost action thrown will be lost upon execution.
    # This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
    id = 20732
    names = ['失传公平交易(CMN)', 'Lost Fair Trade(CMN)']
    _orig_names = ['Lost Fair Trade', '失传公平交易']
    damage = [50, 1000]


class Action20733(Action):
    # 指定一名我方同伴为目标，模仿并继承目标继承中的失传技能
    # 发动条件：自身处于非战斗状态
    # Study the lost techniques used by a targeted ally and make them your own.
    # Cannot be executed while in combat.
    # related: [模仿(0)](Status1056), [模仿(1)](Status2450),
    id = 20733
    names = ['Mimic(CMN)', '模仿(CMN)']
    _orig_names = ['Mimic', '模仿']


class Action20734(Action):
    # 掷出命运骰子，不知道会发生什么
    # 发动条件：自身处于战斗状态
    # 与义军恢复药、义军圣灵药共享复唱时间
    # Place your faith in the goddess Nymeia as she spins the wheel of fate.
    # Can only be executed while in combat.
    # Shares a recast timer with Resistance Potion and Resistance Elixir.
    id = 20734
    names = ['命运骰子(CMN)', 'Dynamis Dice(CMN)']
    _orig_names = ['命运骰子', 'Dynamis Dice']


class Action20735(Action):
    # 令无法战斗的目标以衰弱状态重新振作起来
    # Resurrects target to a weakened state.
    # related: [衰弱](Status43),
    id = 20735
    names = ['Resistance Phoenix(CMN)', '义军不死鸟之尾(CMN)']
    _orig_names = ['Resistance Phoenix', '义军不死鸟之尾']


class Action20736(Action):
    # 持续时间内若陷入无法战斗状态，有70%几率自动复活
    # 持续时间：180分
    # Grants a 70% chance of automatic revival upon KO.
    # Duration: 180m
    id = 20736
    names = ['义军复活药(CMN)', 'Resistance Reraiser(CMN)']
    _orig_names = ['Resistance Reraiser', '义军复活药']


class Action20737(Action):
    # 对自身附加自动恢复药状态
    # 自动恢复药效果：效果时间内体力低于50%时自动恢复
    # 持续时间：600秒
    # 发动恢复效果后有50%的几率解除自动恢复药
    # 盗贼的药状态中追加效果：发动恢复效果后解除自动恢复药状态的几率变为10%
    # 与义军以太药箱和义军治愈箱共享复唱时间
    # Grants Auto-potion to self.
    # Auto-potion Effect: Restores HP automatically when HP falls below 50%
    # Duration: 600s
    # When triggered, there is a 50% chance the effect will end.
    # Spirit of the Breathtaker Effect: Chance for Auto-potion effect to end is reduced to 10%
    # Shares a recast timer with Resistance Ether Kit and Resistance Medikit.
    # related: [盗贼的药](Status2322), [自动恢复药](Status2342),
    id = 20737
    names = ['Resistance Potion Kit(CMN)', '义军恢复药箱(CMN)']
    _orig_names = ['Resistance Potion Kit', '义军恢复药箱']


class Action20738(Action):
    # 对自身附加自动以太药状态
    # 自动以太药效果：效果时间内魔力低于20%时自动恢复
    # 持续时间：600秒
    # 发动恢复效果后有50%的几率解除自动以太药
    # 盗贼的药状态中追加效果：发动恢复效果后解除自动以太药状态的几率变为10%
    # 与义军恢复药箱和义军治愈箱共享复唱时间
    # Grants Auto-ether to self.
    # Auto-ether Effect: Restores MP automatically when MP falls below 20%
    # Duration: 600s
    # When triggered, there is a 50% chance the effect will end.
    # Spirit of the Breathtaker Effect: Chance for Auto-ether effect to end is reduced to 10%
    # Shares a recast timer with Resistance Potion Kit and Resistance Medikit.
    # related: [盗贼的药](Status2322), [自动以太药](Status2343),
    id = 20738
    names = ['义军以太药箱(CMN)', 'Resistance Ether Kit(CMN)']
    _orig_names = ['Resistance Ether Kit', '义军以太药箱']


class Action20739(Action):
    # 解除自身身上部分弱化效果中的一种
    # 如果未能触发该效果，则张开可免疫一次部分弱化效果中一种的防护罩
    # 无法与同样效果的防护罩共存
    # 持续时间：30分
    # 与义军恢复药箱和义军以太药箱共享复唱时间
    # Removes a single detrimental effect from self. When not suffering from detrimental effects, creates a barrier that protects against most status ailments. The barrier is removed after curing the next status ailment suffered.
    # Effect cannot be stacked with similar barrier actions.
    # Duration: 30m
    # Shares a recast timer with Resistance Potion Kit and Resistance Ether Kit.
    id = 20739
    names = ['Resistance Medikit(CMN)', '义军治愈箱(CMN)']
    _orig_names = ['义军治愈箱', 'Resistance Medikit']


class Action20740(Action):
    # 令自身体力持续恢复
    # 恢复力：5000
    # 持续时间：40秒
    # 与命运骰子、义军圣灵药共享复唱时间
    # Gradually restores HP.
    # Cure Potency: 5,000
    # Duration: 40s
    # Shares a recast timer with Dynamis Dice and Resistance Elixir.
    id = 20740
    names = ['Resistance Potion(CMN)', '义军恢复药(CMN)']
    _orig_names = ['Resistance Potion', '义军恢复药']
    # remain metas: {'heal_ot': '5000'}


class Action20741(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高80%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 80%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20741
    names = ['Essence of the Aetherweaver(CMN)', '术士的秘药(CMN)']
    _orig_names = ['术士的秘药', 'Essence of the Aetherweaver']
    # remain metas: {'dmg_increase': '80%'}


class Action20742(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高60%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 60%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20742
    names = ['斗士的秘药(CMN)', 'Essence of the Martialist(CMN)']
    _orig_names = ['斗士的秘药', 'Essence of the Martialist']
    # remain metas: {'dmg_increase': '60%'}


class Action20743(Action):
    # 继承英雄的记忆，令自身发动治疗魔法的治疗量提高60%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases healing potency by 60%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20743
    names = ['Essence of the Savior(CMN)', '治愈者的秘药(CMN)']
    _orig_names = ['Essence of the Savior', '治愈者的秘药']


class Action20744(Action):
    # 继承英雄的记忆，令自身物理防御力提高150%、魔法防御力提高45%、最大体力提高60%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases physical defense by 150%, magic defense by 45%, and maximum HP by 60%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20744
    names = ['Essence of the Veteran(CMN)', '魔战士的秘药(CMN)']
    _orig_names = ['Essence of the Veteran', '魔战士的秘药']


class Action20745(Action):
    # 继承英雄的记忆，令自身防御力提高80%、最大体力提高45%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 80% and maximum HP by 45%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20745
    names = ['重骑兵的秘药(CMN)', 'Essence of the Platebearer(CMN)']
    _orig_names = ['重骑兵的秘药', 'Essence of the Platebearer']


class Action20746(Action):
    # 继承英雄的记忆，令自身防御力提高30%、最大体力提高10%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 30% and maximum HP by 10%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20746
    names = ['守护者的秘药(CMN)', 'Essence of the Guardian(CMN)']
    _orig_names = ['Essence of the Guardian', '守护者的秘药']


class Action20747(Action):
    # 继承英雄的记忆，令自身最大魔力提高50%、发动治疗魔法的治疗量提高25%、发动攻击造成的伤害提高20%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 20%, healing potency by 25%, and maximum MP by 50%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20747
    names = ['祭司的秘药(CMN)', 'Essence of the Ordained(CMN)']
    _orig_names = ['祭司的秘药', 'Essence of the Ordained']
    # remain metas: {'dmg_increase': '20%'}


class Action20748(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高20%、暴击发动率提高15%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 20% and critical hit rate by 15%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20748
    names = ['武人的秘药(CMN)', 'Essence of the Skirmisher(CMN)']
    _orig_names = ['武人的秘药', 'Essence of the Skirmisher']
    # remain metas: {'dmg_increase': '20%、暴击发动率提高15%'}


class Action20749(Action):
    # 继承英雄的记忆，以自身最大体力降低5%为代价，令自身回避率提高40%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Reduces maximum HP by 5% while increasing evasion by 40%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20749
    names = ['Essence of the Watcher(CMN)', '斥候的秘药(CMN)']
    _orig_names = ['Essence of the Watcher', '斥候的秘药']


class Action20750(Action):
    # 继承英雄的记忆，以自身发动治疗魔法的治疗量降低70%为代价，令自身发动攻击造成的伤害提高100%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Reduces healing potency by 70% while increasing damage dealt by 100%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20750
    names = ['Essence of the Profane(CMN)', '破戒僧的秘药(CMN)']
    _orig_names = ['破戒僧的秘药', 'Essence of the Profane']
    # remain metas: {'dmg_increase': '100%'}


class Action20751(Action):
    # 继承英雄的记忆，以自身受到的伤害提高200%、最大体力降低30%为代价，令自身发动攻击造成的伤害提高90%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 90% and damage taken by 200% while reducing maximum HP by 30%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20751
    names = ['Essence of the Irregular(CMN)', '狂战士的秘药(CMN)']
    _orig_names = ['Essence of the Irregular', '狂战士的秘药']
    # remain metas: {'taken_dmg_increase': '200%、最大体力降低30%为代价，令自身发动攻击造成的伤害提高90%'}


class Action20752(Action):
    # 继承英雄的记忆，令自身回避率提高10%，同时提高移动速度和中毒耐性
    # 该移动速度提高效果在骑乘坐骑时也有效
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases poison resistance and movement speed, including mount speed, and increases evasion by 10%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    # related: [移动速度提高(0)](Status1112), [移动速度提高(1)](Status669),
    id = 20752
    names = ['盗贼的秘药(CMN)', 'Essence of the Breathtaker(CMN)']
    _orig_names = ['Essence of the Breathtaker', '盗贼的秘药']


class Action20753(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高40%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 40%.
    # Additional Effect: Absorb a portion of damage dealt as HP
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20753
    names = ['Essence of the Bloodsucker(CMN)', '吸血鬼的秘药(CMN)']
    _orig_names = ['吸血鬼的秘药', 'Essence of the Bloodsucker']
    # remain metas: {'dmg_increase': '40%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态'}


class Action20754(Action):
    # 继承英雄的记忆，令自身防御力提高50%、最大体力提高45%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 50% and maximum HP by 45%.
    # Additional Effect: Absorb a portion of damage dealt as HP
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20754
    names = ['Essence of the Beast(CMN)', '狼人的秘药(CMN)']
    _orig_names = ['狼人的秘药', 'Essence of the Beast']


class Action20755(Action):
    # 继承英雄的记忆，令自身防御力提高50%、最大体力提高45%、发动攻击造成的伤害提高60%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 50%, maximum HP by 45%, and damage dealt by 60%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20755
    names = ['Essence of the Templar(CMN)', '圣骑士的秘药(CMN)']
    _orig_names = ['圣骑士的秘药', 'Essence of the Templar']
    # remain metas: {'dmg_increase': '60%'}


class Action20756(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高96%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 96%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20756
    names = ['Deep Essence of the Aetherweaver(CMN)', '术士的灵药(CMN)']
    _orig_names = ['术士的灵药', 'Deep Essence of the Aetherweaver']
    # remain metas: {'dmg_increase': '96%'}


class Action20757(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高72%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 72%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20757
    names = ['斗士的灵药(CMN)', 'Deep Essence of the Martialist(CMN)']
    _orig_names = ['斗士的灵药', 'Deep Essence of the Martialist']
    # remain metas: {'dmg_increase': '72%'}


class Action20758(Action):
    # 继承英雄的记忆，令自身发动治疗魔法的治疗量提高72%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases healing potency by 72%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20758
    names = ['治愈者的灵药(CMN)', 'Deep Essence of the Savior(CMN)']
    _orig_names = ['治愈者的灵药', 'Deep Essence of the Savior']


class Action20759(Action):
    # 继承英雄的记忆，令自身物理防御力提高180%、魔法防御力提高54%、最大体力提高72%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases physical defense by 180%, magic defense by 54%, and maximum HP by 72%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20759
    names = ['Deep Essence of the Veteran(CMN)', '魔战士的灵药(CMN)']
    _orig_names = ['Deep Essence of the Veteran', '魔战士的灵药']


class Action20760(Action):
    # 继承英雄的记忆，令自身防御力提高96%、最大体力提高54%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 96% and maximum HP by 54%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20760
    names = ['重骑兵的灵药(CMN)', 'Deep Essence of the Platebearer(CMN)']
    _orig_names = ['Deep Essence of the Platebearer', '重骑兵的灵药']


class Action20761(Action):
    # 继承英雄的记忆，令自身防御力提高36%、最大体力提高12%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 36% and maximum HP by 12%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20761
    names = ['Deep Essence of the Guardian (CMN)', '守护者的灵药(CMN)']
    _orig_names = ['Deep Essence of the Guardian ', '守护者的灵药']


class Action20762(Action):
    # 继承英雄的记忆，令自身最大魔力提高60%、发动治疗魔法的治疗量提高30%、发动攻击造成的伤害提高24%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 24%, healing potency by 30%, and maximum MP by 60%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20762
    names = ['祭司的灵药(CMN)', 'Deep Essence of the Ordained(CMN)']
    _orig_names = ['Deep Essence of the Ordained', '祭司的灵药']
    # remain metas: {'dmg_increase': '24%'}


class Action20763(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高24%、暴击发动率提高18%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 24% and critical hit rate by 18%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20763
    names = ['武人的灵药(CMN)', 'Deep Essence of the Skirmisher(CMN)']
    _orig_names = ['Deep Essence of the Skirmisher', '武人的灵药']
    # remain metas: {'dmg_increase': '24%、暴击发动率提高18%'}


class Action20764(Action):
    # 继承英雄的记忆，以自身最大体力降低3%为代价，令自身回避率提高48%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Reduces maximum HP by 3% while increasing evasion by 48%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20764
    names = ['斥候的灵药(CMN)', 'Deep Essence of the Watcher(CMN)']
    _orig_names = ['Deep Essence of the Watcher', '斥候的灵药']


class Action20765(Action):
    # 继承英雄的记忆，以自身发动治疗魔法的治疗量降低70%为代价，令自身发动攻击造成的伤害提高120%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Reduces healing potency by 70% while increasing damage dealt by 120%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20765
    names = ['Deep Essence of the Profane(CMN)', '破戒僧的灵药(CMN)']
    _orig_names = ['破戒僧的灵药', 'Deep Essence of the Profane']
    # remain metas: {'dmg_increase': '120%'}


class Action20766(Action):
    # 继承英雄的记忆，以自身受到的伤害提高200%、最大体力降低30%为代价，令自身发动攻击造成的伤害提高108%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 108% and damage taken by 200% while reducing maximum HP by 30%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20766
    names = ['Deep Essence of the Irregular(CMN)', '狂战士的灵药(CMN)']
    _orig_names = ['Deep Essence of the Irregular', '狂战士的灵药']
    # remain metas: {'taken_dmg_increase': '200%、最大体力降低30%为代价，令自身发动攻击造成的伤害提高108%'}


class Action20767(Action):
    # 继承英雄的记忆，令自身回避率提高20%，同时提高移动速度和中毒耐性
    # 该移动速度提高效果在骑乘坐骑时也有效
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases poison resistance and movement speed, including mount speed, and increases evasion by 20%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    # related: [移动速度提高(0)](Status1112), [移动速度提高(1)](Status669),
    id = 20767
    names = ['盗贼的灵药(CMN)', 'Deep Essence of the Breathtaker(CMN)']
    _orig_names = ['盗贼的灵药', 'Deep Essence of the Breathtaker']


class Action20768(Action):
    # 继承英雄的记忆，令自身发动攻击造成的伤害提高48%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases damage dealt by 48%.
    # Additional Effect: Absorb a portion of damage dealt as HP
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20768
    names = ['Deep Essence of the Bloodsucker(CMN)', '吸血鬼的灵药(CMN)']
    _orig_names = ['吸血鬼的灵药', 'Deep Essence of the Bloodsucker']
    # remain metas: {'dmg_increase': '48%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态'}


class Action20769(Action):
    # 继承英雄的记忆，令自身防御力提高60%、最大体力提高54%，同时附加将自身攻击所造成伤害的一部分转化为自身体力的状态
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 60% and maximum HP by 54%.
    # Additional Effect: Absorb a portion of damage dealt as HP
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20769
    names = ['狼人的灵药(CMN)', 'Deep Essence of the Beast(CMN)']
    _orig_names = ['狼人的灵药', 'Deep Essence of the Beast']


class Action20770(Action):
    # 继承英雄的记忆，令自身防御力提高60%、最大体力提高54%、发动攻击造成的伤害提高72%
    # 无法与其他秘药、灵药系药品同时使用
    # 持续时间：永久
    # Increases defense by 60%, maximum HP by 54%, and damage dealt by 72%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence or Deep Essence actions.
    id = 20770
    names = ['圣骑士的灵药(CMN)', 'Deep Essence of the Templar(CMN)']
    _orig_names = ['圣骑士的灵药', 'Deep Essence of the Templar']
    # remain metas: {'dmg_increase': '72%'}


class Action20940(Action):
    # 恢复自身的体力与能量
    # 体力恢复力：最大体力的40%
    # 能量恢复力：最大能量的30%
    # Restores up to 40% of own HP and 30% of own EP.
    id = 20940
    names = ['Auto Restoration(CMN)', '自我修复(CMN)']
    _orig_names = ['Auto Restoration', '自我修复']
    heal = "最大能量的30%"  # TODO: ['"最大能量的30%"', '"最大体力的40%"']


class Action21324(Action):
    # 鼓舞人工轰击怪的舞蹈
    # Sets a Bombard's heart ablaze. More ablaze than usual, that is.
    id = 21324
    names = ['Enkindling Flame Dance(CMN)', '火焰之舞：燃烧舞步(CMN)']
    _orig_names = ['火焰之舞：燃烧舞步', 'Enkindling Flame Dance']


class Action21325(Action):
    # 促进人工轰击怪自我恢复的舞蹈
    # Fills a Bombard with vim and vigor.
    id = 21325
    names = ['Invigorating Flame Dance(CMN)', '火焰之舞：青磷舞步(CMN)']
    _orig_names = ['火焰之舞：青磷舞步', 'Invigorating Flame Dance']


class Action21494(Action):
    # 对目标发动物理攻击
    # 威力：440
    # Delivers an attack with a potency of 440.
    id = 21494
    names = ['飞刺(CMN)', 'Fleche(CMN)']
    _orig_names = ['Fleche(CMN)', '飞刺(CMN)']
    damage = 440


class Action21495(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：400
    # Delivers an attack with a potency of 400 to target and all enemies nearby it.
    id = 21495
    names = ['Contre Sixte(CMN)(0)', '六分反击(CMN)(0)']
    _orig_names = ['Contre Sixte(CMN)', '六分反击(CMN)']
    damage = 400


class Action21497(Action):
    # 恢复目标的体力
    # 恢复力：350
    # Restores target's HP.
    # Cure Potency: 350
    id = 21497
    names = ['赤治疗(CMN)(0)', 'Vercure(CMN)(0)']
    _orig_names = ['Vercure(CMN)', '赤治疗(CMN)']
    heal = 350


class Action21498(Action):
    # 对目标发动无属性魔法攻击
    # 威力：210
    # Deals unaspected damage with a potency of 210.
    id = 21498
    names = ['Malefic III(CMN)', '祸星(CMN)']
    _orig_names = ['祸星', 'Malefic III']
    damage = 210


class Action21608(Action):
    # 恢复目标的体力
    # 恢复力：400
    # Restores target's HP.
    # Cure Potency: 400
    id = 21608
    names = ['吉星(CMN)', 'Benefic(CMN)']
    _orig_names = ['Benefic', '吉星']
    heal = 400


class Action21609(Action):
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
    # related: [阳星相位](Status836),
    id = 21609
    names = ['Aspected Helios(CMN)', '阳星相位(CMN)']
    _orig_names = ['阳星相位', 'Aspected Helios']
    heal = 200
    # remain metas: {'heal_ot': '100'}


class Action21611(Action):
    # 以自身为中心产生不动宫
    # 范围内的自身及队员所受到的伤害减轻10%
    # 持续时间：18秒
    # 同时，范围内的自身及队员还会附加体力持续恢复的效果
    # 恢复力：100
    # 持续时间：15秒
    # 效果时间内发动技能或进行移动、转身都会使不动宫立即消失
    # 发动之后会停止自动攻击
    # Creates a fixed sign centered around the caster, reducing damage taken by 10% for self and any party members who enter.
    # Duration: 18s
    # Additional Effect: Healing over time
    # Cure Potency: 100
    # Duration: 15s
    # Effect ends upon using another action or moving (including facing a different direction).
    # Cancels auto-attack upon execution.
    # related: [不动宫(0)](Status2640), [不动宫(1)](Status2641), [不动宫(2)](Status2639),
    id = 21611
    names = ['不动宫(CMN)', 'Fixed Sign(CMN)']
    _orig_names = ['Fixed Sign', '不动宫']
    # remain metas: {'taken_dmg_reduce': '10%', 'heal_ot': '100'}


class Action21852(Action):
    # 对目标发动冰属性魔法攻击
    # 威力：300
    # 追加效果：恢复自身最大魔力的40%
    # Deals ice damage with a potency of 300.
    # Additional Effect: Restores up to 40% of MP
    id = 21852
    names = ['亚拉戈冰澈(CMN)', 'Allagan Blizzard IV(CMN)']
    _orig_names = ['Allagan Blizzard IV', '亚拉戈冰澈']
    damage = 300


class Action21884(Action):
    # 对目标及其周围敌人发动雷属性范围魔法攻击
    # 威力：200
    # 追加效果：雷属性持续伤害
    # 威力：30
    # 持续时间：18秒
    # Deals lightning damage with a potency of 200 to target and all enemies nearby it.
    # Additional Effect: Lightning damage over time
    # Potency: 30
    # Duration: 18s
    #
    # related: [霹雷](Status1210),
    id = 21884
    names = ['霹雷(CMN)', 'Thunder IV(CMN)']
    _orig_names = ['霹雷', 'Thunder IV']
    damage = 200
    # remain metas: {'dmg_ot': '30'}


class Action21886(Action):
    # 恢复目标的体力
    # 恢复力：700
    # Restores target's HP.
    # Cure Potency: 700
    id = 21886
    names = ['Cure II(CMN)', '救疗(CMN)']
    _orig_names = ['Cure II', '救疗']
    heal = 700


class Action21888(Action):
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
    # related: [医济](Status150),
    id = 21888
    names = ['Medica II(CMN)', '医济(CMN)']
    _orig_names = ['Medica II', '医济']
    heal = 200
    # remain metas: {'heal_ot': '100'}


class Action21921(Action):
    # 阻碍自身周围的敌人
    # 石化效果：一定时间内阻碍目标的移动与咏唱，可以封禁敌人的所有行动
    # Prevents spellcasting, movement, and other activity of all nearby enemies.
    # related: [石化(0)](Status1), [石化(1)](Status610), [石化(2)](Status1511), [石化(3)](Status2573),
    id = 21921
    names = ['石化(CMN)', 'Break(CMN)']
    _orig_names = ['石化', 'Break']


class Action22344(Action):
    # 发现自身周围15米内隐藏的陷阱
    # 若周围15米内没有陷阱，则可以获知周围36米内是否存在陷阱
    # ※仅可在女王古殿内使用
    # Detect traps within a radius of 15 yalms.
    # If there are no traps within 15 yalms, alerts you to the presence of traps with a radius of 36 yalms.
    # ※This action can only be used in Delubrum Reginae.
    id = 22344
    names = ['Lost Perception(CMN)', '失传探景(CMN)']
    _orig_names = ['Lost Perception', '失传探景']


class Action22345(Action):
    # 复活目标并恢复其全部体力
    # 追加效果：对自己附加“献祭”
    # 持续时间：10秒
    # 献祭效果：持续时间结束后自身将陷入无法战斗的状态
    # 发动条件：非“献祭”状态中
    # Restores all of a KO'd target's HP.
    # Cannot be executed if currently afflicted with Sacrifice.
    # Additional Effect: Inflicts Sacrifice on self
    # Sacrifice Effect: When effect expires, you will be KO'd
    # Duration: 10s
    # related: [献祭](Status1743),
    id = 22345
    names = ['失传献祭(CMN)', 'Lost Sacrifice(CMN)']
    _orig_names = ['Lost Sacrifice', '失传献祭']


class Action22346(Action):
    # 继承英雄的记忆，令自身回避率提高11%、暴击发动率提高77%、直击发动率提高77%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases evasion by 11%, critical hit rate by 77%, and direct hit rate by 77%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22346
    names = ['胜负师的仙药(CMN)', 'Pure Essence of the Gambler(CMN)']
    _orig_names = ['胜负师的仙药', 'Pure Essence of the Gambler']


class Action22347(Action):
    # 继承英雄的记忆，令自身防御力提高25%、最大体力提高100%、发动攻击造成的伤害提高50%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases defense by 25%, damage dealt by 50%, and maximum HP by 100%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22347
    names = ['Pure Essence of the Elder(CMN)', '贤者的仙药(CMN)']
    _orig_names = ['Pure Essence of the Elder', '贤者的仙药']
    # remain metas: {'dmg_increase': '50%'}


class Action22348(Action):
    # 继承英雄的记忆，令自身防御力提高60%、最大体力提高81%、发动攻击造成的伤害提高60%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases defense by 60%, damage dealt by 60%, and maximum HP by 81%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22348
    names = ['剑豪的仙药(CMN)', 'Pure Essence of the Duelist(CMN)']
    _orig_names = ['剑豪的仙药', 'Pure Essence of the Duelist']
    # remain metas: {'dmg_increase': '60%'}


class Action22349(Action):
    # 继承英雄的记忆，令自身防御力提高60%、最大体力提高81%、发动攻击造成的伤害提高50%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases defense by 60%, damage dealt by 50%, and maximum HP by 81%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22349
    names = ['Pure Essence of the Fiendhunter(CMN)', '弓圣的仙药(CMN)']
    _orig_names = ['弓圣的仙药', 'Pure Essence of the Fiendhunter']
    # remain metas: {'dmg_increase': '50%'}


class Action22350(Action):
    # 继承英雄的记忆，令自身防御力提高40%、最大体力提高50%、发动攻击造成的伤害提高72%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases defense by 40%, damage dealt by 72%, and maximum HP by 50%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22350
    names = ['豪杰的仙药(CMN)', 'Pure Essence of the Indomitable(CMN)']
    _orig_names = ['Pure Essence of the Indomitable', '豪杰的仙药']
    # remain metas: {'dmg_increase': '72%'}


class Action22351(Action):
    # 继承英雄的记忆，令自身防御力提高25%、最大体力提高100%、发动攻击造成的伤害提高35%
    # 无法与其他秘药、灵药、仙药系药品同时使用
    # 持续时间：永久
    # 据说仙药具有不为人知的隐藏效果
    # ※仅可在女王古殿内使用
    # Increases defense by 25%, damage dealt by 35%, and maximum HP by 100%.
    # Effect ends upon reuse.
    # Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
    # It is said that Pure Essences may grant unexpected effects...
    # ※This action can only be used in Delubrum Reginae.
    id = 22351
    names = ['圣人的仙药(CMN)', 'Pure Essence of the Divine(CMN)']
    _orig_names = ['圣人的仙药', 'Pure Essence of the Divine']
    # remain metas: {'dmg_increase': '35%'}


class Action22352(Action):
    # 消耗魔力对周围的敌人发动无属性范围魔法攻击
    # 威力：300
    # 追加效果：无属性持续伤害
    # 威力：350
    # 持续时间：60秒
    # 失传耀星的持续伤害效果只能同时附加1个
    # Consumes MP to deal unaspected damage with a potency of 300 to all nearby enemies.
    # Additional Effect: Unaspected damage over time
    # Potency: 350
    # Duration: 60s
    # The damage over time effect of Lost Flare Star can only be applied once per target at any given time. This effect cannot be stacked by multiple players.
    # related: [失传耀星](Status2440),
    id = 22352
    names = ['失传耀星(CMN)', 'Lost Flare Star(CMN)']
    _orig_names = ['失传耀星', 'Lost Flare Star']
    damage = 300
    # remain metas: {'dmg_ot': '350'}


class Action22353(Action):
    # 扑向目标并以目标为中心发动物理伤害
    # 威力：100
    # 追加效果：目标所受伤害提高10%
    # 持续时间：30秒
    # 止步状态下无法发动
    # Delivers a jumping attack with a potency of 100.
    # Additional Effect: Increases target's damage taken by 10%.
    # Duration: 30s
    # Cannot be executed while bound.
    # related: [失传破甲](Status2441),
    id = 22353
    names = ['Lost Rend Armor(CMN)', '失传破甲(CMN)']
    _orig_names = ['Lost Rend Armor', '失传破甲']
    damage = 100
    # remain metas: {'taken_dmg_increase': '10%'}


class Action22354(Action):
    # 消耗魔力扑向目标并以目标为中心发动魔法攻击
    # 威力：500
    # 止步状态下无法发动
    # 追加效果：目标的命中率降低10%
    # 持续时间：15秒
    # 追加效果：对自身附加战姿
    # 战姿效果：以自身体力恢复效果降低60%为代价，令自身发动攻击造成的伤害提高60%
    # 持续时间：15秒
    # Consumes MP to deliver a jumping attack that deals unaspected damage with a potency of 500.
    # Additional Effect: Reduces target's accuracy by 10%.
    # Duration: 15s
    # Additional Effect: Grants Cleric Stance to self.
    # Cleric Stance Bonus: Reduces healing potency by 60% while increasing damage dealt by 60%.
    # Duration: 15s
    # Cannot be executed while bound.
    # related: [战姿(0)](Status145), [战姿(1)](Status2484),
    id = 22354
    names = ['Lost Seraph Strike(CMN)', '失传炽天强袭(CMN)']
    _orig_names = ['Lost Seraph Strike', '失传炽天强袭']
    damage = 500
    # remain metas: {'dmg_increase': '60%'}


class Action22355(Action):
    # 一定时间内令自己与周围队员受到的伤害减轻30%
    # 持续时间：15秒
    # Reduces damage taken by self and nearby party members by 30%.
    # Duration: 15s
    # related: [失传以太之盾](Status2443),
    id = 22355
    names = ['失传以太之盾(CMN)', 'Lost Aethershield(CMN)']
    _orig_names = ['失传以太之盾', 'Lost Aethershield']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action22356(Action):
    # 一定时间内，自身与周围队员的暴击发动率提高10%，攻击造成的伤害提高7%，自动攻击间隔、战技与魔法的咏唱及复唱时间缩短1%
    # 持续时间：60秒
    # Increases critical hit rate of self and nearby party members by 10%, increases damage dealt by 7%, and reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 1%.
    # Duration: 60s
    # related: [失传速度之星](Status2444),
    id = 22356
    names = ['失传速度之星(CMN)', 'Lost Dervish(CMN)']
    _orig_names = ['Lost Dervish', '失传速度之星']
    # remain metas: {'dmg_increase': '7%，自动攻击间隔、战技与魔法的咏唱及复唱时间缩短1%'}


class Action23345(Action):
    # 喷出亚永恒吐息
    # 演出技能，没有任何实际效果
    # Unleash an Eternal Breath...sort-of.
    # ※Has no effect in battle.
    id = 23345
    names = ['亚永恒吐息(CMN)', 'Semi-eternal Breath(CMN)']
    _orig_names = ['亚永恒吐息', 'Semi-eternal Breath']


class Action23907(Action):
    # 发动返回效果
    # 发动条件：自身处于非战斗状态
    # 与战技和魔法共享复唱时间
    # Instantly return to the starting point of the area.
    # Cannot be executed while in combat.
    # Shares a recast timer with all other weaponskills and spells.
    id = 23907
    names = ['Lodestone(CMN)', '返回磁石(CMN)']
    _orig_names = ['返回磁石', 'Lodestone']


class Action23908(Action):
    # 为自身与周围队员附加能够抵御一定伤害的防护罩
    # 该防护罩能够抵消相当于目标最大体力10%的伤害量
    # 持续时间：30秒
    # Creates a barrier around self and all party members near you that absorbs damage totaling 10% of maximum HP.
    # Duration: 30s
    id = 23908
    names = ['失传坚石肤(CMN)', 'Lost Stoneskin II(CMN)']
    _orig_names = ['失传坚石肤', 'Lost Stoneskin II']
    # remain metas: {'shield': '目标最大体力10%'}


class Action23909(Action):
    # 对自身周围的敌人发动雷属性范围魔法攻击
    # 威力：300
    # 追加效果：中断目标的技能咏唱
    # 对弱魔法的敌人发动追加效果
    # 追加效果：目标所受伤害提高10%
    # 持续时间：60秒
    # Deals lightning damage with a potency of 300 to all nearby enemies.
    # Additional Effect: Interrupts all nearby enemies
    # Additional Effect: Increases damage taken by enemies with Magical Aversion by 10%
    # Duration: 60s
    # related: [失传磁暴](Status2558),
    id = 23909
    names = ['Lost Burst(CMN)', '失传磁暴(CMN)']
    _orig_names = ['失传磁暴', 'Lost Burst']
    damage = 300
    # remain metas: {'taken_dmg_increase': '10%'}


class Action23910(Action):
    # 对自身周围的敌人发动范围物理攻击
    # 威力：300
    # 追加效果：中断目标的技能咏唱
    # 对弱物理的敌人发动追加效果
    # 追加效果：目标所受伤害提高10%
    # 持续时间：60秒
    # Delivers an attack with a potency of 300 to all nearby enemies.
    # Additional Effect: Interrupts all nearby enemies
    # Additional Effect: Increases damage taken by enemies with Physical Aversion by 10%
    # Duration: 60s
    # related: [失传暴怒](Status2559),
    id = 23910
    names = ['Lost Rampage(CMN)', '失传暴怒(CMN)']
    _orig_names = ['失传暴怒', 'Lost Rampage']
    damage = 300
    # remain metas: {'taken_dmg_increase': '10%'}


class Action23911(Action):
    # 对自身附加失传反射状态
    # 失传反射效果：反射除特定攻击之外的所有魔法
    # 持续时间：10秒
    # 与战技和魔法共享复唱时间
    # Grants the effect of Lost Reflect to self.
    # Lost Reflect Effect: Reflects most magic attacks
    # Duration: 10s
    # Shares a recast timer with all other weaponskills and spells.
    # related: [失传反射](Status2337),
    id = 23911
    names = ['光之幕帘(CMN)', 'Light Curtain(CMN)']
    _orig_names = ['Light Curtain', '光之幕帘']


class Action23912(Action):
    # 对自身或一名玩家附加重生状态
    # 重生效果：持续时间内若陷入无法战斗状态，有80%几率自动复活
    # 持续时间：180分
    # Grants the effect of Reraise to self or target player.
    # Reraise Effect: Grants an 80% chance of automatic revival upon KO
    # Duration: 180m
    # related: [重生](Status2355),
    id = 23912
    names = ['失传重生(CMN)', 'Lost Reraise(CMN)']
    _orig_names = ['Lost Reraise', '失传重生']


class Action23913(Action):
    # 一定时间内，咏唱魔法不需要咏唱时间
    # 持续时间：30秒
    # 发动条件：自身处于战斗状态
    # 追加效果：对自身附加魔法爆发状态
    # 魔法爆发效果：以自身消耗的魔力增加为代价，令魔法类技能攻击时造成的伤害提高45%
    # 持续时间：30秒
    # 祭司的药状态中追加效果：魔法爆发的消耗魔力增加量变为0，同时造成的伤害提高为100%
    # 斥候的药状态中追加效果：失传连锁咏唱的持续时间变为90秒
    # Temporarily eliminates cast time for all spells.
    # Duration: 30s
    # Additional Effect: Magic Burst
    # Magic Burst Effect: Increases spell damage by 45% while increasing MP cost
    # Duration: 30s
    # Spirit of the Ordained Effect: Raises Magic Burst spell damage increase to 100% and nullifies additional MP cost
    # Spirit of the Watcher Effect: Lost Chainspell duration is extended to 90s
    # Can only be executed while in combat.
    # related: [失传连锁咏唱](Status2560), [魔法爆发](Status1652), [祭司的药](Status2317), [斥候的药](Status2319),
    id = 23913
    names = ['Lost Chainspell(CMN)', '失传连锁咏唱(CMN)']
    _orig_names = ['失传连锁咏唱', 'Lost Chainspell']
    # remain metas: {'dmg_increase': ['为100%', '45%']}


class Action23914(Action):
    # 对目标发动近距离物理攻击
    # 威力：350
    # 背面攻击追加效果：一定几率令目标陷入无法战斗状态，目标剩余体力越少成功率越高
    # 狼人的药状态中追加效果：对自身附加失传力泉状态
    # 失传力泉效果：自身发动攻击造成的伤害提高30%，同时暴击发动率提高40%
    # 持续时间：18秒
    # 该战技有单独计算的复唱时间，不受其他战技与魔法的复唱时间影响
    # Delivers a close-quarter attack with a potency of 350. Chance of instant KO when attacking from the rear, which increases the lower the target's HP.
    # Spirit of the Beast Effect: Grants the effect of Lost Font of Power to self
    # Lost Font of Power Effect: Increases damage dealt by 30% and critical hit rate by 40%
    # Duration: 18s
    # This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
    # related: [失传力泉](Status2346), [狼人的药](Status2324),
    id = 23914
    names = ['Lost Assassination(CMN)', '失传暗杀(CMN)']
    _orig_names = ['Lost Assassination', '失传暗杀']
    damage = 350
    # remain metas: {'dmg_increase': '30%，同时暴击发动率提高40%'}


class Action23915(Action):
    # 指定自身或其他一名玩家，附加物理伤害减轻15%的防护罩
    # 持续时间：30分
    # Applies a barrier to self or target player reducing physical damage taken by 15%.
    # Duration: 30m
    # related: [失传护盾II](Status2561),
    id = 23915
    names = ['失传护盾II(CMN)', 'Lost Protect II(CMN)']
    _orig_names = ['失传护盾II', 'Lost Protect II']
    # remain metas: {'taken_dmg_reduce': '15%的防护罩'}


class Action23916(Action):
    # 指定自身或其他一名玩家，附加魔法伤害减轻15%的防护罩
    # 持续时间：30分
    # Applies a barrier to self or target player reducing magic damage taken by 15%.
    # Duration: 30m
    # related: [失传魔盾II](Status2562),
    id = 23916
    names = ['Lost Shell II(CMN)', '失传魔盾II(CMN)']
    _orig_names = ['失传魔盾II', 'Lost Shell II']
    # remain metas: {'taken_dmg_reduce': '15%的防护罩'}


class Action23917(Action):
    # 指定自身或其他一名玩家，使其最大体力提高30%
    # 持续时间：600秒
    # Increases maximum HP of self or target player by 30%.
    # Duration: 600s
    # related: [失传生机](Status2563),
    id = 23917
    names = ['失传生机(CMN)', 'Lost Bubble(CMN)']
    _orig_names = ['失传生机', 'Lost Bubble']


class Action23918(Action):
    # 迅速移动到自身前方10米处
    # 止步状态下无法发动
    # 追加效果：对自身与周围队员附加失传敏捷状态
    # 失传敏捷效果：令自身的移动速度大幅提高
    # 同时附加了其他移动速度提高的效果时，仅能适用其中1种
    # 持续时间：10秒
    # 盗贼的药状态中追加效果：令自身与周围队员回避率提高15%
    # 持续时间：60秒
    # 斥候的药状态中追加效果：对自身与周围队员附加高速复唱状态
    # 高速复唱效果：效果时间内，自身发动的1次能力类技能复唱时间缩短25%
    # 持续时间：15秒
    # Quickly dash 10 yalms forward.
    # Additional Effect: Applies Lost Swift to self and nearby party members
    # Lost Swift Effect: Greatly increases movement speed
    # Effect cannot be stacked with other movement speed enhancing abilities.
    # Duration: 10s
    # Spirit of the Breathtaker Effect: Increases evasion of self and nearby party members by 15%
    # Duration: 60s
    # Spirit of the Watcher Effect: Grants Rapid Recast to self and nearby party members
    # Rapid Recast Effect: Shortens recast time for next ability used by 25%
    # Effect only applies to certain abilities.
    # Duration: 15s
    # Cannot be executed while bound.
    # related: [盗贼的药](Status2322), [失传敏捷](Status2335), [高速复唱](Status1645), [斥候的药](Status2319),
    id = 23918
    names = ['失传推进(CMN)', 'Lost Impetus(CMN)']
    _orig_names = ['失传推进', 'Lost Impetus']


class Action23919(Action):
    # 使用时解除衰弱状态，一定时间内，除特定攻击之外其他所有对自身发动的攻击均无效，同时自身发动攻击造成的伤害提高65%
    # ※无法解除濒死状态
    # 持续时间：10秒
    # 发动条件：自身处于战斗状态
    # 持续时间结束后对自身附加英杰状态
    # 英杰效果：自身发动攻击造成的伤害提高65%，同时被攻击时受到的伤害减轻10%
    # 持续时间：50秒
    # Instantly cures Weakness and temporarily nullifies most attacks, while increasing damage dealt by 65%. Memorable will be applied when effect ends.
    # Duration: 10s
    # Memorable Effect: Increases damage dealt by 65% while decreasing damage taken by 10%
    # Duration: 50s
    # Can only be executed while in combat.
    # related: [濒死(0)](Status2738), [失传卓异](Status2564), [英杰](Status2565), [衰弱](Status43), [濒死(1)](Status44),
    id = 23919
    names = ['失传卓异(CMN)', 'Lost Excellence(CMN)']
    _orig_names = ['失传卓异', 'Lost Excellence']
    # remain metas: {'dmg_increase': ['65%，同时被攻击时受到的伤害减轻10%', '65%'], 'taken_dmg_reduce': '10%'}


class Action23920(Action):
    # 令自身及周围队员的体力和魔力完全恢复
    # 追加效果：对自身及周围队员附加自动恢复药和自动以太药状态
    # 自动恢复药效果：效果时间内体力低于50%时自动恢复
    # 持续时间：600秒
    # 发动恢复效果后有50%的几率解除自动恢复药
    # 盗贼的药状态中追加效果：发动恢复效果后解除自动恢复药状态的几率变为10%
    # 自动以太药效果：效果时间内魔力低于20%时自动恢复
    # 持续时间：600秒
    # 发动恢复效果后有50%的几率解除自动以太药
    # 盗贼的药状态中追加效果：发动恢复效果后解除自动以太药状态的几率变为10%
    # Fully restores HP and MP while granting Auto-potion and Auto-ether to self and nearby party members.
    # Auto-potion Effect: Restores HP automatically when HP falls below 50%
    # Duration: 600s
    # When triggered, there is a 50% chance the effect will end.
    # Auto-ether Effect: Restores MP automatically when MP falls below 20%
    # Duration: 600s
    # When triggered, there is a 50% chance the effect will end.
    # Spirit of the Breathtaker Effect: Chance for Auto-potion and Auto-ether effect to end is reduced to 10%
    # related: [盗贼的药](Status2322), [自动恢复药](Status2342), [自动以太药](Status2343),
    id = 23920
    names = ['失传痊愈(CMN)', 'Lost Full Cure(CMN)']
    _orig_names = ['失传痊愈', 'Lost Full Cure']


class Action23921(Action):
    # 对自身附加失传血怒状态
    # 失传血怒效果：每档攻击伤害提高15%、所受伤害减轻5%，效果时间内发动突进移动系技能可以增加档数，同时刷新持续时间
    # 持续时间：18秒
    # 发动条件：自身处于战斗状态
    # 最大档数：4档
    # 档数最大时失传血怒会变为血怒觉醒
    # 血怒觉醒效果：攻击伤害提高60%，同时持续恢复体力和魔力，效果时间内发动的能力类技能复唱时间缩短75%
    # 持续时间：30秒
    # Increases damage dealt by 15% and reduces damage taken by 5% per stack. Stacks increase with each use of a dash attack while effect is active, to a maximum of 4.
    # Duration: 18s
    # Maximum stacks grant the effect of Blood Rush.
    # Blood Rush Effect: Increases damage dealt by 60%, shortens recast times by 75%, and gradually restores HP and MP. Recast time reduction does not apply to charged actions.
    # Duration: 30s
    # Can only be executed while in combat.
    # related: [失传血怒](Status2566), [血怒觉醒](Status2567),
    id = 23921
    names = ['Lost Blood Rage(CMN)', '失传血怒(CMN)']
    _orig_names = ['Lost Blood Rage', '失传血怒']
    # remain metas: {'taken_dmg_reduce': '5%，效果时间内发动突进移动系技能可以增加档数，同时刷新持续时间', 'dmg_increase': ['60%，同时持续恢复体力和魔力，效果时间内发动的能力类技能复唱时间缩短75%', '15%、所受伤害减轻5%，效果时间内发动突进移动系技能可以增加档数，同时刷新持续时间']}


class Action23922(Action):
    # 令自身体力和魔力完全恢复
    # 与义军恢复药、命运骰子共享复唱时间
    # Restores own HP and MP to maximum.
    # Shares a recast timer with Resistance Potion and Dynamis Dice.
    id = 23922
    names = ['Resistance Elixir(CMN)', '义军圣灵药(CMN)']
    _orig_names = ['义军圣灵药', 'Resistance Elixir']


class Action24276(Action):
    # 投射巨大的冰花
    # 演出技能，没有任何实际效果
    # Create a shower of delicate frozen crystals.
    # ※Has no effect in battle.
    id = 24276
    names = ['Crystal Ice(CMN)', '冰花(CMN)']
    _orig_names = ['冰花', 'Crystal Ice']


class Action24277(Action):
    # 对肌肉莫古力用肉体之美
    # Do as the Mighty Moogle and show the fine specimen that you are to all present.
    id = 24277
    names = ['肌肉肌肉(CMN)', 'Mighty Maximizer(CMN)']
    _orig_names = ['Mighty Maximizer', '肌肉肌肉']


class Action24278(Action):
    # 对蓬松陆行鸟用指戳
    # Do as the Chirpy Chocobo and point and acknowledge─because safety is paramount.
    id = 24278
    names = ['蓬松蓬松(CMN)', 'Chirpy Checker(CMN)']
    _orig_names = ['Chirpy Checker', '蓬松蓬松']


class Action24279(Action):
    # 对转圈波奇用张望
    # Do as the Perky Piggy and keep your eyes peeled for hidden treasure.
    id = 24279
    names = ['转圈转圈(CMN)', 'Perky Peeler(CMN)']
    _orig_names = ['转圈转圈', 'Perky Peeler']


class Action24619(Action):
    # 进行射击，可以对黑色的墙壁或柱子造成伤害
    # Unleash a digital barrage that damages black walls and pylons.
    id = 24619
    names = ['Liminal Fire(CMN)(0)', '射击(CMN)(0)']
    _orig_names = ['射击', 'Liminal Fire']


class Action24620(Action):
    # 进行射击，可以对白色的墙壁或柱子造成伤害
    # Unleash a digital barrage that damages white walls and pylons.
    id = 24620
    names = ['Liminal Fire(CMN)(1)', '射击(CMN)(1)']
    _orig_names = ['射击', 'Liminal Fire']


class Action24621(Action):
    # 反转自身的色相
    # Swap your color.
    id = 24621
    names = ['色相反转(CMN)(0)', 'F-0 Switch(CMN)(0)']
    _orig_names = ['色相反转', 'F-0 Switch']


class Action24622(Action):
    # 反转自身的色相
    # Swap your color.
    id = 24622
    names = ['色相反转(CMN)(1)', 'F-0 Switch(CMN)(1)']
    _orig_names = ['色相反转', 'F-0 Switch']


class Action25880(Action):
    # 令目标及其周围的敌人陷入睡眠状态
    # 持续时间：30秒
    # 发动之后会停止自动攻击
    # Puts target and all nearby enemies to sleep.
    # Duration: 30s
    # Cancels auto-attack upon execution.
    # related: [睡眠(0)](Status3), [睡眠(1)](Status1348), [睡眠(2)](Status1510), [(1)](Status2983), [睡眠(3)](Status1363), [睡眠(4)](Status1947), [睡眠(5)](Status1596), [睡眠(6)](Status926),
    id = 25880
    names = ['催眠(CMN)', 'Sleep(CMN)']
    _orig_names = ['催眠', 'Sleep']


class Action26224(Action):
    # 恢复目标的体力
    # 恢复力：400
    # Restores target's HP.
    # Cure Potency: 400
    id = 26224
    names = ['Diagnosis(CMN)', '诊断(CMN)']
    _orig_names = ['诊断', 'Diagnosis']
    heal = 400


class Action26225(Action):
    # 一定时间内，自身发动魔法攻击造成的伤害提高5%
    #  持续时间：20秒
    # 追加效果：令周围队员发动物理攻击造成的伤害提高5%
    # 持续时间：20秒
    # Increases own magic damage dealt by 5% and damage dealt by nearby party members by 5%.
    # Duration: 20s
    # related: [鼓励(0)](Status1297), [鼓励(1)](Status1239), [鼓励(2)](Status2282),
    id = 26225
    names = ['Embolden(CMN)', '鼓励(CMN)']
    _orig_names = ['鼓励(CMN)', 'Embolden(CMN)']
    # remain metas: {'dmg_increase': '5%'}


class Action26231(Action):
    # 向指定地点附近发射魔导加农炮
    # Fires cannon at the designated area.
    id = 26231
    names = ['Magitek Cannon(CMN)(3)', '魔导加农炮(CMN)(3)']
    _orig_names = ['Magitek Cannon', '魔导加农炮']


class Action26232(Action):
    # 向指定地点附近发射魔导加农散弹炮
    # Fires diffractive cannon at the designated area.
    id = 26232
    names = ['Diffractive Magitek Cannon(CMN)(1)', '魔导加农散弹炮(CMN)(1)']
    _orig_names = ['Diffractive Magitek Cannon', '魔导加农散弹炮']


class Action26233(Action):
    # 向自身前方发射高功率魔导加农炮
    # Fires a concentrated burst of energy in a forward direction.
    id = 26233
    names = ['High-powered Magitek Cannon(CMN)(1)', '高功率魔导加农炮(CMN)(1)']
    _orig_names = ['High-powered Magitek Cannon', '高功率魔导加农炮']


class Action26252(Action):
    # 一定时间内，自身发动物理攻击造成的伤害提高25%
    # 持续时间：25秒
    # Increases physical damage dealt by 25%.
    # Duration: 25s
    # related: [战逃反应](Status76),
    id = 26252
    names = ['Fight or Flight(CMN)(1)', '战逃反应(CMN)(1)']
    _orig_names = ['战逃反应(CMN)', 'Fight or Flight(CMN)']
    # remain metas: {'dmg_increase': '25%'}


class Action26253(Action):
    # 一定时间内，将自身所受的伤害减轻10%
    # 持续时间：20秒
    # Reduces damage taken by 10%.
    # Duration: 20s
    # related: [铁壁(1)](Status71), [铁壁(0)](Status1191), [铁壁(2)](Status1978),
    id = 26253
    names = ['铁壁(CMN)(1)', 'Rampart(CMN)(1)']
    _orig_names = ['铁壁', 'Rampart']
    # remain metas: {'taken_dmg_reduce': '10%'}


class Action26890(Action):
    # 发射妖异厌恶的光
    # Emits a wavelength of light that voidsent absolutely detest.
    id = 26890
    names = ['Fiendish Lantern(CMN)', '退魔提灯(CMN)']
    _orig_names = ['Fiendish Lantern', '退魔提灯']


class Action26891(Action):
    # 泼洒圣水，解放被囚禁的灵魂
    # Frees captured souls.
    id = 26891
    names = ['Healing Holy Water(CMN)', '导魂圣水(CMN)']
    _orig_names = ['导魂圣水', 'Healing Holy Water']


class Action26988(Action):
    # 为了找出风脉泉位置的仪器。
    # Examine your aether compass to deduce the proximate location of nearby aether currents.
    id = 26988
    names = ['风脉仪(CMN)', 'the Aether Compass(CMN)']
    _orig_names = ['风脉仪', 'the Aether Compass']


class Action27042(Action):
    # 恢复目标的体力
    # 恢复力：300
    # 追加效果：为目标附加能够抵御一定伤害的防护罩
    # 抵消相当于治疗量125%的伤害
    # 持续时间：30秒
    # Restores target's HP.
    # Cure Potency: 300
    # Additional Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored
    # Duration: 30s
    #
    id = 27042
    names = ['Leveilleur Diagnosis(CMN)', '莱韦耶勒尔诊断(CMN)']
    _orig_names = ['莱韦耶勒尔诊断', 'Leveilleur Diagnosis']
    heal = 300
    # remain metas: {'shield': '治疗量125%'}


class Action27043(Action):
    # 恢复自身及周围队员的体力
    #  恢复力：300
    # Restores own HP and the HP of all nearby party members.
    # Cure Potency: 300
    #
    id = 27043
    names = ['预后(CMN)', 'Prognosis(CMN)']
    _orig_names = ['Prognosis', '预后']
    heal = 300


class Action27044(Action):
    # 恢复目标的体力
    # 恢复力：600
    #
    # Restores target's HP.
    # Cure Potency: 600
    id = 27044
    names = ['Leveilleur Druochole(CMN)', '莱韦耶勒尔灵橡清汁(CMN)']
    _orig_names = ['莱韦耶勒尔灵橡清汁', 'Leveilleur Druochole']
    heal = 600


class Action27045(Action):
    # 对目标发动无属性魔法攻击
    # 威力：300
    # Deals unaspected damage with a potency of 300.
    id = 27045
    names = ['注药III(CMN)', 'Dosis III(CMN)']
    _orig_names = ['Dosis III', '注药III']
    damage = 300


class Action27046(Action):
    # 対象とその周囲の敵に無属性範囲魔法攻撃。
    # 威力：300
    # 対象とその周囲の敵に無属性範囲魔法攻撃。
    # 威力：300
    id = 27046
    names = ['ルヴェユール・トキシコンII(CMN)']
    _orig_names = ['ルヴェユール・トキシコンII']
    damage = 300


class Action27047(Action):
    # 对目标及其周围的敌人发动无属性范围魔法攻击
    # 威力：260
    # Deals unaspected damage with a potency of 260 to target and all enemies nearby it.
    id = 27047
    names = ['Leveilleur Toxikon(CMN)', '莱韦耶勒尔箭毒(CMN)']
    _orig_names = ['Leveilleur Toxikon', '莱韦耶勒尔箭毒']
    damage = 260


class Action27053(Action):
    # 对自身周围的敌人发动无属性范围魔法攻击
    # 威力：200
    # Deals unaspected damage with a potency of 200 to all nearby enemies.
    id = 27053
    names = ['Crimson Savior(CMN)(1)', '深红救世(CMN)(1)']
    _orig_names = ['深红救世', 'Crimson Savior']
    damage = 200


class Action27060(Action):
    # 对目标及其周围敌人发动范围物理攻击
    # 威力：400
    # Delivers an attack with a potency of 400 to target and all enemies nearby it.
    id = 27060
    names = ['Contre Sixte(CMN)(1)', '六分反击(CMN)(1)']
    _orig_names = ['Contre Sixte(CMN)', '六分反击(CMN)']
    damage = 400


class Action27061(Action):
    # 恢复目标的体力
    # 恢复力：350
    # Restores target's HP.
    # Cure Potency: 350
    id = 27061
    names = ['Vercure(CMN)(1)', '赤治疗(CMN)(1)']
    _orig_names = ['Vercure(CMN)', '赤治疗(CMN)']
    heal = 350


class Action27062(Action):
    # 向目标所在方向发出直线无属性范围魔法攻击
    #
    # Deals unaspected damage to all enemies in a straight line before you.
    id = 27062
    names = ['Vermilion Pledge(CMN)', '赤红诺言(CMN)']
    _orig_names = ['Vermilion Pledge', '赤红诺言']


class Action27315(Action):
    # 恢复自身最大体力的35%
    # Restores 35% of maximum HP.
    id = 27315
    names = ['Medical Kit(CMN)', '军用恢复药(CMN)']
    _orig_names = ['军用恢复药', 'Medical Kit']


class Action27430(Action):
    # 一定时间内，将自身所受的伤害减轻30%
    #  持续时间：15秒
    # Reduces damage taken by 30%.
    # Duration: 15s
    # related: [星云](Status1834),
    id = 27430
    names = ['星云(CMN)(1)', 'Nebula(CMN)(1)']
    _orig_names = ['星云', 'Nebula']
    # remain metas: {'taken_dmg_reduce': '30%'}


class Action27432(Action):
    # 完全切断自身的气息，迅速移动。
    # 持续时间：10秒
    # 发动条件：自身处于非战斗状态
    # Masks your presence, making it impossible for most enemies to detect you, and increases movement speed. Cannot be cast while in combat.
    # Duration: 10s
    # related: [疾隐](Status2957),
    id = 27432
    names = ['疾隐(CMN)', 'Swift Deception(CMN)']
    _orig_names = ['Swift Deception', '疾隐']


class Action27433(Action):
    # 在切断自身气息的状态下对帝国兵施展强袭，瞬间击倒对象。
    # 该效果对魔导兵器以及军犬无效，只能给予伤害。
    # 威力：100
    # 发动条件：疾隐效果中
    # While hidden, delivers an attack that neutralizes imperial soldiers. When the target is magitek weaponry or a guard dog, delivers an attack with a potency of 100.
    # Can only be executed while under the effect of Swift Deception.
    # related: [疾隐](Status2957),
    id = 27433
    names = ['Silent Takedown(CMN)', '终招(CMN)']
    _orig_names = ['Silent Takedown', '终招']
    damage = 100


class Action27434(Action):
    # 投掷含有刺激嗅觉成分的干扰弹，致使军犬丧失战斗能力。
    # 对帝国兵以及魔导兵器无效
    # Throws a bomb that confuses the senses of guard dogs, neutralizing them. Has no effect on imperial soldiers or magitek weaponry.
    id = 27434
    names = ['Bewilderment Bomb(CMN)', '嗅觉干扰弹(CMN)']
    _orig_names = ['Bewilderment Bomb', '嗅觉干扰弹']


class Action28302(Action):
    # 召唤出八只幼崽。
    # 演出技能，没有任何实际效果
    # Temporarily summons your paissa's eight brats (and counting).
    # ※Has no effect in battle.
    id = 28302
    names = ['Family Outing(CMN)', '家族活动(CMN)']
    _orig_names = ['家族活动', 'Family Outing']


class Action28439(Action):
    # 对目标附加无属性持续伤害状态
    # 威力：70
    # 持续时间：30秒
    # Deals unaspected damage over time.
    # Potency: 70
    # Duration: 30s
    # related: [莱韦耶勒尔注药III](Status2650),
    id = 28439
    names = ['莱韦耶勒尔注药III(CMN)', 'Leveilleur Dosis III(CMN)']
    _orig_names = ['Leveilleur Dosis III', '莱韦耶勒尔注药III']
    # remain metas: {'dmg_ot': '70'}
