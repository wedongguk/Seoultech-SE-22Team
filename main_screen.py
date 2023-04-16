import pygame
import os
import sys
from button import Button
from main import init_bg, init_pygame
from start import start
from view import init_view
from text import Text
import configparser
from checkbox import Checkbox

os.chdir(os.getcwd() + "/img")

init_pygame()

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

x_pos = screen_width / 2 - button_width / 2
y_pos = screen_height / 2 - button_height / 2


def play():
    screen.fill("black")
    play_bg = init_bg("start_screen.jpeg", screen_width, screen_height)
    screen.blit(play_bg, (0, 0))
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    default_mode_button = Button(image=pygame.image.load("default_mode_button.png"),
                                 pos=(x_pos, y_pos - 50),
                                 size=(button_width, button_height))

    story_mode_button = Button(image=pygame.image.load("story_mode_button.png"),
                               pos=(x_pos, y_pos + 50),
                               size=(button_width, button_height))

    init_view(screen, [back_button, default_mode_button, story_mode_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if default_mode_button.rect.collidepoint(event.pos):
                    loby()
                elif story_mode_button.rect.collidepoint(event.pos):
                    print("1")
                    story_mode()
                elif back_button.rect.collidepoint(event.pos):
                    main_screen()
        pygame.display.flip()


def loby():
    screen.fill("white")
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    start_button = Button(image=pygame.image.load("start_button.png"),
                          pos=(x_pos, y_pos + 260),
                          size=(button_width, button_height))

    init_view(screen, [back_button, start_button])


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    start(screen, screen_width, screen_height)
                elif back_button.rect.collidepoint(event.pos):
                    play()
        pygame.display.flip()


def story_mode():
    screen.fill("white")
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    story_mode_1 = Button(image=pygame.image.load("story_mode_1.png"),
                          pos=(screen.get_rect().centerx - 250, screen.get_rect().centery - 100),
                          size=(150, 150))

    story_mode_2 = Button(image=pygame.image.load("story_mode_2.png"),
                          pos=(screen.get_rect().centerx, screen.get_rect().centery - 100),
                          size=(150, 150))

    story_mode_3 = Button(image=pygame.image.load("story_mode_3.png"),
                          pos=(screen.get_rect().centerx - 250, screen.get_rect().centery + 150),
                          size=(150, 150))

    story_mode_4 = Button(image=pygame.image.load("story_mode_4.png"),
                          pos=(screen.get_rect().centerx, screen.get_rect().centery + 150),
                          size=(150, 150))

    init_view(screen, [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    play()
        pygame.display.flip()


def options():
    global UNO, SELECT, LEFT, RIGHT

    # 체크박스 초기화
    COLOR_WEAKNESS_MODE_ON = Checkbox(screen, screen.get_rect().centerx - 100, 130, 0, caption='ON')
    COLOR_WEAKNESS_MODE_OFF = Checkbox(screen, screen.get_rect().centerx + 30, 130, 1, caption='OFF')

    RESOLUTION_1920 = Checkbox(screen, screen.get_rect().centerx - 230, 280, 0, caption='1920 X 1080')
    RESOLUTION_1280 = Checkbox(screen, screen.get_rect().centerx - 70, 280, 1, caption='1280 X 720')
    RESOLUTION_960 = Checkbox(screen, screen.get_rect().centerx + 80, 280, 1, caption='960 X 540')

    color_weakness_boxes = [COLOR_WEAKNESS_MODE_ON, COLOR_WEAKNESS_MODE_OFF]
    resolution_boxes = [RESOLUTION_1920, RESOLUTION_1280, RESOLUTION_960]

    #
    if config['system']['COLOR_WEAKNESS_MODE'] == "True":
        COLOR_WEAKNESS_MODE_ON.checked = True
        COLOR_WEAKNESS_MODE_OFF.checked = False
    else:
        COLOR_WEAKNESS_MODE_ON.checked = False
        COLOR_WEAKNESS_MODE_OFF.checked = True

    if config['system']['SCREEN_WIDTH'] == "1920":
        RESOLUTION_1920.checked = True
        RESOLUTION_1280.checked = False
        RESOLUTION_960.checked = False
    elif config['system']['SCREEN_WIDTH'] == "1280":
        RESOLUTION_1920.checked = False
        RESOLUTION_1280.checked = True
        RESOLUTION_960.checked = False
    elif config['system']['SCREEN_WIDTH'] == "960":
        RESOLUTION_1920.checked = False
        RESOLUTION_1280.checked = False
        RESOLUTION_960.checked = True

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
                             size=(button_width, button_height))
        reset_button = Button(image=pygame.image.load("reset_button.png"),
                              pos=(x_pos, y_pos + 300),
                              size=(button_width, button_height))

        # 텍스트 설정
        color_weakness_mode_text = Text(text_input="Color Weakness Mode",
                                        font="notosanscjkkr",
                                        color=(0, 0, 0),
                                        pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                                        size=50,
                                        screen=screen)
        color_weakness_mode_text.init_text()
        resolution_text = Text(text_input="Resolution",
                               font="notosanscjkkr",
                               color=(0, 0, 0),
                               pos=(screen.get_rect().centerx, screen.get_rect().top + 240),
                               size=50,
                               screen=screen)
        resolution_text.init_text()

        key_setting_text = Text(text_input="Key Setting",
                                font="notosanscjkkr",
                                color=(0, 0, 0),
                                pos=(screen.get_rect().centerx, screen.get_rect().top + 380),
                                size=50,
                                screen=screen)
        key_setting_text.init_text()

        init_view(screen, [back_button, save_button, reset_button])

        UNO = eval(f"{config['system']['UNO']}")
        SELECT = eval(f"{config['system']['SELECT']}")
        LEFT = eval(f"{config['system']['LEFT_MOVE']}")
        RIGHT = eval(f"{config['system']['RIGHT_MOVE']}")

        # 키 설정
        key_setting_bg = pygame.image.load("green_button.png")
        key_setting_bg = pygame.transform.scale(key_setting_bg, (80, 80))
        # 우노 버튼 설정
        Uno_button_rect = key_setting_bg.get_rect()
        Uno_button_rect.centerx = screen.get_rect().centerx - 150
        Uno_button_rect.centery = screen.get_rect().top + 450
        Uno_text = font.render(pygame.key.name(UNO), True, (0, 0, 0))
        Uno_rect = Uno_text.get_rect()
        Uno_rect.centerx = Uno_button_rect.centerx
        Uno_rect.centery = Uno_button_rect.centery
        # 선택 버튼 설정
        Select_button_rect = key_setting_bg.get_rect()
        Select_button_rect.centerx = screen.get_rect().centerx - 50
        Select_button_rect.centery = screen.get_rect().top + 450
        Select_text = font.render(pygame.key.name(SELECT), True, (0, 0, 0))
        Select_rect = Select_text.get_rect()
        Select_rect.centerx = Select_button_rect.centerx
        Select_rect.centery = Select_button_rect.centery
        # 왼쪽 이동 버튼 설정
        L_button_rect = key_setting_bg.get_rect()
        L_button_rect.centerx = screen.get_rect().centerx + 50
        L_button_rect.centery = screen.get_rect().top + 450
        L_text = font.render(pygame.key.name(LEFT), True, (0, 0, 0))
        L_rect = L_text.get_rect()
        L_rect.centerx = L_button_rect.centerx
        L_rect.centery = L_button_rect.centery
        # 오른쪽 이동 버튼 설정
        R_button_rect = key_setting_bg.get_rect()
        R_button_rect.centerx = screen.get_rect().centerx + 150
        R_button_rect.centery = screen.get_rect().top + 450
        R_text = font.render(pygame.key.name(RIGHT), True, (0, 0, 0))
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
                for box in color_weakness_boxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        if box.idnum == 0:
                            config['system']['COLOR_WEAKNESS_MODE'] = "True"
                            print("ON")
                        else:
                            config['system']['COLOR_WEAKNESS_MODE'] = "False"
                            print("off")
                        for b in color_weakness_boxes:
                            if b != box:
                                b.checked = False

                if back_button.rect.collidepoint(event.pos):
                    main_screen()
                elif save_button.rect.collidepoint(event.pos):
                    save_config()
                    main_screen()
                elif Uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Uno direction")
                    UNO = key_change()
                    pygame.key.name(UNO)
                    config['system']['UNO'] = 'pygame.K_' + pygame.key.name(UNO)
                    save_config()
                elif Select_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for Select direction")
                    SELECT = key_change()
                    pygame.key.name(SELECT)
                    config['system']['SELECT'] = 'pygame.K_' + pygame.key.name(SELECT)
                    save_config()
                elif L_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for LEFT direction")

                    LEFT = key_change()
                    pygame.key.name(LEFT)
                    config['system']['LEFT_MOVE'] = 'pygame.K_' + pygame.key.name(LEFT)
                    save_config()
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Press the key for RIGHT direction")
                    RIGHT = key_change()
                    pygame.key.name(RIGHT)
                    config['system']['RIGHT_MOVE'] = 'pygame.K_' + pygame.key.name(RIGHT)
                    save_config()
        for box in color_weakness_boxes:
            box.render_checkbox()
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
                    play()
                elif options_button.rect.collidepoint(event.pos):
                    options()
                elif exit_button.rect.collidepoint(event.pos):
                    quit()
        pygame.display.update()


main_screen()
