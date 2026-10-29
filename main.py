import pygame
import colors
import squares
import ui_drawing

# Инициализация
pygame.init()

squares_list = []

for i1 in range(16):
    for i2 in range(16):
        square = squares.Sqaure(colors.blue, 400+(i1*20), 100+(i2*20), 20)
        squares_list.append(square)

buttons_list = []
for i in range(3):
    square = squares.Sqaure(colors.rgb[i], 425+25*i + 75*i, 450, 75)
    buttons_list.append(square)

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test model 0.1")
current_color = colors.red

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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for square in squares_list:
            if square.is_clicked(mouse_x, mouse_y):
                square.change_color(current_color)

        for square in buttons_list:
            if square.is_clicked(mouse_x, mouse_y):
                current_color = square.color


    # 3. Отрисовка
    screen.fill(colors.background)          # очистить экран
    ui_drawing.draw_squares(squares_list, screen)
    ui_drawing.draw_buttons(screen,current_color)


    pygame.display.flip()       # показать нарисованное

    # 4. Ограничение FPS
    clock.tick(FPS)

# Завершение
pygame.quit()