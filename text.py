import pygame
from view import View

class Text(View):
    def __init__(self, text_input, font, pos, size, base_color):
        self.font = font
        self.base_color = base_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def set_size(self):
        return pygame.transform.scale(self.text_input, (self.width, self.height))

