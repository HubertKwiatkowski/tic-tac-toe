import sys
import pygame
import random

from time import sleep

from settings import Settings
from x_o_field import Field, XField, OField
from button import Button
from game_stats import GameStats
from player import PlayerDisplay
from slashes import Slash, BSlash, HSlash, VSlash

GRID = ['0', '0', '0',
        '0', '0', '0',
        '0', '0', '0',
]

class TicTacToe:
    """A class to manage the game"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic-Tac-Toe")

        # Create an instance to store game statistics,
        #   and create active player sign.
        self.stats = GameStats(self)
        self.pd = PlayerDisplay(self)

        self.fields = pygame.sprite.Group()
        self.lines = pygame.sprite.Group()

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            if self.stats.game_active:
                self._check_move_count()
                self._check_line()

            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_field(mouse_pos)
                self._check_play_button(mouse_pos)

    def _check_field(self, mouse_pos):
        """"Checks for mouse click and flips the field sign"""
        for field in self.fields:
            field_clicked = field.rect.collidepoint(mouse_pos)
            if field_clicked:
                x = field.rect.x
                y = field.rect.y
                a = field.marker
                self.fields.remove(field)
                if self.settings.active_x_sign == True and field.flipped == False:
                    field = XField(self)
                    self.settings.active_x_sign = False
                    self.stats.active_player = "PLAYER O"

                elif self.settings.active_x_sign == False and field.flipped == False:
                    field = OField(self)
                    self.settings.active_x_sign = True
                    self.stats.active_player = "PLAYER X"

                self.pd.prep_player()
                field.rect.x = x
                field.rect.y = y
                field.marker = a
                GRID[a] = field.value
                self.fields.add(field)
                self.stats.moves_count += 1


    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # Draw the play button if game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        else:
            self.fields.draw(self.screen)
            self.lines.draw(self.screen)

            self.pd.show_active_player()

        self.lines.draw(self.screen)
        pygame.display.flip()

    def _create_board(self):
        """Create whole board."""
        field = Field(self)
        field_width, field_height = field.rect.size
        pos = 0
        for row in range(3):
            for col in range(3):
                self._create_field(row, col, pos)
                GRID[pos] = field.value # positions field in the # grid
                pos += 1

    def _create_field(self, row, col, pos):
        """Create single field"""
        field = Field(self)
        field_width, field_height = field.rect.size
        field.x = col * (field_width + 50)
        field.rect.x = field.x
        field.y = 200 + row * (field_height + 50)
        field.rect.y = field.y
        field.marker = pos
        self.fields.add(field)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            # Deletes used fields.
            self.fields.empty()

            self._create_board()

    def _check_move_count(self):
        if self.stats.moves_count == 9:
            self._end_game()

    def _check_line(self):
        """Check if 3 identical signs are in one line"""

        if GRID[0] != '0' and GRID[0] == GRID[1] and GRID[1] == GRID[2]:
            x, y = 50, 200
            self._create_h_slash(x, y)
        elif GRID[3] != '0' and GRID[3] == GRID[4] and GRID[4] == GRID[5]:
            x, y = 50, 450
            self._create_h_slash(x, y)
        elif GRID[6] != '0' and GRID[6] == GRID[7] and GRID[7] == GRID[8]:
            x, y = 50, 700
            self._create_h_slash(x, y)
        elif GRID[0] != '0' and GRID[0] == GRID[3] and GRID[3] == GRID[6]:
            x, y = 0, 250
            self._create_v_slash(x, y)
        elif GRID[1] != '0' and GRID[1] == GRID[4] and GRID[4] == GRID[7]:
            x, y = 250, 250
            self._create_v_slash(x, y)
        elif GRID[2] != '0' and GRID[2] == GRID[5] and GRID[5] == GRID[8]:
            x, y = 500, 250
            self._create_v_slash(x, y)
        elif GRID[0] != '0' and GRID[0] == GRID[4] and GRID[4] == GRID[8]:
            x, y = 50, 250
            self._create_b_slash(x, y)
        elif GRID[2] != '0' and GRID[2] == GRID[4] and GRID[4] == GRID[6]:
            x, y = 50, 250
            self._create_slash(x, y)

    def _end_game(self):
        sleep(0.5)
        self.lines.empty()
        self.stats.game_active = False

    def _create_slash(self, x, y):
        """Create slash line."""
        line = Slash(self)
        line_width, line_height = line.rect.size
        line.rect.x = x
        line.rect.y = y
        self.lines.add(line)
        sleep(0.5)
        self._update_screen()
        self._end_game()

    def _create_b_slash(self, x, y):
        """Create slash line."""
        line = BSlash(self)
        line_width, line_height = line.rect.size
        line.rect.x = x
        line.rect.y = y
        self.lines.add(line)
        sleep(0.5)
        self._update_screen()
        self._end_game()

    def _create_v_slash(self, x, y):
        """Create slash line."""
        line = VSlash(self)
        line_width, line_height = line.rect.size
        line.rect.x = x
        line.rect.y = y
        self.lines.add(line)
        sleep(0.5)
        self._update_screen()
        self._end_game()

    def _create_h_slash(self, x, y):
        """Create slash line."""
        line = HSlash(self)
        line_width, line_height = line.rect.size
        line.rect.x = x
        line.rect.y = y
        self.lines.add(line)
        sleep(0.5)
        self._update_screen()
        self._end_game()

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()
