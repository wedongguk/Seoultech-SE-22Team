import pygame

class Button():
    def __init__(self, image, pos, width, height):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        # self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)


    def update(self, btn, screen):
        screen.blit(btn, (self.x_pos, self.y_pos))


    def set_size(self):
        return pygame.transform.scale(self.image, (self.width, self.height))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

def init_button(screen, list):
    for button in list:
        temp = button.set_size()
        button.update(temp, screen)