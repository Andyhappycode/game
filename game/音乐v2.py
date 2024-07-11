import pygame
import time
import threading

x=1
r=True

def print_numbers():
    global x,r
    while r:
        time.sleep(1)
        if x!=9:
            x+=1
        else:
            x=1

def changeBackground():
    global r,x
    pygame.init()
    window = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption('MUSIC')
    window.fill((255, 255, 255))
    # 第一次刷新pygame.display.flip()
    # 第一次以后刷新：pygame.update()
    pygame.mixer.music.load('../../../../其他/好听的音乐.wav')
    pygame.mixer.music.play(loops=-1)
    a1 = pygame.image.load('素材/背景1.png')
    a2 = pygame.transform.scale(a1, (1200, 1000))
    b1 = pygame.image.load('素材/背景2.png')
    b2 = pygame.transform.scale(b1, (1200, 1000))
    c1 = pygame.image.load('素材/背景3.png')
    c2 = pygame.transform.scale(c1, (1200, 1000))
    d1 = pygame.image.load('素材/背景4.png')
    d2 = pygame.transform.scale(d1, (1200, 1000))
    e1 = pygame.image.load('素材/背景5.png')
    e2 = pygame.transform.scale(e1, (1200, 1000))
    f1 = pygame.image.load('素材/背景6.png')
    f2 = pygame.transform.scale(f1, (1200, 1000))
    g1 = pygame.image.load('素材/背景7.png')
    g2 = pygame.transform.scale(g1, (1200, 1000))
    h1 = pygame.image.load('素材/背景8.png')
    h2 = pygame.transform.scale(h1, (1200, 1000))
    pygame.display.flip()
    while r:
        if x == 1:
            window.blit(a2, (0, 0))
        if x == 2:
            window.blit(b2, (0, 0))
        if x == 3:
            window.blit(c2, (0, 0))
        if x == 4:
            window.blit(d2, (0, 0))
        if x == 5:
            window.blit(e2, (0, 0))
        if x == 6:
            window.blit(f2, (0, 0))
        if x == 7:
            window.blit(g2, (0, 0))
        if x == 8:
            window.blit(h2, (0, 0))
        pygame.display.update()
        time.sleep(5)


thread1 = threading.Thread(target=print_numbers)
# 启动线程
thread2 = threading.Thread(target=changeBackground)


thread1.start()
thread2.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
            time.sleep(5)
            quit()
    time.sleep(1)
