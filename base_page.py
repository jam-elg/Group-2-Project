import pygame

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Base Page Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
DARK_BLUE = (0, 80, 200)

# Font
font = pygame.font.Font(None, 36)
text = font.render("Welcome to Auction App", True, BLACK)

# Button rectangle
button_rect = pygame.Rect(300, 200, 200, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
    
    # Fill screen with white
    screen.fill(WHITE)
    
    # Draw text
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50))
    
    # Draw button (change color on hover)
    mouse_pos = pygame.mouse.get_pos()
    button_color = DARK_BLUE if button_rect.collidepoint(mouse_pos) else BLUE
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Test Button", True, WHITE)
    screen.blit(button_text, (330, 210))
    
    pygame.display.flip()

pygame.quit()