import pygame
import time

y = 0

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('移动的小球')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.update()
pygame.display.flip()


while True:
    y+=1
    pygame.draw.circle(window,(255,0,0),(250,y),50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
    window.fill((255, 255, 255))
    time.sleep(0.01)
    if y==700:
        quit()