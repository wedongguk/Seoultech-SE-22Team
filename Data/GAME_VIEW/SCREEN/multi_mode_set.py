import pygame.image

from Data.GAME_LOGIC.uno_Const import MODE_NORMAL
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.OBJECT.textbox import TextBox
from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.SCREEN.multi_start import multi_start_game
from Data.GAME_VIEW.util import *
from Data.SOCKET.client_socket_m import client
from Data.SOCKET.server_socket_m import start_server, start_new_thread


def multi_mode_set(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, mode=MODE_NORMAL):
    init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)

    back_button = Button(image=pygame.image.load(BUTTON_PATH + "back_button.png"),
                         pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                         size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))

    join_box = Button(image=pygame.image.load(ASSET_PATH + "box.png"),
                      pos=(SCREEN.get_rect().right - 580, 70),
                      size=(400, 500))
    create_box = Button(image=pygame.image.load(ASSET_PATH + "box.png"),
                        pos=(SCREEN.get_rect().left + 170, 70),
                        size=(400, 500))
    create_button = Button(image=pygame.image.load(BUTTON_PATH + "create_button.png"),
                           pos=(create_box.rect.centerx - 110, SCREEN.get_rect().bottom - 110),
                           size=(BUTTON_WIDTH, BUTTON_HEIGHT))
    join_button = Button(image=pygame.image.load(BUTTON_PATH + "join_button.png"),
                         pos=(join_box.rect.centerx - 110, SCREEN.get_rect().bottom - 110),
                         size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    create_game_text = Text(text_input="CREATE GAME",
                            font="notosanscjkkr",
                            color=(0, 0, 0),
                            pos=(create_box.rect.centerx, SCREEN.get_rect().top + 110),
                            size=set_size(50, SCREEN_WIDTH),
                            screen=SCREEN)
    join_game_text = Text(text_input="JOIN GAME",
                          font="notosanscjkkr",
                          color=(0, 0, 0),
                          pos=(join_box.rect.centerx, SCREEN.get_rect().top + 110),
                          size=set_size(50, SCREEN_WIDTH),
                          screen=SCREEN)

    input_boxes = []

    for i in range(0, 2):
        input_boxes.append(
            TextBox(SCREEN.get_rect().left + set_size(200, SCREEN_WIDTH),
                    set_size(200 + i*100, SCREEN_WIDTH),
                    set_size(340, SCREEN_WIDTH),
                    set_size(32, SCREEN_WIDTH))
        )

    for i in range(0, 2):
        input_boxes.append(
            TextBox(SCREEN.get_rect().right - set_size(550, SCREEN_WIDTH),
                    set_size(200 + i*100, SCREEN_WIDTH),
                    set_size(340, SCREEN_WIDTH),
                    set_size(32, SCREEN_WIDTH))
        )

    create_game_text.init_text()
    join_game_text.init_text()

    init_view(SCREEN, [back_button, create_box, join_box, create_button, join_button])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_server = True
                if create_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    # 서버 소켓 생성
                    print("server")
                    # start_server()
                    # start_new_thread()
                    
                    AI_num = 2
                    name_list = ["1번 플레이어", "2번 플레이어", "3번 플레이어"]
                    color_weakness_value = False
                    
                    multi_start_game(is_server, int(config['system']['SCREEN_WIDTH']), int(config['system']['SCREEN_HEIGHT']),AI_num, name_list, color_weakness_value, mode)

                    
                    pass

                elif join_button.rect.collidepoint(event.pos):
                    # 클라이언트 소켓 생성
                    is_server = False
                    print("client")
                    client()
                    multi_start_game(is_server)
                    pass

                
                elif back_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        init_bg(SCREEN, SCREEN_PATH + "options_screen.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        init_view(SCREEN, [back_button, create_box, join_box, create_button, join_button])
        create_game_text.init_text()
        join_game_text.init_text()
        for box in input_boxes:
            box.draw(SCREEN)
        pygame.display.flip()
