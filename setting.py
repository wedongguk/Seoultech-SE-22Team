
from main_screen import config


def save_config():
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)