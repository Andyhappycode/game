import random
ceshi=[]
shuju=[]
shuju1=[]
shumu=0
chenggong=0
shibai=0
for i in range(1,10000):
    shuju=[]
    shuju1=[]
    shumu=0
    for j in range(0,9):
        shuju.append(random.randint(1,100))
    for j in range(0,9):
        if shuju[j] in shuju1:
            shumu=shumu+1
        shuju1.append(shuju[j])
    if shumu>=2:
        ceshi.append(1)
        chenggong=chenggong+1
    else:
        ceshi.append(0)
        shibai=shibai+1
    print("第{}次：".format(i))
    print("成功{}次".format(chenggong))
    print("失败{}次".format(shibai))
    print("成功率{}%".format(round(chenggong/(chenggong+shibai)*100)))
print(ceshi)