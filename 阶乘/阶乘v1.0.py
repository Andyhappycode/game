import sys
sys.set_int_max_str_digits(1000000)
while True:
    a = int(input("？的阶乘"))
    b = 1
    try:
    
        while a >= 1:
            b = b*a
            a = a-1
        print(b)
    except Exception as e:
        print("数值错误")
        print(e)

    print('The length of {} is {}'.format('上一结果', len(str(b))))
