import pygame
import time

y = 0
t = 0

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('小球游戏')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.update()
pygame.display.flip()
font1 = pygame.font.Font('素材/标准字体.ttc',100)
font2 = pygame.font.Font('素材/标准字体.ttc',40)


while True:
    y+=1
    pygame.draw.circle(window,(255,0,0),(250,y),50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            y-=5
    pygame.display.update()
    window.fill((255, 255, 255))
    time.sleep(0.01)
    t+=0.01
    if y==700:
        word1 = font1.render('游戏结束', True, (255, 0, 0), )
        window.blit(word1, (20, 330))
        word2 = font2.render('得分'+str(t), True, (255, 0, 0), )
        window.blit(word2,(20,500))
        pygame.display.update()
        time.sleep(2)
        quit()