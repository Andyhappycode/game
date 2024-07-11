print("华氏度与摄氏度的转换")
while True:
    moshi=int(input("1、华氏度转摄氏度 2、摄氏度转华氏度"))
    if moshi==1:
        s=int(input("华氏度："))
        print("摄氏度：",end='')
        print((s-32)/1.8)
    else:
        s=int(input("摄氏度："))
        print("华氏度：",end='')
        print((s*1.8)+32)

