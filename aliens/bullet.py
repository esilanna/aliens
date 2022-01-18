import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""

    def __init__(self, alien_game):
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.color = self.settings.bullet_color

        #make a bullet rect then set the correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = alien_game.ship.rect.midtop

        #store the bullet's pos as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        #update the pos of the bullet
        self.y -= self.settings.bullet_speed
        #update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the scereen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
