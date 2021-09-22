import pygame


class Ship:
    """A class to mangae the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = (
            ai_game.screen
        )  # ai_game is an instance of object AlienInvasion, that has attribute screen, settings
        self.screen_rect = (
            ai_game.get_rect()
        )  # haven't defined this method inside AlienInvasion????????

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
