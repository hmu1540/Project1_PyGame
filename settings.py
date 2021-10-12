class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialze the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3  # pixels
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # dark grey
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = (
            10  # alien drops down each time it hit the right edge of the screen
        )
        # fleet_direction of 1 represents right. -1 represents left
        self.fleet_direction = 1
