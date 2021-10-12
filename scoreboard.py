import pygame


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)  # instantiate a font object
        # Prepare the inital score image.
        self.prep_score()  # turn the text to a image object

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(
            self.stats.score, -1
        )  # ???????????????????/report scores as multiples of 10. 1 round to 1 decimal place, 2 round to 2 decimal places; -1 round to nearest 10, -2 round to 100...
        score_str = "{:,}".format(
            rounded_score
        )  # ?????????????/format the score to include comma separators in large numbers. convert to a string and insert commas
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )  # render() creates image from the string

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # fix the right margin
        self.score_rect.top = 20  # fix the top margin

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(
            self.score_image, self.score_rect
        )  # draw the image at the position specified by rect object.
