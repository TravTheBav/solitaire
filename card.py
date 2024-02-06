import pygame as pg


class Card(pg.sprite.Sprite):
    """Represents a standard playing card."""

    def __init__(self, suit, value, image):
        pg.sprite.Sprite.__init__(self)

        self._image = image
        self._suit = suit
        self._value = value
        self._rect = self._image.get_rect()
        self._x_coord = None
        self._y_coord = None

    def get_image(self):
        """Returns a scaled image of the card."""
        return self._image

    def get_rect(self):
        """Returns the rectangle attribute."""
        return self._rect

    def get_x(self):
        """Returns the x coordinate."""
        return self._x_coord

    def get_y(self):
        """Returns the y coordinate."""
        return self._y_coord

    def get_pos(self):
        """Returns a tuple in the form (x-coordinate, y-coordinate)."""
        return self._x_coord, self._y_coord

    def set_pos(self, x, y):
        """Sets the card's coordinates."""
        self._x_coord = x
        self._y_coord = y
