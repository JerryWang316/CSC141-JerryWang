import pygame
import sys

# begin Pygame
pygame.init()

# set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Sky")

# define blue color
BLUE = (135, 206, 235)  # sky blue color

# pygame main loop
running = True
while running:
    # deal with events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with blue color
    screen.fill(BLUE)
    
    # display the updated screen
    pygame.display.flip()

# quit Pygame
pygame.quit()
sys.exit()