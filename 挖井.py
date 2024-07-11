import turtle
print("挖井中……\n请耐心等待……")
i=0
j=10
turtle.pu()
turtle.goto(0,100)
turtle.down()
while i<=850:
    turtle.forward(20)
    turtle.right(j)
    j=j+0.1
    i=i+1
