import pygame
i = 0

pygame.init()

window = pygame.display.set_mode((800, 500))
pygame.display.set_caption('图片')
window.fill((255,255,255))

image1 = pygame.image.load('素材/大自然.png')
image2 = pygame.transform.scale(image1,(800,500))
image3 = pygame.image.load('素材/桥.jpg')
image4 = pygame.transform.scale(image3,(800,500))
window.blit(image2,(0,0))

pygame.display.flip()#第一次刷新
#第一次以后刷新：pygame.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if i == 0:
                window.blit(image4,(0,0))
                i=1
            else:
                window.blit(image2,(0,0))
                i=0
    pygame.display.update()