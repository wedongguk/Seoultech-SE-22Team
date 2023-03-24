import pygame
import sys
import os

os.chdir(os.getcwd() + "/img")

# Pygame 초기화
pygame.init()

# 필요한 함수 정의
def init_button(filename, width, height):
    button = pygame.image.load(filename)
    button = pygame.transform.scale(button, (width, height))
    return button

pygame.display.set_caption("Uno game")

# 화면 크기 설정
screen_width = 1280
screen_height = 720
button_width = 220
button_height = 50

screen = pygame.display.set_mode((screen_width, screen_height))

# 버튼 초기화
background = init_button("start_screen.jpeg", screen_width, screen_height)
play_button = init_button("play_button.png", button_width, button_height)
options_button = init_button("options_button.png", button_width, button_height)
exit_button = init_button("exit_button.png", button_width, button_height)

# 버튼 좌표 설정
play_button_x = screen_width/2 - button_width/2
play_button_y = screen_height/2 - button_height/2 + 200

options_button_x = screen_width/2 - button_width/2
options_button_y = screen_height/2 - button_height/2 + 260

exit_button_x = screen_width/2 - button_width/2
exit_button_y = screen_height/2 - button_height/2 + 320

# 버튼 영역 설저
play_button_rect = pygame.Rect(play_button_x, play_button_y, button_width, button_height)
options_button_rect = pygame.Rect(options_button_x, options_button_y, button_width, button_height)
exit_button_rect = pygame.Rect(exit_button_x, exit_button_y, button_width, button_height)

game_screen = pygame.display.set_mode((screen_width, screen_height))
game_screen_background = init_button("play_screen.jpg", screen_width, screen_height)


# 게임 시작 화면 루프
screen.blit(background, (0, 0))
screen.blit(play_button, (play_button_x, play_button_y))
screen.blit(options_button, (options_button_x, options_button_y))
screen.blit(exit_button, (exit_button_x, exit_button_y))

def start_screen():
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 게임 시작 버튼
                if play_button_rect.collidepoint(event.pos):
                    screen.blit(game_screen_background, (0, 0))
                # 옵션 버튼
                elif options_button_rect.collidepoint(event.pos):
                    print("h")
                # quit 버튼을 누르면 게임 종료
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        # 화면 업데이트
        pygame.display.flip()

start_screen()