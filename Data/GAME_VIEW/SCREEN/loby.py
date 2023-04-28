from Data.GAME_LOGIC.uno_Const import MODE_NORMAL
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.textbox import TextBox
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *


def loby(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, mode=MODE_NORMAL):
    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    start_button = Button(image=pygame.image.load(BUTTON_PATH + "start_button.png"),
                          pos=(x_pos, y_pos + 260),
                          size=(BUTTON_WIDTH, BUTTON_HEIGHT))

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
                    CLICK_SOUND.play(0)
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
                    from Data.GAME_VIEW.SCREEN.start import start_game
                    MAIN_BGM.stop()
                    from UNO_RUN import color_weakness_value
                    start_game(int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']),
                               AI_num,
                               name_list, color_weakness_value, mode)
                elif back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif AI_2.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    set_computer(2)
                elif AI_3.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    set_computer(3)
                elif AI_4.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    set_computer(4)
                elif AI_5.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
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
