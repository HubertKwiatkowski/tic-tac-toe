class Settings:
    """A class to store all settings for Tic-Tac-Toe"""

    def __init__(self):
        """Initilialize the game's settings"""
        # Screen settings
        self.screen_width = 700
        self.screen_height = 900
        self.bg_color = (150, 150, 150)

        # Move number
        self.moves = 0

        # Active player x
        self.active_x_sign = True
