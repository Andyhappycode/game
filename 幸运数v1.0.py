a=0
xingyun=[]
shanchu=[]
shuliang=int(input("你要查找1到多少之间的幸运数"))
for i in range(1,shuliang+1):
    xingyun.append(i)
try:
    for i in range(1,len(xingyun)-1):
        if xingyun[i-1]%2==0:
            del(xingyun[i-1])
except:
    pass
i=1
b=0
while True:
    shanchu=[]
    i=i+1
    b=b+1
    try:
        a=xingyun[i-1]
    except:
        break
    for j in range(len(xingyun)):
        if (j+1)%a==0:
            shanchu.append(xingyun[j])
    for j in range(len(shanchu)):
        xingyun.remove(shanchu[j])
print("幸运数：")
print(xingyun)
print("一共有{}个".format(len(xingyun)))