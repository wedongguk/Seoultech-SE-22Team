import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Checkbox Demo")

# Define the checkbox class
class Checkbox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.checked = False
        self.check_image = pygame.Surface((width, height))
        self.check_image.fill((255, 255, 255))
        pygame.draw.line(self.check_image, (0, 0, 0), (0, height // 2), (width // 2, height), 2)
        pygame.draw.line(self.check_image, (0, 0, 0), (width // 2, height), (width, 0), 2)

    def draw(self, surface):
        if self.checked:
            surface.blit(self.check_image, self.rect)
        else:
            pygame.draw.rect(surface, (255, 255, 255), self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked

# Create a checkbox instance
checkbox = Checkbox(100, 100, 50, 50)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        checkbox.handle_event(event)

    # Draw the checkbox
    checkbox.draw(screen)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()