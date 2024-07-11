import datetime
a=1
while a==1:
    import random
    
    print(str(datetime.datetime.now().year)+str("年"))
    print(str(datetime.datetime.now().month)+str("月"))
    print(str(datetime.datetime.now().day)+str("日"))
    if datetime.datetime.now().weekday() == 0:
        weekday = "星期一"
    elif datetime.datetime.now().weekday() == 1:
        weekday = "星期二"
    elif datetime.datetime.now().weekday() == 2:
        weekday = "星期三"
    elif datetime.datetime.now().weekday() == 3:
        weekday = "星期四"
    elif datetime.datetime.now().weekday() == 4:
        weekday = "星期五"
    elif datetime.datetime.now().weekday() == 5:
        weekday = "星期六"
    elif datetime.datetime.now().weekday() == 6:
        weekday = "星期日"
    print(weekday)
    print(str(datetime.datetime.now().hour)+str("时"))
    print(str(datetime.datetime.now().minute)+str("分"))
    print(str(datetime.datetime.now().second)+str("秒"))

    statement = ["做对的事情比把事情做对重要。","不要等到明天，因为明天太遥远，今天就行动。","求知若饥，虚心若愚。","成功将属于那些从不说“不可能”的人。","人的理想往往和他的能力成正比。","读书有三到，谓心到，眼到，口到。","少年易学老难成，一寸光阴不可轻。","合理安排时间，就等于节约时间。","勤奋，是步入成功之门的通行证。","生活充满了选择，而生活的态度就是一切。","学习是劳动，是充满思想的劳动。","熟读唐诗三百首，不会作诗也会吟。","一寸光阴一寸金，寸金难买寸光阴。","一年之计在于春，一日之计在于晨。"]
    print("名言：")
    print(random.choice(statement))
    a=int(input("1、结束 2、全部名言 3、继续 4、全部名言+继续"))
    if a==1:
        a=0
    elif a==2:
        for item in statement:
            print(item)
    elif a==4:
        for item in statement:
            print(item)
        a=1
    else:
        a=1
print("程序已结束")
