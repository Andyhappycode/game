shan=0
shijian=0
juli=0
tili=0
shuifen=0
qian=0
xuanze=0
while True:
    xuanze=int(input("1、爬山 2、规则"))
    if xuanze==1:
        shan=int(input("1、庐山（1474米） 2、泰山（1532米） 3、黄山（1864米） 4、华山（2154米） 5、武夷山（2158米） 6、长白山（2691米） 7、五台山（3061米） 8、峨眉山（3099米） 9、玉山（3952米） 10、珠穆拉玛峰（8844米）"))
        if shan==1:
            print("开始爬山--庐山！")
            juli=1474
            tili=100
            shuifen=100
            qian=0
            shijian=0
            while True:
                shijian=1
                print("现在剩余距离：")
                print(juli)
                print("现在体力：")
                print(tili)
                print("现在水分：")
                print(shuifen)
                print("现在已经花费的钱：")
                print(qian)
                xuanze=int(input("1、爬山 2、食物 3、水 4、退出"))
                if xuanze==1:
                    shijian=shijian+10
                    tili=tili-5
                    shuifen=shuifen-7.5
                    juli=juli-10
                    print("成功爬了10米！")
                elif xuanze==2:
                    qian=qian+25
                    tili=tili+7.5
                    shuifen=shuifen+3.5
                elif xuanze==3:
                    qian=qian+5
                    tili=tili+2
                    shuifen=shuifen+78
                elif xuanze==4:
                    break
                if tili<=0:
                    print("体力小于0，你输了。")
                    break
                elif shuifen<=0:
                    print("水分小于0，你输了。")
                    break
                elif juli<=0:
                    print("成功登顶！")
                    break
    if shan==2:
            print("开始爬山--泰山！")
            juli=1532
            tili=100
            shuifen=100
            qian=0
            shijian=0
            while True:
                shijian=1
                print("现在剩余距离：")
                print(juli)
                print("现在体力：")
                print(tili)
                print("现在水分：")
                print(shuifen)
                print("现在已经花费的钱：")
                print(qian)
                xuanze=int(input("1、爬山 2、食物 3、水 4、退出"))
                if xuanze==1:
                    shijian=shijian+10
                    tili=tili-5
                    shuifen=shuifen-7.5
                    juli=juli-10
                    print("成功爬了10米！")
                elif xuanze==2:
                    qian=qian+25
                    tili=tili+7.5
                    shuifen=shuifen+3.5
                elif xuanze==3:
                    qian=qian+5
                    tili=tili+2
                    shuifen=shuifen+78
                elif xuanze==4:
                    break
                if tili<=0:
                    print("体力小于0，你输了。")
                    break
                elif shifen<=0:
                    print("水分小于0，你输了。")
                    break
                elif juli<=0:
                    print("成功登顶！")
                    break
    if shan==3:
            print("开始爬山--黄山！")
            juli=1864
            tili=100
            shuifen=100
            qian=0
            shijian=0
            while True:
                shijian=1
                print("现在剩余距离：")
                print(juli)
                print("现在体力：")
                print(tili)
                print("现在水分：")
                print(shuifen)
                print("现在已经花费的钱：")
                print(qian)
                xuanze=int(input("1、爬山 2、食物 3、水 4、退出"))
                if xuanze==1:
                    shijian=shijian+10
                    tili=tili-5
                    shuifen=shuifen-7.5
                    juli=juli-10
                    print("成功爬了10米！")
                elif xuanze==2:
                    qian=qian+25
                    tili=tili+7.5
                    shuifen=shuifen+3.5
                elif xuanze==3:
                    qian=qian+5
                    tili=tili+2
                    shuifen=shuifen+78
                elif xuanze==4:
                    break
                if tili<=0:
                    print("体力小于0，你输了。")
                    break
                elif shifen<=0:
                    print("水分小于0，你输了。")
                    break
                elif juli<=0:
                    print("成功登顶！")
                    break