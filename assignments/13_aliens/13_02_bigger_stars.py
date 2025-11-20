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
ORANGE = (255, 165, 0)
BLUE = (100, 100, 255)
RED = (255, 0, 0)

class Star(Sprite):
    def __init__(self, screen, x, y, random_offset=False, enhanced=False):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Random star properties for enhanced version
        if enhanced:
            self.size = random.randint(1, 4)
            self.color = random.choice([WHITE, YELLOW, ORANGE, BLUE])
            self.brightness = random.randint(150, 255)
        else:
            self.size = 2
            self.color = YELLOW
            self.brightness = 255
        
        # Adjust color based on brightness
        actual_color = (
            min(255, self.color[0] * self.brightness // 255),
            min(255, self.color[1] * self.brightness // 255),
            min(255, self.color[2] * self.brightness // 255)
        )
        
        # Create star surface
        self.image = pygame.Surface((self.size * 2 + 1, self.size * 2 + 1), pygame.SRCALPHA)
        
        # Draw star
        pygame.draw.circle(self.image, actual_color, (self.size, self.size), self.size)
        
        # Add a tiny brighter center for larger stars
        if self.size > 1:
            pygame.draw.circle(self.image, WHITE, (self.size, self.size), 1)
        
        self.rect = self.image.get_rect()
        
        # Apply random offset if requested
        if random_offset:
            offset_range = 20 if enhanced else 15
            offset_x = random.randint(-offset_range, offset_range)
            offset_y = random.randint(-offset_range, offset_range)
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
        pygame.display.set_caption("Stars Grid - Enhanced")
        self.clock = pygame.time.Clock()
        
        # Create stars group
        self.stars = Group()
        
        # Game state
        self.mode = "perfect"  # "perfect", "random", "enhanced"
        self.font = pygame.font.Font(None, 36)
        
        # Create initial grid of stars
        self._create_stars()
    
    def _create_stars(self):
        """Create stars based on current mode"""
        self.stars.empty()
        
        # Grid parameters
        grid_width = 12  # Number of columns
        grid_height = 10  # Number of rows
        
        # Calculate spacing
        x_spacing = SCREEN_WIDTH // (grid_width + 1)
        y_spacing = SCREEN_HEIGHT // (grid_height + 1)
        
        # Create stars
        for row in range(1, grid_height + 1):
            for col in range(1, grid_width + 1):
                x = col * x_spacing
                y = row * y_spacing
                
                # Create star based on current mode
                if self.mode == "perfect":
                    star = Star(self.screen, x, y, random_offset=False, enhanced=False)
                elif self.mode == "random":
                    star = Star(self.screen, x, y, random_offset=True, enhanced=False)
                else:  # enhanced
                    star = Star(self.screen, x, y, random_offset=True, enhanced=True)
                
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
                    self.mode = "perfect"
                    self._create_stars()
                elif event.key == pygame.K_2:
                    self.mode = "random"
                    self._create_stars()
                elif event.key == pygame.K_3:
                    self.mode = "enhanced"
                    self._create_stars()
                elif event.key == pygame.K_r:
                    # Cycle through modes
                    modes = ["perfect", "random", "enhanced"]
                    current_index = modes.index(self.mode)
                    self.mode = modes[(current_index + 1) % len(modes)]
                    self._create_stars()
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(BLACK)
        
        # Draw stars
        for star in self.stars.sprites():
            star.blitme()
        
        # Draw mode information
        mode_names = {
            "perfect": "Perfect Grid (Exercise 13-1)",
            "random": "Random Stars (Exercise 13-2)", 
            "enhanced": "Enhanced Random Stars"
        }
        
        mode_text = self.font.render(mode_names[self.mode], True, WHITE)
        self.screen.blit(mode_text, (10, 10))
        
        instructions = [
            "Press 1: Perfect Grid",
            "Press 2: Random Stars", 
            "Press 3: Enhanced Random Stars",
            "Press R: Cycle through modes"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, YELLOW)
            self.screen.blit(text, (10, 50 + i * 30))
        
        # Draw star count
        count_text = pygame.font.Font(None, 24).render(
            f"Stars: {len(self.stars)}", True, BLUE
        )
        self.screen.blit(count_text, (SCREEN_WIDTH - 150, 10))
        
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run
    stars_game = Game()
    stars_game.run_game()