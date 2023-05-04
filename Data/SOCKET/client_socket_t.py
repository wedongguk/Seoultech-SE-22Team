import pygame
from network_t import Network
from player_t import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# 화면 업데이트
def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    # 스타트 위치를 읽어옴
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        # 루프를 돌며 계속 서로 정보를 주고 받으며 위치를 업데이트 함
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # p를 움직임
        p.move()
        redrawWindow(win, p, p2)

main()