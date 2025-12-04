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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# Game settings
FPS = 60
SHIP_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED = 1.5
ALIEN_DROP_SPEED = 5

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create ship surface
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        
        # Draw a more detailed ship
        pygame.draw.polygon(self.image, GREEN, [
            (25, 0),    # Nose
            (0, 40),    # Bottom left
            (20, 30),   # Left wing tip
            (30, 30),   # Right wing tip
            (50, 40)    # Bottom right
        ])
        
        # Add cockpit
        pygame.draw.circle(self.image, YELLOW, (25, 15), 8)
        
        self.rect = self.image.get_rect()
        
        # Start ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update ship position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += SHIP_SPEED
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= SHIP_SPEED
    
    def blitme(self):
        """Draw ship at current position"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship at bottom of screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create bullet surface
        self.image = pygame.Surface((5, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Position bullet at ship's top
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store vertical position for smooth movement
        self.y = float(self.rect.y)
    
    def update(self):
        """Move bullet upward"""
        self.y -= BULLET_SPEED
        self.rect.y = self.y
        
        # Remove bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()
    
    def draw_bullet(self):
        """Draw bullet to the screen"""
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create alien surface
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        
        # Draw alien body
        pygame.draw.circle(self.image, BLUE, (20, 20), 15)
        
        # Draw alien eyes
        pygame.draw.circle(self.image, WHITE, (12, 15), 5)
        pygame.draw.circle(self.image, WHITE, (28, 15), 5)
        pygame.draw.circle(self.image, BLACK, (12, 15), 2)
        pygame.draw.circle(self.image, BLACK, (28, 15), 2)
        
        # Draw alien mouth
        pygame.draw.arc(self.image, RED, (10, 20, 20, 10), 0, 3.14, 2)
        
        self.rect = self.image.get_rect()
        
        # Start position (random at top)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        
        # Store position for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement direction
        self.horizontal_speed = random.uniform(-0.5, 0.5)
    
    def update(self):
        """Move alien downward with slight horizontal movement"""
        self.y += ALIEN_SPEED
        self.x += self.horizontal_speed
        
        # Keep alien within screen bounds
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.horizontal_speed *= -1
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Remove alien if it goes off bottom of screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
    
    def blitme(self):
        """Draw alien at current position"""
        self.screen.blit(self.image, self.rect)

class Button:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = GREEN
        self.text_color = WHITE
        self.font = pygame.font.Font(None, 48)
        
        # Build button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Prepare message
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Alien Invasion - Press P to Play")
        self.clock = pygame.time.Clock()
        
        # Create game objects
        self.ship = Ship(self.screen)
        self.bullets = Group()
        self.aliens = Group()
        
        # Game state
        self.score = 0
        self.level = 1
        self.game_active = False  # Game starts inactive
        self.font = pygame.font.Font(None, 36)
        
        # Alien spawn timer
        self.alien_spawn_time = 0
        self.alien_spawn_delay = 1500
        
        # Create play button
        self.play_button = Button(self.screen, "Play")
    
    def _start_game(self):
        """Start a new game"""
        self.game_active = True
        self.score = 0
        self.level = 1
        self.bullets.empty()
        self.aliens.empty()
        self.ship.center_ship()
    
    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._spawn_aliens()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(FPS)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE and self.game_active:
                    self._fire_bullet()
                elif event.key == pygame.K_p and not self.game_active:
                    # Start game when P is pressed
                    self._start_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        if len(self.bullets) < 5:
            new_bullet = Bullet(self.screen, self.ship)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and remove old ones"""
        self.bullets.update()
    
    def _update_aliens(self):
        """Update position of aliens"""
        self.aliens.update()
    
    def _spawn_aliens(self):
        """Spawn new aliens at regular intervals"""
        current_time = pygame.time.get_ticks()
        if current_time - self.alien_spawn_time > self.alien_spawn_delay:
            new_alien = Alien(self.screen)
            self.aliens.add(new_alien)
            self.alien_spawn_time = current_time
    
    def _check_collisions(self):
        """Check for bullet-alien collisions and alien-ship collisions"""
        # Check bullet-alien collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.score += len(collisions)
        
        # Check alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.game_active = False
        
        # Check if aliens reached bottom (game over condition)
        for alien in self.aliens:
            if alien.rect.bottom >= SCREEN_HEIGHT:
                self.game_active = False
                break
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(BLACK)
        
        # Draw game objects if game is active
        if self.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            for alien in self.aliens.sprites():
                alien.blitme()
            
            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Draw level
            level_text = self.font.render(f"Level: {self.level}", True, WHITE)
            self.screen.blit(level_text, (SCREEN_WIDTH - 120, 10))
        else:
            # Draw play button and instructions
            self.play_button.draw_button()
            
            # Draw instructions
            instructions = [
                "Press P to Start Game",
                "or Click the Play Button",
                "",
                "Controls:",
                "LEFT/RIGHT ARROW: Move Ship",
                "SPACEBAR: Shoot"
            ]
            
            for i, instruction in enumerate(instructions):
                text = pygame.font.Font(None, 30).render(instruction, True, WHITE)
                text_rect = text.get_rect()
                text_rect.centerx = self.screen.get_rect().centerx
                text_rect.y = 350 + i * 35
                self.screen.blit(text, text_rect)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run
    ai_game = Game()
    ai_game.run_game()