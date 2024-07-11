xiaocan = 0
leiji = 0
print("小餐计算器")
while True:
    print("规则：\n小餐=50元，其余见文件")
    a = int(input("1、小餐 2、小餐累计 3、现在情况"))
    if a == 1:
        b = int(input("1、+ 2、-"))
        if b == 1:
            c = int(input("数量？"))
            xiaocan = xiaocan+c
        if b == 2:
            c = int(input("数量？"))
            xiaocan = xiaocan-c
    if a == 2:
        b = int(input("1、+ 2、-"))
        if b == 1:
            c = int(input("数量？"))
            leiji = leiji+c
        if b == 2:
            c = int(input("数量？"))
            leiji = leiji-c
    if a == 3:
        print("小餐：")
        print(xiaocan)
        print("小餐累计：")
        print(leiji)
    if leiji > 4:
        xiaocan = xiaocan+(leiji-leiji%5)/5
        leiji = leiji % 5
    print("操作完成！")
    print("\n")
    xiaocan = xiaocan//1
