import pygame
from checkbox import Checkbox

pygame.font.init()

boxes = []
screen = pygame.display.set_mode([800, 600])
screen.fill((255, 255, 255))

button = Checkbox(screen, 200, 200, 0, caption='button1')
button2 = Checkbox(screen, 200, 250, 1, caption='button2')
button3 = Checkbox(screen, 200, 300, 2, caption='button3')
boxes.append(button)
boxes.append(button2)
boxes.append(button3)
boxes[0].checked = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                box.update_checkbox(event)
                if box.checked is True:
                    for b in boxes:
                        if b != box:
                            b.checked = False
    for box in boxes:
        box.render_checkbox()

    pygame.display.flip()
pygame.time.wait(1000)
