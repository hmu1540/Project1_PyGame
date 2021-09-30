import pygame


class Ship:
    """A class to mangae the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = (
            ai_game.screen
        )  # ai_game is an instance of object AlienInvasion, that has attribute screen, settings
        self.screen_rect = (
            ai_game.screen.get_rect()
        )  # haven't defined this method inside AlienInvasion????????

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            "images/ship.bmp"
        )  # returns a surface representing the ship
        self.rect = (
            self.image.get_rect()
        )  # access the ship surface’s rect attribute so we can later use it to place the ship. return a rect object that has attributes: left right top bottom center centerx mid-

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = (
            self.screen_rect.midbottom
        )  # image midbottom location is screen_rect midbottom loc; bounding rectangle attributs of locations

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(
            self.image, self.rect
        )  # draws the image to the screen at the position specified by self.rect


print("")
