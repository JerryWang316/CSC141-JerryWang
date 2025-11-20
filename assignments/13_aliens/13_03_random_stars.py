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
BLUE = (65, 105, 225)
LIGHT_BLUE = (135, 206, 250)
DARK_BLUE = (25, 25, 112)

class Raindrop(Sprite):
    def __init__(self, screen, x, y, speed, continuous=False):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create raindrop surface
        self.image = pygame.Surface((3, 15), pygame.SRCALPHA)
        
        # Draw raindrop shape (teardrop)
        pygame.draw.line(self.image, LIGHT_BLUE, (1, 0), (1, 12), 2)
        pygame.draw.circle(self.image, LIGHT_BLUE, (1, 14), 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Raindrop properties
        self.speed = speed
        self.continuous = continuous
        
        # Store original position for continuous mode
        self.original_y = y
    
    def update(self):
        """Move raindrop downward"""
        self.rect.y += self.speed
        
        # Handle continuous mode (Exercise 13-4)
        if self.continuous:
            if self.rect.top > self.screen_rect.bottom:
                # Reset to top with random position
                self.rect.y = random.randint(-100, -20)
                self.rect.x = random.randint(0, self.screen_rect.width)
        else:
            # Remove if off screen (Exercise 13-3)
            if self.rect.top > self.screen_rect.bottom:
                self.kill()
    
    def blitme(self):
        """Draw raindrop at current position"""
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Raindrops Simulation")
        self.clock = pygame.time.Clock()
        
        # Create raindrops group
        self.raindrops = Group()
        
        # Game state
        self.mode = "falling"  # "falling" or "continuous"
        self.font = pygame.font.Font(None, 36)
        
        # Create initial raindrops
        self._create_raindrops()
    
    def _create_raindrops(self):
        """Create a grid of raindrops"""
        self.raindrops.empty()
        
        # Grid parameters
        grid_cols = 15
        grid_rows = 10
        
        # Calculate spacing
        x_spacing = SCREEN_WIDTH // (grid_cols + 1)
        y_spacing = SCREEN_HEIGHT // (grid_rows + 1)
        
        # Create raindrops in a grid pattern
        for row in range(1, grid_rows + 1):
            for col in range(1, grid_cols + 1):
                x = col * x_spacing + random.randint(-10, 10)  # Slight random offset
                y = row * y_spacing
                
                # Vary speed slightly for more natural look
                speed = random.uniform(3, 7)
                
                raindrop = Raindrop(
                    self.screen, 
                    x, 
                    y, 
                    speed, 
                    continuous=(self.mode == "continuous")
                )
                self.raindrops.add(raindrop)
    
    def _add_new_row(self):
        """Add a new row of raindrops at the top (for continuous mode)"""
        if self.mode == "continuous":
            # Check if we need more raindrops (some might have been removed)
            if len(self.raindrops) < 150:  # Maximum raindrops on screen
                for _ in range(15):  # Add 15 new raindrops
                    x = random.randint(0, self.screen.get_rect().width)
                    y = random.randint(-50, -10)
                    speed = random.uniform(3, 7)
                    
                    raindrop = Raindrop(
                        self.screen, 
                        x, 
                        y, 
                        speed, 
                        continuous=True
                    )
                    self.raindrops.add(raindrop)
    
    def run_game(self):
        """Main game loop"""
        last_row_add_time = 0
        row_add_delay = 500  # milliseconds
        
        while True:
            current_time = pygame.time.get_ticks()
            
            self._check_events()
            
            # Update raindrops
            self.raindrops.update()
            
            # Add new row periodically in continuous mode
            if (self.mode == "continuous" and 
                current_time - last_row_add_time > row_add_delay):
                self._add_new_row()
                last_row_add_time = current_time
            
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Exercise 13-3: Falling raindrops
                    self.mode = "falling"
                    self._create_raindrops()
                elif event.key == pygame.K_2:
                    # Exercise 13-4: Continuous rain
                    self.mode = "continuous"
                    self._create_raindrops()
                elif event.key == pygame.K_r:
                    # Toggle between modes
                    self.mode = "continuous" if self.mode == "falling" else "falling"
                    self._create_raindrops()
                elif event.key == pygame.K_SPACE:
                    # Add more raindrops
                    self._add_new_row()
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Create a gradient background (darker at top, lighter at bottom)
        for y in range(SCREEN_HEIGHT):
            # Calculate color based on y position
            ratio = y / SCREEN_HEIGHT
            r = int(25 * (1 - ratio) + 65 * ratio)
            g = int(25 * (1 - ratio) + 105 * ratio)
            b = int(112 * (1 - ratio) + 225 * ratio)
            color = (r, g, b)
            pygame.draw.line(self.screen, color, (0, y), (SCREEN_WIDTH, y))
        
        # Draw raindrops
        for raindrop in self.raindrops.sprites():
            raindrop.blitme()
        
        # Draw mode information
        mode_names = {
            "falling": "Falling Raindrops (Exercise 13-3)",
            "continuous": "Steady Rain (Exercise 13-4)"
        }
        
        mode_text = self.font.render(mode_names[self.mode], True, WHITE)
        self.screen.blit(mode_text, (10, 10))
        
        # Draw raindrop count
        count_text = pygame.font.Font(None, 24).render(
            f"Raindrops: {len(self.raindrops)}", True, WHITE
        )
        self.screen.blit(count_text, (10, 50))
        
        instructions = [
            "Press 1: Falling Raindrops",
            "Press 2: Steady Rain",
            "Press R: Toggle between modes",
            "Press SPACE: Add more raindrops"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, LIGHT_BLUE)
            self.screen.blit(text, (10, 80 + i * 25))
        
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run
    rain_game = Game()
    rain_game.run_game()