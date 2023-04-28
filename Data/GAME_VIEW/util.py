import os
import sys
import configparser
import pygame

pygame.init()

config = configparser.ConfigParser()
config.read('Data/config.ini', encoding='utf-8')

font = pygame.font.SysFont("notosanscjkkr", 30)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BUTTON_WIDTH = 220
BUTTON_HEIGHT = 50

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x_pos = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
y_pos = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

BUTTON_PATH = os.getcwd() + "/Data/Asset/image/button/"
SCREEN_PATH = os.getcwd() + "/Data/Asset/image/screen/"
SOUND_PATH = os.getcwd() + "/Data/Asset/sound/"
ASSET_PATH = os.getcwd() + "/Data/Asset/image/etc/"
BLIND_CARD_PATH = os.getcwd() + "/Data/Asset/image/blind_card/"
CARD_PATH = os.getcwd() + "/Data/Asset/image/normal_card/"

CLICK_SOUND = pygame.mixer.Sound(SOUND_PATH + "click_bgm.wav")
MAIN_BGM = pygame.mixer.Sound(SOUND_PATH + "main_bgm.mp3")


def init_pygame():
    pygame.init()
    pygame.display.set_caption("Uno game")
    icon = pygame.image.load(os.getcwd() + "/Data/Asset/image/etc/icon.png")
    pygame.display.set_icon(icon)


def init_bg(screen, image, width, height):
    screen.fill("black")
    bg = pygame.image.load(image)
    bg = pygame.transform.scale(bg, (width, height))
    screen.blit(bg, (0, 0))


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
    with open('/Data/config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def quit():
    pygame.quit()
    sys.exit()
