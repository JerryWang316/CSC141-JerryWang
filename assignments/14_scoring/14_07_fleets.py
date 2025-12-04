import pygame

# New AlienBullet class
class AlienBullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from aliens."""
    
    def __init__(self, ai_game, alien):
        """Create a bullet object at the alien's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color
        
        # Create bullet rect at (0, 0) then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width,
            self.settings.alien_bullet_height)
        self.rect.midbottom = alien.rect.midbottom
        
        # Store bullet's position as decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet down the screen."""
        # Update decimal position
        self.y += self.settings.alien_bullet_speed
        # Update rect position
        self.rect.y = self.y