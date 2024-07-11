caidan={}
print("管理员模式--初始")
try:
    while True:
        password=int(input("设置密码:"))
        password1=int(input("验证密码（再输一遍）"))
        if password == password1:
            print("设置完成")
            break
        else:
            print("两次输入密码不一样，请重新输入")
    print("初始化菜单：")
    
    while True:
        moshi=int(input("1、购买商品 2、管理员模式"))
        if moshi==1:
            pass
            #待完成
        elif moshi==2:
            password1=int(input("请输入管理员密码："))
            if password1==password:
                print("已进入管理员模式")
                gx=int(input("1、更改密码 2、更改菜单"))
                if gx==1:
                    password1=int(input("旧密码："))
                    if password1==password:
                        while True:
                            password=int(input("新密码："))
                            password1=int(input("新密码验证（再输一遍新密码）"))
                            if password==password1:
                                print("更改完成")
                                break
                            else:
                                print("两次输入不同")
                    else:
                        print("旧密码错误！")
                elif gx==2:
                    pass
                    #待完成
            else:
                print("密码错误")
except:
    print("请不要漏输")
