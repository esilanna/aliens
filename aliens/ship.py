import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, alien_game):
        """instantiate a ship and mark its starting position"""
        self.screen = alien_game.screen
        self.screen_rect = alien_game.screen.get_rect()

        #load image
        self.image = pygame.image.load('aliens/images/ship.bmp')
        self.rect = self.image.get_rect()

        #starting position is at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update the ships position based on moving (left and right) boolean"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
            
    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)
