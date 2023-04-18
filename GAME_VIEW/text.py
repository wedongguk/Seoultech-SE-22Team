import pygame
from GAME_VIEW.view import View

class Text(View):
    def __init__(self, text_input, font, pos, size, color, screen):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.size = size
        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(text_input, True, color)
        self.rect = self.text.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos
        self.screen = screen


    def set_size(self):
        pass

    def init_text(self):
        self.screen.blit(self.text, self.rect)
