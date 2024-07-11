import random as r
c=0
s=[]
renshu = int(input("模拟人数为：（大于3,小于8）"))
ren = []
piao = []
fen = []
if renshu<=3:
    print("不符合标准")
    quit()
elif renshu==4:
    fen = ["狼人","女巫","预言家","平民"]
elif renshu==5:
    fen = ["狼人","女巫","预言家","平民","平民"]
elif renshu==6:
    fen = ["狼人","女巫","预言家","猎人","平民","平民"]
elif renshu==7:
    fen = ["狼人","狼人","女巫","预言家","猎人","平民","平民"]
r.shuffle(fen)
ren.append("我")
piao.append(0)
for i in range(renshu-1):
    ren.append(i+2)
    piao.append(0)
print("你是{}。一号选手".format(fen[0]))
while renshu!=1:
    piao=[]
    for i in range(renshu - 1):
        piao.append(0)
    print("新的一天开始了。")
    print("天黑请闭眼。")


    if "狼人" in fen:
        print("狼人请睁眼。")
        if fen[0]=="狼人":
            c=int(input("请说出你要干掉的人的编号："))
            if c>0 and c<=len(fen) and c!=1:
                s.append(c-1)
            else:
                while c>0 and c<=len(fen) and c!=1:
                    print("回答不符合要求。")
                    c = int(input("请说出你要干掉的人的编号："))
            if renshu==7:
                print("你的队友开始选择干掉的人……")
                while not fen[c-1]=="狼人":
                    c=r.randint(1,7)
                print("队友选择完毕，他选择了{}号".format(c))
                s.append(c-1)
        else:
            print("一番秘密谈话后……")


    if "女巫" in fen:
        print("狼人请闭眼。\n女巫请睁眼。")
        if fen[0]=="女巫":
            if len(s)!=0:
                for i in range(len(s)):
                    print("今天，{}号被干掉了。".format(s[1]+1))
                c = int(input("1、救人 2、毒人 3、什么也不做"))
                if c==1:
                    if len(s)==1:
                        s=[]
                    else:
                        c=int(input("救谁？"))
                        if c in s:
                            print("救助成功！")
                        else:
                            while not c in s:
                                print("回答不符合要求。")
                                c = int(input("救谁？"))
                            print("救助成功！")
            else:
                print("本回合至此为止，还没有人被干掉")
                c=int(input("是否毒人（1、是 2、否）"))
                if c==1:
                    c = int(input("毒谁？"))
                    if c<=len(fen) and c!=1:
                        print("毒成功！")
                    else:
                        while not c<=len(fen) and c!=1:
                            print("回答不符合要求。")
                            c = int(input("毒谁？"))
                        print("毒成功！")
        else:
            s.append(r.randint(0,renshu-1))
            print("一番秘密谈话后……")


    if "预言家" in fen:
        print("女巫请闭眼。\n预言家请睁眼。")
        if fen[0] == "预言家":
            c = int(input("请说出你要看身份的人的编号："))
            if c > 0 and c <= len(fen) and c != 1:
                print("他的身份是{}。".format(fen[c - 1]))
            else:
                while c > 0 and c <= len(fen) and c != 1:
                    print("回答不符合要求。")
                    c = int(input("请说出你要看身份的人的编号："))
        else:
            print("一番秘密谈话后……")


    if "猎人" in fen:
        print("预言家请闭眼。\n猎人请睁眼。")
        if fen[0] == "预言家":
            print("你没有可以做的。")
        print("猎人请闭眼。")


    #结算阶段
    print("天亮了！")
    print("今天晚上",end="")
    if len(s)==0:
        print("是一个平安夜！")
    else:
        for i in range(len(s)):
            print("{}号".format(s[i]+1),end="")
        print("被干掉了。")
        if 1 in s:
            print("这一回合里，你被干掉了。")
            quit()
        else:
            try:
                sn1 = []
                sn2 = []
                for i in range(len(s)):
                    sn1.append(fen[s[i]])
                    sn2.append(ren[s[i]])
                    renshu-=1
                for i in range(len(s)):
                    del fen[index(sn1[i])]
                    del ren[index(sn2[i])]
            except Exception as e:
                pass
    s=[]
    if len(fen)==1:
        print("你赢了！")
    else:
        f=0
        for i in range(len(fen)):
            if fen[i]!=fen[0]:
                break
            else:
                f+=1
        if f!=0:
            print("你赢了！")

    print("接下来开始投票！")
    c=int(input("你要投几号？"))
    if c<=len(fen) and c>1:
        piao[c-1]+=1
    else:
        while c<=len(fen) and c>1:
            print("回答不符合要求。")
            c = int(input("你要投几号？"))
            if c <= len(fen) and c > 1:
                piao[c - 1] += 1
    print("其他人开始投票……")
    for i in range(renshu-1):
        piao[r.randint(1,renshu-1)]+=1
    print("其他人投票完毕！")
    print("这是结果：")
    print(piao)
    m=max(piao)
    for i in range(renshu-1):
        if piao[i]==m:
            if i==0:
                print("这轮投票导致你被干掉。")
                quit()
            else:
                s.append(i)
    for i in range(len(s)):
        print("{}号".format(s[i]), end="")
        print("因为这轮投票被干掉了。")
        try:
            sn1 = []
            sn2 = []
            for i in range(len(s)):
                sn1.append(fen[s[i]])
                sn2.append(ren[s[i]])
                renshu -= 1
            for i in range(len(s)):
                del fen[index(sn1[i])]
                del ren[index(sn2[i])]
        except Exception as e:
            pass


    print("本回合结束。")