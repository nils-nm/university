import pygame
import random

WIDTH = 500
HEIGHT = 500
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

x = random.randint(10, 490)
y = random.randint(10, 490)
r = 10

move = [0, 0, 1, 1]

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            exit()

    # Обновление

    if (x >= WIDTH - r):
        move[3] = 0
        move[0] = 1
    if (x <= r):
        move[0] = 0
        move[3] = 1
    if (y >= HEIGHT - r):
        move[1] = 1
        move[2] = 0
    if (y <= r):
        move[2] = 1
        move[1] = 0


    if move == [0, 1, 0, 1]:
        x += 5
        y -= 5
    elif move == [1, 1, 0, 0]:
        x -= 5
        y -= 5
    elif move == [1, 0, 1, 0]:
        x -= 5
        y += 5
    elif move == [0, 0, 1, 1]:
        x += 5
        y += 5



    # Рендеринг
    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (x, y), r)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
