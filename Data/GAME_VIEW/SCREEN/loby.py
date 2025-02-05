from Data.GAME_LOGIC.uno_Const import MODE_NORMAL
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.textbox import TextBox
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.util import *

init_pygame()
check_config(config)

if bool(config['system']['COLOR_WEAKNESS_MODE']):
    color_weakness_value = True
else:
    color_weakness_value = False


def loby(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, mode=MODE_NORMAL):
    x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))
    start_button = Button(image=pygame.image.load(BUTTON_PATH + "start_button.png"),
                          pos=(x_pos, y_pos + set_size(260, SCREEN_WIDTH)),
                          size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    AI_1 = Button(image=pygame.image.load(BUTTON_PATH + "1_checked.png"),
                  pos=(x_pos - set_size(360, SCREEN_WIDTH), y_pos - set_size(180, SCREEN_WIDTH)),
                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    AI_2 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos - set_size(160, SCREEN_WIDTH), y_pos - set_size(180, SCREEN_WIDTH)),
                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    AI_3 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + set_size(40, SCREEN_WIDTH), y_pos - set_size(180, SCREEN_WIDTH)),
                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    AI_4 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + set_size(240, SCREEN_WIDTH), y_pos - set_size(180, SCREEN_WIDTH)),
                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))
    AI_5 = Button(image=pygame.image.load(BUTTON_PATH + "empty.png"),
                  pos=(x_pos + set_size(440, SCREEN_WIDTH), y_pos - set_size(180, SCREEN_WIDTH)),
                  size=(set_size(100, SCREEN_WIDTH), set_size(100, SCREEN_WIDTH)))

    title_text = Text(text_input="Set computer that will play with you",
                      font=FONT_PATH,
                      color=(0, 0, 0),
                      pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(100, SCREEN_WIDTH)),
                      size=set_size(50, SCREEN_WIDTH),
                      screen=SCREEN)
    subtitle_text = Text(text_input="Set your name",
                         font=FONT_PATH,
                         color=(0, 0, 0),
                         pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + set_size(400, SCREEN_WIDTH)),
                         size=set_size(50, SCREEN_WIDTH),
                         screen=SCREEN)
    AI_list = [AI_1, AI_2, AI_3, AI_4, AI_5]
    title_text.init_text()
    subtitle_text.init_text()

    input_boxes = [TextBox(SCREEN.get_rect().left + set_size(535, SCREEN_WIDTH),
                           set_size(450, SCREEN_WIDTH),
                           set_size(200, SCREEN_WIDTH),
                           set_size(32, SCREEN_WIDTH))]

    for i in range(0, 5):
        input_boxes.append(
            TextBox(SCREEN.get_rect().left + set_size(130 + i*200, SCREEN_WIDTH),
                    set_size(270, SCREEN_WIDTH),
                    set_size(170, SCREEN_WIDTH),
                    set_size(32, SCREEN_WIDTH))
        )

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
                # start 버튼 클릭 이벤트 발생시
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
