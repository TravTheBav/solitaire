import pygame as pg


class Display:
    """A class for managing the display."""

    def __init__(self, screen_size):
        # A tuple in the form (width, height)
        self._screen_size = screen_size
        self._surface = pg.display.set_mode(self._screen_size)

    def fill_background(self, color):
        """Fills in the display surface with the given color."""

        self._surface.fill(color)

    def draw(self, image, position):
        """Takes in an image and a position and draws the image onto the screen at that position."""

        self._surface.blit(image, position)

    def update(self):
        """Update the screen."""

        pg.display.flip()