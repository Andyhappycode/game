#模块导入
import playsound

#加载
print("加载中……请耐心等待……\nloading……")
playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/加载.WAV")
loading = 0
for i in range(100):
    print("loading…… {}%".format(loading))
    loading+=1
print("加载成功！")

#播放和显示提示语
print("您好，欢迎使用古诗词学习程序。\nHello, welcome to the program for learning ancient poetry.")
playsound.playsound("D:/Andy/Andy/Information/Code/python/古诗词学习程序/素材/音频/启动提示语.WAV")

#定义全局变量
choose = 0
language = 1 #1为中文 2为英文



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
                if language==1:
                    print("非常抱歉，该模块暂未开放，感谢您的理解。")
                    playsound.playsound("D:\Andy\Andy\Information\Code\python\古诗词学习程序\素材\音频\模块未开发中文.WAV")
                else:
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