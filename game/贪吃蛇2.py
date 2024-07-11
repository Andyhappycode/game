import pygame
import sys
import random

pygame.init()

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("贪吃蛇")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

snake_pos = [[100,100],[80,100],[60,100]]
food_pos = [300,300]

snake_speed = [20,0]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed = [0,-20]
            elif event.key == pygame.K_DOWN:
                snake_speed = [0,20]
            elif event.key == pygame.K_LEFT:
                snake_speed = [-20,0]
            elif event.key == pygame.K_RIGHT:
                snake_speed = [20,0]
    snake_pos.insert(0,[snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])

    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(1,screen_size[0] // 20) * 20,random.randrange(1,screen_size[0] // 20) * 20]
    else:
        snake_pos.pop()

    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_size[0] or snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_size[1] or snake_pos[0] in snake_pos[1:]:
        pygame.quit()
        sys.exit()


    screen.fill(WHITE)

    for pos in snake_pos:
        pygame.draw.rect(screen,GREEN,pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 20, 20))

    pygame.display.flip()

    pygame.time.Clock().tick(10)