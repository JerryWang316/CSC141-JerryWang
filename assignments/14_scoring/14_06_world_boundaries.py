import pygame
# Refactored _check_bullet_alien_collisions
def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(aliens)
        self.sb.prep_score()
        self.sb.check_high_score()
    
    # Start new level if all aliens are destroyed
    if not self.aliens:
        self._start_new_level()

def _start_new_level(self):
    """Start a new level when all aliens are destroyed."""
    # Destroy existing bullets and create new fleet
    self.bullets.empty()
    self._create_fleet()
    self.settings.increase_speed()
    
    # Increase level
    self.stats.level += 1
    self.sb.prep_level()

# In scoreboard.py - refactor __init__
def __init__(self, ai_game):
    """Initialize scorekeeping attributes."""
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats
    
    # Font settings for scoring information
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)
    
    # Prepare the initial score images
    self.prep_images()

def prep_images(self):
    """Prepare all scoreboard images."""
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_ships()