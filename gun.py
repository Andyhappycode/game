class gun:
    def fire(self):
        if self.botton>0:
            print("     *")
            self.botton-=1
        else:
            print("#")
    def __init__(self):
        self.colour="orange"
        self.botton=0
    def take(self):
        self.botton+=1
    def __str__(self):
        return "%s,%d"%(self.colour,self.botton)
mygun=gun()
while True:
    a=int(input("1、加子弹 2、发射"))
    if a==1:
        mygun.take()
    else:
        mygun.fire()
    print("当前状态：",mygun)