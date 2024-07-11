import random as r
def fun1(a):
    for i in range(a):
        b=round(r.uniform(0,20))
        if b>=10:
            if b>=15:
                print('{}:{}>=10!!'.format(i,b))
            else:
                print('{}:{}>=10'.format(i,b))
        else:
            if b<=5:
                print('{}:{}<10!'.format(i,b))
            else:
                print('{}:{}<10'.format(i,b))



if __name__ == '__main__':
    fun1(10)
