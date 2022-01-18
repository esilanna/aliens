import sys
import pygame
from settings import Settings

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
        pygame.display.set_caption("Aliens!")
    def run_game(self):
        """Starting the main loop"""
        while True:
            #watching for keyboard and mouse input.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            #displays the most recently drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    #instantiate and run the game
    alien = Aliens()
    alien.run_game()
