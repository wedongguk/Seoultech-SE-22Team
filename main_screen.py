import pygame
import os
import sys
from button import Button, init_button

os.chdir(os.getcwd() + "/img")

pygame.init()
pygame.display.set_caption("Uno game")

screen_width = 1280
screen_height = 720
button_width = 220
button_height = 50

screen = pygame.display.set_mode((screen_width, screen_height))

main_bg = pygame.image.load("start_screen.jpeg")
main_bg = pygame.transform.scale(main_bg, (screen_width, screen_height))


def play():
    return 0


def options():
    return 0


def quit():
    pygame.quit()
    sys.exit()


# 메인 루프
def main_screen():
    while True:
        screen.blit(main_bg, (0, 0))

        play_button = Button(image=pygame.image.load("play_button.png"),
                             pos=(screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 200),
                             width=button_width,
                             height=button_height)

        options_button = Button(image=pygame.image.load("options_button.png"),
                                pos=(screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 260),
                                width=button_width,
                                height=button_height)

        exit_button = Button(image=pygame.image.load("exit_button.png"),
                             pos=(screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 320),
                             width=button_width,
                             height=button_height)

        init_button(screen, [play_button, options_button, exit_button])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    print("1")
                elif options_button.rect.collidepoint(event.pos):
                    print("2")
                elif exit_button.rect.collidepoint(event.pos):
                    quit()
        pygame.display.update()



main_screen()
