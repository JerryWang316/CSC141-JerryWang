import pygame
import sys
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
BULLET_SPEED = 10
TARGET_SPEED = 3

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create ship surface
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        
        # Draw ship facing right
        pygame.draw.polygon(self.image, GREEN, [
            (0, 15),    # Left tip
            (30, 0),    # Top front
            (40, 15),   # Right tip
            (30, 30)    # Bottom front
        ])
        
        # Add cockpit
        pygame.draw.circle(self.image, YELLOW, (25, 15), 5)
        
        self.rect = self.image.get_rect()
        
        # Start ship on left side
        self.rect.left = 50
        self.rect.centery = self.screen_rect.centery
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update ship position based on movement flags"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= SHIP_SPEED
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += SHIP_SPEED
    
    def blitme(self):
        """Draw ship at current position"""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create bullet surface
        self.image = pygame.Surface((15, 5))
        self.image.fill(RED)
        
        # Add bullet tip
        pygame.draw.rect(self.image, YELLOW, (10, 0, 5, 5))
        
        self.rect = self.image.get_rect()
        
        # Position bullet at ship's right side
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right
        
        # Store horizontal position for smooth movement
        self.x = float(self.rect.x)
    
    def update(self):
        """Move bullet to the right"""
        self.x += BULLET_SPEED
        self.rect.x = self.x
        
        # Remove bullet if it goes off screen
        if self.rect.left > self.screen_rect.right:
            self.kill()
            return True  # Return True if bullet missed
        return False
    
    def draw_bullet(self):
        """Draw bullet to the screen"""
        self.screen.blit(self.image, self.rect)

class Target(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create target surface
        self.width = 30
        self.height = 100
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        
        # Add target rings
        pygame.draw.rect(self.image, WHITE, (5, 5, self.width-10, self.height-10), 2)
        pygame.draw.rect(self.image, RED, (10, 20, self.width-20, self.height-40), 2)
        
        self.rect = self.image.get_rect()
        
        # Position target on right side
        self.rect.right = self.screen_rect.right - 20
        self.rect.centery = self.screen_rect.centery
        
        # Movement direction
        self.direction = 1  # 1 for down, -1 for up
    
    def update(self):
        """Move target up and down"""
        self.rect.y += TARGET_SPEED * self.direction
        
        # Reverse direction if hitting top or bottom
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.direction *= -1
    
    def blitme(self):
        """Draw target at current position"""
        self.screen.blit(self.image, self.rect)

class Button:
    def __init__(self, screen, msg, x, y, width=200, height=50):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set button dimensions and properties
        self.width, self.height = width, height
        self.button_color = GREEN
        self.text_color = WHITE
        self.font = pygame.font.Font(None, 48)
        
        # Build button rect and position it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        
        # Prepare message
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class TargetPractice:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Target Practice")
        self.clock = pygame.time.Clock()
        
        # Create game objects
        self.ship = Ship(self.screen)
        self.bullets = Group()
        self.target = Target(self.screen)
        
        # Game state
        self.score = 0
        self.misses = 0
        self.max_misses = 3
        self.game_active = False
        self.font = pygame.font.Font(None, 36)
        
        # Create play button
        self.play_button = Button(self.screen, "Play", SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    def _start_game(self):
        """Start a new game"""
        self.game_active = True
        self.score = 0
        self.misses = 0
        self.bullets.empty()
        self.ship.rect.centery = self.screen.get_rect().centery
        self.target.rect.centery = self.screen.get_rect().centery
    
    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.target.update()
                missed_bullets = self._update_bullets()
                
                # Count missed bullets
                if missed_bullets:
                    self.misses += missed_bullets
                    if self.misses >= self.max_misses:
                        self.game_active = False
                
                self._check_collisions()
            self._update_screen()
            self.clock.tick(FPS)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE and self.game_active:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
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
        if len(self.bullets) < 3:  # Limit bullets on screen
            new_bullet = Bullet(self.screen, self.ship)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and return count of missed bullets"""
        missed_count = 0
        for bullet in self.bullets.sprites():
            if bullet.update():  # Returns True if bullet missed
                missed_count += 1
        return missed_count
    
    def _check_collisions(self):
        """Check for bullet-target collisions"""
        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)
        if collisions:
            self.score += len(collisions)
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(BLACK)
        
        # Draw game objects if game is active
        if self.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.target.blitme()
            
            # Draw score and misses
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            misses_text = self.font.render(f"Misses: {self.misses}/{self.max_misses}", True, WHITE)
            self.screen.blit(misses_text, (SCREEN_WIDTH - 150, 10))
            
            # Draw instructions
            instructions = [
                "Controls: UP/DOWN ARROW = Move, SPACE = Shoot",
                "Hit the blue target to score points!",
                f"Game ends after {self.max_misses} misses."
            ]
            
            for i, instruction in enumerate(instructions):
                text = pygame.font.Font(None, 24).render(instruction, True, YELLOW)
                self.screen.blit(text, (10, 40 + i * 25))
        else:
            # Draw play button
            self.play_button.draw_button()
            
            # Draw game title
            title_font = pygame.font.Font(None, 64)
            title_text = title_font.render("TARGET PRACTICE", True, WHITE)
            title_rect = title_text.get_rect()
            title_rect.centerx = self.screen.get_rect().centerx
            title_rect.y = 100
            self.screen.blit(title_text, title_rect)
            
            # Draw game over message if applicable
            if self.misses >= self.max_misses:
                game_over_font = pygame.font.Font(None, 48)
                game_over_text = game_over_font.render("GAME OVER", True, RED)
                game_over_rect = game_over_text.get_rect()
                game_over_rect.centerx = self.screen.get_rect().centerx
                game_over_rect.y = 180
                self.screen.blit(game_over_text, game_over_rect)
                
                final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
                final_score_rect = final_score_text.get_rect()
                final_score_rect.centerx = self.screen.get_rect().centerx
                final_score_rect.y = 240
                self.screen.blit(final_score_text, final_score_rect)
            
            # Draw instructions
            instructions = [
                "Click Play to Start",
                "",
                "Controls:",
                "UP/DOWN ARROW: Move Ship",
                "SPACEBAR: Shoot Bullets",
                "",
                "Goal:",
                f"Hit the moving target to score points.",
                f"Avoid missing {self.max_misses} times!"
            ]
            
            for i, instruction in enumerate(instructions):
                text = pygame.font.Font(None, 30).render(instruction, True, WHITE)
                text_rect = text.get_rect()
                text_rect.centerx = self.screen.get_rect().centerx
                text_rect.y = 300 + i * 35
                self.screen.blit(text, text_rect)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run
    target_game = TargetPractice()
    target_game.run_game()