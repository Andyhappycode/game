import pygame

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('飞行')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.update()
jian1 = pygame.image.load('../素材/火箭.svg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()