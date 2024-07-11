import threading
import time
mystore = 0
fertilizer = 0
grow=False
class tree:
    def __init__(self):
        self.store=0
        self.high=0
        self.shengyu=0
    def grow(self):
        global mystore,grow
        mystore+=self.store
        self.store=0
        self.shengyu=0
        self.high=0
        grow=True
    def look(self):
        print("This tree high is:")
        print(self.high)
        print("This tree store is:")
        print(self.store)
        print("This tree remaining time is:")
        print(self.shengyu)

    def worker(self):
        global grow
        while True:
            if grow:
                time.sleep(1)
                if self.shengyu > 0:
                    self.shengyu -= 1
                else:
                    self.high += 20
                    self.store += 0.5 * self.high
                    self.shengyu = 100

    def use(self):
        global fertilizer
        if fertilizer>=1:
            fertilizer-=1
            self.shengyu=0
            print("Successful use")
        else:
            print("No fertilizer")

t = tree()

# 启动线程
t.thread = threading.Thread(target=t.worker)
t.thread.start()


while True:
    c=int(input("1.grow a tree 2.look to the tree 3.purchase fertilizer 4.using fertilizer"))
    if c==1:
        t.grow()
        print("Planted well！")
    if c==2:
        t.look()
    if c==3:
        if mystore>=50:
            mystore-=50
            fertilizer+=1
            print("Successful purchase！")
        else:
            print("Insufficient points")
    if c==4:
        t.use()