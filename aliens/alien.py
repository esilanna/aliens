import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien"""

    def __init__(self, alien_game):
        """initalize the alien and its pos"""
        super().__init__()
        self.screen = alien_game.screen

        #this is the alien image
        self.image = pygame.image.load('aliens/images/alien.bmp')
        self.rect = self.image.get_rect()

        #starting each alien in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing an alien's x pos
        self.x = float(self.rect.x)