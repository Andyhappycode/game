while True:
    print("算出a是b的百分之几")
    a=float(input("小：a等于："))
    b=float(input("大：b等于："))
    d=int(input("精确到小数点后几位?"))
    print(str("a是b的")+str(round(float(str(b/a*1.0),d)))+str("%"))
    c=int(input("1、结束 2、继续"))
    if c==1:
        break
print("程序结束")
