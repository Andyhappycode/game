import pygame
import time

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('图形')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.display.update()
pygame.draw.circle(window,(0,255,0),(250,350),150,0)
pygame.display.flip()
time.sleep(1.5)
window.fill((255,255,255))
pygame.draw.rect(window,(255,0,255),(80,500,70,350))
pygame.display.update()
time.sleep(1.5)
window.fill((255,255,255))
pygame.draw.ellipse(window,(255,0,255),(80,500,70,350),0)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()