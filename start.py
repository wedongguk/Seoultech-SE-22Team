import pygame
import os
from uno_Player import *
from unoCore import Game
from uno_Card import *
from uno_Pile import *
from uno_Const import *
from main import init_bg
from view import init_view
from text import Text
from button import Button

volume = 1

def start(screen, screen_width, screen_height, num, name):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)

    x_pos = screen_width / 2
    y_pos = screen_height / 2

    screen.fill((0, 0, 0))

    user1 = Player(name[0], True)
    gamePlayerList = [user1]
    for i in range(1, num + 1):
        gamePlayerList.append(Player(name[i], False))
    g = Game(gamePlayerList)

    screen = pygame.display.set_mode(screen_size)

    g.ready(screen_size)

    clock = pygame.time.Clock()
    global bgm
    bgm = pygame.mixer.Sound("bgm.mp3")
    bgm.play(-1)
    while True:
        screen.fill((0, 0, 0))
        user_rect = (0, screen_height * 3 / 5, screen_width * 3 / 5, screen_height * 2 / 5)
        playerArea = pygame.draw.rect(screen, (120, 120, 120), user_rect)

        bot_rect = (screen_width * 3 / 5, 0, screen_width * 2 / 5, screen_height)
        playerArea = pygame.draw.rect(screen, (120, 120, 0), bot_rect)

        board_rect = (0, 0, screen_width * 3 / 5, screen_height * 3 / 5)
        playerArea = pygame.draw.rect(screen, (25, 150, 75), board_rect)

        for i in range(g.playerList.size()):
            playerSlot(screen, i, g.playerList.idxPlayer(i), bot_rect)

        hand = g.userHand()  # 유저 핸드 부분
        userH = createCards(hand, user_rect)
        init_view(screen, userH)

        openCardIndicator(screen, g, board_rect)  # openCard
        createIndicator(screen, g.openCard.cardList[-1], board_rect)  # indicator
        createDeck(screen, g, board_rect)  # deck

        actlist = g.actList()
        # drawbtn

        dbtn = createDrawBtn(screen, g, board_rect)  # draw 버튼
        ubtn = createUnoBtn(screen, g, board_rect)  # uno 버튼

        TIMER_FONT = pygame.font.SysFont('Arial', 30)  # 타이머
        timer_text = TIMER_FONT.render(str(g.timer.time // 60 + 1), True, (255, 255, 255))
        timer_rect = timer_text.get_rect()
        timer_rect.center = (screen_height // 2, 50)
        button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
        screen.blit(timer_text, timer_rect)
        g.update()
        # botHand(screen, screen_size, pc1)
        pause_button = Button(image=pygame.image.load("pause_button.png"),
                              pos=(30, 30),
                              size=(50, 50))
        init_view(screen, [pause_button])
        cbtn = createColorBtn(board_rect)

        # colorChangebtn
        if actlist['colorBtn']:
            init_view(screen, cbtn)
        # numberChangebtn
        if actlist['numberBtn']:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(userH)):
                    if userH[i].rect.collidepoint(event.pos):  # 카드 버튼
                        played = g.eventCardBtn(i)
                        if played:
                            pass  ## 카드 냈을 때 소리
                        else:
                            pass  ## 카드 못냈을 때 소리

                for i in range(0, len(cbtn)):  # 색깔 바꾸는 버
                    if cbtn[i].rect.collidepoint(event.pos):
                        g.eventColorBtn(i)

                if dbtn.rect.collidepoint(event.pos):  # 드로우 버튼
                    if actlist['drawBtn']:  # actList가 true인 경우에만 함수 실행
                        g.eventDrawBtn()
                elif ubtn.rect.collidepoint(event.pos):  # 우노 버튼
                    if actlist['unoBtn']:  # actList가 true인 경우에만 함수 실행
                        g.eventUnoBtn()
                elif pause_button.rect.collidepoint(event.pos):
                    pause(screen, screen_width, screen_height)
        pygame.display.flip()

        if g.winner != None:
            winner_screen(screen, screen_width, screen_height, g.winner.playerName)

        clock.tick(60)


def pause(screen, screen_width, screen_height):
    global volume
    back_button = Button(image=pygame.image.load("back_button.png"),
                         pos=(30, 30),
                         size=(50, 50))
    volume_up_button = Button(image=pygame.image.load("volume_up_button.png"),
                       pos=(screen.get_rect().centerx - 150, screen.get_rect().centery - 230),
                       size=(130, 60))
    volume_down_button = Button(image=pygame.image.load("volume_down_button.png"),
                        pos=(screen.get_rect().centerx + 50, screen.get_rect().centery - 230),
                        size=(130, 60))
    bool = True
    while bool:
        screen.fill("black")
        options_bg = init_bg("options_screen.png", screen_width, screen_height)
        screen.blit(options_bg, (0, 0))
        init_view(screen, [back_button, volume_up_button, volume_down_button])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    bool = False
                elif volume_up_button.rect.collidepoint(event.pos):
                    volume += 0.1
                    bgm.set_volume(volume)
                elif volume_down_button.rect.collidepoint(event.pos):
                    volume -= 0.1
                    bgm.set_volume(volume)
        pygame.display.flip()


def winner_screen(screen, screen_width, screen_height, winner):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    screen.fill("black")

    winner_bg = init_bg("options_screen.png", screen_width, screen_height)
    screen.blit(winner_bg, (0, 0))

    button_width = 220
    button_height = 50

    x_pos = screen_width / 2 - button_width / 2
    y_pos = screen_height / 2 - button_height / 2

    play_button = Button(image=pygame.image.load("play_button.png"),
                         pos=(x_pos, y_pos + 200),
                         size=(button_width, button_height))
    winnername_text = Text(text_input=winner + ' is winner!',
                           font=None,
                           color=(0, 0, 0),
                           pos=(screen.get_rect().centerx, screen.get_rect().top + 100),
                           size=screen_height // 5,
                           screen=screen)
    winnername_text.init_text()
    init_view(screen, [play_button])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    print("game start")
                    file_path = os.getcwd()
                    dir_path = os.path.dirname(file_path)
                    os.chdir(dir_path)
                    from main_screen import main_screen
                    main_screen()
        pygame.display.flip()


def createOneCard(card_o, pos_o, size_o):
    c = card_o
    c_img = f"images/" + c.imgName() + ".png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn


def createBackCard(pos_o, size_o):
    c_img = f"images/back.png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn


##### card generator #####


def createCards(card_lst, rect):
    temp = []
    cnt = 0
    cnt_x = 0
    cnt_y = 0
    for i in range(0, len(card_lst)):
        x = rect[2] / 8 * 0.8
        y = x * 1.2
        if (rect[0] + (x * 1.1) * (i - cnt_x + 1)) >= rect[0] + rect[2]:
            cnt_x = cnt
            cnt_y = cnt_y + 1
        c_pos = ((rect[0] + (x * 1.1) * (i - cnt_x)), (rect[1] + (y * 1.1) * (cnt_y)))
        cnt = cnt + 1
        temp.append(createOneCard(card_lst[i], c_pos, (x, y)))
    return temp


def createBackCards(card_lst, rect):
    temp = []
    for i in range(0, len(card_lst)):
        x = rect[2] / 8 * 0.8
        y = x * 1.2
        c_pos = (rect[0] + (x * 1.1) * i, rect[1])
        temp.append(createBackCard(c_pos, (x, y)))
    return temp


##### card generator #####


##### board space #####

def openCardIndicator(screen, game, rect):
    topCard = game.openCard.cardList[-1]  # openCard

    center = rectCenter(rect)
    pos_o = (center[0], center[1])
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
    topC = createOneCard(topCard, pos_o, size_o)
    init_view(screen, [topC])


def createIndicator(screen, card_o, rect):
    c = card_o
    txt = COLOR_TABLE2[c.applyColor]
    c_img = f"images/" + txt + ".png"

    center = rectCenter(rect)
    pos_o = (center[0] + rect[2] * 0.1, center[1])
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)

    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    init_view(screen, [btn])


def createDeck(screen, game, rect):
    if len(game.deckList.cardList) == 0:
        pass
    else:
        center = rectCenter(rect)
        pos_o = (center[0] - rect[2] * 0.1, center[1])
        size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
        btn = createBackCard(pos_o, size_o)
        init_view(screen, [btn])


def createDrawBtn(screen, game, rect):
    center = rectCenter(rect)
    pos_o = (center[0] - rect[2] * 0.1, center[1] + rect[2] * 0.1 * 1.2 * 0.25)
    size_o = (rect[2] * 0.1, rect[2] * 0.1 * 1.2)
    btn = createBackCard(pos_o, size_o)
    if game.actList()['drawBtn']:
        init_view(screen, [btn])

    return btn


def createUnoBtn(screen, game, rect):
    center = rectCenter(rect)
    pos_o = (center[0] - rect[2] * 0.1, center[1] - rect[2] * 0.1)
    size_o = (rect[2] * 0.1, rect[2] * 0.1)
    btn = Button(image=pygame.image.load(f"UNO.png"), pos=pos_o, size=size_o)
    if game.actList()['unoBtn']:
        init_view(screen, [btn])

    return btn


##### board space #####


##### bot space #####

def playerSlotBG(screen, offset, player, rect):
    pos_x = rect[0] + rect[2] * 0.01
    pos_y = rect[1] + (offset * rect[3] / 6) + rect[3] * 0.01

    size_x = rect[2] * 0.98
    size_y = round(0.92 * rect[3] / 6)

    bgArea = (pos_x, pos_y, size_x, size_y)

    if player.isUser:
        pygame.draw.rect(screen, (0, 0, 0), bgArea)
    else:
        pygame.draw.rect(screen, (75, 75, 75), bgArea)

    return bgArea


def nameSlot(screen, rect, player):
    pos_x = rect[0]
    pos_y = rect[1]

    size_x = round(rect[2] / 5)
    size_y = round(rect[3] * 1 / 5)

    nameArea = (pos_x, pos_y, size_x, size_y)
    pygame.draw.rect(screen, (255, 255, 255), nameArea)

    font_size = size_y
    font = pygame.font.Font(None, font_size)

    center = rectCenter(nameArea)
    text = font.render(player.playerName, True, (0, 0, 0))
    screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))

    return nameArea


def playerSlot(screen, idx, player, rect):
    slotBg = playerSlotBG(screen, idx, player, rect)
    slotName = nameSlot(screen, slotBg, player)

    card_anchor = (slotName[0], slotName[1] + slotName[3] * 1.5, slotBg[2], slotBg[3])
    if len(player.handCardList) > 9:
        temp = []
        for i in range(9):
            temp.append(Card(0, 0, NO_EFFECT))
        card_s = createBackCards(temp, card_anchor)
        init_view(screen, card_s)

        card_9 = card_s[8].rect
        font_size = card_9[3] * 2 // 3
        font = pygame.font.Font(None, font_size)

        center = rectCenter(card_9)
        text = font.render('+' + str(len(player.handCardList) - 9), True, (255, 255, 255))
        screen.blit(text, (center[0] - text.get_width() / 2, center[1] - text.get_height() / 2))
    else:
        card_s = createBackCards(player.handCardList, card_anchor)
        init_view(screen, card_s)


##### bot space #####

def createColorBtn(rect):
    lst = []
    x = rect[2] * 0.05
    y = x * 1.2
    for i in range(0, 4):
        pos_o = (rect[0] + i * x, rect[1] + y+ 50)
        size_o = (x, y)
        img_o = f"images/" + COLOR_TABLE[i] + ".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst


def createNumberBtn(rect):
    lst = []
    x = rect[2] * 0.05
    y = x * 1.2
    for i in range(0, 10):
        pos_o = (rect[0] + i * x, rect[1] + 2 * y)
        size_o = (x, y)
        img_o = f"images/red_" + str(i) + ".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst


def rectCenter(rect):
    x1 = rect[0]
    x2 = rect[0] + rect[2]

    y1 = rect[1]
    y2 = rect[1] + rect[3]
    return ((x1 + x2) / 2, (y1 + y2) / 2)
