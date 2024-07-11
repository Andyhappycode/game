juesedengji=1
jueseshengming=30
juesefangyu=25
juesegongji=35
chongwudengji=1
chongwushengming=5
chongwufangyu=5
chongwugongji=10
shengli=0
shibai=0
jinbi=0
mingchengku=["小偷","山贼","强盗","恶魔"]
tiandi=[]
beibao=[]
zhongzhiwu=0
jiayuanxuanze=""
ewaijinbi=0
lianxichangxuanze=0
print("欢迎体验勇者战斗游戏")
while True:
    try:
        import random
        xuanze=int(input("1、角色查看 2、宠物老虎查看 3、总值查看 4、战斗 5、规则 6、退出 7、胜率查看 8、田地 9、练习场"))
        zongdengji=juesedengji+chongwudengji
        zongshengming=jueseshengming+chongwushengming
        zongfangyu=juesefangyu+chongwufangyu
        zonggongji=juesegongji+chongwugongji
        direnshengming=random.randint(zongshengming-zongdengji*5,zongshengming+zongdengji*10)
        import random
        direnfangyu=random.randint(zongfangyu-zongdengji*5,zongfangyu+zongdengji*10)
        import random
        direngongji=random.randint(zonggongji-zongdengji*5,zonggongji+zongdengji*10)
        import random
        direnmingcheng=random.choice(mingchengku)
        wofangshengming=zongshengming
        if xuanze==1:
            print("角色等级：")
            print(juesedengji)
            print("角色生命：")
            print(jueseshengming)
            print("角色防御：")
            print(juesefangyu)
            print("角色攻击：")
            print(juesegongji)
        elif xuanze==2:
            print("宠物老虎等级：")
            print(chongwudengji)
            print("宠物老虎生命：")
            print(chongwushengming)
            print("宠物老虎防御：")
            print(chongwufangyu)
            print("宠物老虎攻击：")
            print(chongwugongji)
        elif xuanze==3:
            print("总等级：")
            print(zongdengji)
            print("总生命：")
            print(zongshengming)
            print("总防御：")
            print(zongfangyu)
            print("总攻击：")
            print(zonggongji)
        elif xuanze==4:
            huihe=1
            while wofangshengming>=0 and direnshengming>=0:
                print("回合数：",end='')
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
                zuozhanxuanze=int(input("1、战斗 2、魔法（每次使用消耗最高生命的20%，攻击时增加15%）"))
                if zuozhanxuanze==1:
                    print("战斗--造成攻击：")
                    print(zonggongji-direnfangyu)
                    direnshengming=direnshengming-(zonggongji-direnfangyu)
                else:
                    wofangshengming=wofangshengming-jueseshengming*0.2
                    print("魔法--造成攻击：")
                    print(zonggongji*1.15-direnfangyu)
                direnshengming=direnshengming-(zonggongji*1.15-direnfangyu)
                print("")
                print("对方开始攻击")
                print("造成攻击：")
                print(direngongji-zongfangyu)
                wofangshengming=wofangshengming-(direngongji-zongfangyu)
                huihe=huihe+1
            if direnshengming<=0:
                print("胜利！奖励已放入。")
                print("回合数：",end='')
                print(huihe)
                juesedengji=juesedengji+1
                jueseshengming=jueseshengming+30
                juesefangyu=juesefangyu+25
                juesegongji=juesegongji+35
                chongwudengji=chongwudengji+1
                chongwushengming=chongwushengming+5
                chongwufangyu=chongwufangyu+5
                chongwugongji=chongwugongji+10
                shengli=shengli+1
                ewaijinbi=0
                if juesedengji>=10:
                    jinbi=jinbi+5
                    for z in range(len(tiandi)):
                        if tiandi[z]=="胜利树":
                            jinbi=jinbi+5
                            ewaijinbi=ewaijinbi+5
                    print("你因为种植田地而额外获得了（金币）：{}".format(ewaijinbi))
            elif wofangshengming<=0:
                shibai=shibai+1
                print("很遗憾，失败了，再来一次吧！")
                if juesedengji>=10:
                    jinbi=jinbi+1
        elif xuanze==5:
            print("查看选项可以得知各种我方数据。")
            print("战斗中，战斗选项是使用原数据进行计算。")
            print("金币计算规则：角色等级到5级以上时，在战斗中胜利一次+5，失败一次+1")
            print("田地里可以进行购买、种植，具体见家园商店")
        elif xuanze==6:
            break
        elif xuanze==7:
            print("胜利次数：",end='')
            print(shengli)
            print("失败次数:",end='')
            print(shibai)
            print("胜率(%):",end='')
            if shibai==0:
                print(100)
            else:
                print(round(shengli/(shengli+shibai)*100,3))
        elif xuanze==8:
            if juesedengji>=5:
                while True:
                    #开发中
                    print("现在你有",end='')
                    print(jinbi,end='')
                    print("金币")
                    jiayuanxuanze=int(input("你要：1、购买 2、查看 3、种植 4、退出"))
                    if jiayuanxuanze==1:
                        print("家园商店")
                        jiayuanxuanze=int(input("1、空地（可以种植) 10金币  2、胜利树（战斗胜利后额外获得5金币） 20金币"))
                        if jiayuanxuanze==1:
                            if jinbi>=10:
                                jinbi=jinbi-10
                                tiandi.append("空地")
                            else:
                                print("金币不够了")
                        elif jiayuanxuanze==2:
                            if jinbi>=20:
                                jinbi=jinbi-20
                                xunzhao=0
                                for i in range(len(tiandi)):
                                    if tiandi[i]=="空地":
                                        print("有空地，已自动植入")
                                        tiandi[i]="胜利树"
                                        xunzhao=1
                                        break
                                if xunzhao==0:
                                    print("没有空地，已放入背包")
                                    beibao.append("胜利树")
                    elif jiayuanxuanze==2:
                        print("田地:")
                        print(tiandi)
                        print("背包:")
                        print(beibao)
                    elif jiayuanxuanze==3:
                        print("田地:")
                        print(tiandi)
                        print("背包:")
                        print(beibao)
                        xunzhao=0
                        zhongzhiwu=input("你要种植(退出输“无”)：")
                        if zhongzhiwu=="无":
                            break
                        for i in range(len(beibao)):
                            if beibao[i]==zhongzhiwu:
                                for j in range(len(tiandi)):
                                    if tiandi[j]=="空地":
                                        print("种植成功！")
                                        tiandi[j]=zhongzhiwu
                                        xunzhao=1
                                        break
                            if xunzhao==1:
                                del beibao[i]
                                break
                        if xunzhao==0:
                            print("种植失败（可能是因为背包里没有或没有空地了）")
                        print("现在田地:")
                        print(tiandi)
                        print("现在背包:")
                        print(beibao)
                    elif jiayuanxuanze==4:
                        break
            else:
                print("你的角色等级还没到5级")
        elif xuanze==9:
            print("已进入练习场：")
            print("你现在有（金币）：{}".format(jinbi))
            lianxichangxuanze=int(input("1、加10生命（金币20） 2、加10防御（金币30） 3、加10攻击（金币30） 4、退出"))
            if lianxichangxuanze==1:
                if jinbi>=20:
                    jinbi=jinbi-20
                    jueseshengming=jueseshengming+10
                    print("已加入10生命")
                else:
                    print("金币不够了")
            elif lianxichangxuanze==2:
                if jinbi>=30:
                    jinbi=jinbi-30
                    juesefangyu=juesefangyu+10
                    print("已加入10防御")
                else:
                    print("金币不够了")
            elif lianxichangxuanze==3:
                if jinbi>=30:
                    jinbi=jinbi-30
                    juesegongji=juesegongji+10
                    print("已加入10攻击")
                else:
                    print("金币不够了")
            else:
                pass
        print("\n")
    except Exception as e:
        print(e)
        print("抱歉，程序出错")
        pass
print("欢迎再次体验。")
