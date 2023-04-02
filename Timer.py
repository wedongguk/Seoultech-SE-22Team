import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the font for the timer
pygame.font.init() # 타이머 실행
TIMER_FONT = pygame.font.SysFont(None, 30) # 타이머 폰트


# Define the Timer class
class Timer:
    def __init__(self, time):
        self.time = time
        self.text = TIMER_FONT.render(str(self.time), True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, 50)

    def update(self): # 타이머 시간 업데이트
        self.time -= 1
        (pygame.time.get_ticks() - start_ticks) - 1000
        self.text = TIMER_FONT.render(str(self.time), True, BLACK)

    def reset(self):
        self.time = 30
        self.text = TIMER_FONT.render(str(self.time), True, BLACK)


# Define the TimeOver function
def TimeOver(timer):
    print("Time's up!")
    timer.reset()


# Define the btnclick function
def btnclick(button):
    print(f"Button {button} clicked!")


# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("My Game")

# Set up the timer
timer = Timer(60)

# Set up the buttons
buttons = []
button_width = 100
button_height = 50
button_spacing = 20
total_button_width = button_width * 3 + button_spacing * 2
button_x = (SCREEN_WIDTH - total_button_width) // 2
button_y = SCREEN_HEIGHT // 2 - button_height // 2
for i in range(1, 4):
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_text = TIMER_FONT.render(str(i), True, BLACK)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = button_rect.center
    buttons.append((i, button_rect))
    button_x += button_width + button_spacing

# Start the game loop
running = True
clock = pygame.time.Clock()
total_time = 30
start_ticks = pygame.time.get_ticks()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button[1].collidepoint(event.pos):
                    btnclick(button[0])

    # Update the timer
    timer.update() # 시간 -1 씩 감소
    if timer.time <= 0: # 시간이 0보다 작거나 같으면
        TimeOver(timer) # 타이머 종료

    # Draw everything
    screen.fill(WHITE)
    for button in buttons:
        pygame.draw.rect(screen, GREEN, button[1])
        screen.blit(TIMER_FONT.render(str(button[0]), True, BLACK), button[1])
    screen.blit(timer.text, timer.rect)
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(60)

# Clean up
pygame.quit()