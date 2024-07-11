juesedengji = 1
jueseshengming = 30
juesefangyu = 25
juesegongji = 35
chongwudengji = 1
chongwushengming = 5
chongwufangyu = 5
chongwugongji = 10
shengli = 0
shibai = 0
jinbi = 0
mingchengku = ["小偷", "山贼", "强盗", "恶魔"]
tiandi = []
beibao = []
zhongzhiwu = 0
jiayuanxuanze = 0
ewaijinbi = 0
lianxichangxuanze = 0
baoxiangleibie = 0
jinengxuanze = 0
zongdengji = 0
direnmingcheng = 0
direnshengming = 0
direnfangyu = 0
direngongji = 0
wofangshengming = 0
wofangfangyu = 0
wofanggongji = 0
jineng=["战斗","魔法（每次使用消耗最高生命的20%，攻击时增加15%）"]
jinengshangdian=["连发（攻击加倍）","快速（使敌人一回合攻击力降低%35，并进行普通攻击）","恢复（恢复当前生命的1.25倍）"]
suoxujinbi=[1000,1350,600]
renwu = ["达到2级（加20攻击）","达到3级（加20防御）","达到5级（赠送50金币）","达到10级（土地自由（增加50田地））","达到25级（加666生命）","达到100级（金币自由（加10000金币））"]
renwuxuanze = 0
tiaozhanxuanze = 0
queding = 0



print("欢迎体验勇者战斗游戏")
# 函数定义
def x1(d, s, f, g):
    print("角色等级：")
    print(d)
    print("角色生命：")
    print(s)
    print("角色防御：")
    print(f)
    print("角色攻击：")
    print(g)


def x2(d, s, f, g):
    print("宠物老虎等级：")
    print(d)
    print("宠物老虎生命：")
    print(s)
    print("宠物老虎防御：")
    print(f)
    print("宠物老虎攻击：")
    print(g)


def x3(d, s, f, g):
    print("总等级：")
    print(d)
    print("总生命：")
    print(s)
    print("总防御：")
    print(f)
    print("总攻击：")
    print(g)


def x4(juesedengji, jueseshengming, juesefangyu, juesegongji, chongwudengji, chongwushengming, chongwufangyu,
       chongwugongji, shengli, shibai, jinbi, tiandi, zongfangyu, zonggongji, direnshengming, direnfangyu, direngongji,
       direnmingcheng, wofangshengming):
    global ewaijinbi
    import random
    direnshengming = random.randint(zongshengming - zongdengji * 5, zongshengming + zongdengji * 10)
    import random
    direnfangyu = random.randint(zongfangyu - zongdengji * 5, zongfangyu + zongdengji * 10)
    import random
    direngongji = random.randint(zonggongji - zongdengji * 5, zonggongji + zongdengji * 10)
    import random
    direnmingcheng = random.choice(mingchengku)
    wofangshengming = zongshengming
    huihe = 0
    ewaijinbi = 0
    # 主循环
    while wofangshengming >= 0 and direnshengming >= 0:
        print("回合数：", end='')
        print(huihe)
        print("敌人名称：")
        print(direnmingcheng)
        print("敌人生命：")
        print(direnshengming)
        print("敌人防御：")
        print(direnfangyu)
        print("敌人攻击：")
        print(direngongji)
        print("")
        print("我方生命：")
        print(wofangshengming)
        print("我方防御：")
        print(zongfangyu)
        print("我方攻击：")
        print(zonggongji)
        print("")
        huihe = huihe + 1
        zuozhanxuanze = int(input(str(jineng)+"请输入编号"))
        if jineng[zuozhanxuanze-1] == "战斗":
            print("战斗--造成攻击：")
            print(zonggongji - direnfangyu)
            direnshengming = direnshengming - (zonggongji - direnfangyu)
        elif jineng[zuozhanxuanze-1] == "魔法（每次使用消耗最高生命的20%，攻击时增加15%）":
            wofangshengming = wofangshengming - jueseshengming * 0.2
            print("魔法--造成攻击：")
            print(zonggongji * 1.15 - direnfangyu)
            direnshengming = direnshengming - (zonggongji * 1.15 - direnfangyu)
        elif jineng[zuozhanxuanze-1] == "连发（攻击加倍）":
            print("连发--造成攻击：")
            print(zonggongji*2 - direnfangyu)
            direnshengming = direnshengming - (zonggongji*2 - direnfangyu)
        elif jineng[zuozhanxuanze-1] == "快速（使敌人一回合攻击力降低%35，并进行普通攻击）":
            print("快速--造成攻击：")
            print(zonggongji - direnfangyu)
            direnshengming = direnshengming - (zonggongji - direnfangyu)
            continue
        elif jineng[zuozhanxuanze-1] == "恢复（恢复当前生命的1.25倍）":
            print("恢复--当前生命：")
            wofangshengming = wofangshengming*1.25
            print(wofangshengming)
        if direnshengming <= 0:
            break
        print("")
        print("对方开始攻击")
        print("造成攻击：")
        print(direngongji - zongfangyu)
        wofangshengming = wofangshengming - (direngongji - zongfangyu)

    # 结束时统计
    if direnshengming <= 0:
        print("胜利！奖励已放入。")
        print("回合数：", end='')
        print(huihe)
        juesedengji = juesedengji + 1
        jueseshengming = jueseshengming + 30
        juesefangyu = juesefangyu + 25
        juesegongji = juesegongji + 35
        chongwudengji = chongwudengji + 1
        chongwushengming = chongwushengming + 5
        chongwufangyu = chongwufangyu + 5
        chongwugongji = chongwugongji + 10
        shengli = shengli + 1
        ewaijinbi = 0
        if juesedengji >= 5:
            jinbi = jinbi + 5
            for z in range(len(tiandi)):
                if tiandi[z] == "胜利树":
                    jinbi = jinbi + 5
                    ewaijinbi = ewaijinbi + 5

    elif wofangshengming <= 0:
        shibai = shibai + 1
        print("很遗憾，失败了，再来一次吧！")
        if juesedengji >= 5:
            jinbi = jinbi + 1
    for z in range(len(tiandi)):
        if tiandi[z] == "局数树":
            jinbi = jinbi + 2
            ewaijinbi = ewaijinbi + 2
        if tiandi[z] == "回合树":
            jinbi = jinbi+3*huihe
            ewaijinbi = ewaijinbi + 3*huihe
    print("你因为种植田地而额外获得了（金币）：{}".format(ewaijinbi))
    # 返回参数
    return juesedengji, jueseshengming, juesefangyu, juesegongji, shengli, shibai, jinbi


def x7(shengli, shibai):
    print("胜利次数：", end='')
    print(shengli)
    print("失败次数:", end='')
    print(shibai)
    print("胜率(%):", end='')
    if shibai == 0:
        print(100)
    else:
        print(round(shengli / (shengli + shibai) * 100, 3))


def x8():
    global jiayuanxuanze, jinbi, zhongzhiwu
    if juesedengji >= 5:
        while True:
            print("现在你有", end='')
            print(jinbi, end='')
            print("金币")
            jiayuanxuanze = int(input("你要：1、购买 2、查看 3、种植 4、退出"))
            if jiayuanxuanze == 1:
                print("家园商店")
                jiayuanxuanze = int(input(
                    "1、空地（可以种植） 10金币  2、胜利树（战斗胜利后额外获得5金币） 20金币 3、局数树（每战斗一局后额外获得2金币） 20金币 4、回合树（每和怪物交战一回合获得3金币）20金币 5、退出"))
                if jiayuanxuanze == 1:
                    if jinbi >= 10:
                        jinbi = jinbi - 10
                        tiandi.append("空地")
                    else:
                        print("金币不够了")
                elif jiayuanxuanze == 2:
                    if jinbi >= 20:
                        jinbi = jinbi - 20
                        xunzhao = 0
                        for i in range(len(tiandi)):
                            if tiandi[i] == "空地":
                                print("有空地，已自动植入")
                                tiandi[i] = "胜利树"
                                xunzhao = 1
                                break
                        if xunzhao == 0:
                            print("没有空地，已放入背包")
                            beibao.append("胜利树")
                elif jiayuanxuanze == 3:
                    if jinbi >= 20:
                        jinbi = jinbi - 20
                        xunzhao = 0
                        for i in range(len(tiandi)):
                            if tiandi[i] == "空地":
                                print("有空地，已自动植入")
                                tiandi[i] = "局数树"
                                xunzhao = 1
                                break
                        if xunzhao == 0:
                            print("没有空地，已放入背包")
                            beibao.append("局数树")
                elif jiayuanxuanze == 4:
                    if jinbi >= 20:
                        jinbi = jinbi - 20
                        xunzhao = 0
                        for i in range(len(tiandi)):
                            if tiandi[i] == "空地":
                                print("有空地，已自动植入")
                                tiandi[i] = "回合树"
                                xunzhao = 1
                                break
                        if xunzhao == 0:
                            print("没有空地，已放入背包")
                            beibao.append("回合树")
            elif jiayuanxuanze == 2:
                print("田地:")
                print(tiandi)
                print("背包:")
                print(beibao)
            elif jiayuanxuanze == 3:
                print("田地:")
                print(tiandi)
                print("背包:")
                print(beibao)
                xunzhao = 0
                zhongzhiwu = int(input("你要种植的编号(退出输0)："))
                if zhongzhiwu == 0:
                    break
                zhongzhiwu = beibao[zhongzhiwu - 1]
                for i in range(len(beibao)):
                    if beibao[i] == zhongzhiwu:
                        for j in range(len(tiandi)):
                            if tiandi[j] == "空地":
                                print("种植成功！")
                                tiandi[j] = zhongzhiwu
                                xunzhao = 1
                                break
                    if xunzhao == 1:
                        del beibao[i]
                        break
                if xunzhao == 0:
                    print("种植失败（可能是因为背包里没有或没有空地了）")
                print("现在田地:")
                print(tiandi)
                print("现在背包:")
                print(beibao)
            elif jiayuanxuanze == 4:
                break
    else:
        print("你的角色等级还没到5级")


def x9():
    global lianxichangxuanze, jinbi, jueseshengming, juesefangyu, juesegongji
    print("已进入练习场：")
    print("你现在有（金币）：{}".format(jinbi))
    lianxichangxuanze = int(input("1、加10生命（金币20） 2、加10防御（金币30） 3、加10攻击（金币30） 4、退出"))
    if lianxichangxuanze == 1:
        if jinbi >= 20:
            jinbi = jinbi - 20
            jueseshengming = jueseshengming + 10
            print("已加入10生命")
        else:
            print("金币不够了")
    elif lianxichangxuanze == 2:
        if jinbi >= 30:
            jinbi = jinbi - 30
            juesefangyu = juesefangyu + 10
            print("已加入10防御")
        else:
            print("金币不够了")
    elif lianxichangxuanze == 3:
        if jinbi >= 30:
            jinbi = jinbi - 30
            juesegongji = juesegongji + 10
            print("已加入10攻击")
        else:
            print("金币不够了")
    else:
        pass


def x10():
    global baoxiangleibie, jinbi, jueseshengming, juesefangyu, juesegongji
    print("你有现在有（金币）：{}".format(jinbi))
    baoxiangleibie = int(input(
        "1、小宝箱（10金币） 2、中宝箱（20金币） 3、大宝箱（30金币） 4、超大宝箱（40金币） 5、超级大宝箱（50金币） 6、退出 7、内容"))
    #宝箱
    if baoxiangleibie == 1:
        if jinbi >= 10:
            import random

            jinbi = jinbi - 10
            baoxiangleibie = random.randint(1, 10)
            if baoxiangleibie == 1:
                jinbi = jinbi + 15
                print("获得金币+15")
            elif baoxiangleibie == 2:
                jueseshengming = jueseshengming + 5
                print("获得角色生命+5")
            elif baoxiangleibie == 3:
                jinbi = jinbi + 5
                print("获得金币+5")
            elif baoxiangleibie == 4:
                juesefangyu = juesefangyu + 3
                print("获得角色防御+3")
            elif baoxiangleibie == 5:
                beibao.append("胜利树")
                print("获得胜利树+1")
            elif baoxiangleibie == 6:
                beibao.append("空地")
                print("获得空地+1")
            elif baoxiangleibie == 7:
                juesegongji = juesegongji + 5
                print("获得角色防御+5")
            elif baoxiangleibie == 8:
                tiandi.append("空地")
                tiandi.append("空地")
                print("获得空地+2")
            elif baoxiangleibie == 9:
                jinbi = jinbi + 10
                print("获得金币+10")
            elif baoxiangleibie == 10:
                jueseshengming = jueseshengming + 7
                print("获得角色生命+7")
        else:
            print("金币不够了")
    if baoxiangleibie == 2:
        if jinbi >= 20:
            import random

            jinbi = jinbi - 20
            baoxiangleibie = random.randint(1, 10)
            if baoxiangleibie == 1:
                jinbi = jinbi + 30
                print("获得金币+30")
            elif baoxiangleibie == 2:
                jueseshengming = jueseshengming + 10
                print("获得角色生命+10")
            elif baoxiangleibie == 3:
                jinbi = jinbi + 15
                print("获得金币+15")
            elif baoxiangleibie == 4:
                juesefangyu = juesefangyu + 6
                print("获得角色防御+6")
            elif baoxiangleibie == 5:
                beibao.append("胜利树")
                beibao.append("空地")
                print("获得胜利树+1、空地+1")
            elif baoxiangleibie == 6:
                beibao.append("空地")
                jinbi = jinbi + 10
                print("获得空地+1、金币+10")
            elif baoxiangleibie == 7:
                juesegongji = juesegongji + 10
                print("获得角色攻击+10")
            elif baoxiangleibie == 8:
                tiandi.append("空地")
                tiandi.append("空地")
                tiandi.append("空地")
                print("获得空地+3")
            elif baoxiangleibie == 9:
                jinbi = jinbi + 25
                print("获得金币+25")
            elif baoxiangleibie == 10:
                jueseshengming = jueseshengming + 10
                print("获得角色生命+10")
        else:
            print("金币不够了")
    elif baoxiangleibie == 3:
        if jinbi >= 30:
            import random

            jinbi = jinbi - 30
            baoxiangleibie = random.randint(1, 10)
            if baoxiangleibie == 1:
                jinbi = jinbi + 35
                print("获得金币+35")
            elif baoxiangleibie == 2:
                jueseshengming = jueseshengming + 20
                print("获得角色生命+20")
            elif baoxiangleibie == 3:
                jinbi = jinbi + 20
                print("获得金币+20")
            elif baoxiangleibie == 4:
                juesefangyu = juesefangyu + 10
                print("获得角色防御+10")
            elif baoxiangleibie == 5:
                beibao.append("胜利树")
                jinbi = jinbi + 8
                beibao.append("空地")
                print("获得胜利树+1、空地+1、金币+8")
            elif baoxiangleibie == 6:
                tiandi.append("空地")
                beibao.append("胜利树")
                jinbi = jinbi + 2
                print("获得空地+1、金币+2、胜利树+1")
            elif baoxiangleibie == 7:
                juesegongji = juesegongji + 10
                jinbi = jinbi + 10
                print("获得角色攻击+10、金币+10")
            elif baoxiangleibie == 8:
                tiandi.append("空地")
                tiandi.append("空地")
                tiandi.append("空地")
                beibao.append("胜利树")
                print("获得空地+3、胜利树+1")
            elif baoxiangleibie == 9:
                jinbi = jinbi + 30
                print("获得金币+30")
            elif baoxiangleibie == 10:
                jueseshengming = jueseshengming + 20
                print("获得角色生命+20")
        else:
            print("金币不够了")
    elif baoxiangleibie == 4:
        if jinbi >= 40:
            import random

            jinbi = jinbi - 30
            baoxiangleibie = random.randint(1, 10)
            if baoxiangleibie == 1:
                jinbi = jinbi + 45
                print("获得金币+45")
            elif baoxiangleibie == 2:
                jueseshengming = jueseshengming + 25
                print("获得角色生命+25")
            elif baoxiangleibie == 3:
                jinbi = jinbi + 30
                print("获得金币+30")
            elif baoxiangleibie == 4:
                juesefangyu = juesefangyu + 15
                print("获得角色防御+15")
            elif baoxiangleibie == 5:
                beibao.append("胜利树")
                jinbi = jinbi + 16
                beibao.append("空地")
                print("获得胜利树+1、空地+1、金币+16")
            elif baoxiangleibie == 6:
                tiandi.append("空地")
                beibao.append("胜利树")
                jinbi = jinbi + 5
                print("获得空地+1、金币+5、胜利树+1")
            elif baoxiangleibie == 7:
                juesegongji = juesegongji + 15
                jinbi = jinbi + 20
                print("获得角色攻击+15、金币+20")
            elif baoxiangleibie == 8:
                tiandi.append("空地")
                tiandi.append("空地")
                tiandi.append("空地")
                beibao.append("胜利树")
                print("获得空地+3、胜利树+1")
            elif baoxiangleibie == 9:
                jinbi = jinbi + 35
                print("获得金币+35")
            elif baoxiangleibie == 10:
                jueseshengming = jueseshengming + 20
                print("获得角色生命+20")
        else:
            print("金币不够了")
    elif baoxiangleibie == 5:
        if jinbi >= 40:
            import random

            jinbi = jinbi - 30
            baoxiangleibie = random.randint(1, 10)
            if baoxiangleibie == 1:
                jinbi = jinbi + 45
                print("获得金币+55")
            elif baoxiangleibie == 2:
                jueseshengming = jueseshengming + 30
                print("获得角色生命+30")
            elif baoxiangleibie == 3:
                jinbi = jinbi + 40
                print("获得金币+40")
            elif baoxiangleibie == 4:
                juesefangyu = juesefangyu + 20
                print("获得角色防御+20")
            elif baoxiangleibie == 5:
                beibao.append("胜利树")
                jinbi = jinbi + 16
                beibao.append("空地")
                beibao.append("空地")
                print("获得胜利树+1、空地+2、金币+16")
            elif baoxiangleibie == 6:
                tiandi.append("空地")
                beibao.append("胜利树")
                jinbi = jinbi + 10
                print("获得空地+1、金币+10、胜利树+1")
            elif baoxiangleibie == 7:
                juesegongji = juesegongji + 18
                jinbi = jinbi + 20
                print("获得角色攻击+18、金币+20")
            elif baoxiangleibie == 8:
                tiandi.append("空地")
                tiandi.append("空地")
                tiandi.append("空地")
                beibao.append("胜利树")
                jinbi = jinbi + 10
                print("获得空地+3、胜利树+1")
            elif baoxiangleibie == 9:
                jinbi = jinbi + 45
                print("获得金币+45")
            elif baoxiangleibie == 10:
                jueseshengming = jueseshengming + 25
                print("获得角色生命+25")
        else:
            print("金币不够了")
    elif baoxiangleibie == 6:
        pass
    elif baoxiangleibie == 7:
        print("小宝箱：")
        print(
            "可能获得:金币+15/角色生命+5/金币+5/角色防御+3/胜利树+1/空地+1/角色防御+5/空地+2/金币+10/角色生命+7")
        print("中宝箱：")
        print(
            "可能获得:金币+30/角色生命+10/金币+15/角色防御+6/胜利树+1、空地+1/空地+1、金币+10/角色攻击+10/空地+3/金币+25/角色生命+10")
        print("大宝箱：")
        print(
            "可能获得:金币+35/角色生命+20/金币+20/角色防御+10/胜利树+1、空地+1、金币+8/空地+1、金币+2、胜利树+1/角色攻击+10、金币+10/空地+3、胜利树+1/金币+30/角色生命+20")
        print("超大宝箱：")
        print(
            "可能获得：金币+45/角色生命+25/金币+30/角色防御+15/胜利树+1、空地+1、金币+16/空地+1、金币+5、胜利树+1/角色攻击+15、金币+20/空地+3、胜利树+1/金币+35/角色生命+20")
        print("超级大宝箱：")
        print(
            "可能获得：金币+55/角色生命+30/金币+40/角色防御+20/胜利树+1、空地+2、金币+16/空地+1、金币+10、胜利树+1/角色攻击+18、金币+20/空地+3、胜利树+1、金币+10/金币+45/角色生命+25")


def x11():
    global jinengxuanze,goumai,jinbi
    jinengxuanze = int(input("1、查看技能 2、购买技能 3、退出"))
    if jinengxuanze == 1:
        print(jineng)
    elif jinengxuanze == 2:
        print("商店：{}".format(jinengshangdian))
        print("金额：{}".format(suoxujinbi))
        print("你拥有的技能：{}".format(jineng))
        print("你目前的金币：{}".format(jinbi))
        goumai = int(input("你要购买的编号：(0为不买)"))
        if goumai == 0:
            pass
        else:
            if jinbi>=suoxujinbi[goumai-1]:
                jinbi-=suoxujinbi[goumai-1]
                jineng.append(jinengshangdian[goumai-1])
                del jinengshangdian[goumai-1]
                del suoxujinbi[goumai-1]
                print("购买成功！")
            else:
                print("金币不够了")
    else:
        pass

def x12():
    global juesegongji,juesefangyu,juesedengji,tiandi,jueseshengming,jinbi
    print("达到指定项，即可获得奖励")
    print("任务：")
    print(renwu)
    renwuxuanze = int(input("请输入需要兑换的编号（退出输0）："))
    if renwuxuanze == 0:
        pass
    else:
        if renwu[renwuxuanze-1] == "达到2级（加20攻击）":
            if juesedengji>=2:
                juesegongji+=20
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")
        elif renwu[renwuxuanze-1] == "达到3级（加20防御）":
            if juesedengji>=3:
                juesefangyu+=20
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")
        elif renwu[renwuxuanze - 1] == "达到5级（赠送50金币）":
            if juesedengji>=5:
                jinbi+=50
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")
        elif renwu[renwuxuanze - 1] == "达到10级（土地自由（增加50空地））":
            if juesedengji>=10:
                for t in range(50):
                    tiandi.append("空地")
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")
        elif renwu[renwuxuanze - 1] == "达到25级（加666生命）":
            if juesedengji>=25:
                jueseshengming+=666
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")
        elif renwu[renwuxuanze - 1] == "达到100级（金币自由（加10000金币））":
            if juesedengji>=100:
                jinbi+=10000
                print("兑换成功！")
                del renwu[renwuxuanze-1]
            else:
                print("还未达到要求")

def x13():
    global jinbi,wofangshengming,direnshengming,juesedengji,jueseshengming,wofangfangyu,chongwugongji,chongwufangyu,chongwushengming,chongwudengji
    global wofanggongji,juesefangyu,juesegongji,ewaijinbi,shengli,shibai
    if juesedengji>=10:
        print("挑战模式")
        print("你来到了一个地方，这个地方有一个很小的村子。\n你进村后，发现大家都说这里时常有妖怪出现\n你听见后，决定要留下来帮助他们除妖。")
        while True:
            tiaozhanxuanze=int(input("1、退出 2、开始战斗 3、规则"))
            if tiaozhanxuanze==1:
                break
            elif tiaozhanxuanze==2:
                if jinbi>=50:
                    jinbi-=50
                    print("金币已扣除，开始战斗！")
                    huihe=0
                    direnshengming = 2375481
                    direnfangyu = 999
                    direngongji = 3421
                    wofanggongji=juesegongji
                    wofangfangyu=juesefangyu
                    wofangshengming=jueseshengming
                    while wofangshengming >= 0 and direnshengming >= 0:
                        print("回合数：", end='')
                        print(huihe)
                        print("敌人名称：")
                        print("妖怪")
                        print("敌人生命：")
                        print(direnshengming)
                        print("敌人防御：")
                        print(direnfangyu)
                        print("敌人攻击：")
                        print(direngongji)
                        print("")
                        print("我方生命：")
                        print(wofangshengming)
                        print("我方防御：")
                        print(zongfangyu)
                        print("我方攻击：")
                        print(zonggongji)
                        print("")
                        huihe = huihe + 1
                        zuozhanxuanze = int(input(str(jineng) + "请输入编号"))
                        if jineng[zuozhanxuanze - 1] == "战斗":
                            print("战斗--造成攻击：")
                            print(zonggongji - direnfangyu)
                            direnshengming = direnshengming - (zonggongji - direnfangyu)
                        elif jineng[zuozhanxuanze - 1] == "魔法（每次使用消耗最高生命的20%，攻击时增加15%）":
                            wofangshengming = wofangshengming - jueseshengming * 0.2
                            print("魔法--造成攻击：")
                            print(zonggongji * 1.15 - direnfangyu)
                            direnshengming = direnshengming - (zonggongji * 1.15 - direnfangyu)
                        elif jineng[zuozhanxuanze - 1] == "连发（攻击加倍）":
                            print("连发--造成攻击：")
                            print(zonggongji * 2 - direnfangyu)
                            direnshengming = direnshengming - (zonggongji * 2 - direnfangyu)
                        elif jineng[zuozhanxuanze - 1] == "快速（使敌人一回合攻击力降低%35，并进行普通攻击）":
                            print("快速--造成攻击：")
                            print(zonggongji - direnfangyu)
                            direnshengming = direnshengming - (zonggongji - direnfangyu)
                            print("")
                            print("对方开始攻击")
                            print("造成攻击：")
                            print(direngongji*0.65 - zongfangyu)
                            wofangshengming = wofangshengming - (direngongji*0.65 - zongfangyu)
                            continue
                        elif jineng[zuozhanxuanze - 1] == "恢复（恢复当前生命的1.25倍）":
                            print("恢复--当前生命：")
                            wofangshengming = wofangshengming * 1.25
                            print(wofangshengming)
                        if direnshengming <= 0:
                            break
                        print("")
                        print("对方开始攻击")
                        print("造成攻击：")
                        print(direngongji - zongfangyu)
                        wofangshengming = wofangshengming - (direngongji - zongfangyu)
                    if direnshengming <= 0:
                        print("胜利！奖励已放入。")
                        print("回合数：", end='')
                        print(huihe)
                        juesedengji = juesedengji + 1
                        jueseshengming = jueseshengming + 30
                        juesefangyu = juesefangyu + 25
                        juesegongji = juesegongji + 35
                        chongwudengji = chongwudengji + 1
                        chongwushengming = chongwushengming + 5
                        chongwufangyu = chongwufangyu + 5
                        chongwugongji = chongwugongji + 10
                        shengli = shengli + 1
                        ewaijinbi = 0
                        jinbi = jinbi + 5
                        for z in range(len(tiandi)):
                            if tiandi[z] == "胜利树":
                                jinbi = jinbi + 5
                                ewaijinbi = ewaijinbi + 5
                        jinbi+=10000
                        print("村民资助10000金币已放入")
                    elif wofangshengming <= 0:
                        shibai = shibai + 1
                        print("很遗憾，失败了，再来一次吧！")
                        if juesedengji >= 5:
                            jinbi = jinbi + 1
                        tiandi.append("空地")
                    for z in range(len(tiandi)):
                        if tiandi[z] == "局数树":
                            jinbi = jinbi + 2
                            ewaijinbi = ewaijinbi + 2
                        if tiandi[z] == "回合树":
                            jinbi = jinbi + 3 * huihe
                            ewaijinbi = ewaijinbi + 3 * huihe
                    print("你因为种植田地而额外获得了（金币）：{}".format(ewaijinbi))
                else:
                    print("金币不够了")
            elif tiaozhanxuanze==3:
                print("这里的妖怪十分强大，生命很高，防御也不少，攻击也没有差到哪里\n想要和他打，就要有很多生命和攻击\n如果你想和他战斗，就要花费50金币来准备\n当然，如果你打赢了，可以获得10000金币的村民资助,而且正常奖励照旧\n如果你打输了，也可以在村里获得属于自己的一块地\n快点开始吧！")
    else:
        print("等级到达10级才能解锁此模块")



#主程序
while True:
    try:
        xuanze = int(input(
            "1、角色查看 2、宠物老虎查看 3、总值查看 4、战斗 5、规则 6、退出 7、胜率查看 8、田地 9、练习场 10、宝箱 11、技能 12、任务 13、挑战模式"))
        zongdengji = juesedengji + chongwudengji
        zongshengming = jueseshengming + chongwushengming
        zongfangyu = juesefangyu + chongwufangyu
        zonggongji = juesegongji + chongwugongji
        if xuanze == 1:
            x1(juesedengji, jueseshengming, juesefangyu, juesegongji)
        elif xuanze == 2:
            x2(chongwudengji, chongwushengming, chongwufangyu, chongwugongji)
        elif xuanze == 3:
            x3(zongdengji, zongshengming, zongfangyu, zonggongji)
        elif xuanze == 4:
            juesedengji, jueseshengming, juesefangyu, juesegongji, shengli, shibai, jinbi = x4(juesedengji,
                                                                                               jueseshengming,
                                                                                               juesefangyu, juesegongji,
                                                                                               chongwudengji,
                                                                                               chongwushengming,
                                                                                               chongwufangyu,
                                                                                               chongwugongji, shengli,
                                                                                               shibai, jinbi, tiandi,
                                                                                               zongfangyu, zonggongji,
                                                                                               direnshengming,
                                                                                               direnfangyu, direngongji,
                                                                                               direnmingcheng,
                                                                                               wofangshengming)
        elif xuanze == 5:
            print("查看选项可以得知各种我方数据。")
            print("战斗中，战斗选项是使用原数据进行计算。")
            print("金币计算规则：角色等级到5级以上时，在战斗中胜利一次+5，失败一次+1")
            print("田地里可以进行购买、种植，具体见家园商店")
            print("任务中的等级指角色等级")
        elif xuanze == 6:
            queding=int(input("确定退出吗？1、确定 2、取消（退出后保存记录，但下次不录入）"))
            if queding == 1:
                f = open("text.txt","w",encoding="UTF-8")
                try:
                    f.write("金币：{}\n等级：{}\n攻击：{}\n防御：{}\n生命：{}\n田地：{}\n技能：{}\n胜率：{}\n总局数：{}".format(jinbi,juesedengji,juesegongji,juesefangyu,jueseshengming,tiandi,jineng,shengli/(shengli+shibai)*100,shengli+shibai))
                except:
                    f.write("金币：{}\n等级：{}\n攻击：{}\n防御：{}\n生命：{}\n田地：{}\n技能：{}\n胜率：{}\n总局数：{}".format(jinbi,juesedengji,juesegongji,juesefangyu,jueseshengming,tiandi,jineng,100,shengli + shibai))
                f.close()
                break
            else:
                pass
        elif xuanze == 7:
            x7(shengli, shibai)
        elif xuanze == 8:
            x8()
        elif xuanze == 9:
            x9()
        elif xuanze == 10:
            x10()
        elif xuanze == 11:
            x11()
        elif xuanze == 12:
            x12()
        elif xuanze == 13:
            x13()
        print("\n")
    except Exception as e:
        print(e)
        print("抱歉，程序出错")
        pass
print("欢迎再次体验。")
