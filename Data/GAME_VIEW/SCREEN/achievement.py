from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.util import *
import pygame



# 메인 루프
def achievement_screen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT):
    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    single_win_button = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                         pos=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))
    key_setting_text = Text(text_input=config['system']['SINGLE_WIN_DATE'],
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(380, SCREEN_WIDTH)),
                            size=set_size(50, SCREEN_WIDTH),
                            screen=SCREEN)
    
    if config['system']['SINGLE_WIN'] == "True":
        single_win_button.image = pygame.image.load(BUTTON_PATH + "achievement_checked.png")
        key_setting_text.text_input = config['system']['SINGLE_WIN_DATE']
    else:
        single_win_button.image = pygame.image.load(BUTTON_PATH + "achievement_button.png")
    while True:
        init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        init_view(SCREEN, [back_button, single_win_button])
        key_setting_text.init_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from UNO_RUN import main_screen
                    main_screen()
        pygame.display.update()