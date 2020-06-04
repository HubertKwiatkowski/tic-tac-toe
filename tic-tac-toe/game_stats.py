class GameStats:
    """Track statistics of Tic-Tac-Toe"""

    def __init__(self, ttt_game):
        """Initialize statistics."""
        self.settings = ttt_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        self.moves_count = self.settings.moves
        self.active_player = "PLAYER X"
