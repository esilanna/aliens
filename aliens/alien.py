from cmath import rect
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien"""

    def __init__(self, alien_game):
        """initalize the alien and its pos"""
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings

        #this is the alien image
        self.image = pygame.image.load('aliens/images/alien.bmp')
        self.rect = self.image.get_rect()

        #starting each alien in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing an alien's x pos
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """returns true if alien reaches edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move alien to right/left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x