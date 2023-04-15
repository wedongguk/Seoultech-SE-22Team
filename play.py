import pygame
from uno_Player import *
from unoCore import Game
from uno_Card import *
from uno_Pile import *
from main import init_bg

def play(screen, screen_width, screen_height):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    screen.fill("black")
        
    user1 = Player('USER', True)
    pc1 = Player('Pcard', False)
    pc2 = Player('PC2', False)
    pc3 = Player('PC3', False)

    gamePlayerList = [user1, pc1, pc2, pc3]
    g = Game(gamePlayerList)

    screen = pygame.display.set_mode(screen_size)

    g.ready(screen_size)
    hand = g.userHand()
    userHand(screen, g, user1, screen_size)
    botHand(screen, screen_size, pc1)
    screen.blit(g.openCard.cardList[0].default_image, (100,200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, sprite in enumerate(hand):
                    if sprite.rect.collidepoint(pos):
                        print("tlqkf")
                        g.eventCardBtn(i)
                        userHand(screen, g, user1, screen_size)
                        screen.blit(g.openCard.cardList[0].default_image, (100,200))
        pygame.display.flip()

def userHand(screen, game, player, screen_size) :
    hand = game.userHand()
    for i in range (0,len(player.handCardList)) :
        screen.blit(hand[i].default_image, (screen_size[0] / 12 +(i*screen_size[0] / 12.5),screen_size[1] * 4 / 5))
        #screen_size[0] / 12.5, screen_size[0] / 8.333

def botHand(screen, screen_size, player) :
    for i in range (0,len(player.handCardList)) :
        image = pygame.transform.smoothscale(pygame.image.load(f"images/back.png"), (screen_size[0] / 12.5, screen_size[0] / 8.333))
        screen.blit(image, (screen_size[0] / 12 +(i*screen_size[0] / 12.5),screen_size[1] * 3 / 5))
    