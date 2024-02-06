import pygame as pg


class Card(pg.sprite.Sprite):
    """Represents a standard playing card."""

    def __init__(self, x_coord, y_coord):
        pg.sprite.Sprite.__init__(self)

        # CURRENTLY IMAGE IS JUST CARDS.PNG; THIS WILL NEED TO CHANGE TO BY DYNAMICALLY GENERATED
        self._image = pg.image.load('cards.png').convert()
        self._scaled_image = pg.transform.scale(self._image, (111, 148))
        self._rect = self._scaled_image.get_rect()
        self._rect.x = x_coord
        self._rect.y = y_coord

    def get_scaled_image(self):
        """Returns a scaled image of the card."""
        return self._scaled_image

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
