import pygame
from GAME_VIEW.view import View


class Button(View):
    def __init__(self, image, pos, size, check=False):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        # self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.width = size[0]
        self.height = size[1]
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def set_size(self):
        return pygame.transform.scale(self.image, (self.width, self.height))
