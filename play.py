import pygame

from main import init_bg


def play(screen, screen_width, screen_height):
    while True:
        screen.fill("black")
        play_bg = init_bg("play_screen.png", screen_width, screen_height)
        screen.blit(play_bg, (0, 0))
        pygame.display.flip()
