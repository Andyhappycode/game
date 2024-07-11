#模块导入
import playsound

#加载
print("加载中……请耐心等待……\nloading……")
playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/加载.WAV")
loading = 0
for i in range(50):
    print("loading…… {}%".format(loading))
    loading+=1


#创建数据库,诗名、朝代、作者、内容、释文一一匹配
shiming = ["江南","敕勒歌","咏鹅"] #诗名
chaodai = ["汉","北朝时期","唐"]
zuozhe = ["汉乐府","北朝民歌","骆宾王"] #作者
neirong = ["江南可采莲，莲叶何田田。\n鱼戏莲叶间。\n鱼戏莲叶东，鱼戏莲叶西，\n鱼戏莲叶南，鱼戏莲叶北。",
           "敕勒川，阴山下。天似穹庐，笼盖四野。\n天苍苍，野茫茫。风吹草低见牛羊。",
           "鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波。"] #内容
shiwen = ["江南水上可以采莲，莲叶多么茂盛，\n鱼儿在莲叶间嬉戏。\n鱼在莲叶的东边游戏，鱼在莲叶的西边游戏，鱼在莲叶的南边游戏，鱼在莲叶的北边游戏。",
          "辽阔的敕勒大平原，就在阴山脚下。\n敕勒川的天空啊，看起来好像牧民们居住的毡帐一般。\n它的四面与大地相连，蔚蓝的天空一望无际，碧绿的原野茫茫不尽。\n那风吹到草低处，有一群群的牛羊时隐时现。",
          "鹅鹅鹅，面向蓝天，一群鹅儿伸着弯曲的脖子在歌唱。\n洁白的羽毛，漂浮在碧绿水面。红红的脚掌，拨动着清清水波。"]  #释文


for i in range(50):
    print("loading…… {}%".format(loading))
    loading+=1
print("加载成功！")

#播放和显示提示语
print("您好，欢迎使用古诗词学习程序。\nHello, welcome to the program for learning ancient poetry.")
playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/启动提示语.WAV")

#定义全局变量
choose = 0
language = 1 #1为中文 2为英文


#定义输出中文古诗的函数
def Chinese(number):
    print("         {}".format(shiming[number]))
    print("     {}  {}".format(chaodai[number],zuozhe[number]))
    print("{}".format(neirong[number]))
    print("\n释文：\n{}".format(shiwen[number]))



#主程序
while True:
    try:#出错捕获机制
        #真正的主程序
        while True:
            #主询问
            if language==1:
                choose = int(input("1、查询古诗词 2、语言 3、退出"))
            else:
                choose = int(input("1. Search for Ancient Poetry 2, Language 3, quit"))

            #分类
            if choose==1:
                if language==1: #中文查询模式
                    name = input("请输入您要查询的古诗词名称：")
                    number = shiming.index(name)
                    Chinese(number) #调用函数Chinese（在40行）
                    choose = 0 #选择变量清零
                    #用户操作
                    while True:
                        choose = int(input("1、听古诗 2、退出查询模式"))
                        if choose==1:
                            print("加载中……请耐心等待……")
                            if number==0:
                                playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/古诗词音频/江南.WAV")
                            elif number==1:
                                playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/古诗词音频/敕勒歌.WAV")
                            elif number==2:
                                playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/古诗词音频/咏鹅.WAV")
                        else:
                            break
                else: #英文查询模式
                    print("Very sorry, this module is currently not open. Thank you for your understanding.")
                    playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\模块未开发英文.WAV")
            elif choose==2:
                choose = int(input("1、简体中文 2、English"))
                if choose==1:
                    language = 1
                    playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\设置成功中文.WAV")
                else:
                    language = 2
                    playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\设置成功英文.WAV")
            elif choose==3:
                quit()

            #空行
            print()
    except Exception as orror:  #出错响应
        if language==1:
            print("抱歉，程序出错，以下是出错代码:{}".format(orror))
            playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\程序出错中文.WAV")
        else:
            print("Program error, here is the error code: {}".format(orror))
            playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\程序出错英文.WAV")
        #空行
        print("\n")