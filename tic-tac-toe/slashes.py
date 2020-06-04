import pygame
from pygame.sprite import Sprite

class Slash(Sprite):
    """Slash line"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the slash image and set its rec attribure
        self.image = pygame.image.load('images/slash.png')
        self.rect = self.image.get_rect()

        # Starts slash in top left ot the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store slash exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class BSlash(Sprite):
    """Slash line"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the slash image and set its rec attribure
        self.image = pygame.image.load('images/b_slash.png')
        self.rect = self.image.get_rect()

        # Starts slash in top left ot the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store slash exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class HSlash(Sprite):
    """Slash line"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the slash image and set its rec attribure
        self.image = pygame.image.load('images/hor.png')
        self.rect = self.image.get_rect()

        # Starts slash in top left ot the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store slash exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class VSlash(Sprite):
    """Slash line"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the slash image and set its rec attribure
        self.image = pygame.image.load('images/ver.png')
        self.rect = self.image.get_rect()

        # Starts slash in top left ot the screen.
        self.rect.x = 0
        self.rect.y = 0

        # Store slash exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
