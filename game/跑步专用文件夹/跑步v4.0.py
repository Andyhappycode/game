import pygame
import random
import time
import threading

gametime = 0
stop = False
cun = 0
# 定义一个线程执行的函数
def print_numbers():
    global gametime,cun
    while not stop:
        time.sleep(1)
        gametime+=1
        cun+=1

thread1 = threading.Thread(target=print_numbers)

# 启动线程
thread1.start()

px = 250
sx = 0
sy = 0
have = 0
ming = 10

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('跑步游戏')
window.fill((255, 255, 255))
font1 = pygame.font.Font('../素材/标准字体.ttc', 40)
font2 = pygame.font.Font('../素材/标准字体.ttc', 80)
# 第一次刷新pygame.display.flip()
# 第一次以后刷新：pygame.update()
people1 = pygame.image.load('../素材/人物.png')
people = pygame.transform.scale(people1,(50,100))
stone = pygame.image.load('../素材/警告.png')
start = pygame.image.load('../素材/开始游戏.png')
hunberger1 = pygame.image.load('../素材/汉堡.png')
hunberger = pygame.transform.scale(hunberger1,(130,100))
dan1 = pygame.image.load('../素材/子弹.png')
dan = pygame.transform.scale(dan1,(5,10))
beijin1 = pygame.image.load('../素材/背景.png')
beijin = pygame.transform.scale(beijin1,(500,700))
l1 = pygame.image.load('../素材/里程碑1.png')
l2 = pygame.image.load('../素材/里程碑2.png')
lt1 = 0
lt2 = 0
dan_list = []
dan_x = []
dan_y = []
window.blit(beijin,(0,0))
window.blit(start,(100,200))
pygame.display.flip()
clock = pygame.time.Clock()
hhave = 0
keys_pressed = pygame.key.get_pressed()
hx=0
hy=0
z=1
wait = 0
word3 = font1.render('结束中……', True, (255, 0, 0))
word4 = font2.render('出界了！',True,(255,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
            window.blit(word3, (50, 150))
            pygame.display.update()
            time.sleep(1.1)
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            z = 0
            break
    if z==0:
        break

while True:
    window.fill((255,255,255))
    window.blit(beijin, (0, 0))
    keys_pressed = pygame.key.get_pressed()
    stone_rect = stone.get_rect()
    people_rect = people.get_rect()
    hunberger_rest = hunberger.get_rect()
    stone_rect.x = sx
    stone_rect.y = sy
    stone_rect.height = 99
    stone_rect.width = 134
    people_rect.x = px
    people_rect.y = 500
    people_rect.height = 100
    people_rect.width = 50
    hunberger_rest.x = hx
    hunberger_rest.y = hy
    hunberger_rest.height = 100
    hunberger_rest.width = 130

    word1=font1.render('生命：{} 时间：{}'.format(ming,gametime),True,(0,0,0))
    window.blit(word1, (0, 0))
    if ming>=50 and lt1<=500:
        lt1+=1
        window.blit(l1,(150,100))
    if gametime>=600 and lt2<=500:
        lt2+=1
        window.blit(l2,(50,280))
    window.blit(people, people_rect)
    window.blit(stone, stone_rect)
    sy+=2.5
    hy+=2.5
    try:
        for i in range(len(dan_list)):
            dan_y[i]-=2
            window.blit(dan, (dan_x[i], dan_y[i]))
            if (dan_x[i]<=stone_rect.x+134 and dan_x[i]>=stone_rect.x)and(dan_y[i]<=stone_rect.y+99 and dan_y[i]>=stone_rect.y):
                have = 0
                del dan_list[i],dan_x[i],dan_y[i]
            if dan_y[i]<=0:
                del dan_list[i], dan_x[i], dan_y[i]
    except Exception as e:
        pass
    if people_rect.x<=0 or people_rect.x>=450:
        ming-=0.001
        print("已出界！")
        window.blit(word4,(100,300))
    if have==0:
        have=1
        sy = 0
        sx = random.randint(1,450)
        window.blit(stone,(sx,sy))
    else:
        window.blit(stone, (sx, sy))
        if sy>=700:
            have = 0
    if hhave==0:
        hhave=1
        hy = 0
        hx = random.randint(1,450)
        window.blit(hunberger,(hx,hy))
    else:
        window.blit(hunberger, (hx, hy))
        if hy>=700:
            hhave = 0
    for event in pygame.event.get():
        #print('event.type={}'.format(event.type))
        if event.type == pygame.QUIT:
            stop = True
            window.blit(word3, (50, 150))
            pygame.display.update()
            time.sleep(1.1)
            quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            px-=10
            window.blit(people, (px, 500))
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            px+=10
            window.blit(people, (px, 500))
        if keys[pygame.K_UP]:
            if gametime-wait>=1 or cun>=1:
                dan_list.append("one")
                dan_x.append(px+20)
                dan_y.append(500)
                wait = gametime
                cun-=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if gametime - wait >= 1 or cun >= 1:
            dan_list.append("one")
            dan_x.append(px+20)
            dan_y.append(500)
            wait = gametime
            cun -= 1
    # if keys[pygame.K_e]:
    #     word4 = font1.render('暂停中', True, (255, 0, 0))
    #     window.blit(word4, (50, 300))
    #     pygame.display.update()
    #     stop = True
    #     time.sleep(1)
    #     keys = pygame.key.get_pressed()
    #     while not keys[pygame.K_e]:
    #         keys = pygame.key.get_pressed()
    #     stop = False
    #     thread1.start()
    if stone_rect.colliderect(people_rect):
        ming-=0.5
        have = 0
    if hunberger_rest.colliderect(people_rect):
        ming+=0.35
        hhave = 0
    if ming<=0:
        word2 = font2.render('Game Over!', True, (255, 0, 0))
        window.blit(word2, (50, 300))
        print("game over！")
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True
                    window.blit(word3, (50, 150))
                    pygame.display.update()
                    time.sleep(1.1)
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    stop = True
                    window.blit(word3, (50, 150))
                    pygame.display.update()
                    time.sleep(1.1)
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    stop = True
                    window.blit(word3, (50, 150))
                    pygame.display.update()
                    time.sleep(1.1)
                    quit()
    ming=round(ming,3)
    pygame.display.update()