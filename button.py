import pygame


class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # bright green
        self.text_color = (255, 255, 255)  # white
        self.font = pygame.font.SysFont(None, 48)  # defautl font

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(
            0, 0, self.width, self.height
        )  # pygame.Rect object ??????????????
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once. ????????????????????????//
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # font.render() turns the text stored in msg into an image
        # font.render() takes a Boolean value to turn antialiasing on or off(smoothign the edges of teh text or not: bacground color same as the button)
        # font.render() takes the font color and backgroudn color
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(
            self.button_color, self.rect
        )  # draw the rectanglular portion of the button
        self.screen.blit(
            self.msg_image, self.msg_image_rect
        )  # draw the text image and the rect object associated
