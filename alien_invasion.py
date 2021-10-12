import sys  # ???????????
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.stats = GameStats(self)

        self.ship = Ship(
            self
        )  # e call to Ship() requires one argument, an instance of AlienInvasion
        self.bullets = pygame.sprite.Group()  # ????????????/
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            # refactoring to simplify...use a helper method inside a class, not called by an instance
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()  # aliens can be hit by bullets, thus following update_bullets()

            self._update_screen()

    def _check_events(self):
        # action that user performs, eg. press a key, move the mouse.
        # return a list of events since last time get() called
        for event in pygame.event.get():
            # click the game window close button, exit the game
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # We can use elif blocks here because each event is connected to only one key.???????????????????
                # If the player presses both keys at once, two separate events will be detected.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = (
                    pygame.mouse.get_pos()
                )  # return a tuple(x,y) of the mouse cursor
                self._check_play_button(
                    mouse_pos
                )  # restrict mousebuttondown event only to play button

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet adn center the ship
            self._create_fleet()
            self.ship.center_ship()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullet and get rid of old bullets."""
        # Update bullets postions.
        self.bullets.update()  # the group automatically calls update() for each sprite in the group, i.e., update each bullet in the group we built

        # Get rid of bullet that have disappeared to aviod unnecessary storage consumption
        for (
            bullet
        ) in self.bullets.copy():  # a copy of bullets list stays the same in the loop
            if (
                bullet.rect.bottom <= 0
            ):  # why not rect.y? rect is a shape of all points data
                self.bullets.remove(bullet)  # the bullets list changes in the list
            # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        # If so, get rid fo teh bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )  # Delete both sprites if collided

        if not self.aliens:  # check for empty aliens, then create a new fleet
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """
        Check if the fleet is at an edge, then
        update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(
            self.ship, self.aliens
        ):  # returns the first alien it finds that has collided with ship or return None.

            self._ship_hit()
            # print("Ship hit!!!")
            # print("Hit alien, left ", self.stats.ships_left)

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        self.stats.ships_left -= 1
        # print(self.stats.ships_left)

        if self.stats.ships_left > 0:
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()  # ????????????????????????????????have i defind this method

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien and find teh number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the sceen.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):  # from 0 to number_aliens_x -1
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and plce it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """update ... and flip ..."""

        self.screen.fill(self.settings.bg_color)
        # Redrawn the screen during each pass through the loop.
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # When you call draw() on a group, Pygame draws each element in the group at the position
        # defined by its rect attribute. The draw() method requires one argument: a surface on
        # which to draw the elements from the group.

        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        # disply most recently drawn game window, update continually

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                # print("Ship hit!!!")
                # print("hit bottom, left: ", self.stats.ships_left)
                break


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
