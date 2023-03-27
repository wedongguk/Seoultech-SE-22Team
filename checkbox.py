import pygame

class Checkbox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.checked = False
        self.check_image = pygame.Surface((width, height))
        self.check_image.fill((255, 255, 255))
        pygame.draw.line(self.check_image, (0, 0, 0), (0, height // 2), (width // 2, height), 2)
        pygame.draw.line(self.check_image, (0, 0, 0), (width // 2, height), (width, 0), 2)

    def draw(self, surface):
        if self.checked:
            surface.blit(self.check_image, self.rect)
        else:
            pygame.draw.rect(surface, (255, 255, 255), self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked