no = int(input("娃娃机数量："))
wa = []
for i in range(no):
    wa.append(70)
time = int(input("营业时长："))
people = []
peopletime = []
peopleno = 0
x = 0
wano = 0
zhen = 0
ci = 0
for i in range(time):
    import random
    if i%5==0:
        people.append(peopleno+1)
        peopleno+=1
        peopletime.append(random.randint(1,50))
    for j in range(len(people)):
        ci+=1
        x = random.randint(1,len(wa))
        try:
            if wa[x-1]>=random.randint(1,100):
                wano+=1
                zhen+=1
                wa[x-1]-=3
                peopletime[j]-=1
                for z in range(len(wa)):
                    wa[z]-=2
        except Exception as e:
            print(i)
            print(j)
            print(people)
            print(peopletime)
            print(wa)
            raise e
    for j in range(len(people)):
        try:
            if peopletime[j-1]<=0:
                del people[j-1]
                del peopletime[j-1]
        except Exception as e:
            pass
    for j in range(len(wa)):
        if wa[j]<=5:
            wa[j]=10
        wa[j]+=10
    if i%10==0:
        if i>1:
            for z in range(len(wa)):
                wa[z]-=2
        zhen = 0
print(wa)
print(people)
print(peopletime)
print(peopleno)
print(wano)
print(ci)