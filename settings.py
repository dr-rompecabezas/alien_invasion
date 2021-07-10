class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200            # Default: 1200
        self.screen_height = 800            # Default: 800
        self.bg_color = (230, 230, 230)     # Default: (230, 230, 230)
        self.fullscreen = False             # Default: False

        # Ship settings
        self.ship_limit = 2                 # Default: 2

        # Bullet settings
        self.bullet_width = 3               # Default: 3
        self.bullet_height = 15             # Default: 15
        self.bullet_color = (60, 60, 60)    # Default: (60, 60, 60)
        self.bullets_allowed = 3            # Default: 3

        # Alien settings     
        self.fleet_drop_speed = 10          # Default: 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1            # Default: 1.1

        # How quickly the the alien points increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5               # Default: 1.5
        self.bullet_speed = 3.0             # Default: 3.0
        self.alien_speed = 1.0              # Default: 1.0
            
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1            # Default: 1

        # Scoring
        self.alien_points = 50              # Default: 50

    def increase_speed(self):
        """Increase speed settings and alien points."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
