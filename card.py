import pygame
from uno_Player import *
from unoCore import Game
from uno_Card import *

screen_size = (800, 600)
user1 = Player('USER', True)
pcard = Player('Pcard', False)
pc2 = Player('PC2', False)
pc3 = Player('PC3', False)

gamePlayerList = [user1, pcard, pc2, pc3]
g = Game(gamePlayerList)
# Create the screen
screen = pygame.display.set_mode(screen_size)
image = pygame.transform.smoothscale(pygame.image.load(f"images/red_4.png"), (20, 40))
#screen.blit(image, (10,10))

deck = g.setDeck()
for i in range (0,56) :
    screen.blit(deck[i].default_image, (i*10,10))
while True:
    pygame.display.flip() 

