#声明变量
gongli=0
disu=0
dili=0
chun=0
shi=0
#获取数据
gongli = int(input("行驶了？公里"))
disu = int(input("低速时长?分（12公里/小时以下为低速）"))
dili = int(input("低速公里"))
chun = int(input("是否为春节（是1不是2）"))
shi = int(input("开始小时"))
#计算价格
#仅使用起步费的情况
if gongli<=3:
    print(13)
#不超过10公里的情况
elif gongli>3 and gongli<=10:
    if chun==1:
        print(round(13+(gongli-3-dili)*2.5+disu/4*2.5+10,2))
    elif shi>=23 or shi<=5:
        print(round((13+(gongli-3-dili)*2.5+disu/4*2.5)*1.3,2))
    elif shi>=23 or shi<=5 and chun==1:
        print(round((13+(gongli-3-dili)*2.5+disu/4*2.5)*1.3+10,2))
    else:
        print(round(13+(gongli-3-dili)*2.5+disu/4*2.5,2))
#超过10公里的情况
elif gongli>10:
    if chun==1:
        print(round((13+(gongli-3-dili)*2.5+disu/4*2.5+10)*1.5,2))
    elif shi>=23 or shi<=5:
        print(round(((13+(gongli-3-dili)*2.5+disu/4*2.5)*1.3)*1.5,2))
    elif shi>=23 or shi<=5 and chun==1:
        print(round(((13+(gongli-3-dili)*2.5+disu/4*2.5)*1.3+10)*1.5,2))
    else:
        print(round((13+(gongli-3-dili)*2.5+disu/4*2.5)*1.5,2))
#处理其他状况
else:
    print("输入错误")    
