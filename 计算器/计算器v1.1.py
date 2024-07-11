while True:
    try:
        print("算式(不要输入=):")
        a=eval(input())
        print("={}".format(a))
    except Exception as e:
        print("错误：",end='')
        print(e)
