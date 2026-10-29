import pygame
import colors

def draw_squares(list_of_squares, screen):
    for square in list_of_squares:
        square.draw(screen)

def draw_buttons(screen, color):
    pygame.draw.rect(screen, colors.red, [425, 450, 75,75], 75, 10)
    if color == colors.red:
        pygame.draw.rect(screen, colors.white, [425, 450, 75, 75], 5, 10)
    pygame.draw.rect(screen, colors.green, [425+75+25, 450, 75,75], 75, 10)
    if color == colors.green:
        pygame.draw.rect(screen, colors.white, [425+100, 450, 75, 75], 5, 10)
    pygame.draw.rect(screen, colors.blue, [425+150+50, 450, 75,75], 75, 10)
    if color == colors.blue:
        pygame.draw.rect(screen, colors.white, [425+200, 450, 75, 75], 5, 10)

def draw_screen(screen):
    pass

