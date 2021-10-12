class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()  # ????????????????????????????????????????//why not directly codeing the attribute here
        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit  # ?????????????????????
        self.score = 0  # ??????????????????? page 288
        # To reset the score each time a new game starts, we initialize score in reset_stats() rather than __init__()
