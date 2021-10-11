import sys  # ???????????
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize the background settings
        self.settings = Settings()
        # attribute settings is an instance of Settings object, so it has attributs, methods

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN
        )  # figure out a window size that will fill the screen
        self.settings.screen_width = (
            self.screen.get_rect().width
        )  # update these settings after the screen is created
        self.settings.screen_height = self.screen.get_rect().height

        """ 
        RHS Creates a display window 1200 pi * 800 pi   
        RHS is called a surface: part of a screen for displaying a game element
        Each element is its own surface, like an alien or a ship 
        display.set_mode() represents the entire game window, redrawn in loop
        """

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(
            self
        )  # e call to Ship() requires one argument, an instance of AlienInvasion
        self.bullets = pygame.sprite.Group()  # ????????????/

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            # refactoring to simplify...use a helper method inside a class, not called by an instance
            self._check_events()
            self.ship.update()
            self.bullets.update()  # the group automatically calls update() for each sprite in the group, i.e., update each bullet in the group we built

            # Get rid of bullet that have disappeared to aviod unnecessary storage consumption
            for (
                bullet
            ) in (
                self.bullets.copy()
            ):  # a copy of bullets list stays the same in the loop
                if (
                    bullet.rect.bottom <= 0
                ):  # why not rect.y? rect is a shape of all points data
                    self.bullets.remove(bullet)  # the bullets list changes in the list
                # print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        # action that user performs, eg. press a key, move the mouse.
        # return a list of events since last time get() called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # click the game window close button, exit the game
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # We can use elif blocks here because each event is connected to only one key.???????????????????
                # If the player presses both keys at once, two separate events will be detected.

    # two helper methods
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """update ... and flip ..."""

        self.screen.fill(self.settings.bg_color)
        # Redrawn the screen during each pass through the loop.
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible
        pygame.display.flip()
        # disply most recently drawn game window, update continually


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
