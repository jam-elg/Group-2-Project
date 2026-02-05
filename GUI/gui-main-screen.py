from cProfile import label
from cmath import rect
from operator import index
import pygame
import gui_bid_screen  # import from bid screen module

# List of auction items (9 items for 3x3 grid)
auction_items = [
    {"id": 1, "name": "Wireless Headphones","number": 0, "description": "RGB Gaming Edition", "starting_price": 50.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 2, "name": "Gaming Controller","number": 1, "description": "Glow in the dark!", "starting_price": 35.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 3, "name": "Phone Ring Light", "number": 2,"description": "Perfect for TikToks!", "starting_price": 15.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 4, "name": "LED Backpack","number": 3, "description": "Changes colors!", "starting_price": 40.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 5, "name": "Mini Skateboard","number": 4, "description": "Fingerboard pro set", "starting_price": 10.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 6, "name": "Bubble Tea Kit","number": 5, "description": "Make your own boba!", "starting_price": 20.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 7, "name": "Karaoke Mic","number": 6, "description": "Bluetooth speaker", "starting_price": 25.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 8, "name": "LED Strip Lights","number": 7, "description": "16 million colors!", "starting_price": 18.00, "current_bid": 0, "highest_bidder_id": None},
    {"id": 9, "name": "Portable Projector","number": 8, "description": "Movie nights!", "starting_price": 60.00, "current_bid": 0, "highest_bidder_id": None},
]

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Group 2 - Auction Zone Main Screen")

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

# Font
font = pygame.font.Font(None, 26)
small_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font(None, 48)
med_font = pygame.font.Font(None, 34)

# Grid settings
COLS = 3
ROWS = 3
CARD_WIDTH = 220
CARD_HEIGHT = 140
MARGIN_X = 25
MARGIN_Y = 20
START_Y = 70

BID_BUTTON_WIDTH = 100
BID_BUTTON_HEIGHT = 48
BID_BUTTON_X = MARGIN_X + 300
BID_BUTTON_Y = MARGIN_Y + 520

# Main loop
running = True
while running:

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Fill background
    screen.fill(DARK_BG)

    # Draw title
    title = title_font.render("Group 2 - Auction Zone", True, PINK)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 18))

    bid_button_rect = pygame.Rect(BID_BUTTON_X, BID_BUTTON_Y, BID_BUTTON_WIDTH, BID_BUTTON_HEIGHT)
    bid_button_color = (50, 150, 50) if bid_button_rect.collidepoint(mouse_pos) else (GREEN)
    pygame.draw.rect(screen, bid_button_color, bid_button_rect, border_radius=12)
    pygame.draw.rect(screen, BLACK , bid_button_rect, 2, border_radius=12)

    bid_text = title_font.render("BID", True, (255,255,255))
    screen.blit(bid_text, (BID_BUTTON_X + 22 , BID_BUTTON_Y + 10))


    # Draw 3x3 grid of items
    for i, item in enumerate(auction_items):
        if i >= 9:  # Only show 9 items
            break
        
        row = i // COLS
        col = i % COLS
        
        x = MARGIN_X + col * (CARD_WIDTH + MARGIN_X)
        y = START_Y + row * (CARD_HEIGHT + MARGIN_Y)
        
        # Card background
        card_rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        
        # Check if the mouse is over the card
        is_hovering = card_rect.collidepoint(mouse_pos)
        card_color = (100, 100, 150) if is_hovering else (CARD_BG)  # Lighter when hovered

        pygame.draw.rect(screen, card_color, card_rect, border_radius=12)
        pygame.draw.rect(screen, PURPLE, card_rect, 2, border_radius=12)
        
        # Item name
        name_text = font.render(item["name"], True, WHITE)
        screen.blit(name_text, (x + 10, y + 15))
        
        # Item description
        desc_text = small_font.render(item["description"], True, LIGHT_GRAY)
        screen.blit(desc_text, (x + 10, y + 45))

        # Starting ID label
        num_label = small_font.render("ID: ", True, PINK)
        screen.blit(num_label, (x + 181, y + 115))

        # Item number value
        num_text = small_font.render(f"{item['number']}", True, PINK)
        screen.blit(num_text, (x + 200, y + 115))

        # Starting price label
        price_label = small_font.render("Starting Price:", True, LIGHT_GRAY)
        screen.blit(price_label, (x + 10, y + 80))
        
        # Price value
        price_text = font.render(f"£{item['starting_price']:.2f}", True, PINK)
        screen.blit(price_text, (x + 10, y + 100))

    # Event handling when clicking on an item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if click is on any item card
            for i, item in enumerate(auction_items):
                if i >= 9:
                    break
                row = i // COLS
                col = i % COLS
                x = MARGIN_X + col * (CARD_WIDTH + MARGIN_X)
                y = START_Y + row * (CARD_HEIGHT + MARGIN_Y)
                card_rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
                
                # if card_rect.collidepoint(mouse_pos):
                #     gui_bid_screen.bid_screen()
                #     break

    pygame.display.flip()

pygame.quit()