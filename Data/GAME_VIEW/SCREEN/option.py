from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *
import pygame


def options(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT):
    global UNO, SELECT, LEFT, RIGHT, DRAW, width, height
    global color_weakness_value

    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    # option 화면에 필요한 버튼 설정
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))
    save_button = Button(image=pygame.image.load(BUTTON_PATH + "save_button.png"),
                         pos=(x_pos, y_pos + set_size(230, SCREEN_WIDTH)),
                         size=(BUTTON_WIDTH, BUTTON_HEIGHT))
    reset_button = Button(image=pygame.image.load(BUTTON_PATH + "reset_button.png"),
                          pos=(x_pos, y_pos + set_size(300, SCREEN_WIDTH)),
                          size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    on_button = Button(image=pygame.image.load(BUTTON_PATH + "on.png"),
                       pos=(SCREEN.get_rect().centerx - set_size(150, SCREEN_WIDTH),
                            SCREEN.get_rect().centery - set_size(230, SCREEN_WIDTH)),
                       size=(set_size(130, SCREEN_WIDTH), set_size(60, SCREEN_WIDTH)))
    off_button = Button(image=pygame.image.load(BUTTON_PATH + "off.png"),
                        pos=(SCREEN.get_rect().centerx + set_size(50, SCREEN_WIDTH),
                             SCREEN.get_rect().centery - set_size(230, SCREEN_WIDTH)),
                        size=(set_size(130, SCREEN_WIDTH), set_size(60, SCREEN_WIDTH)))

    resolution_button = []


    button_1920 = Button(image=pygame.image.load(BUTTON_PATH + "1920_button.png"),
                         pos=(SCREEN.get_rect().centerx - set_size(300, SCREEN_WIDTH),
                              SCREEN.get_rect().centery - set_size(80, SCREEN_WIDTH)),
                         size=(set_size(160, SCREEN_WIDTH), set_size(60, SCREEN_WIDTH)))
    button_1280 = Button(image=pygame.image.load(BUTTON_PATH + "1280_button.png"),
                         pos=(SCREEN.get_rect().centerx - set_size(80, SCREEN_WIDTH),
                              SCREEN.get_rect().centery - set_size(80, SCREEN_WIDTH)),
                         size=(set_size(160, SCREEN_WIDTH), set_size(60, SCREEN_WIDTH)))
    button_960 = Button(image=pygame.image.load(BUTTON_PATH + "960_button.png"),
                        pos=(SCREEN.get_rect().centerx + set_size(140, SCREEN_WIDTH),
                             SCREEN.get_rect().centery - set_size(80, SCREEN_WIDTH)),
                        size=(set_size(160, SCREEN_WIDTH), set_size(60, SCREEN_WIDTH)))

    # option 화면에 필요한 텍스트 설정
    color_weakness_mode_text = Text(text_input="Color Weakness Mode",
                                    font="notosanscjkkr",
                                    color=(0, 0, 0),
                                    pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(100, SCREEN_WIDTH)),
                                    size=set_size(50, SCREEN_WIDTH),
                                    screen=SCREEN)

    resolution_text = Text(text_input="Resolution",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(240, SCREEN_WIDTH)),
                           size=set_size(50, SCREEN_WIDTH),
                           screen=SCREEN)

    key_setting_text = Text(text_input="Key Setting",
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(380, SCREEN_WIDTH)),
                            size=set_size(50, SCREEN_WIDTH),
                            screen=SCREEN)

    uno_text = Text(text_input="UNO",
                    font="notosanscjkkr",
                    color=(0, 0, 0),
                    pos=(SCREEN.get_rect().centerx - set_size(200, SCREEN_WIDTH),
                         SCREEN.get_rect().top + set_size(420, SCREEN_WIDTH)),
                    size=set_size(25, SCREEN_WIDTH),
                    screen=SCREEN)

    uno_set_button = Button(image=pygame.image.load(BUTTON_PATH + "key_button.png"),
                            pos=(SCREEN.get_rect().centerx - set_size(240, SCREEN_WIDTH),
                                 SCREEN.get_rect().centery + set_size(90, SCREEN_WIDTH)),
                            size=(set_size(80, SCREEN_WIDTH), set_size(80, SCREEN_WIDTH)))

    uno_button_text = Text(text_input="UNO",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(SCREEN.get_rect().centerx - set_size(200, SCREEN_WIDTH),
                                uno_set_button.y_pos),
                           size=set_size(25, SCREEN_WIDTH),
                           screen=SCREEN)

    return_text = Text(text_input="RETURN",
                       font="notosanscjkkr",
                       color=(0, 0, 0),
                       pos=(SCREEN.get_rect().centerx - set_size(100, SCREEN_WIDTH),
                            SCREEN.get_rect().top + set_size(420, SCREEN_WIDTH)),
                       size=set_size(25, SCREEN_WIDTH),
                       screen=SCREEN)

    left_move_text = Text(text_input="LEFT",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(420, SCREEN_WIDTH)),
                          size=set_size(25, SCREEN_WIDTH),
                          screen=SCREEN)

    right_move_text = Text(text_input="RIGHT",
                           font="notosanscjkkr",
                           color=(0, 0, 0),
                           pos=(SCREEN.get_rect().centerx + set_size(100, SCREEN_WIDTH),
                                SCREEN.get_rect().top + set_size(420, SCREEN_WIDTH)),
                           size=set_size(25, SCREEN_WIDTH),
                           screen=SCREEN)

    draw_text = Text(text_input="DRAW",
                     font="notosanscjkkr",
                     color=(0, 0, 0),
                     pos=(SCREEN.get_rect().centerx + set_size(200, SCREEN_WIDTH),
                          SCREEN.get_rect().top + set_size(420, SCREEN_WIDTH)),
                     size=set_size(25, SCREEN_WIDTH),
                     screen=SCREEN)

    # 설정값 불러오기
    if config['system']['COLOR_WEAKNESS_MODE'] == "True":
        on_button.image = pygame.image.load(BUTTON_PATH + "on_checked.png")
        off_button.image = pygame.image.load(BUTTON_PATH + "off.png")
    else:
        on_button.image = pygame.image.load(BUTTON_PATH + "on.png")
        off_button.image = pygame.image.load(BUTTON_PATH + "off_checked.png")

    if config['system']['SCREEN_WIDTH'] == "1920":
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_checked.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "1280":
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_checked.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
    elif config['system']['SCREEN_WIDTH'] == "960":
        button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
        button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
        button_960.image = pygame.image.load(BUTTON_PATH + "960_checked.png")

    RESOLUTION = [config['system']['SCREEN_WIDTH'], config['system']['SCREEN_HEIGHT']]
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
                   button_1920, button_1280, button_960, reset_button,
                   uno_set_button])

        uno_button_text.init_text()

        UNO = eval(f"{config['system']['UNO']}")
        SELECT = eval(f"{config['system']['SELECT']}")
        LEFT = eval(f"{config['system']['LEFT_MOVE']}")
        RIGHT = eval(f"{config['system']['RIGHT_MOVE']}")
        DRAW = eval(f"{config['system']['DRAW']}")

        # 키 설정
        key_setting_bg = pygame.image.load(BUTTON_PATH + "key_button.png")
        key_setting_bg = pygame.transform.scale(key_setting_bg,
                                                (set_size(80, SCREEN_WIDTH), set_size(80, SCREEN_WIDTH)))

        # 우노 버튼 설정
        Uno_button_rect = key_setting_bg.get_rect()
        Uno_button_rect.centerx = SCREEN.get_rect().centerx - set_size(200, SCREEN_WIDTH)
        Uno_button_rect.centery = SCREEN.get_rect().top + set_size(480, SCREEN_WIDTH)
        Uno_text = font.render(pygame.key.name(UNO), True, (0, 0, 0))
        Uno_rect = Uno_text.get_rect()
        Uno_rect.centerx = Uno_button_rect.centerx
        Uno_rect.centery = Uno_button_rect.centery

        # 선택 버튼 설정
        Select_button_rect = key_setting_bg.get_rect()
        Select_button_rect.centerx = SCREEN.get_rect().centerx - set_size(100, SCREEN_WIDTH)
        Select_button_rect.centery = SCREEN.get_rect().top + set_size(480, SCREEN_WIDTH)
        Select_text = font.render(pygame.key.name(SELECT), True, (0, 0, 0))
        Select_rect = Select_text.get_rect()
        Select_rect.centerx = Select_button_rect.centerx
        Select_rect.centery = Select_button_rect.centery

        # 왼쪽 이동 버튼 설정
        L_button_rect = key_setting_bg.get_rect()
        L_button_rect.centerx = SCREEN.get_rect().centerx
        L_button_rect.centery = SCREEN.get_rect().top + set_size(480, SCREEN_WIDTH)
        L_text = font.render(pygame.key.name(LEFT), True, (0, 0, 0))
        L_rect = L_text.get_rect()
        L_rect.centerx = L_button_rect.centerx
        L_rect.centery = L_button_rect.centery

        # 오른쪽 이동 버튼 설정
        R_button_rect = key_setting_bg.get_rect()
        R_button_rect.centerx = SCREEN.get_rect().centerx + set_size(100, SCREEN_WIDTH)
        R_button_rect.centery = SCREEN.get_rect().top + set_size(480, SCREEN_WIDTH)
        R_text = font.render(pygame.key.name(RIGHT), True, (0, 0, 0))
        R_rect = R_text.get_rect()
        R_rect.centerx = R_button_rect.centerx
        R_rect.centery = R_button_rect.centery

        # 드로우 버튼 설정
        Draw_button_rect = key_setting_bg.get_rect()
        Draw_button_rect.centerx = SCREEN.get_rect().centerx + set_size(200, SCREEN_WIDTH)
        Draw_button_rect.centery = SCREEN.get_rect().top + set_size(480, SCREEN_WIDTH)
        Draw_text = font.render(pygame.key.name(DRAW), True, (0, 0, 0))
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
                    CLICK_SOUND.play(0)
                    from UNO_RUN import main_screen
                    main_screen()
                elif save_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    config['system']['SCREEN_WIDTH'] = str(RESOLUTION[0])
                    config['system']['SCREEN_HEIGHT'] = str(RESOLUTION[1])
                    save_config(config)
                    from UNO_RUN import main_screen
                    main_screen()
                elif reset_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    on_button.image = pygame.image.load(BUTTON_PATH + "on.png")
                    off_button.image = pygame.image.load(BUTTON_PATH + "off_checked.png")
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_checked.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")

                    reset_config(config)

                    width = "1280"
                    height = "720"
                elif Uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                    CLICK_SOUND.play(0)
                    print("Press the key for Uno direction")
                    UNO = key_change()
                    # if pygame.key.name(UNO) == 'up' or pygame.key.name(UNO) == 'right' or pygame.key.name(
                    #         UNO) == 'left' or pygame.key.name(UNO) == 'return':
                    #     config['system']['UNO'] = 'pygame.K_' + (pygame.key.name(UNO)).upper()
                    # else:
                    #     config['system']['UNO'] = 'pygame.K_' + pygame.key.name(UNO)
                    # save_config(config)
                elif Select_button_rect.collidepoint(pygame.mouse.get_pos()):
                    CLICK_SOUND.play(0)
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
                    CLICK_SOUND.play(0)
                    print("Press the key for LEFT")
                    LEFT = key_change()
                    # if pygame.key.name(LEFT) == 'up' or pygame.key.name(LEFT) == 'right' or pygame.key.name(
                    #         LEFT) == 'left' or pygame.key.name(LEFT) == 'return':
                    #     config['system']['LEFT_MOVE'] = 'pygame.K_' + (pygame.key.name(LEFT)).upper()
                    # else:
                    #     config['system']['LEFT_MOVE'] = 'pygame.K_' + pygame.key.name(LEFT)
                    # save_config(config)
                elif R_button_rect.collidepoint(pygame.mouse.get_pos()):
                    CLICK_SOUND.play(0)
                    print("Press the key for RIGHT")
                    RIGHT = key_change()
                    # if pygame.key.name(RIGHT) == 'up' or pygame.key.name(RIGHT) == 'right' or pygame.key.name(
                    #         RIGHT) == 'left' or pygame.key.name(RIGHT) == 'return':
                    #     config['system']['RIGHT_MOVE'] = 'pygame.K_' + (pygame.key.name(RIGHT)).upper()
                    # else:
                    #     config['system']['RIGHT_MOVE'] = 'pygame.K_' + pygame.key.name(RIGHT)
                    # save_config(config)
                elif Draw_rect.collidepoint(pygame.mouse.get_pos()):
                    CLICK_SOUND.play(0)
                    print("Press the key for DRAW")
                    DRAW = key_change()
                    if pygame.key.name(DRAW) == 'up' or pygame.key.name(DRAW) == 'right' or pygame.key.name(
                            DRAW) == 'left' or pygame.key.name(DRAW) == 'return':
                        config['system']['DRAW'] = 'pygame.K_' + (pygame.key.name(DRAW)).upper()
                    else:
                        config['system']['DRAW'] = 'pygame.K_' + pygame.key.name(DRAW)
                    save_config(config)
                elif on_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    on_button.image = pygame.image.load(BUTTON_PATH + "on_checked.png")
                    off_button.image = pygame.image.load(BUTTON_PATH + "off.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "True"
                    color_weakness_value = True
                elif off_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    on_button.image = pygame.image.load(BUTTON_PATH + "on.png")
                    off_button.image = pygame.image.load(BUTTON_PATH + "off_checked.png")
                    config['system']['COLOR_WEAKNESS_MODE'] = "False"
                    color_weakness_value = False
                elif button_1920.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_checked.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
                    RESOLUTION[0] = 1920
                    RESOLUTION[1] = 1080
                elif button_1280.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_checked.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_button.png")
                    RESOLUTION[0] = 1280
                    RESOLUTION[1] = 720
                elif button_960.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    button_1920.image = pygame.image.load(BUTTON_PATH + "1920_button.png")
                    button_1280.image = pygame.image.load(BUTTON_PATH + "1280_button.png")
                    button_960.image = pygame.image.load(BUTTON_PATH + "960_checked.png")
                    RESOLUTION[0] = 960
                    RESOLUTION[1] = 540
                elif uno_set_button.rect.collidepoint(event.pos):
                    UNO = key_change()
                    print("Press the key for DRAW")

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
