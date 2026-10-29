import pygame


class Sqaure:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.width])


    def change_color(self, color):
        self.color = color


    def is_clicked(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.width:
            return True
        return False
