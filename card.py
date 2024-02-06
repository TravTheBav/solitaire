import pygame as pg


class Card(pg.sprite.Sprite):
    """Represents a standard playing card."""

    def __init__(self, x_coord, y_coord, image):
        pg.sprite.Sprite.__init__(self)

        self._image = image
        self._rect = self._image.get_rect()
        self._rect.x = x_coord
        self._rect.y = y_coord

    def get_image(self):
        """Returns a scaled image of the card."""
        return self._image

    def get_rect(self):
        """Returns the rectangle attribute."""
        return self._rect

    def get_x(self):
        """Returns the x coordinate."""
        return self._rect.x

    def get_y(self):
        """Returns the y coordinate."""
        return self._rect.y

    def get_pos(self):
        """Returns a tuple in the form (x-coordinate, y-coordinate)."""
        return self._rect.x, self._rect.y

    def set_pos(self, x, y):
        """Sets the card's coordinates."""
        self._rect.x = x
        self._rect.y = y
