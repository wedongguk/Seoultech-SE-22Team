from Data.GAME_LOGIC.uno_Const import MODE_NORMAL
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.textbox import TextBox
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *


def multi_mode_set(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, mode=MODE_NORMAL):
    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    init_view(SCREEN, [back_button])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.display.flip()
