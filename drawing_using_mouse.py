import pygame
from pygame.locals import *
import sys

# initialize pygame
pygame.init()

# set the clock and FPS 
clock = pygame.time.Clock()
FPS = 200

# Create the display
WINDOW_SIZE = [800, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Drawing app")

# Colors reference
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# Setting the font
sys_font = pygame.font.SysFont("Times New Roman", 32)

# Background
screen.fill(WHITE)

# Brush types
brushes = {"round" : False, "square" : False}

# Brush size
brush_size = 32

# Initial color
color = BLACK




# brush funct
def brush(x, y):
    #if round is clicked
    if brushes["round"]:
        return pygame.draw.circle(screen, color, (x, y), brush_size //2, 0)
    #if square is clicked
    elif brushes["square"]:
        return pygame.draw.rect(screen, color, (x - brush_size//2, y - brush_size//2, brush_size, brush_size))
    
# The main loop
while True:
    
    # Color buttons
    red_button = pygame.draw.rect(screen, RED, (0, WINDOW_SIZE[1] - 32, 32,32))
    blue_button = pygame.draw.rect(screen, BLUE, (32, WINDOW_SIZE[1] - 32, 32, 32))
    green_button = pygame.draw.rect(screen, GREEN, (64, WINDOW_SIZE[1] - 32, 32, 32))
    cyan_button = pygame.draw.rect(screen, CYAN, (96, WINDOW_SIZE[1] - 32, 32, 32))
    yellow_button = pygame.draw.rect(screen, YELLOW, (128, WINDOW_SIZE[1] - 32, 32, 32))
    magenta_button = pygame.draw.rect(screen, MAGENTA, (160, WINDOW_SIZE[1] - 32, 32, 32))
    white_button = pygame.draw.rect(screen, WHITE, (192, WINDOW_SIZE[1] - 32, 32, 32))
    black_button = pygame.draw.rect(screen, BLACK, (224, WINDOW_SIZE[1] - 32, 32, 32))
    
    #Brush buttons
    round_brush = pygame.draw.circle(screen, BLACK, (WINDOW_SIZE[0] - 16, WINDOW_SIZE[1] - 16), 16, 0)
    square_brush = pygame.draw.rect(screen, BLACK, (WINDOW_SIZE[0] - 64, WINDOW_SIZE[1] - 32, 32, 32))
    
    # Eraser button
    eraser_text = sys_font.render("Erase all", True, BLACK, WHITE)
    eraser_button = eraser_text.get_rect()
    eraser_button.topright = (WINDOW_SIZE[0], 0)
    
    # Blitting the eraser
    screen.blit(eraser_text, eraser_button)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
             

            # Check if the cursor 
            if mouse_y < WINDOW_SIZE[1] - 48:
                 # you could also load an image
                brush(mouse_x, mouse_y)
                
            if red_button.collidepoint(mouse_x, mouse_y):
                color = RED
                
            elif blue_button.collidepoint(mouse_x, mouse_y):
                color = BLUE
                
            elif green_button.collidepoint(mouse_x, mouse_y):
                color = GREEN
            
            elif cyan_button.collidepoint(mouse_x, mouse_y):
                color = CYAN
                
            elif yellow_button.collidepoint(mouse_x, mouse_y):
                color = YELLOW
                
            elif magenta_button.collidepoint(mouse_x, mouse_y):
                color = MAGENTA
            
            elif white_button.collidepoint(mouse_x, mouse_y):
                color = WHITE
                
            elif black_button.collidepoint(mouse_x, mouse_y):
                color = BLACK
            
            elif round_brush.collidepoint(mouse_x, mouse_y):
                brushes["square"] = False
                brushes["round"] = True
                
            elif square_brush.collidepoint(mouse_x, mouse_y):
                brushes["round"] = False
                brushes["square"] = True
                
            elif eraser_button.collidepoint(mouse_x, mouse_y):
                screen.fill(WHITE)
                
            surf = pygame.image.load("cursor2.png")
                    # and use that as your surface
            colour = pygame.cursors.Cursor((16, 16), surf)
            pygame.mouse.set_cursor(colour)
            
            
        if event.type == MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            if mouse_y < WINDOW_SIZE[1] - 48:
                brush(mouse_x, mouse_y)
                
            
            
    pygame.display.update()
    clock.tick(FPS)
    