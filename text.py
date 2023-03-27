import pygame
from view import View

class Text(View):
    def __init__(self, text_input, font, pos, size, color, screen):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.size = size
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(text_input, True, color)
        screen.blit(self.text, (self.x_pos, self.y_pos))

    def set_size(self):
        pass

