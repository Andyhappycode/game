import datetime as d
import time

def fun():
    i=0
    while True:
        i+=1
        print(i)        
        print(d.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        time.sleep(1)



if __name__ == '__main__':
    fun()

