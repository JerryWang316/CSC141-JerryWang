import pygame
import sys
import random
from pygame.sprite import Sprite, Group

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Game settings
FPS = 60
SHIP_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED_MIN = 1
ALIEN_SPEED_MAX = 4
ALIEN_SPAWN_RATE = 1000  # milliseconds
POWERUP_SPAWN_RATE = 10000  # milliseconds

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create ship surface
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        
        # Draw detailed ship facing right
        pygame.draw.polygon(self.image, GREEN, [
            (0, 15),    # Left tip
            (30, 0),    # Top front
            (40, 15),   # Right tip
            (30, 30)    # Bottom front
        ])
        
        # Add cockpit
        pygame.draw.circle(self.image, YELLOW, (25, 15), 5)
        
        # Add engine glow
        pygame.draw.polygon(self.image, RED, [
            (0, 10), (0, 20), (-10, 15)
        ])
        
        self.rect = self.image.get_rect()
        
        # Start ship on left side
        self.rect.left = 20
        self.rect.centery = self.screen_rect.centery
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        
        # Ship stats
        self.health = 3
        self.power_level = 1
        self.power_timer = 0
    
    def update(self):
        """Update ship position based on movement flags"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= SHIP_SPEED
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += SHIP_SPEED
        
        # Decrease power level over time
        if self.power_level > 1:
            self.power_timer -= 1
            if self.power_timer <= 0:
                self.power_level = 1
    
    def blitme(self):
        """Draw ship at current position"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the left side"""
        self.rect.left = 20
        self.rect.centery = self.screen_rect.centery
        self.health = 3
        self.power_level = 1
    
    def apply_powerup(self, power_type):
        """Apply power-up effect"""
        if power_type == "rapid_fire":
            self.power_level = 2
            self.power_timer = 500  # frames
        elif power_type == "shield":
            self.health = min(5, self.health + 1)

class Bullet(Sprite):
    def __init__(self, screen, ship, power_level=1):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Bullet size based on power level
        width = 15 if power_level == 1 else 25
        height = 5 if power_level == 1 else 8
        
        # Create bullet surface
        self.image = pygame.Surface((width, height))
        self.image.fill(RED if power_level == 1 else ORANGE)
        
        # Add bullet tip
        pygame.draw.rect(self.image, YELLOW, (width-5, 0, 5, height))
        
        self.rect = self.image.get_rect()
        
        # Position bullet at ship's right side
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right
        
        # Store horizontal position for smooth movement
        self.x = float(self.rect.x)
        
        # Speed based on power level
        self.speed = BULLET_SPEED if power_level == 1 else BULLET_SPEED * 1.5
    
    def update(self):
        """Move bullet to the right"""
        self.x += self.speed
        self.rect.x = self.x
        
        # Remove bullet if it goes off screen
        if self.rect.left > self.screen_rect.right:
            self.kill()
    
    def draw_bullet(self):
        """Draw bullet to the screen"""
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, screen, alien_type="normal"):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.alien_type = alien_type
        
        # Set properties based on alien type
        if alien_type == "fast":
            size = 25
            self.color = YELLOW
            self.speed = random.uniform(ALIEN_SPEED_MAX-1, ALIEN_SPEED_MAX+1)
            self.points = 3
        elif alien_type == "tough":
            size = 60
            self.color = PURPLE
            self.speed = random.uniform(ALIEN_SPEED_MIN, ALIEN_SPEED_MIN+1)
            self.points = 5
            self.health = 2
        else:  # normal
            size = 40
            self.color = BLUE
            self.speed = random.uniform(ALIEN_SPEED_MIN, ALIEN_SPEED_MAX)
            self.points = 1
            self.health = 1
        
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Draw alien body
        pygame.draw.circle(self.image, self.color, (size//2, size//2), size//2)
        
        # Draw alien eyes
        eye_size = size // 5
        pygame.draw.circle(self.image, WHITE, (size//3, size//3), eye_size)
        pygame.draw.circle(self.image, WHITE, (2*size//3, size//3), eye_size)
        pygame.draw.circle(self.image, BLACK, (size//3, size//3), eye_size//2)
        pygame.draw.circle(self.image, BLACK, (2*size//3, size//3), eye_size//2)
        
        # Draw alien mouth
        pygame.draw.arc(self.image, RED, 
                       (size//4, size//2, size//2, size//4), 
                       0, 3.14, 2)
        
        self.rect = self.image.get_rect()
        
        # Start position on right side with random y
        self.rect.right = self.screen_rect.right
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
        # Store position for smooth movement
        self.x = float(self.rect.x)
    
    def update(self):
        """Move alien to the left"""
        self.x -= self.speed
        self.rect.x = self.x
        
        # Remove alien if it goes off screen on the left
        if self.rect.right < 0:
            self.kill()
            return True  # Return True if alien passed the ship
        return False
    
    def hit(self):
        """Handle alien being hit by bullet"""
        if self.alien_type == "tough":
            self.health -= 1
            if self.health <= 0:
                self.kill()
                return self.points
            return 0  # Hit but not destroyed
        else:
            self.kill()
            return self.points
    
    def blitme(self):
        """Draw alien at current position"""
        self.screen.blit(self.image, self.rect)

class PowerUp(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Random power-up type
        self.power_type = random.choice(["rapid_fire", "shield"])
        
        # Create power-up surface
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        
        # Draw power-up based on type
        if self.power_type == "rapid_fire":
            pygame.draw.circle(self.image, ORANGE, (10, 10), 10)
            pygame.draw.rect(self.image, YELLOW, (5, 8, 10, 4))
        else:  # shield
            pygame.draw.circle(self.image, BLUE, (10, 10), 10)
            pygame.draw.circle(self.image, WHITE, (10, 10), 6, 2)
        
        self.rect = self.image.get_rect()
        
        # Start position on right side with random y
        self.rect.right = self.screen_rect.right
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
        # Store position for smooth movement
        self.x = float(self.rect.x)
        
        # Movement speed
        self.speed = 2
    
    def update(self):
        """Move power-up to the left"""
        self.x -= self.speed
        self.rect.x = self.x
        
        # Remove if off screen
        if self.rect.right < 0:
            self.kill()
    
    def blitme(self):
        """Draw power-up at current position"""
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sideways Shooter - Advanced")
        self.clock = pygame.time.Clock()
        
        # Create game objects
        self.ship = Ship(self.screen)
        self.bullets = Group()
        self.aliens = Group()
        self.powerups = Group()
        
        # Game state
        self.score = 0
        self.level = 1
        self.game_active = True
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Spawn timers
        self.alien_spawn_time = 0
        self.powerup_spawn_time = 0
        
        # Game statistics
        self.aliens_shot = 0
        self.ship_hits = 0
        self.max_ship_hits = 3
    
    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                aliens_passed = self._update_aliens()
                self._update_powerups()
                self._spawn_aliens()
                self._spawn_powerups()
                self._check_collisions()
                
                # Count aliens that passed the ship
                if aliens_passed:
                    self.ship_hits += 1
                    if self.ship_hits >= self.max_ship_hits:
                        self.game_active = False
                
                # Increase level based on score
                if self.score >= self.level * 15:
                    self.level += 1
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
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_r and not self.game_active:
                    self._restart_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        max_bullets = 8 if self.ship.power_level == 1 else 12
        
        if len(self.bullets) < max_bullets:
            new_bullet = Bullet(self.screen, self.ship, self.ship.power_level)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and remove old ones"""
        self.bullets.update()
    
    def _update_aliens(self):
        """Update position of aliens and return count of aliens that passed"""
        aliens_passed = 0
        for alien in self.aliens.sprites():
            if alien.update():  # Returns True if alien passed the ship
                aliens_passed += 1
        return aliens_passed
    
    def _update_powerups(self):
        """Update position of power-ups"""
        self.powerups.update()
    
    def _spawn_aliens(self):
        """Spawn new aliens at regular intervals"""
        current_time = pygame.time.get_ticks()
        
        # Adjust spawn rate based on level
        spawn_delay = max(200, ALIEN_SPAWN_RATE - (self.level - 1) * 100)
        
        if current_time - self.alien_spawn_time > spawn_delay:
            # Determine alien type based on level
            rand = random.random()
            if self.level >= 3 and rand < 0.2:
                alien_type = "tough"
            elif self.level >= 2 and rand < 0.4:
                alien_type = "fast"
            else:
                alien_type = "normal"
                
            new_alien = Alien(self.screen, alien_type)
            self.aliens.add(new_alien)
            self.alien_spawn_time = current_time
    
    def _spawn_powerups(self):
        """Spawn power-ups at regular intervals"""
        current_time = pygame.time.get_ticks()
        
        if current_time - self.powerup_spawn_time > POWERUP_SPAWN_RATE:
            new_powerup = PowerUp(self.screen)
            self.powerups.add(new_powerup)
            self.powerup_spawn_time = current_time
    
    def _check_collisions(self):
        """Check for various collisions"""
        # Check bullet-alien collisions
        for bullet in self.bullets.sprites():
            alien_hit = pygame.sprite.spritecollideany(bullet, self.aliens)
            if alien_hit:
                points = alien_hit.hit()
                if points > 0:  # Alien was destroyed
                    self.score += points
                    self.aliens_shot += 1
                bullet.kill()
        
        # Check alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hits += 1
            # Remove all aliens that collided with the ship
            for alien in pygame.sprite.spritecollide(self.ship, self.aliens, True):
                pass
            
            if self.ship_hits >= self.max_ship_hits:
                self.game_active = False
        
        # Check powerup-ship collisions
        powerup_hit = pygame.sprite.spritecollideany(self.ship, self.powerups)
        if powerup_hit:
            self.ship.apply_powerup(powerup_hit.power_type)
            powerup_hit.kill()
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(BLACK)
        
        # Draw game objects
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blitme()
        for powerup in self.powerups.sprites():
            powerup.blitme()
        
        # Draw UI elements
        self._draw_ui()
        
        # Draw game over screen
        if not self.game_active:
            self._draw_game_over()
        
        pygame.display.flip()
    
    def _draw_ui(self):
        """Draw user interface elements"""
        # Score and level
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (SCREEN_WIDTH - 120, 10))
        
        # Ship health
        health_text = self.font.render(f"Health: {self.ship.health}", True, GREEN)
        self.screen.blit(health_text, (10, 50))
        
        # Power level indicator
        power_text = self.font.render(f"Power: {self.ship.power_level}", True, ORANGE)
        self.screen.blit(power_text, (10, 90))
        
        # Statistics
        stats_text = self.small_font.render(
            f"Aliens Shot: {self.aliens_shot} | Ship Hits: {self.ship_hits}", 
            True, YELLOW
        )
        self.screen.blit(stats_text, (10, SCREEN_HEIGHT - 30))
        
        # Controls
        controls_text = self.small_font.render(
            "Controls: UP/DOWN = Move, SPACE = Shoot, R = Restart", 
            True, BLUE
        )
        self.screen.blit(controls_text, (SCREEN_WIDTH - 450, SCREEN_HEIGHT - 30))
        
        # Alien types key
        if self.level >= 2:
            key_text = self.small_font.render(
                "Blue=Normal(1) | Yellow=Fast(3) | Purple=Tough(5)", 
                True, WHITE
            )
            self.screen.blit(key_text, (SCREEN_WIDTH//2 - 180, 10))
    
    def _draw_game_over(self):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font.render("GAME OVER", True, RED)
        self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 80))
        
        # Final score
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 30))
        
        # Statistics
        stats_text = self.font.render(
            f"Aliens Shot: {self.aliens_shot} | Level Reached: {self.level}", 
            True, YELLOW
        )
        self.screen.blit(stats_text, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2 + 10))
        
        # Restart instruction
        restart_text = self.font.render("Press R to Restart", True, GREEN)
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 60))
    
    def _restart_game(self):
        """Restart the game"""
        self.game_active = True
        self.score = 0
        self.level = 1
        self.aliens_shot = 0
        self.ship_hits = 0
        self.bullets.empty()
        self.aliens.empty()
        self.powerups.empty()
        self.ship.center_ship()

if __name__ == '__main__':
    # Create game instance and run
    shooter_game = Game()
    shooter_game.run_game()