import pygame


class Ship:
    """A class to mangae the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = (
            ai_game.screen
        )  # ai_game is an instance of object AlienInvasion, that has attribute screen, settings
        self.settings = ai_game.settings
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

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.right returns the x­coordinate of the right edge of the ship’s rect
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # not elif to allow x vlaues  to be increased and then decreased when both arrow keys
            # are held down.makes the movements more accurate when switching from right to left
            # when the player might momentarily hold down both keys.

            self.x -= self.settings.ship_speed

        # rect will only keep the integer portion of that value.
        # To keep track of the ship’s position accurately, we define a new self.x attribute that can hold decimal values
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(
            self.image, self.rect
        )  # draws the image to the screen at the position specified by self.rect
