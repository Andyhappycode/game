import datetime
import pygame
pygame.init()
caidan = []
jiage = []
changdu = 0
password = ""
passwordcopy = ""
caidanxuanze = 0
e=""
x=""
goumai = []
goumaijiage = []
zongfeiyong = 0
xiangmu = 0
xuanze = 0
queren = 0
yingli = 0
dingdanshu = 0
ming = ''
running = True
i = 0
while True:
    i+=1
    try:
        def first():
            global caidan,password,passwordcopy,e,jiage,ming
            print("管理员模式")
            while len(password)<10 or password != passwordcopy:
                password = input("请输入管理员密码(需大于等于10个字符):")
                passwordcopy = input("请再次输入（验证）：")
            ming = input("超市名：")
            changdu = int(input("菜单长度："))
            for i in range(changdu):
                try:
                    caidan.append(input("请输入第{}件商品名称：".format(i+1)))
                    jiage.append(int(input("请输入“{}”的标价：".format(caidan[i]))))
                except Exception as e:
                    pass
            for i in range(10000):
                print('刷新……\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n刷新……')
        if i==1:
            first()
        def boss():
            global caidan, password, passwordcopy,caidanxuanze,e,x,ming
            print("管理员模式")
            passwordcopy = input("请输入密码：")
            while password!=passwordcopy and passwordcopy!=0:
                passwordcopy = input("请输入密码：")
                if password!=passwordcopy:
                    print("密码输入错误")
                    break

            if password==passwordcopy:
                print("密码输入正确")
                caidanxuanze=0
                while caidanxuanze!=2:
                    caidanxuanze = int(input("1、查看菜单 2、退出 3、删除项目 4、增加项目 5、更改密码 6、查看总营业金额 7、订单数 8、更改超市名 9、付款码更改"))
                    if caidanxuanze==1:
                        print("菜单：")
                        print(caidan)
                        print("标价：")
                        print(jiage)
                    elif caidanxuanze==3:
                        print("菜单：")
                        print(caidan)
                        print("标价：")
                        print(jiage)
                        try:
                            caidanxuanze = input("你要删除（输入名称或编号）：")
                            caidanxuanze = int(caidanxuanze)
                            del caidan[caidanxuanze-1]
                            del jiage[caidanxuanze-1]
                            print("操作成功！")
                        except Exception as e:
                            try:
                                x=caidanxuanze
                                caidanxuanze = caidan.index(x)
                                del caidan[caidanxuanze - 1]
                                del jiage[caidanxuanze - 1]
                                print("操作成功！")
                            except Exception as e:
                                print("无该项目")
                        caidanxuanze=0
                    elif caidanxuanze==4:
                        caidan.append(input("你要加入的名称："))
                        jiage.append(int(input("你要加入的商品价格：")))
                    elif caidanxuanze==5:
                        passwordcopy = input("原密码：")
                        if passwordcopy==password:
                            password = input("请输入管理员密码(需大于等于10个字符):")
                            passwordcopy = input("请再次输入（验证）：")
                            while len(password) < 10 or password != passwordcopy:
                                password = input("请输入管理员密码(需大于等于10个字符):")
                                passwordcopy = input("请再次输入（验证）：")
                        else:
                            print("原密码输入错误！")
                    elif caidanxuanze==6:
                        print("总营业金额为：")
                        print(yingli)
                    elif caidanxuanze==7:
                        print("订单数：")
                        print(dingdanshu)
                    elif caidanxuanze==8:
                        ming = input("更改超市名为：")
                    elif caidanxuanze==9:
                        print("付款码更改说明：\n1、请新建文件夹名为“game”放入本代码文件路径下\n2、请在game文件夹下新建名为“素材”的文件夹\n3、请将付款码图片放入刚刚创建的“素材”文件夹\n4、请把付款码图片名称改为“图”，后缀名改为“png”\n5、若还是无法更改，请联系销售商")
                for i in range(10000):
                    print('刷新……\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n刷新……')



        def user():
            global goumai,goumaijiage,zongfeiyong,caidan,jiage,xiangmu,x,e,queren,dingdanshu,yingli,ming,running
            print("欢迎来到{}购物！".format(ming))
            goumai = []
            goumaijiage = []
            zongfeiyong = 0
            while True:
                print("菜单：")
                print(caidan)
                print("价格:")
                print(jiage)
                print("你的购买：")
                print(goumai)
                print("单价：")
                print(goumaijiage)
                print("数量：")
                print(len(goumai))
                print("总价：")
                print(zongfeiyong)
                try:
                    xiangmu=input("你要购买的编号或内容（不买输0）")
                    if xiangmu=="0":
                        break
                    x = int(xiangmu)
                    goumai.append(caidan[x-1])
                    goumaijiage.append(jiage[x - 1])
                except Exception as e:
                    try:
                        x = int(xiangmu)
                        goumai.append(caidan[caidan.index(xiangmu)])
                        goumaijiage.append(caidan.index(xiangmu))
                    except Exception as e:
                        print("该商品不存在")
                zongfeiyong = 0
                for i in range(len(goumaijiage)):
                    zongfeiyong+=goumaijiage[i]
            print("购买结束！")
            print("请凭一下小票付款：")
            print("\n             裁剪线")
            print("_____________________________")
            print("    欢迎光临{}！".format(ming))
            print("订单号：{}".format(dingdanshu+1))
            print("_____________________________")
            print("   名称               单价")
            for i in range(len(goumai)):
                print("  ",end='')
                print(str(i+1)+"、"+goumai[i],end='')
                print("             ",end='')
                print(goumaijiage[i])
            print("_____________________________")
            print("数量：{}".format(len(goumai)))
            print("总价：{}".format(zongfeiyong))
            print("{}年{}月{}日{}时{}分{}秒".format(datetime.date.today().year,datetime.datetime.now().month,datetime.datetime.now().day,datetime.datetime.now().hour,datetime.datetime.now().minute,datetime.datetime.now().second))
            print("        欢迎再次光临！")
            print("_____________________________")
            print("            小票完")
            print("\n")
            queren=int(input("是否确认交易？（1、是 2、否）"))
            if queren==1:
                yingli+=zongfeiyong
                dingdanshu+=1
                m=0
                window = pygame.display.set_mode((500, 600))
                pygame.display.set_caption('付款码：')
                window.fill((255, 255, 255))
                ma1 = pygame.image.load('game/素材/图.png')
                ma = pygame.transform.scale(ma1, (500, 600))
                window.blit(ma, (0, 0))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False  # 设置程序结束标志
                            pygame.display.quit()  # 关闭窗口



        #主程序
        while True:
            xuanze = int(input("1、管理员模式 2、顾客模式"))
            if xuanze==1:
                boss()
            else:
                user()
    except Exception as e:
        print("抱歉，程序出了一点小问题（常见原因：忘记输入）\n以下是错误原因（可联系服务员）")
        print(e)