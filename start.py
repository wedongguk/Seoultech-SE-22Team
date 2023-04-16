import pygame
from uno_Player import *
from unoCore import Game
from uno_Card import *
from uno_Pile import *
from main import init_bg
from view import init_view
from button import Button

def start(screen, screen_width, screen_height):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    
    x_pos = screen_width / 2
    y_pos = screen_height / 2
    
    screen.fill((0, 0, 0))
        
    user1 = Player('USER', True)
    pc1 = Player('Pcard', False)
    pc2 = Player('PC2', False)
    pc3 = Player('PC3', False)

    gamePlayerList = [user1, pc1, pc2, pc3]
    g = Game(gamePlayerList)

    screen = pygame.display.set_mode(screen_size)

    g.ready(screen_size)
    c1 = Card(RED, 2)
    c2 = Card(RED, 3)
    c3 = Card(RED, 4)
    clist = [c1, c2, c3]
    
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        
        hand = g.userHand() # 유저 핸드 부분
        userH = createCards(hand, screen_size)
        init_view(screen, userH)
        
        topCard = g.openCard.cardList[-1] # openCard
        pos=(screen_size[0] / 12 +(screen_size[0] / 12.5),screen_size[1] * 1 / 5)
        topC = createOneCard(topCard, pos, (50, 70))
        init_view(screen, [topC])
        
        TIMER_FONT = pygame.font.SysFont('Arial', 30) # 타이머
        timer_text = TIMER_FONT.render(str(g.timer.time//60 + 1), True, (255,255,255))
        timer_rect = timer_text.get_rect()
        timer_rect.center = (screen_height // 2, 50)
        button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 - 25, 100, 50)
        pygame.draw.rect(screen, (0,255,0), button_rect)
        screen.blit(timer_text, timer_rect)
        g.update()
        #botHand(screen, screen_size, pc1)
        
        actlist = g.actList()
        #drawbtn
        if actlist['drawBtn'] == True:
            pass
        #unobtn
        if actlist['unoBtn'] == True:
            pass
        #colorChangebtn
        if actlist['colorBtn'] == True:
            pass
        #numberChangebtn
        if actlist['numberBtn'] == True:
            pass
        
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, len(userH)):
                    if userH[i].rect.collidepoint(event.pos):
                        g.eventCardBtn(i)
        
        
        pygame.display.update()
                
            
        pygame.display.flip()
        
        clock.tick(60)

def createOneCard(card_o, pos_o, size_o):
    c = card_o
    c_img = f"images/"+c.imgName()+".png" 
    btn = Button(image=pygame.image.load(c_img),  pos=pos_o, size=size_o)
    return btn

def createCards(card_lst, screen_size):
    temp = []
    for i in range (0,len(card_lst)):
        c_pos=(screen_size[0] / 12 +(i*screen_size[0] / 12.5),screen_size[1] * 4 / 5)
        temp.append(createOneCard(card_lst[i], c_pos, (50, 70)))
    return temp
    
 


def botHand(screen, screen_size, player) :
    for i in range (0,len(player.handCardList)) :
        image = pygame.transform.smoothscale(pygame.image.load(f"images/back.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
        screen.blit(image, (screen_size[0] / 12 +(i*screen_size[0] / 12.5),screen_size[1] * 3 / 5))
    