import random
while True:
    a=int(input("生成几张彩票？"))
    for i in range(a):
        z=random.randint(1,200)
        print("           中奖码：{}".format(z))
        for i in range(1,10):
            print("{}: ".format(i),end='')
            for i in range(1,10):
                print("{} ".format(random.randint(1,200)),end='')
            print("  中奖酸奶数：{}".format(random.randint(1,3)))
        print()