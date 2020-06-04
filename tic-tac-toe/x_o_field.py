import pygame
from pygame.sprite import Sprite

class Field(Sprite):
    """Blank field"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the empty field image and set its rec attribute.
        self.image = pygame.image.load('images/blank.png')
        self.rect = self.image.get_rect()

        # Start each new field near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store sign exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.marker = 0
        self.value = '0'

        self.flipped = False

class XField(Sprite):
    """X-mark field"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the X field image and set its rec attribute.
        self.image = pygame.image.load('images/x_sign.png')
        self.rect = self.image.get_rect()

        # Start each new field near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store sign exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.marker = 0
        self.value = '1'

        self.flipped = True

class OField(Sprite):
    """O-mark field"""
    def __init__(self, ttt_game):
        super().__init__()
        self.screen = ttt_game.screen

        # Load the O field image and set its rec attribute.
        self.image = pygame.image.load('images/o_sign.png')
        self.rect = self.image.get_rect()

        # Start each new field near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store sign exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.marker = 0
        self.value = '2'

        self.flipped = True
