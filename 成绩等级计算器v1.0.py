while True:
    print("成绩等级计算器（100分制）")
    a=float(input("成绩"))
    if a==100:
        print("太棒了，满分！")
    elif a>=95 and a<100:
        print("很棒，优上！")
    elif a>=90 and a<95:
        print("棒，优！")
    elif a>=85 and a<90:
        print("不错，优下！")
    elif a>=80 and a<85:
        print("加油，良。")
    elif a>=60 and a<80:
        print("再接再厉，合格。")
    elif a>=0 and a<60:
        print("要努力了，需努力。")
    else:
        print("成绩无效。")
        break
    print("成绩：",end='')
    print(a)
    print()
