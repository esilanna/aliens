class Stats:
    """track the game's stats"""

    def __init__(self, alien_game):
        """initalize stats"""
        self.settings = alien_game.settings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        """initalize the stats that change in the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0