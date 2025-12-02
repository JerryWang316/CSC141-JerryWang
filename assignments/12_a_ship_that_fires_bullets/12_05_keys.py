import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Press Detector")
    
    # Set up font
    font = pygame.font.Font(None, 36)
    
    # Main game loop
    while True:
        # Fill background
        screen.fill((0, 0, 0))
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Print key attribute to console
                print(f"Key pressed: {event.key}")
                
                # Display key value on screen
                key_text = font.render(f"Key pressed: {event.key}", True, (255, 255, 255))
                screen.blit(key_text, (50, 50))
        
        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    run_game()