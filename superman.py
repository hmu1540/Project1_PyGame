import pygame


class Superman:
    def __init__(self, ai_game):

        # place it
        # change screen bg color to match the surface' bg color, or vice versa

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.transform.scale(
            pygame.image.load("images/superhero-304712_1280.bmp"), (120, 60)
        )

        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.settings = ai_game.settings

    def blitme(self):
        self.screen.blit(self.image, self.rect)
