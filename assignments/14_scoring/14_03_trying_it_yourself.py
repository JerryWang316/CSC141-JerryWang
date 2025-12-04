# In your Target class
def increase_speed(self):
    """Increase the target's speed"""
    self.speed *= self.speed_increase_factor

# In your game class when starting/restarting
def reset_target(self):
    """Reset target to original speed"""
    self.target.speed = self.settings.target_speed