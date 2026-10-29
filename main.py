import pygame
import colors
import squares

# Инициализация
pygame.init()

squares_list = []
for i1 in range(16):
    for i2 in range(16):
        square = squares.Sqaure((255,255,255), 400+(i1*20), 100+(i2*20), 20,20)
        squares_list.append(square)


# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test model 0.1")

clock = pygame.time.Clock()
FPS = 60

# Главный цикл
running = True
while running:
    # 1. Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mouse_but = pygame.mouse.get_pressed()
    if mouse_but[0]:
        mmouse_x, mouse_y = pygame.mouse.get_pos()
        for square in squares_list:
            if square.is_clicked(mmouse_x, mouse_y):
                square.change_color(colors.black)
    # 3. Отрисовка
    screen.fill(colors.background)          # очистить экран
    for square in squares_list:
        square.draw(screen)


    pygame.display.flip()       # показать нарисованное

    # 4. Ограничение FPS
    clock.tick(FPS)

# Завершение
pygame.quit()