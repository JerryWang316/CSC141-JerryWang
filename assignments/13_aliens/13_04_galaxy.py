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
GRAY = (128, 128, 128)

class Raindrop(Sprite):
    def __init__(self, screen, x, y, rain_type="normal"):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rain_type = rain_type
        
        # Set properties based on rain type
        if rain_type == "drizzle":
            self.width = 1
            self.length = 8
            self.speed = random.uniform(2, 4)
            self.color = LIGHT_BLUE
        elif rain_type == "heavy":
            self.width = 4
            self.length = 20
            self.speed = random.uniform(8, 12)
            self.color = WHITE
        else:  # normal
            self.width = 2
            self.length = 12
            self.speed = random.uniform(4, 7)
            self.color = LIGHT_BLUE
        
        # Create raindrop surface
        self.image = pygame.Surface((self.width, self.length), pygame.SRCALPHA)
        
        # Draw raindrop
        pygame.draw.line(
            self.image, 
            self.color, 
            (self.width//2, 0), 
            (self.width//2, self.length-2), 
            self.width
        )
        # Add droplet at bottom
        pygame.draw.circle(
            self.image, 
            self.color, 
            (self.width//2, self.length-1), 
            self.width//2
        )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # For continuous mode
        self.continuous = True
    
    def update(self):
        """Move raindrop downward"""
        self.rect.y += self.speed
        
        # Reset to top when off screen
        if self.rect.top > self.screen_rect.bottom:
            self.rect.y = random.randint(-100, -20)
            self.rect.x = random.randint(0, self.screen_rect.width)
    
    def blitme(self):
        """Draw raindrop at current position"""
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Enhanced Rain Simulation")
        self.clock = pygame.time.Clock()
        
        # Create raindrops group
        self.raindrops = Group()
        
        # Game state
        self.rain_type = "normal"  # "drizzle", "normal", "heavy"
        self.font = pygame.font.Font(None, 36)
        
        # Create initial raindrops
        self._create_raindrops()
    
    def _create_raindrops(self):
        """Create raindrops based on current rain type"""
        self.raindrops.empty()
        
        # Number of raindrops based on rain type
        if self.rain_type == "drizzle":
            num_drops = 50
        elif self.rain_type == "heavy":
            num_drops = 300
        else:  # normal
            num_drops = 150
        
        # Create raindrops
        for _ in range(num_drops):
            x = random.randint(0, self.screen.get_rect().width)
            y = random.randint(-SCREEN_HEIGHT, 0)
            
            raindrop = Raindrop(self.screen, x, y, self.rain_type)
            self.raindrops.add(raindrop)
    
    def _add_more_raindrops(self):
        """Add more raindrops to maintain density"""
        target_count = {
            "drizzle": 50,
            "normal": 150,
            "heavy": 300
        }
        
        current_count = len(self.raindrops)
        target = target_count[self.rain_type]
        
        if current_count < target:
            for _ in range(target - current_count):
                x = random.randint(0, self.screen.get_rect().width)
                y = random.randint(-100, -10)
                
                raindrop = Raindrop(self.screen, x, y, self.rain_type)
                self.raindrops.add(raindrop)
    
    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            
            # Update raindrops
            self.raindrops.update()
            
            # Maintain raindrop count
            self._add_more_raindrops()
            
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.rain_type = "drizzle"
                    self._create_raindrops()
                elif event.key == pygame.K_2:
                    self.rain_type = "normal"
                    self._create_raindrops()
                elif event.key == pygame.K_3:
                    self.rain_type = "heavy"
                    self._create_raindrops()
                elif event.key == pygame.K_r:
                    # Cycle through rain types
                    types = ["drizzle", "normal", "heavy"]
                    current_index = types.index(self.rain_type)
                    self.rain_type = types[(current_index + 1) % len(types)]
                    self._create_raindrops()
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Create sky background based on rain intensity
        if self.rain_type == "drizzle":
            bg_color = (100, 149, 237)  # Light blue
        elif self.rain_type == "heavy":
            bg_color = (47, 79, 79)  # Dark slate gray
        else:  # normal
            bg_color = (65, 105, 225)  # Royal blue
            
        self.screen.fill(bg_color)
        
        # Draw raindrops
        for raindrop in self.raindrops.sprites():
            raindrop.blitme()
        
        # Draw mode information
        type_names = {
            "drizzle": "Light Drizzle",
            "normal": "Normal Rain",
            "heavy": "Heavy Rainstorm"
        }
        
        type_text = self.font.render(type_names[self.rain_type], True, WHITE)
        self.screen.blit(type_text, (10, 10))
        
        # Draw raindrop count
        count_text = pygame.font.Font(None, 24).render(
            f"Raindrops: {len(self.raindrops)}", True, WHITE
        )
        self.screen.blit(count_text, (10, 50))
        
        instructions = [
            "Press 1: Light Drizzle",
            "Press 2: Normal Rain",
            "Press 3: Heavy Rainstorm",
            "Press R: Cycle through rain types"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, LIGHT_BLUE)
            self.screen.blit(text, (10, 80 + i * 25))
        
        # Draw rain intensity meter
        self._draw_intensity_meter()
        
        pygame.display.flip()
    
    def _draw_intensity_meter(self):
        """Draw a visual intensity meter"""
        meter_width = 200
        meter_height = 20
        meter_x = SCREEN_WIDTH - meter_width - 10
        meter_y = 10
        
        # Draw meter background
        pygame.draw.rect(self.screen, DARK_BLUE, (meter_x, meter_y, meter_width, meter_height))
        
        # Draw intensity level
        intensity_levels = {"drizzle": 0.25, "normal": 0.5, "heavy": 1.0}
        level = intensity_levels[self.rain_type]
        fill_width = int(meter_width * level)
        
        pygame.draw.rect(self.screen, LIGHT_BLUE, (meter_x, meter_y, fill_width, meter_height))
        
        # Draw meter label
        label_text = pygame.font.Font(None, 20).render("Rain Intensity", True, WHITE)
        self.screen.blit(label_text, (meter_x, meter_y + meter_height + 5))

if __name__ == '__main__':
    # Create game instance and run
    rain_game = Game()
    rain_game.run_game()