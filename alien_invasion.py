import sys  # ???????????
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize the background settings
        self.settings = Settings()
        # attribute settings is an instance of Settings object, so it has attributs, methods

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )  # don't think this is a good way, access attributes directly instead of via methods

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

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            """for event in pygame.event.get():
            # action that user performs, eg. press a key, move the mouse.
            # return a list of events since last time get() called
            #
            if event.type == pygame.QUIT:  # click the game wind close button
                sys.exit()  # exit the game"""

            """ # Redrawn the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip() 
            # disply most recently drawn game window, update continually """

            self._check_events()  # refactoring to simplify...use a helper method inside a class, not called by an instance
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.key == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1

    def _update_screen(self):
        """update ... and flip ..."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        """ self.superman.scale()
        self.superman.set_color()
        self.superman.blitme()
        """
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
