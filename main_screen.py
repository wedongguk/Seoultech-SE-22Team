import pygame
import os
import sys
from button import Button
from view import init_view
from text import Text
import configparser

os.chdir(os.getcwd() + "/img")

pygame.init()
pygame.display.set_caption("Uno game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


def save_config():
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def change_str_to_var(str):
    return eval(f"{str}")


try:
    if config['system']['is_new'] == "False":
        print("config file o")
except:
    print("config file x")
    config['system'] = {}
    config['system']['is_new'] = "False"
    config['system']['COLOR_WEAKNESS_MODE'] = "FALSE"
    config['system']['SCREEN_WIDTH'] = "1280"
    config['system']['SCREEN_HEIGHT'] = "720"
    config['system']['UNO'] = 'pygame.K_u'
    config['system']['LEFT_MOVE'] = 'pygame.K_RIGHT'
    config['system']['RIGHT_MOVE'] = 'pygame.K_LEFT'
    config['system']['SELECT'] = 'pygame.K_RETURN'
    save_config()


screen_width = int(config['system']['SCREEN_WIDTH'])
screen_height = int(config['system']['SCREEN_HEIGHT'])

button_width = 220
button_height = 50

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont(None, 30)


def init_bg(image, width, height):
    bg = pygame.image.load(image)
    return pygame.transform.scale(bg, (width, height))


def play():
    return 0

def options():
    global UNO, SELECT, LEFT, RIGHT
    while True:
        screen.fill("black")
        options_bg = init_bg("options_screen.png", screen_width, screen_height)
        screen.blit(options_bg, (0, 0))

        # option screen에서 필요한 버튼 설정
        x_pos = screen_width / 2 - button_width / 2
        y_pos = screen_height / 2 - button_height / 2

        back_button = Button(image=pygame.image.load("back_button.png"),
                             pos=(30, 30),
                             size=(50, 50))
        save_button = Button(image=pygame.image.load("save_button.png"),
                             pos=(x_pos, y_pos + 230),
                             size=(button_width - 30, button_height + 5))
        reset_button = Button(image=pygame.image.load("reset_button.png"),
                              pos=(x_pos, y_pos + 300),
                              size=(button_width - 30, button_height + 5))

        # 텍스트 설정
        Text(text_input="Color Weakness Mode",
             font="notosanscjkkr",
             color=(0, 0, 0),
             pos=(x_pos, 20),
             size=50,
             screen=screen)

        Text(text_input="Resolution",
             font="notosanscjkkr",
             color=(0, 0, 0),
             pos=(x_pos, 100),
             size=50,
             screen=screen)

        Text(text_input="Key Setting",
             font="notosanscjkkr",
             color=(0, 0, 0),
             pos=(x_pos, 200),
             size=50,
             screen=screen)

        init_view(screen, [back_button, save_button, reset_button])

        UNO = eval(f"{config['system']['UNO']}")
        SELECT = eval(f"{config['system']['SELECT']}")
        LEFT = eval(f"{config['system']['LEFT_MOVE']}")
        RIGHT = eval(f"{config['system']['RIGHT_MOVE']}")

        # 키 설정
        key_setting_bg = pygame.image.load("gray_button.png")
        key_setting_bg = pygame.transform.scale(key_setting_bg, (80, 80))
        # 우노 버튼 설정
        Uno_button_rect = key_setting_bg.get_rect()
        Uno_button_rect.centerx = screen.get_rect().centerx - 120
        Uno_button_rect.centery = screen.get_rect().centery - 100
        Uno_text = font.render(pygame.key.name(UNO), True, (255, 255, 255))
        Uno_rect = Uno_text.get_rect()
        Uno_rect.centerx = Uno_button_rect.centerx
        Uno_rect.centery = Uno_button_rect.centery
        # 선택 버튼 설정
        Select_button_rect = key_setting_bg.get_rect()
        Select_button_rect.centerx = screen.get_rect().centerx - 40
        Select_button_rect.centery = screen.get_rect().centery - 100
        Select_text = font.render(pygame.key.name(SELECT), True, (255, 255, 255))
        Select_rect = Select_text.get_rect()
        Select_rect.centerx = Select_button_rect.centerx
        Select_rect.centery = Select_button_rect.centery
        # 왼쪽 이동 버튼 설정
        L_button_rect = key_setting_bg.get_rect()
        L_button_rect.centerx = screen.get_rect().centerx + 40
        L_button_rect.centery = screen.get_rect().centery - 100
        L_text = font.render(pygame.key.name(LEFT), True, (255, 255, 255))
        L_rect = L_text.get_rect()
        L_rect.centerx = L_button_rect.centerx
        L_rect.centery = L_button_rect.centery
        # 오른쪽 이동 버튼 설정
        R_button_rect = key_setting_bg.get_rect()
        R_button_rect.centerx = screen.get_rect().centerx + 120
        R_button_rect.centery = screen.get_rect().centery - 100
        R_text = font.render(pygame.key.name(RIGHT), True, (255, 255, 255))
        R_rect = R_text.get_rect()
        R_rect.centerx = R_button_rect.centerx
        R_rect.centery = R_button_rect.centery

        screen.blit(key_setting_bg, Uno_button_rect)
        screen.blit(Uno_text, Uno_rect)
        screen.blit(key_setting_bg, Select_button_rect)
        screen.blit(Select_text, Select_rect)
        screen.blit(key_setting_bg, L_button_rect)
        screen.blit(L_text, L_rect)
        screen.blit(key_setting_bg, R_button_rect)
        screen.blit(R_text, R_rect)

        # 메인 루프
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    main_screen()
                elif save_button.rect.collidepoint(event.pos):
                    pygame.display.set_mode((720, 480))
                elif Uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Uno direction")
                    UNO = key_change()
                    pygame.key.name(UNO)
                    config['system']['UNO'] = 'pygame.K_' + pygame.key.name(UNO)
                    save_config()
                elif Select_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Select direction")
                    SELECT = key_change()
                elif L_button_rect.collidepoint(pygame.mouse.get_pos()):
                    LEFT = key_change()
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for RIGHT direction")
                    RIGHT = key_change()

            elif event.type == pygame.KEYDOWN:
                if event.key == UNO:
                    print("Press the key Uno")
                    pass
                elif event.key == SELECT:
                    print("Press the key Select")
                    pass
                elif event.key == LEFT:
                    print("Press the key Left")
                    pass
                elif event.key == RIGHT:
                    print("Press the key Rignt")
                    pass
        pygame.display.flip()


def key_change():
    tmp = 0
    # 바꿀 조작키 입력 루프
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            tmp = event.key
            if tmp == UNO or tmp == SELECT or tmp == LEFT or tmp == RIGHT:
                print("used key")
            else:
                break
    return tmp

def quit():
    pygame.quit()
    sys.exit()


# 메인 루프
def main_screen():
    main_bg = init_bg("start_screen.jpeg", screen_width, screen_height)
    x_pos = screen_width / 2 - button_width / 2
    y_pos = screen_height / 2 - button_height / 2

    while True:
        screen.blit(main_bg, (0, 0))

        play_button = Button(image=pygame.image.load("play_button.png"),
                             pos=(x_pos, y_pos + 200),
                             size=(button_width, button_height))

        options_button = Button(image=pygame.image.load("options_button.png"),
                                pos=(x_pos, y_pos + 260),
                                size=(button_width, button_height))

        exit_button = Button(image=pygame.image.load("exit_button.png"),
                             pos=(x_pos, y_pos + 320),
                             size=(button_width, button_height))

        init_view(screen, [play_button, options_button, exit_button])

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