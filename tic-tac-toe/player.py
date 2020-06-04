import pygame.font

class PlayerDisplay:
    """A class reporting active player"""

    def __init__(self, ttt_game):
        self.screen = ttt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ttt_game.settings
        self.stats = ttt_game.stats

        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 150)

        self.prep_player()

    def prep_player(self):
        """Turn the player label into a rendered image."""
        player_str = self.stats.active_player
        self.player_image = self.font.render(player_str, True,
            self.text_color, self.settings.bg_color)

        # Display the label in top center of the screen.
        self.player_rect = self.player_image.get_rect()
        self.player_rect.top = 50
        self.player_rect.left = 100

    def show_active_player(self):
        """Draw active player to the screen"""
        self.screen.blit(self.player_image, self.player_rect)
