from card import Card
from sprite_sheet import SpriteSheet
import random


class Deck:
    """A class representing a standard 52 playing card deck."""

    def __init__(self):
        self._cards = []

        # fill deck with cards
        self.create_deck()
        
    def create_deck(self):
        """Creates all cards and adds them to self._cards attribute."""

        cards_sprite_sheet = SpriteSheet('images/cards.png')
        width, height = 48, 64

        for suit in range(0, 4):
            x_coord = 0
            y_coord = height * suit

            for card_value in range(0, 13):
                sprite = cards_sprite_sheet.get_sprite(x_coord, y_coord, width, height, 2)
                card = Card(suit + 1, card_value + 1, sprite)

                # add card to list
                self._cards.append(card)

                # increment x coordinate by the width of a card
                x_coord += width