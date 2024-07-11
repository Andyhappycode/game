mima=int(input("初始密码？（数字）"))
while True:
    leixing=int(input("1、购物结算 2、商品编辑"))
    if leixing==2:
        shimima=int(input("密码?"))
        if shimima==mima:
            print("密码正确！")
        else :
            while False:
                print("密码错误！")
