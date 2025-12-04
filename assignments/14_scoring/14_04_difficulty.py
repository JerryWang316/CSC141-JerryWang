# In your Settings class
def set_difficulty(self, difficulty):
    """Set game difficulty level"""
    if difficulty == 'easy':
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
    elif difficulty == 'medium':
        self.ship_speed = 2.0
        self.bullet_speed = 2.5
        self.alien_speed = 1.5
    elif difficulty == 'hard':
        self.ship_speed = 2.5
        self.bullet_speed = 2.0
        self.alien_speed = 2.0