import pygame

pygame.init()

window = pygame.display.set_mode((500, 700))
pygame.display.set_caption('春联————横')
window.fill((255,255,255))
#第一次刷新pygame.display.flip()
#第一次以后刷新：pygame.update()

font = pygame.font.Font('素材/书法.TTF',40)
word = font.render('四季如春',True,(255,255,0),(255,0,0))
window.blit(word,(175,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()