import sys
import pygame
from settings import Settings
from ship import Ship

class Aliens: 
    """this class manages game behavior and assets """

    def __init__(self):
        """Initialize the game and create game resources """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        #Setting background color
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("aliens aliens aliens!")

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #watching for keyboard and mouse input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """update images on screen, flips to new screen"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        #displays the most recently drawn screen
        pygame.display.flip()

if __name__ == '__main__':
    #instantiate and run the game
    alien = Aliens()
    alien.run_game()
