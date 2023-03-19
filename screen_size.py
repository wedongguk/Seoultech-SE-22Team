import pygame

# Pygame 초기화
pygame.init()

# 초기 화면 사이즈
screen_size = (800, 600)

# 스크린 만들기
screen = pygame.display.set_mode(screen_size)

# 텍스트 사이즈, 폰트 설정
font = pygame.font.SysFont(None, 30)

# 옵션 텍스트 만듦
option1_text = font.render("640x480", True, (255, 255, 255))
option2_text = font.render("800x600", True, (255, 255, 255))
option3_text = font.render("1024x768", True, (255, 255, 255))

# 옵션 위치 설정
option1_rect = option1_text.get_rect()
option1_rect.centerx = screen.get_rect().centerx - 100
option1_rect.centery = screen.get_rect().centery

option2_rect = option2_text.get_rect()
option2_rect.centerx = screen.get_rect().centerx
option2_rect.centery = screen.get_rect().centery

option3_rect = option3_text.get_rect()
option3_rect.centerx = screen.get_rect().centerx + 100
option3_rect.centery = screen.get_rect().centery


# 옵션 선택 기다림
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 위치 입력받음
            mouse_pos = pygame.mouse.get_pos()
            # 마우스로 옵션 중 하나 클릭했는지 확인
            if option1_rect.collidepoint(mouse_pos):
                screen_size = (640, 480)
            elif option2_rect.collidepoint(mouse_pos):
                screen_size = (800, 600)
            elif option3_rect.collidepoint(mouse_pos):
                screen_size = (1024, 768)
            # 화면 크기 새로 설정
            screen = pygame.display.set_mode(screen_size)
            # Loop 종료
            break
    
    # 옵션 위치 설정
    option1_rect = option1_text.get_rect()
    option1_rect.centerx = screen.get_rect().centerx - 100
    option1_rect.centery = screen.get_rect().centery

    option2_rect = option2_text.get_rect()
    option2_rect.centerx = screen.get_rect().centerx
    option2_rect.centery = screen.get_rect().centery

    option3_rect = option3_text.get_rect()
    option3_rect.centerx = screen.get_rect().centerx + 100
    option3_rect.centery = screen.get_rect().centery

    # 옵션 출력
    screen.blit(option1_text, option1_rect)
    screen.blit(option2_text, option2_rect)
    screen.blit(option3_text, option3_rect)
        
    pygame.display.update()
