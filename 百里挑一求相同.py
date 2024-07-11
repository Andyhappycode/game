import random
a=0
b=0
ceshi=[]
sheng=0
bai=0
for i in range(1,10000):
    a=random.randint(1,100)
    b=random.randint(1,100)
    if a==b:
        sheng=sheng+1
        ceshi.append(1)
    else:
        bai=bai+1
        ceshi.append(0)
    print("第{}次：".format(i))
    print("成功{}次".format(sheng))
    print("失败{}次".format(bai))
    print("成功率{}%".format(round(sheng/(sheng+bai)*100,4)))
print(ceshi)