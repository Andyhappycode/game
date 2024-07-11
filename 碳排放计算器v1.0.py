while True:
    try:
        print("碳排放计算器")
        yue = int(input("每月耗电？度"))
        yuet = yue*0.785
        hyuet = yuet/1000
        print("你们每月大约产生{}千克碳排放,合{}吨".format(yuet,hyuet))
        niant = yuet*12
        hniant = niant/1000
        print("你们每年大约产生{}千克碳排放,合{}吨".format(niant,hniant))
        qyuet = 7600000000*yuet
        hqyuet = qyuet/1000
        print("假设全球有76亿人口，照这样计算，每月大约会产生{}千克碳排放,合{}吨".format(qyuet,hqyuet))
        qniant = qyuet*12
        hqniant = qniant/1000
        print("假设全球有76亿人口，照这样计算，每年大约会产生{}千克碳排放,合{}吨".format(qniant,hqniant))
    except Exception as e:
        print("请在输入时输入数字(无小数),错误：{}".format(e))
    print("\n")
