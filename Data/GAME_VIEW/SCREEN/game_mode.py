from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.util import *
from Data.GAME_VIEW.OBJECT.view import init_view
import pygame


def select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT):
    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))

    single_mode_button = Button(image=pygame.image.load(BUTTON_PATH + "single_mode_button.png"),
                                 pos=(x_pos, y_pos - 100),
                                 size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    multi_mode_button = Button(image=pygame.image.load(BUTTON_PATH + "multi_mode_button.png"),
                                pos=(x_pos, y_pos),
                                size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    story_mode_button = Button(image=pygame.image.load(BUTTON_PATH + "story_mode_button.png"),
                               pos=(x_pos, y_pos + 100),
                               size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    title_text = Text(text_input="Select game mode",
                      font="notosanscjkkr",
                      color=(0, 0, 0),
                      pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 100),
                      size=50,
                      screen=SCREEN)
    title_text.init_text()
    init_view(SCREEN, [back_button, single_mode_button, multi_mode_button, story_mode_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_mode_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.loby import loby
                    loby(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                if multi_mode_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.multi_mode_set import multi_mode_set
                    multi_mode_set(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif story_mode_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.story_mode import story_mode
                    story_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from UNO_RUN import main_screen
                    main_screen()
        pygame.display.update()
