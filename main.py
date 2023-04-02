import pygame


def init_pygame():
    pygame.init()
    pygame.display.set_caption("Uno game")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)


def init_bg(image, width, height):
    bg = pygame.image.load(image)
    return pygame.transform.scale(bg, (width, height))
