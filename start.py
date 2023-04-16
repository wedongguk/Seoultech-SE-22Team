import pygame
from uno_Player import *
from unoCore import Game
from uno_Card import *
from uno_Pile import *
from uno_Const import *
from main import init_bg
from view import init_view
from button import Button


def start(screen, screen_width, screen_height, num, name):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)

    x_pos = screen_width / 2
    y_pos = screen_height / 2

    screen.fill((0, 0, 0))
    
    user1 = Player(name[0], True)
    gamePlayerList = [user1]
    for i in range(1, num+1):
        gamePlayerList.append(Player(name[i], False))
    g = Game(gamePlayerList)

    screen = pygame.display.set_mode(screen_size)

    g.ready(screen_size)

    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        
        user_rect = (0, screen_height*3/5 ,screen_width*3/5, screen_height*2/5)
        playerArea = pygame.draw.rect(screen, (120,120,120), user_rect)
        
        bot_rect = (screen_width*3/5, 0 ,screen_width*2/5, screen_height)
        playerArea = pygame.draw.rect(screen, (120,120,0), bot_rect)
        
        board_rect = (0, 0 ,screen_width*3/5, screen_height*3/5)
        playerArea = pygame.draw.rect(screen, (25,150,75), board_rect)
        
        
        playerSlot(screen, 0, g.playerList.idxPlayer(0), bot_rect)
        playerSlot(screen, 1, g.playerList.idxPlayer(1), bot_rect)
        
        

        hand = g.userHand()  # 유저 핸드 부분
        userH = createCards(hand, user_rect)
        init_view(screen, userH)

        topCard = g.openCard.cardList[-1]  # openCard
        pos = ((board_rect[0]+(board_rect[0]+board_rect[2]))/2, (board_rect[1]+(board_rect[1]+board_rect[3]))/2)
        topC = createOneCard(topCard, pos, (50, 70))
        init_view(screen, [topC])
        
        pos = ((board_rect[0]+(board_rect[0]+board_rect[2]))/2 + 50, (board_rect[1]+(board_rect[1]+board_rect[3]))/2)
        topC_a = createIndicator(topCard, pos, (50, 70))
        init_view(screen, [topC_a])

        TIMER_FONT = pygame.font.SysFont('Arial', 30)  # 타이머
        timer_text = TIMER_FONT.render(str(g.timer.time // 60 + 1), True, (255, 255, 255))
        timer_rect = timer_text.get_rect()
        timer_rect.center = (screen_height // 2, 50)
        button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
        screen.blit(timer_text, timer_rect)
        g.update()
        # botHand(screen, screen_size, pc1)

        actlist = g.actList()
        # drawbtn
        
        
        dbtn = createDrawBtn(board_rect)
        ubtn = createUnoBtn(board_rect)
        cbtn = createColorBtn(board_rect)
       
        
        if actlist['drawBtn'] == True:
            init_view(screen, [dbtn])
        # unobtn
        if actlist['unoBtn'] == True:
            init_view(screen, [ubtn])
        # colorChangebtn
        if actlist['colorBtn'] == True:
            init_view(screen, cbtn)
        # numberChangebtn
        if actlist['numberBtn'] == True:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(userH)):
                    if userH[i].rect.collidepoint(event.pos):
                        g.eventCardBtn(i)
                        print(g.openCard.cardList[-1].applyColor)
                for i in range(0, len(cbtn)):
                    if cbtn[i].rect.collidepoint(event.pos):
                        g.eventColorBtn(i)
                if dbtn.rect.collidepoint(event.pos):
                    if actlist['drawBtn'] == True: # actList가 true인 경우에만 함수 실
                        g.eventDrawBtn()
        pygame.display.flip()
        clock.tick(60)


def createOneCard(card_o, pos_o, size_o):
    c = card_o
    c_img = f"images/" + c.imgName() + ".png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn

def createIndicator(card_o, pos_o, size_o):
    c = card_o
    txt = COLOR_TABLE2[c.applyColor]
    c_img = f"images/" + txt + ".png"
    btn = Button(image=pygame.image.load(c_img), pos=pos_o, size=size_o)
    return btn

def createCards(card_lst, rect):
    temp = []
    for i in range(0, len(card_lst)):
        x = rect[2]/8*0.8
        y = x*1.2
        c_pos = (rect[0] +(x*1.1)*i, rect[1])
        temp.append(createOneCard(card_lst[i], c_pos, (x, y)))
    return temp

def createDrawBtn(rect):
    x = rect[2]*0.05
    y = x*1.2
    pos_o = (rect[0], rect[1])
    size_o = (x,y)
    btn = Button(image=pygame.image.load(f"images/back.png"), pos=pos_o, size=size_o)
    return btn

def createUnoBtn(rect):
    x = rect[2]*0.05
    y = x*1.2
    pos_o = (rect[0]+rect[2]*0.05+10, rect[1])
    
    size_o = (x,y)
    btn = Button(image=pygame.image.load(f"images/back.png"), pos=pos_o, size=size_o)
    return btn

def createColorBtn(rect):
    lst = []
    x = rect[2]*0.05
    y = x*1.2
    for i in range(0, 4):
        pos_o = (rect[0]+i*x, rect[1]+y)
        size_o = (x,y)
        img_o = f"images/"+COLOR_TABLE[i]+".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst

def createNumberBtn(rect):
    lst = []
    x = rect[2]*0.05
    y = x*1.2
    for i in range(0, 10):
        pos_o = (rect[0]+i*x, rect[1]+2*y)
        size_o = (x,y)
        img_o = f"images/red_"+str(i)+".png"
        btn = Button(image=pygame.image.load(img_o), pos=pos_o, size=size_o)
        lst.append(btn)
    return lst
    

    btn = Button(image=pygame.image.load(f"images/back.png"), pos=pos_o, size=size_o)
    return btn


def one_botArea(offset, rect):
    pos_x = rect[0] + rect[2]*0.01
    pos_y = rect[1] + (offset* rect[3]/6) + rect[3]*0.01
    
    size_x = rect[2]*0.98
    size_y = round(0.92*rect[3]/6)
    
    result = (pos_x, pos_y, size_x, size_y)
    return result

def playerSlot(screen ,idx, player, rect):
    temp_rect = one_botArea(idx, rect)
    if player.isUser == True:
        pygame.draw.rect(screen, (0,0,0), temp_rect)
    else:
        pygame.draw.rect(screen, (75,75,75), temp_rect)
    
def botHand(screen, screen_size, player):
    for i in range(0, len(player.handCardList)):
        image = pygame.transform.smoothscale(pygame.image.load(f"images/back.png"),
                                             (screen_size[0] / 12.5, screen_size[0] / 8.333))
        screen.blit(image, (screen_size[0] / 12 + (i * screen_size[0] / 12.5), screen_size[1] * 3 / 5))
