import pygame
from uno_Player import *
from unoCore import Game
from uno_Card import *
from main import init_bg

def play(screen, screen_width, screen_height):
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size)
    screen.fill("black")
    play_bg = init_bg("play_screen.png", screen_width, screen_height)
    screen.blit(play_bg, (0, 0))
        
    user1 = Player('USER', True)
    pcard = Player('Pcard', False)
    pc2 = Player('PC2', False)
    pc3 = Player('PC3', False)

    gamePlayerList = [user1, pcard, pc2, pc3]
    g = Game(gamePlayerList)

    screen = pygame.display.set_mode(screen_size)

    g.ready(screen_size)
    hand = user1.allHand()
    for i in range (0,5) :
        screen.blit(hand[i].default_image, (i*100,60))
    
    while True:
        pygame.display.flip()
