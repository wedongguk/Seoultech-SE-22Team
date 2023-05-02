from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.util import *
import os

init_pygame()
check_config(config)
print('process id', os.getpid())

if bool(config['system']['COLOR_WEAKNESS_MODE']):
    color_weakness_value = True
else:
    color_weakness_value = False


# 메인 루프
def main_screen():
    init_bg(SCREEN, SCREEN_PATH + "start_screen.jpeg", 1280, 720)
    MAIN_BGM.set_volume(0.7)
    MAIN_BGM.play(-1)
    while True:
        play_button = Button(image=pygame.image.load(BUTTON_PATH + "play_button.png"),
                             pos=(x_pos, y_pos + 200),
                             size=(BUTTON_WIDTH, BUTTON_HEIGHT))

        options_button = Button(image=pygame.image.load(BUTTON_PATH + "options_button.png"),
                                pos=(x_pos, y_pos + 260),
                                size=(BUTTON_WIDTH, BUTTON_HEIGHT))

        exit_button = Button(image=pygame.image.load(BUTTON_PATH + "exit_button.png"),
                             pos=(x_pos, y_pos + 320),
                             size=(BUTTON_WIDTH, BUTTON_HEIGHT))

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
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT+5)
                elif options_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.option import options
                    options(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif exit_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    quit()
        pygame.display.update()


main_screen()
