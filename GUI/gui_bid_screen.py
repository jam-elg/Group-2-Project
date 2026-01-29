import pygame


def bid_screen():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 750, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Place Your Bid")

    font = pygame.font.Font(None, 36)

    # Currency
    CURRENCY = "£"

    # Fonts
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 20)
    title_font = pygame.font.Font(None, 48)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    PURPLE = (138, 43, 226)
    PINK = (255, 105, 180)
    DARK_BG = (30, 30, 50)
    GREEN = (50, 205, 50)
    RED = (255, 80, 80)
    CARD_BG = (60, 60, 90)
    INPUT_BG = (50, 50, 70)
    CARD_GRAY = (100, 100, 150)

    # Back button settings
    BACK_BUTTON_WIDTH = 67
    BACK_BUTTON_HEIGHT = 36
    BACK_BUTTON_X = 20
    BACK_BUTTON_Y = 20

    # Grid settings
    COLS = 1
    ROWS = 1
    CARD_WIDTH = 385
    CARD_HEIGHT = 245
    MARGIN_X = 25
    MARGIN_Y = 100
    START_Y = 50

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        screen.fill((DARK_BG))
        #text = font.render("Bid Screen", True, (PINK))
        #screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        # Draw back button
        back_button_rect = pygame.Rect(BACK_BUTTON_X, BACK_BUTTON_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
        back_button_color = (205, 92, 92, 255) if back_button_rect.collidepoint(mouse_pos) else (RED)
        pygame.draw.rect(screen, back_button_color, back_button_rect, border_radius=8)
        pygame.draw.rect(screen, (BLACK), back_button_rect, 2, border_radius=8)

        small_font = pygame.font.Font(None, 28)
        back_text = small_font.render("Back", True, (WHITE))
        screen.blit(back_text, (BACK_BUTTON_X + 10, BACK_BUTTON_Y + 8))

        # Draw item card
        card_rect = pygame.Rect(MARGIN_X, MARGIN_Y, CARD_WIDTH, CARD_HEIGHT)
        is_hovering = card_rect.collidepoint(mouse_pos)
        x = MARGIN_X + COLS * (CARD_WIDTH + MARGIN_X)
        y = START_Y + ROWS * (CARD_HEIGHT + MARGIN_Y)
        card_color = (CARD_GRAY) if is_hovering else (CARD_BG)  # Lighter when hovered
        pygame.draw.rect(screen, card_color, card_rect, border_radius=12)
        pygame.draw.rect(screen, PURPLE, card_rect, 2, border_radius=12)

        small_font = pygame.font.Font(None, 28)
        card_text = small_font.render("ITEM", True, (WHITE))
        screen.blit(card_text, (MARGIN_X + 10, MARGIN_Y + 8))

        # Item title description
        text = small_font.render("Name: ", True, (WHITE))
        screen.blit(text, (MARGIN_X + 400, MARGIN_Y + 12))

        # Item description
        text = small_font.render("Description: ", True, (WHITE))
        screen.blit(text, (MARGIN_X + 400, MARGIN_Y + 40))

        # Current highest bid
        text = small_font.render("Current Highest Bid: ", True, (WHITE))
        screen.blit(text, (MARGIN_X + 400, MARGIN_Y + 68))

        # originial price
        text = small_font.render("Original Price: ", True, (WHITE))
        screen.blit(text, (MARGIN_X + 400, MARGIN_Y + 96))

        # bid limit
        text = small_font.render("Bid Limit: ", True, (WHITE))
        screen.blit(text, (MARGIN_X + 400, MARGIN_Y + 124))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_pos):
                    running = False