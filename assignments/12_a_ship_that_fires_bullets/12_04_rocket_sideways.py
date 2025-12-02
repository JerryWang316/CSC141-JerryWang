import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Create rocket surface
        self.image = pygame.Surface((50, 100))
        self.image.fill((255, 0, 0))  # Red rectangle as rocket
        self.rect = self.image.get_rect()
        
        # Position rocket at center
        self.rect.center = self.screen_rect.center
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Movement speed
        self.speed = 5
    
    def update(self):
        """Update rocket position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
    
    def blitme(self):
        """Draw rocket at current position"""
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Rocket")
    
    # Create rocket instance
    rocket = Rocket(screen)
    
    # Main game loop
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False
        
        # Update rocket position
        rocket.update()
        
        # Redraw screen and rocket
        screen.fill((230, 230, 230))
        rocket.blitme()
        
        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    run_game()