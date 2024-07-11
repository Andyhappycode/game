#导入模块
import turtle
#获取作图信息
a = int(input("1、日食 2、月食："))
if a == 2:
    #获取作图信息
    b = int(input("距离（请不要等于或大于200）："))
    #创建pen，写入pen的参数
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("blue")
    pen.pensize(5)
    #开始做图
    pen.circle(100,360,30)
    pen.fillcolor('orange')
    pen.up()
    pen.back(b)
    pen.down()
    pen.begin_fill()
    pen.circle(100,360,30)
    pen.end_fill()
    #画完提示
    print("月食绘制完毕")
elif a == 1:
    #获取作图信息
    b = int(input("距离（请不要等于或大于200）："))
    #创建pen，写入pen的参数
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("orange")
    pen.pensize(5)
    #开始做图
    pen.fillcolor('orange')
    pen.begin_fill()
    pen.circle(100,360,30)
    pen.end_fill()
    pen.up()
    pen.back(b)
    pen.down()
    pen.color("blue")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(100,360,30)
    pen.end_fill()
    #画完提示
    print("日食绘制完毕")
else:
    #错误提示
    print("输入错误，请输入一个在规定范围内的数字")
#结束提示
print("程序结束")
