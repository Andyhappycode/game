import pygame

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('金箍棒')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.update()
pygame.draw.line(window,(255,255,0),(240,0),(240,50),30)
pygame.draw.line(window,(255,0,0),(240,50),(240,650),30)
pygame.draw.line(window,(255,255,0),(240,650),(240,700),30)
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()