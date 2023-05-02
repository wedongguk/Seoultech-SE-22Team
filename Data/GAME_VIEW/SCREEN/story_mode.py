from Data.GAME_LOGIC.uno_Const import MODE_NORMAL, MODE_ALLCARD, MODE_CHANGECOLOR, MODE_OPENSHUFFLE
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.textbox import TextBox
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *


def story_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT):
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
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif story_mode_1.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.SCREEN.loby import loby
                    loby(SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif story_mode_2.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.SCREEN.start import start_game
                    from UNO_RUN import color_weakness_value
                    start_game(SCREEN, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 3,
                               ["USER", "COMPUTER1", "COMPUTER2", "COMPUTER3", "COMPUTER4"], color_weakness_value,
                               MODE_ALLCARD)
                elif story_mode_3.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.SCREEN.start import start_game
                    from UNO_RUN import color_weakness_value
                    start_game(SCREEN, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']), 2,
                               ["USER", "COMPUTER1", "COMPUTER2"], color_weakness_value,
                               MODE_CHANGECOLOR)
                elif story_mode_4.rect.collidepoint(event.pos):
                    from Data.GAME_VIEW.SCREEN.start import start_game
                    loby(SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, BUTTON_WIDTH, BUTTON_HEIGHT, mode = MODE_OPENSHUFFLE)
        pygame.display.flip()