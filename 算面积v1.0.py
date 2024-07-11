while True:
    e = int(input("1、查看面积公式 2、计算面积 3、结束使用（填写“1、2、3”整数）："))
    if e == 2:
        d = int(input("1、长（正）方形 2、三角形 3、平行四边形："))
        if d == 1:
            a = int(input("输入长（正）方形的长："))
            b = int(input("输入长（正）方形的宽："))
            c = a*b
            print((str("长（正）方形的面积是:") + str(c)))
        if d == 2:
            a = int(input("输入三角形的底："))
            b = int(input("输入三角形的高："))
            c = a*b/2
            print((str("三角形的面积是:") + str(c)))
        if d == 3:
            a = int(input("输入平行四边形的底："))
            b = int(input("输入平行四边形的高："))
            c = a*b
            print((str("平行四边形的面积是:") + str(c)))
    elif e == 1:
        d = int(input("1、长（正）方形 2、三角形 3、平行四边形"))
        if d == 1:
            print("长（正）方形面积：长×宽（边长×边长）")
        if d == 2:
            print("三角形面积：底×高÷2")
        if d == 3:
            print("平行四边形：底×高")
    elif e == 3:
        break
    print(" ")
print("已结束使用")
