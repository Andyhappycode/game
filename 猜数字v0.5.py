import getpass
import random
shuru=0
shezhi1=1
shezhi2=100
while True:
    print("数字炸弹宝箱游戏")
    xuanze=int(input("1、数字炸弹 2、数字宝箱 3、设置 4、规则 5、退出"))
    if xuanze==1:
        xuanze=int(input("1、人机对战 2、双人对战"))
        if xuanze==1:
            fanwei1=shezhi1
            fanwei2=shezhi2
            dream=random.randint(1,100)
            print("计算机已经想好了（范围：1-100）")
            while True:
                shuru=int(input("输入一个{}到{}的数".format(fanwei1,fanwei2)))
                if shuru<dream and shuru>=fanwei1:
                    print("没碰到炸弹，比炸弹小！")
                    fanwei1=shuru
                elif shuru>dream and shuru<=fanwei2:
                    print("没碰到炸弹，比炸弹大！")
                    fanwei2=shuru
                elif shuru==dream:
                    print("碰到炸弹！")
                    break
                else:
                    print("请输入范围内的数！")
        if xuanze==2:
            fanwei1=shezhi1
            fanwei2=shezhi2
            print("请一号选手操作…")
            while dream>=1 and dream<=100:
                dream=int(getpass.getpass("请输入一个1-100以内的整数"))
            print("请二号选手操作…")
            while True:
                shuru=int(input("输入一个{}到{}的数".format(fanwei1,fanwei2)))
                if shuru<dream and shuru>=fanwei1:
                    print("没碰到炸弹，比炸弹小！")
                    fanwei1=shuru
                elif shuru>dream and shuru<=fanwei2:
                    print("没碰到炸弹，比炸弹大！")
                    fanwei2=shuru
                elif shuru==dream:
                    print("碰到炸弹！")
                    break
                else:
                    print("请输入范围内的数！")
    if xuanze==2:
        xuanze=int(input("1、人机对战 2、双人对战"))
        if xuanze==1:
            fanwei1=shezhi1
            fanwei2=shezhi2
            dream=random.randint(1,100)
            print("计算机已经想好了（范围：1-100）")
            while True:
                shuru=int(input("输入一个{}到{}的数".format(fanwei1,fanwei2)))
                if shuru<dream and shuru>=fanwei1:
                    print("小了！")
                    fanwei1=shuru
                elif shuru>dream and shuru<=fanwei2:
                    print("大了！")
                    fanwei2=shuru
                elif shuru==dream:
                    print("碰到宝箱！胜利！")
                    break
                else:
                    print("请输入范围内的数！")
        if xuanze==2:
            fanwei1=shezhi1
            fanwei2=shezhi2
            print("请一号选手操作…")
            while dream>=1 and dream<=100:
                dream=int(getpass.getpass("请输入一个1-100以内的整数"))
            print("请二号选手操作…")
            while True:
                shuru=int(input("输入一个{}到{}的数".format(fanwei1,fanwei2)))
                if shuru<dream and shuru>=fanwei1:
                    print("小了！")
                    fanwei1=shuru
                elif shuru>dream and shuru<=fanwei2:
                    print("大了！")
                    fanwei2=shuru
                elif shuru==dream:
                    print("碰到宝箱！胜利！")
                    break
                else:
                    print("请输入范围内的数！")
    if xuanze==3:
        xuanze=int(input("1、调整最小值 2、调整最大值"))
        if xuanze==1:
            while shezh#1
    if xuanze==4:
        print("规则：")
        print("1、数字炸弹玩法：一人想一个数字（规定范围），另一个人猜，目标：避开这个数")
        print("2、数字宝箱玩法：一人想一个数字（规定范围），另一个人猜，目标：找到这个数")
        print("3、双人玩法时，一号选手输入时，二号选手不能观看")
        print("4、设置模式可以调整范围")
    if xuanze==5:
        xuanze=int(input("真的要退出吗？ 1、真 2、假"))
        if xuanze==1:
            break
    print()
    print()
