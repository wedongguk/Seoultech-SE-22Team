import pygame
import os

os.chdir(os.getcwd() + "/img")

pygame.init()

# 초기 화면 사이즈
screen_size = (800, 600)

# 스크린 만들기
screen = pygame.display.set_mode(screen_size)

font = pygame.font.SysFont(None, 30)
button = pygame.image.load("save_button.png")
button = pygame.transform.scale(button, (40, 40))

# 옵션 텍스트 만듦
option1_text = font.render("640x480", True, (255, 255, 255))
option2_text = font.render("800x600", True, (255, 255, 255))
option3_text = font.render("1024x768", True, (255, 255, 255))

# 조작키 기본 값 설정
UNO = pygame.K_u
SELECT = pygame.K_RETURN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT



def key_change() :
    tmp = 0
    # 바꿀 조작키 입력 루프
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
                tmp = event.key
                if (tmp == UNO or tmp == SELECT or tmp == LEFT or tmp == RIGHT) :
                    print("used key")
                else :
                    break
    return tmp

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 위치 입력받음
            mouse_pos = pygame.mouse.get_pos()
            # 마우스로 옵션 중 하나 클릭했는지 확인
            if Uno_rect.collidepoint(mouse_pos):
                print("Press the key for Uno direction")
                UNO = key_change()
            elif Select_rect.collidepoint(mouse_pos):
                print("Press the key for Select direction")
                SELECT = key_change()
            elif L_rect.collidepoint(mouse_pos):
                LEFT = key_change()
            elif R_rect.collidepoint(mouse_pos):
                print("Press the key for RIGHT direction")
                RIGHT = key_change()
            elif option1_rect.collidepoint(mouse_pos):
                screen_size = (640, 480)
            elif option2_rect.collidepoint(mouse_pos):
                screen_size = (800, 600)
            elif option3_rect.collidepoint(mouse_pos):
                screen_size = (1024, 768)
            # 화면 크기 새로 설정
            screen = pygame.display.set_mode(screen_size)
            # Loop 종료
            break     
        elif event.type == pygame.KEYDOWN:
            if event.key == UNO:
                print("Press the key Uno")
                pass
            elif event.key == SELECT:
                print("Press the key Select")
                pass
            elif event.key == LEFT:
                print("Press the key Left")
                pass
            elif event.key == RIGHT:
                print("Press the key Rignt")
                pass

    # 옵션 위치 설정
    option1_rect = option1_text.get_rect()
    option1_rect.centerx = screen.get_rect().centerx - 150
    option1_rect.centery = screen.get_rect().centery - 150

    option2_rect = option2_text.get_rect()
    option2_rect.centerx = screen.get_rect().centerx
    option2_rect.centery = screen.get_rect().centery - 150

    option3_rect = option3_text.get_rect()
    option3_rect.centerx = screen.get_rect().centerx + 150
    option3_rect.centery = screen.get_rect().centery - 150
    
    Uno_button_rect = button.get_rect()
    Uno_button_rect.centerx = screen.get_rect().centerx
    Uno_button_rect.centery = screen.get_rect().centery-100
    Uno_text = font.render(pygame.key.name(UNO), True, (255, 255, 255))
    Uno_rect = Uno_text.get_rect()
    Uno_rect.centerx = Uno_button_rect.centerx
    Uno_rect.centery = Uno_button_rect.centery

    Select_button_rect = button.get_rect()
    Select_button_rect.centerx = screen.get_rect().centerx
    Select_button_rect.centery = screen.get_rect().centery-35
    Select_text = font.render(pygame.key.name(SELECT), True, (255, 255, 255))
    Select_rect = Select_text.get_rect()
    Select_rect.centerx = Select_button_rect.centerx
    Select_rect.centery = Select_button_rect.centery

    L_button_rect = button.get_rect()
    L_button_rect.centerx = screen.get_rect().centerx
    L_button_rect.centery = screen.get_rect().centery+35
    L_text = font.render(pygame.key.name(LEFT), True, (255, 255, 255))
    L_rect = L_text.get_rect()
    L_rect.centerx = L_button_rect.centerx
    L_rect.centery = L_button_rect.centery

    R_button_rect = button.get_rect()
    R_button_rect.centerx = screen.get_rect().centerx
    R_button_rect.centery = screen.get_rect().centery+100
    R_text = font.render(pygame.key.name(RIGHT), True, (255, 255, 255))
    R_rect = R_text.get_rect()
    R_rect.centerx = R_button_rect.centerx
    R_rect.centery = R_button_rect.centery

    # 옵션 출력
    screen.blit(option1_text, option1_rect)
    screen.blit(option2_text, option2_rect)
    screen.blit(option3_text, option3_rect)
    
    screen.blit(button, Uno_button_rect)
    screen.blit(Uno_text, Uno_rect)
    screen.blit(button, Select_button_rect)
    screen.blit(Select_text, Select_rect)
    screen.blit(button, L_button_rect)
    screen.blit(L_text, L_rect)
    screen.blit(button, R_button_rect)
    screen.blit(R_text, R_rect)
    
    pygame.display.update()

pygame.quit()

