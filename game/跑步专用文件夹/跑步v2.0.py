import pygame
import random

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
window.blit(start,(50,200))
pygame.display.flip()
clock = pygame.time.Clock()
gametime = 0
hhave = 0
keys_pressed = pygame.key.get_pressed()
hx=0
hy=0
z=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            z = 0
            break
    if z==0:
        break

while True:
    keys_pressed = pygame.key.get_pressed()
    gametime+=0.001
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
    window.fill((255,255,255))
    word1=font1.render('生命：{} 时间：{}'.format(ming,gametime),True,(0,0,0))
    window.blit(word1, (0, 0))
    window.blit(people, people_rect)
    window.blit(stone, stone_rect)
    sy+=0.5
    hy+=0.5
    if people_rect.x<=0 or people_rect.x>=450:
        ming-=0.001
        print("已出界！")
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
            quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            px-=10
            window.blit(people, (px, 500))
        if keys[pygame.K_d]:
            px+=10
            window.blit(people, (px, 500))
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
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quit()
    ming=round(ming,3)
    pygame.display.update()