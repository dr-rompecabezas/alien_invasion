class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset.
        self.read_all_time_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_all_time_high_score(self):
        """Read all-time high score from text file."""
        file_path = 'stats/highest_score.txt'
        try:
            with open(file_path) as file_object:
                self.high_score = int(file_object.read())
        except FileNotFoundError:
            self.high_score = 0
    
    def save_high_score(self):
        """Write current high score to text file."""
        file_path = 'stats/highest_score.txt'
        with open(file_path, 'w') as file_object:
            file_object.write(str(self.high_score))
