import pygame
import sys
import os

# Pygame 초기화
pygame.init()

# 필요한 함수 정의
def init_button(filename, width, height):
    button = pygame.image.load(filename)
    button = pygame.transform.scale(button, (width, height))
    return button

os.chdir(os.getcwd()+"/img")
# 화면 크기 설정
screen_width = 1280
screen_height = 720
button_width = 220
button_hegiht = 50

screen = pygame.display.set_mode((screen_width, screen_height))

# 버튼 초기화
background = init_button("start_screen.jpeg", screen_width, screen_height)
play_button = init_button("play_button.png", button_width, button_hegiht)
options_button = init_button("options_button.png", button_width, button_hegiht)
exit_button = init_button("exit_button.png", button_width, button_hegiht)

play_button_x = screen_width/2 - button_width/2
play_button_y = screen_height/2 - button_hegiht/2 + 200

options_button_x = screen_width/2 - button_width/2
options_button_y = screen_height/2 - button_hegiht/2 + 260

exit_button_x = screen_width/2 - button_width/2
exit_button_y = screen_height/2 - button_hegiht/2 + 320

# 게임 시작 화면 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()


    # 게임 시작 화면 이미지 출력
    screen.blit(background, (0, 0))
    screen.blit(play_button, (play_button_x, play_button_y))
    screen.blit(options_button, (options_button_x, options_button_y))
    screen.blit(exit_button, (exit_button_x, exit_button_y))

    # 화면 업데이트
    pygame.display.flip()