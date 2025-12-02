import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cute Anime Character")

# Define colors
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

class AnimeCharacter:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create a surface for our character
        self.image = pygame.Surface((200, 200), pygame.SRCALPHA)  # Use SRCALPHA for transparency
        
        # Draw the character - a cute anime-style face
        self._draw_anime_face()
        
        # Get the rectangle of the image
        self.rect = self.image.get_rect()
        
        # Position the character at the center of the screen
        self.rect.center = self.screen_rect.center
    
    def _draw_anime_face(self):
        # Draw face (yellow circle)
        pygame.draw.circle(self.image, YELLOW, (100, 100), 80)
        
        # Draw eyes (large anime eyes)
        # Left eye
        pygame.draw.ellipse(self.image, WHITE, (40, 60, 40, 50))
        pygame.draw.ellipse(self.image, BLACK, (50, 70, 20, 30))
        
        # Right eye
        pygame.draw.ellipse(self.image, WHITE, (120, 60, 40, 50))
        pygame.draw.ellipse(self.image, BLACK, (130, 70, 20, 30))
        
        # Draw blush (pink circles on cheeks)
        pygame.draw.circle(self.image, PINK, (60, 120), 15)
        pygame.draw.circle(self.image, PINK, (140, 120), 15)
        
        # Draw mouth (smile)
        pygame.draw.arc(self.image, BLACK, (70, 100, 60, 50), math.pi, 2 * math.pi, 3)
        
        # Draw eyebrows (cute curved lines)
        pygame.draw.arc(self.image, BLACK, (40, 45, 40, 20), math.pi, 2 * math.pi, 2)
        pygame.draw.arc(self.image, BLACK, (120, 45, 40, 20), math.pi, 2 * math.pi, 2)
    
    def draw(self):
        """Draw the character on the screen"""
        self.screen.blit(self.image, self.rect)

# Create character instance
character = AnimeCharacter(screen)

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with blue
    screen.fill(SKY_BLUE)
    
    # Draw the character
    character.draw()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()