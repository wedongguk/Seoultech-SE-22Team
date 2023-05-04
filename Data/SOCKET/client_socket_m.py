import pygame
from Data.SOCKET.network_m import Network

# 플레이어 생성 정의
# class Player


def client():
     # main
    run = True
    # 소켓 생성
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    # while loop

    while run:
        # 루프를 돌며 정보를 주고 받음
        clock.tick(60)
        
        # 상대방 정보
        p2Screen = n.send(p)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

        
        
        # 상대방으로 부터 읽은 num 표시
        print()
        print("{0} 가 받은 카드리스트  : {1}".format(p.__class__.__name__, p2Screen.handCardList))
