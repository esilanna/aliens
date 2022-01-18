import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, alien_game):
        """instantiate a ship and mark its starting position"""
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.screen_rect = alien_game.screen.get_rect()

        #load image
        self.image = pygame.image.load('aliens/images/ship.bmp')
        self.rect = self.image.get_rect()

        #starting position is at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal for the ship's x position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update the ships position based on moving (left and right) boolean"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
