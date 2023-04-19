import pygame.mixer

from Data.GAME_LOGIC.uno_Const import MODE_NORMAL, MODE_ALLCARD, MODE_CHANGECOLOR, MODE_OPENSHUFFLE
from Data.GAME_VIEW.textbox import TextBox
from Data.GAME_VIEW.view import init_view
from Data.GAME_VIEW.button import Button
from Data.GAME_VIEW.text import Text
from Data.GAME_VIEW.util import *
import configparser

init_pygame()

config = configparser.ConfigParser()
config.read('Data/config.ini', encoding='utf-8')

check_config(config)

if bool(config['system']['COLOR_WEAKNESS_MODE']):
    color_weakness_value = True
else:
    color_weakness_value = False

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

button_width = 220
button_height = 50

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FONT = pygame.font.SysFont(None, 30)

x_pos = SCREEN_WIDTH / 2 - button_width / 2
y_pos = SCREEN_HEIGHT / 2 - button_height / 2

click_sound = pygame.mixer.Sound(SOUND_PATH + "click_bgm.wav")
bgm = pygame.mixer.Sound(SOUND_PATH + "main_bgm.mp3")
bgm.set_volume(0.7)
bgm.play(-1)


def play():
    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    default_mode_button = Button(image=pygame.image.load(BUTTON_PATH + "default_mode_button.png"),
                                 pos=(x_pos, y_pos - 50),
                                 size=(button_width, button_height))

    story_mode_button = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_button.png"),
                               pos=(x_pos, y_pos + 50),
                               size=(button_width, button_height))

    title_text = Text(text_input="Select game mode",
                      font="notosanscjkkr",
                      color=(0, 0, 0),
                      pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 100),
                      size=50,
                      screen=SCREEN)
    title_text.init_text()
    init_view(SCREEN, [back_button, default_mode_button, story_mode_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if default_mode_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    loby()
                elif story_mode_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    story_mode()
                elif back_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    main_screen()
        pygame.display.flip()


def loby(mode=MODE_NORMAL):
    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    start_button = Button(image=pygame.image.load(BUTTON_PATH + "start_button.png"),
                          pos=(x_pos, y_pos + 260),
                          size=(button_width, button_height))

    AI_1 = Button(image=pygame.image.load(BUTTON_PATH + "1_checked.png"),
                  pos=(x_pos - 360, y_pos - 120),
                  size=(100, 100))
    AI_2 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos - 160, y_pos - 120),
                  size=(100, 100))
    AI_3 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + 40, y_pos - 120),
                  size=(100, 100))
    AI_4 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + 240, y_pos - 120),
                  size=(100, 100))
    AI_5 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + 440, y_pos - 120),
                  size=(100, 100))

    title_text = Text(text_input="Set computer that will play with you",
                      font="notosanscjkkr",
                      color=(0, 0, 0),
                      pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 100),
                      size=50,
                      screen=SCREEN)
    subtitle_text = Text(text_input="Set your name",
                         font="notosanscjkkr",
                         color=(0, 0, 0),
                         pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 450),
                         size=50,
                         screen=SCREEN)
    AI_list = [AI_1, AI_2, AI_3, AI_4, AI_5]
    title_text.init_text()
    subtitle_text.init_text()

    input_boxes = [TextBox(SCREEN.get_rect().left + 520, 500, 80, 32),
                   TextBox(SCREEN.get_rect().left + 120, 350, 80, 32),
                   TextBox(SCREEN.get_rect().left + 320, 350, 80, 32),
                   TextBox(SCREEN.get_rect().left + 520, 350, 80, 32),
                   TextBox(SCREEN.get_rect().left + 720, 350, 80, 32),
                   TextBox(SCREEN.get_rect().left + 920, 350, 80, 32)]

    init_view(SCREEN, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
    bool_list = [True, False, False, False, False]

    def set_computer(num):
        if bool_list[num - 1]:
            AI_list[num - 1].image = pygame.image.load(BUTTON_PATH + "empty.png")
            bool_list[num - 1] = False
        else:
            AI_list[num - 1].image = pygame.image.load(BUTTON_PATH + str(num) + "_checked.png")
            bool_list[num - 1] = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    AI_num = 0
                    name_list = []
                    temp = 1
                    if input_boxes[0].text == '':
                        name_list.append("USER")
                    else:
                        name_list.append(input_boxes[0].text)
                    for i in bool_list:
                        if i:
                            AI_num += 1
                            if input_boxes[temp].text == '':
                                name_list.append("Computer" + str(temp))
                            else:
                                name_list.append(input_boxes[temp].text)
                        temp += 1
                    from Data.GAME_VIEW.start import start_game
                    bgm.stop()
                    start_game(SCREEN, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']),
                               AI_num,
                               name_list, color_weakness_value, mode)
                elif back_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    play()
                elif AI_2.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    set_computer(2)
                elif AI_3.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    set_computer(3)
                elif AI_4.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    set_computer(4)
                elif AI_5.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    set_computer(5)
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        init_view(SCREEN, [back_button, start_button, AI_1, AI_2, AI_3, AI_4, AI_5])
        title_text.init_text()
        subtitle_text.init_text()
        for box in input_boxes:
            box.draw(SCREEN)
        pygame.display.flip()


def story_mode():
    init_bg(SCREEN, SCREEN_PATH + "story_mode_map.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    story_mode_1 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_1.png"),
                          pos=(SCREEN.get_rect().centerx - 420, SCREEN.get_rect().centery - 200),
                          size=(70, 70))

    story_mode_2 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_2.png"),
                          pos=(SCREEN.get_rect().centerx - 400, SCREEN.get_rect().centery + 100),
                          size=(70, 70))

    story_mode_3 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_3.png"),
                          pos=(SCREEN.get_rect().centerx + 150, SCREEN.get_rect().centery - 180),
                          size=(70, 70))

    story_mode_4 = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_4.png"),
                          pos=(SCREEN.get_rect().centerx + 390, SCREEN.get_rect().centery + 110),
                          size=(70, 70))

    init_view(SCREEN, [back_button, story_mode_1, story_mode_2, story_mode_3, story_mode_4])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    play()
                elif story_mode_1.rect.collidepoint(event.pos):
                    loby()
                elif story_mode_2.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.start import start_game
                    start_game(SCREEN, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 3,
                               ["USER", "COMPUTER1", "COMPUTER2", "COMPUTER3", "COMPUTER4"], color_weakness_value,
                               MODE_ALLCARD)
                elif story_mode_3.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.start import start_game
                    start_game(SCREEN, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 2,
                               ["USER", "COMPUTER1", "COMPUTER2"], color_weakness_value,
                               MODE_CHANGECOLOR)
                elif story_mode_4.rect.collidepoint(event.pos):
                    loby(MODE_OPENSHUFFLE)
        pygame.display.flip()


def options():
    global UNO, SELECT, LEFT, RIGHT, DRAW, width, height
    global color_weakness_value

    # option 화면에 필요한 버튼 설정
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    save_button = Button(image=pygame.image.load(BUTTON_PATH + "save_button.png"),
                         pos=(x_pos, y_pos + 230),
                         size=(button_width, button_height))
    reset_button = Button(image=pygame.image.load(BUTTON_PATH + "reset_button.png"),
                          pos=(x_pos, y_pos + 300),
                          size=(button_width, button_height))

    on_button = Button(image=pygame.image.load(BUTTON_PATH + "on.png"),
                       pos=(SCREEN.get_rect().centerx - 150, SCREEN.get_rect().centery - 230),
                       size=(130, 60))
    off_button = Button(image=pygame.image.load(BUTTON_PATH + "off.png"),
                        pos=(SCREEN.get_rect().centerx + 50, SCREEN.get_rect().centery - 230),
                        size=(130, 60))
    button_1920 = Button(image=pygame.image.load(BUTTON_PATH + "1920_button.png"),
                         pos=(SCREEN.get_rect().centerx - 300, SCREEN.get_rect().centery - 80),
                         size=(160, 60))
    button_1280 = Button(image=pygame.image.load(BUTTON_PATH + "1280_button.png"),
                         pos=(SCREEN.get_rect().centerx - 80, SCREEN.get_rect().centery - 80),
                         size=(160, 60))
    button_960 = Button(image=pygame.image.load(BUTTON_PATH + "960_button.png"),
                        pos=(SCREEN.get_rect().centerx + 140, SCREEN.get_rect().centery - 80),
                        size=(160, 60))

    # option 화면에 필요한 텍스트 설정
    color_weakness_mode_text = Text(text_input="Color Weakness Mode",
                                    font="notosanscjkkr",
                                    color=(0, 0, 0),
                                    pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 100),
                                    size=50,
                                    screen=SCREEN)

    resolution_text = Text(text_input="Resolution",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 240),
                           size=50,
                           screen=SCREEN)

    key_setting_text = Text(text_input="Key Setting",
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 380),
                            size=50,
                            screen=SCREEN)

    uno_text = Text(text_input="UNO",
                    font="notosanscjkkr",
                    color=(0, 0, 0),
                    pos=(SCREEN.get_rect().centerx - 200, SCREEN.get_rect().top + 420),
                    size=25,
                    screen=SCREEN)

    return_text = Text(text_input="RETURN",
                       font="notosanscjkkr",
                       color=(0, 0, 0),
                       pos=(SCREEN.get_rect().centerx - 100, SCREEN.get_rect().top + 420),
                       size=25,
                       screen=SCREEN)

    left_move_text = Text(text_input="LEFT",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 420),
                          size=25,
                          screen=SCREEN)

    right_move_text = Text(text_input="RIGHT",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(SCREEN.get_rect().centerx + 100, SCREEN.get_rect().top + 420),
                           size=25,
                           screen=SCREEN)

    draw_text = Text(text_input="DRAW",
                     font="notosanscjkkr",
                     color=(0, 0, 0),
                     pos=(SCREEN.get_rect().centerx + 200, SCREEN.get_rect().top + 420),
                     size=25,
                     screen=SCREEN)

    # 설정값 불러오기
    if config['system']['COLOR_WEAKNESS_MODE'] == "True":
        on_button.image = pygame.image.load(BUTTON_PATH + "on_checked.png")
        off_button.image = pygame.image.load(BUTTON_PATH + "off.png")
    else:
        on_button.image = pygame.image.load(BUTTON_PATH + "on.png")
        off_button.image = pygame.image.load(BUTTON_PATH + "off_checked.png")

    if config['system']['SCREEN_WIDTH'] == "1920":
        width = "1920"
        height = "1080"
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_checked.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "1280":
        width = "1280"
        height = "720"
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_checked.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "960":
        width = "960"
        height = "540"
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_checked.png")

    while True:
        init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        # 텍스트 표시
        color_weakness_mode_text.init_text()
        resolution_text.init_text()
        key_setting_text.init_text()
        uno_text.init_text()
        return_text.init_text()
        left_move_text.init_text()
        right_move_text.init_text()
        draw_text.init_text()

        # 버튼 표시
        init_view(SCREEN,
                  [back_button, save_button, on_button, off_button,
                   button_1920, button_1280, button_960, reset_button])

        UNO = eval(f"{config['system']['UNO']}")
        SELECT = eval(f"{config['system']['SELECT']}")
        LEFT = eval(f"{config['system']['LEFT_MOVE']}")
        RIGHT = eval(f"{config['system']['RIGHT_MOVE']}")
        DRAW = eval(f"{config['system']['DRAW']}")

        # 키 설정
        key_setting_bg = pygame.image.load(BUTTON_PATH + "key_button.png")
        key_setting_bg = pygame.transform.scale(key_setting_bg, (80, 80))

        # 우노 버튼 설정
        Uno_button_rect = key_setting_bg.get_rect()
        Uno_button_rect.centerx = SCREEN.get_rect().centerx - 200
        Uno_button_rect.centery = SCREEN.get_rect().top + 480
        Uno_text = FONT.render(pygame.key.name(UNO), True, (0, 0, 0))
        Uno_rect = Uno_text.get_rect()
        Uno_rect.centerx = Uno_button_rect.centerx
        Uno_rect.centery = Uno_button_rect.centery

        # 선택 버튼 설정
        Select_button_rect = key_setting_bg.get_rect()
        Select_button_rect.centerx = SCREEN.get_rect().centerx - 100
        Select_button_rect.centery = SCREEN.get_rect().top + 480
        Select_text = FONT.render(pygame.key.name(SELECT), True, (0, 0, 0))
        Select_rect = Select_text.get_rect()
        Select_rect.centerx = Select_button_rect.centerx
        Select_rect.centery = Select_button_rect.centery

        # 왼쪽 이동 버튼 설정
        L_button_rect = key_setting_bg.get_rect()
        L_button_rect.centerx = SCREEN.get_rect().centerx
        L_button_rect.centery = SCREEN.get_rect().top + 480
        L_text = FONT.render(pygame.key.name(LEFT), True, (0, 0, 0))
        L_rect = L_text.get_rect()
        L_rect.centerx = L_button_rect.centerx
        L_rect.centery = L_button_rect.centery

        # 오른쪽 이동 버튼 설정
        R_button_rect = key_setting_bg.get_rect()
        R_button_rect.centerx = SCREEN.get_rect().centerx + 100
        R_button_rect.centery = SCREEN.get_rect().top + 480
        R_text = FONT.render(pygame.key.name(RIGHT), True, (0, 0, 0))
        R_rect = R_text.get_rect()
        R_rect.centerx = R_button_rect.centerx
        R_rect.centery = R_button_rect.centery

        # 드로우 버튼 설정
        Draw_button_rect = key_setting_bg.get_rect()
        Draw_button_rect.centerx = SCREEN.get_rect().centerx + 200
        Draw_button_rect.centery = SCREEN.get_rect().top + 480
        Draw_text = FONT.render(pygame.key.name(DRAW), True, (0, 0, 0))
        Draw_rect = Draw_text.get_rect()
        Draw_rect.centerx = Draw_button_rect.centerx
        Draw_rect.centery = Draw_button_rect.centery

        SCREEN.blit(key_setting_bg, Uno_button_rect)
        SCREEN.blit(Uno_text, Uno_rect)
        SCREEN.blit(key_setting_bg, Select_button_rect)
        SCREEN.blit(Select_text, Select_rect)
        SCREEN.blit(key_setting_bg, L_button_rect)
        SCREEN.blit(L_text, L_rect)
        SCREEN.blit(key_setting_bg, R_button_rect)
        SCREEN.blit(R_text, R_rect)
        SCREEN.blit(key_setting_bg, Draw_button_rect)
        SCREEN.blit(Draw_text, Draw_rect)

        # 메인 루프
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    main_screen()
                elif save_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    config['system']['SCREEN_WIDTH'] = str(width)
                    config['system']['SCREEN_HEIGHT'] = str(height)
                    save_config(config)
                    main_screen()
                elif reset_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    on_button.image = pygame.image.load("on.png")
                    off_button.image = pygame.image.load("off_checked.png")
                    button_1920.image = pygame.image.load("1920_button.png")
                    button_1280.image = pygame.image.load("1280_checked.png")
                    button_960.image = pygame.image.load("960_button.png")

                    config['system']['COLOR_WEAKNESS_MODE'] = "FALSE"
                    config['system']['SCREEN_WIDTH'] = "1280"
                    config['system']['SCREEN_HEIGHT'] = "720"
                    config['system']['UNO'] = 'pygame.K_u'
                    config['system']['LEFT_MOVE'] = 'pygame.K_RIGHT'
                    config['system']['RIGHT_MOVE'] = 'pygame.K_LEFT'
                    config['system']['SELECT'] = 'pygame.K_RETURN'

                    width = "1280"
                    height = "720"
                elif Uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play(0)
                    print("Press the key for Uno direction")
                    UNO = key_change()
                    if pygame.key.name(UNO) == 'up' or pygame.key.name(UNO) == 'right' or pygame.key.name(
                            UNO) == 'left' or pygame.key.name(UNO) == 'return':
                        config['system']['UNO'] = 'pygame.K_' + (pygame.key.name(UNO)).upper()
                    else:
                        config['system']['UNO'] = 'pygame.K_' + pygame.key.name(UNO)
                    save_config(config)
                elif Select_button_rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play(0)
                    print("Press the key for Select")
                    SELECT = key_change()
                    pygame.key.name(SELECT)
                    if pygame.key.name(SELECT) == 'up' or pygame.key.name(SELECT) == 'right' or pygame.key.name(
                            SELECT) == 'left' or pygame.key.name(SELECT) == 'return':
                        config['system']['SELECT'] = 'pygame.K_' + (pygame.key.name(SELECT)).upper()
                    else:
                        config['system']['SELECT'] = 'pygame.K_' + pygame.key.name(SELECT)
                    save_config(config)
                elif L_button_rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play(0)
                    print("Press the key for LEFT")
                    LEFT = key_change()
                    pygame.key.name(LEFT)
                    if pygame.key.name(LEFT) == 'up' or pygame.key.name(LEFT) == 'right' or pygame.key.name(
                            LEFT) == 'left' or pygame.key.name(LEFT) == 'return':
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + (pygame.key.name(LEFT)).upper()
                    else:
                        config['system']['LEFT_MOVE'] = 'pygame.K_' + pygame.key.name(LEFT)
                    save_config(config)
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play(0)
                    print("Press the key for RIGHT")
                    RIGHT = key_change()
                    if pygame.key.name(RIGHT) == 'up' or pygame.key.name(RIGHT) == 'right' or pygame.key.name(
                            RIGHT) == 'left' or pygame.key.name(RIGHT) == 'return':
                        config['system']['RIGHT_MOVE'] = 'pygame.K_' + (pygame.key.name(RIGHT)).upper()
                    else:
                        config['system']['RIGHT_MOVE'] = 'pygame.K_' + pygame.key.name(RIGHT)
                    save_config(config)
                elif Draw_rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play(0)
                    print("Press the key for DRAW")
                    DRAW = key_change()
                    if pygame.key.name(DRAW) == 'up' or pygame.key.name(DRAW) == 'right' or pygame.key.name(
                            DRAW) == 'left' or pygame.key.name(DRAW) == 'return':
                        config['system']['DRAW'] = 'pygame.K_' + (pygame.key.name(DRAW)).upper()
                    else:
                        config['system']['DRAW'] = 'pygame.K_' + pygame.key.name(DRAW)
                    save_config(config)
                elif on_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    on_button.image = pygame.image.load(BUTTON_PATH + "on_checked.png")
                    off_button.image = pygame.image.load(BUTTON_PATH + "off.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "True"
                    color_weakness_value = True
                elif off_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    on_button.image = pygame.image.load(BUTTON_PATH + "on.png")
                    off_button.image = pygame.image.load(BUTTON_PATH + "off_checked.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "False"
                    color_weakness_value = False
                elif button_1920.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_checked.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
                    width = "1920"
                    height = "1080"
                elif button_1280.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_checked.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
                    width = "1280"
                    height = "720"
                elif button_960.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_checked.png")
                    width = "960"
                    height = "540"
        pygame.display.flip()


def key_change():
    # 바꿀 조작키 입력 루프
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            tmp = event.key
            if tmp == UNO or tmp == SELECT or tmp == LEFT or tmp == RIGHT or tmp == DRAW:
                print("used key")
            else:
                break
    return tmp


# 메인 루프
def main_screen():
    init_bg(SCREEN, SCREEN_PATH + "start_screen.jpeg", 1280, 720)
    while True:
        play_button = Button(image=pygame.image.load(BUTTON_PATH + "play_button.png"),
                             pos=(x_pos, y_pos + 200),
                             size=(button_width, button_height))

        options_button = Button(image=pygame.image.load(BUTTON_PATH + "options_button.png"),
                                pos=(x_pos, y_pos + 260),
                                size=(button_width, button_height))

        exit_button = Button(image=pygame.image.load(BUTTON_PATH + "exit_button.png"),
                             pos=(x_pos, y_pos + 320),
                             size=(button_width, button_height))

        title_text = Text(text_input="UNO GAME",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 30),
                          size=70,
                          screen=SCREEN)

        init_view(SCREEN, [play_button, options_button, exit_button])
        title_text.init_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    play()
                elif options_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    options()
                elif exit_button.rect.collidepoint(event.pos):
                    click_sound.play(0)
                    quit()
        pygame.display.update()


main_screen()
