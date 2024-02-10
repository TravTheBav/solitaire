class Settings:
    """A class for holding game settings."""

    def __init__(self):
        # screen dimensions
        self._screen_width = 800
        self._screen_height = 640
        # screen size
        self._screen_size = (self._screen_width, self._screen_height)
        # screen background color
        self._bg_color = (75, 105, 47, 255)

    def get_screen_width(self):
        """Returns the screen width."""

        return self._screen_width
    
    def get_screen_height(self):
        """Returns the screen height."""

        return self._screen_height

    def get_screen_size(self):
        """Returns the screen size as a tuple."""

        return self._screen_size
    
    def get_background_color(self):
        """Returns the screen's background color."""

        return self._bg_color