import random
poke=["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A","Joker-","Joker+"]
random.shuffle(poke)
print("Current playing cards:")
a = []
b = []
c = []
d = []
print(poke)
for i in range(len(poke)):
    if i%4 == 0:
        a.append(poke[i])
    elif i%4 == 1:
        b.append(poke[i])
    elif i%4 == 2:
        c.append(poke[i])
    else:
        d.append(poke[i])
print("player1:")
for i in a:
    print(i)
print("player2:")
for i in b:
    print(i)
print("player3:")
for i in c:
    print(i)
print("player4:")
for i in d:
    print(i)
