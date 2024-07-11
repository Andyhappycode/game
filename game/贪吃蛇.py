import pygame  
import random  
  
# 初始化pygame  
pygame.init()  
  
# 设置游戏窗口大小  
WIDTH, HEIGHT = 640, 480  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("贪吃蛇")  
  
# 设置颜色  
WHITE = (255, 255, 255)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
  
# 设置蛇和食物的大小  
SNAKE_BLOCK = 20  
FOOD_BLOCK = 10  
  
# 初始化蛇和食物的位置  
snake = [(10, 10), (9, 10), (8, 10)]  
food = (random.randint(0, (WIDTH // SNAKE_BLOCK) - 1), random.randint(0, (HEIGHT // SNAKE_BLOCK) - 1))  
  
# 设置游戏的速度  
clock = pygame.time.Clock()  
FPS = 10  
  
# 游戏主循环  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:  
                if snake[0][1] > 0:  
                    snake[0] = (snake[0][0], snake[0][1] - 1)  
            elif event.key == pygame.K_DOWN:  
                if snake[0][1] < (HEIGHT // SNAKE_BLOCK) - 1:  
                    snake[0] = (snake[0][0], snake[0][1] + 1)  
            elif event.key == pygame.K_LEFT:  
                if snake[0][0] > 0:  
                    snake[0] = (snake[0][0] - 1, snake[0][1])  
            elif event.key == pygame.K_RIGHT:  
                if snake[0][0] < (WIDTH // SNAKE_BLOCK) - 1:  
                    snake[0] = (snake[0][0] + 1, snake[0][1])  
  
    # 检查蛇是否吃到食物  
    if snake[0] == food:  
        food = (random.randint(0, (WIDTH // SNAKE_BLOCK) - 1), random.randint(0, (HEIGHT // SNAKE_BLOCK) - 1))  
    else:  
        snake.pop()  # 移除蛇尾  

  
    # 添加新的蛇头到蛇身  
    snake.insert(0, snake[0])  
  
    # 渲染游戏  
    screen.fill(WHITE)  
    for segment in snake:  
        pygame.draw.rect(screen, GREEN, (segment[0] * SNAKE_BLOCK, segment[1] * SNAKE_BLOCK, SNAKE_BLOCK, SNAKE_BLOCK))  
    pygame.draw.rect(screen, RED, (food[0] * SNAKE_BLOCK, food[1] * SNAKE_BLOCK, FOOD_BLOCK, FOOD_BLOCK))  
    pygame.display.flip()  
  
    # 控制游戏速度  
    clock.tick(FPS)  
  
pygame.quit()
