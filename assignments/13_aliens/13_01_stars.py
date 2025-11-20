import pygame
import sys
import random
from pygame.sprite import Sprite, Group

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 100, 255)

class Star(Sprite):
    def __init__(self, screen, x, y, random_offset=False):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create star surface
        self.image = pygame.Surface((5, 5), pygame.SRCALPHA)
        
        # Draw a simple star (small circle)
        pygame.draw.circle(self.image, YELLOW, (2, 2), 2)
        
        # Add a tiny glow effect
        pygame.draw.circle(self.image, WHITE, (2, 2), 1)
        
        self.rect = self.image.get_rect()
        
        # Apply random offset if requested
        if random_offset:
            offset_x = random.randint(-15, 15)
            offset_y = random.randint(-15, 15)
            self.rect.x = x + offset_x
            self.rect.y = y + offset_y
        else:
            # Perfect grid positioning
            self.rect.x = x
            self.rect.y = y
    
    def blitme(self):
        """Draw star at current position"""
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Stars Grid")
        self.clock = pygame.time.Clock()
        
        # Create stars group
        self.stars = Group()
        
        # Game state
        self.show_random_stars = False
        self.font = pygame.font.Font(None, 36)
        
        # Create initial grid of stars
        self._create_star_grid()
    
    def _create_star_grid(self):
        """Create a grid of stars"""
        self.stars.empty()
        
        # Grid parameters
        grid_width = 10  # Number of columns
        grid_height = 8  # Number of rows
        
        # Calculate spacing
        x_spacing = SCREEN_WIDTH // (grid_width + 1)
        y_spacing = SCREEN_HEIGHT // (grid_height + 1)
        
        # Create stars in a grid pattern
        for row in range(1, grid_height + 1):
            for col in range(1, grid_width + 1):
                x = col * x_spacing
                y = row * y_spacing
                
                # Create star with or without random offset
                star = Star(self.screen, x, y, self.show_random_stars)
                self.stars.add(star)
    
    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Show perfect grid (Exercise 13-1)
                    self.show_random_stars = False
                    self._create_star_grid()
                elif event.key == pygame.K_2:
                    # Show random stars (Exercise 13-2)
                    self.show_random_stars = True
                    self._create_star_grid()
                elif event.key == pygame.K_r:
                    # Toggle between grid and random
                    self.show_random_stars = not self.show_random_stars
                    self._create_star_grid()
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(BLACK)
        
        # Draw stars
        for star in self.stars.sprites():
            star.blitme()
        
        # Draw instructions
        mode_text = self.font.render(
            "Perfect Grid" if not self.show_random_stars else "Random Stars", 
            True, 
            BLUE
        )
        self.screen.blit(mode_text, (10, 10))
        
        instructions = [
            "Press 1: Perfect Grid (Exercise 13-1)",
            "Press 2: Random Stars (Exercise 13-2)",
            "Press R: Toggle between modes"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, WHITE)
            self.screen.blit(text, (10, 50 + i * 30))
        
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run
    stars_game = Game()
    stars_game.run_game()