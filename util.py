import os
import sys

import pygame

BUTTON_PATH = os.getcwd() + "/Asset/image/button/"
SCREEN_PATH = os.getcwd() + "/Asset/image/screen/"
SOUND_PATH = os.getcwd() + "/Asset/sound/"
ASSET_PATH = os.getcwd() + "/Asset/image/etc/"
BLIND_CARD_PATH = os.getcwd() + "/Asset/image/blind_card/"


def init_pygame():
    pygame.init()
    pygame.display.set_caption("Uno game")
    icon = pygame.image.load(os.getcwd() + "/Asset/image/etc/icon.png")
    pygame.display.set_icon(icon)


def init_bg(screen, image, width, height):
    screen.fill("black")
    bg = pygame.image.load(image)
    bg = pygame.transform.scale(bg, (width, height))
    screen.blit(bg, (0,0))


def check_config(config):
    try:
        if config['system']['is_new'] == "False":
            print("config file o")
    except:
        print("config file x")
        config['system'] = {}
        config['system']['is_new'] = "False"
        config['system']['COLOR_WEAKNESS_MODE'] = "FALSE"
        config['system']['SCREEN_WIDTH'] = "1280"
        config['system']['SCREEN_HEIGHT'] = "720"
        config['system']['UNO'] = 'pygame.K_u'
        config['system']['LEFT_MOVE'] = 'pygame.K_RIGHT'
        config['system']['RIGHT_MOVE'] = 'pygame.K_LEFT'
        config['system']['SELECT'] = 'pygame.K_RETURN'
        config['system']['DRAW'] = 'pygame.K_d'
        save_config(config)


def save_config(config):
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def quit():
    pygame.quit()
    sys.exit()