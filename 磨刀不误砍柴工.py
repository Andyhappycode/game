print("磨刀不误砍柴工游戏")
shengli=0
shibai=0
while True:
    import random
    xuanze=int(input("1、规则 2、开始游戏 3、游戏信息 4、结束游戏"))
    if xuanze==1:
        print("开始游戏后，要在规定选择次数内砍完规定数量的柴，开始时刀的锋利程度是1，每一次磨刀刀的锋利程度+1")
    if xuanze==2:
        print("开始游戏！")
        cishu=random.randint(20,100)
        fengli=1
        import random
        shuliang=random.randint(cishu*2,cishu*5)
        while True:
            print("选择次数剩余：",end='')
            print(cishu)
            print("柴的剩余数量：",end='')
            print(shuliang)
            print("刀的锋利程度：",end='')
            print(fengli)
            x=int(input("1、砍柴 2、磨刀"))
            if x==1:
                cishu=cishu-1
                shuliang=shuliang-fengli
                print("操作完成")
                if shuliang<=0:
                    print("胜利！柴已经砍完了！")
                    shengli=shengli+1
                    break
            elif x==2:
                cishu=cishu-1
                fengli=fengli+1
                print("操作完成")
            else:
                print("输错了，再输一遍吧！")
            if cishu<=0:
                print("失败，次数已用完。")
                shibai=shibai+1
                break
    if xuanze==3:
        print("胜利次数：",end='')
        print(shengli)
        print("失败次数：",end='')
        print(shibai)
    if xuanze==4:
        xz=int(input("真的要退出吗？（1、真 2、假）"))
        if xz==1:
            break
    print()
