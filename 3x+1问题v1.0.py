a = int(input("请输入一个整数："))
b = 0
while True:
    b=b+1
    if a%2!=0:
        a=a*3+1
        print(str(b)+str('、')+str(a))
    else:
        a=a//2
        print(str(b)+str('、')+str(a))

