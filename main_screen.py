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


def init_bg(image, width, height):
    bg = pygame.image.load(image)
    return pygame.transform.scale(bg, (width, height))


def play():
    return 0


def options():
    while True:
        screen.fill("black")
        options_bg = init_bg("options_screen.png", screen_width, screen_height)
        screen.blit(options_bg, (0,0))

        # option screen에서 필요한 버튼 정의
        x_pos = screen_width / 2 - button_width / 2
        y_pos = screen_height / 2 - button_height / 2

        back_button = Button(image=pygame.image.load("back_button.png"),
                            pos=(30,30),
                            size=(50,50))
        save_button = Button(image=pygame.image.load("save_button.png"),
                             pos=(x_pos,y_pos+200),
                             size=(button_width-10, button_height+10))
        reset_button = Button(image=pygame.image.load("reset_button.png"),
                              pos=(x_pos, y_pos+260),
                              size=(button_width-10, button_height+10))

        
        init_button(screen, [back_button, save_button, reset_button])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    main_screen()

        pygame.display.update()


def quit():
    pygame.quit()
    sys.exit()

# 메인 루프
def main_screen():
    main_bg = init_bg("start_screen.jpeg", screen_width, screen_height)
    x_pos = screen_width/2 - button_width/2
    y_pos = screen_height/2 - button_height/2

    while True:
        screen.blit(main_bg, (0, 0))

        play_button = Button(image=pygame.image.load("play_button.png"),
                             pos=(x_pos, y_pos+200),
                             size=(button_width,button_height))

        options_button = Button(image=pygame.image.load("options_button.png"),
                                pos=(x_pos, y_pos+260),
                                size=(button_width,button_height))

        exit_button = Button(image=pygame.image.load("exit_button.png"),
                             pos=(x_pos, y_pos+320),
                             size=(button_width,button_height))

        init_button(screen, [play_button, options_button, exit_button])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    print("1")
                elif options_button.rect.collidepoint(event.pos):
                    options()
                elif exit_button.rect.collidepoint(event.pos):
                    quit()
        pygame.display.update()

main_screen()
