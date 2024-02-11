from mappable_sprite import MappableSprite
from card import Card
from sprite_sheet import SpriteSheet
import random


class Deck(MappableSprite):
    """A class representing a standard 52 playing card deck."""

    def __init__(self):
        # base width and height before scaling
        self._width = 48
        self._height = 64

        # scale multiplier for a deck
        self._scale = 2

        # set up the images first so it can be passed to the parent class initializer
        self._deck_sprites = {}
        self.init_deck_sprites()

        # get the image first and pass it to super
        super().__init__(self._deck_sprites["not empty"])

        # fill deck with cards
        self._cards = []
        self.create_deck()

    def get_scaled_width(self):
        """Returns the scaled width of the deck, which is the same as a card's width."""

        return self._width * self._scale
    
    def get_scaled_height(self):
        """Returns the scaled height of the deck, which is the same as a card's height."""

        return self._height * self._scale
    
    def get_top_card(self):
        """Returns the card on the top of the deck."""

        return self._cards[-1]
    
    def init_deck_sprites(self):
        """Set the sprites for an empty deck and a non-empty deck."""

        cards_sprite_sheet = SpriteSheet('images/cards.png')
        # set sprite for a card back
        card_back_sprite = cards_sprite_sheet.get_sprite(0, 256, self._width, self._height, self._scale)
        # set sprite for an empty deck
        empty_deck_sprite = cards_sprite_sheet.get_sprite(48, 256, self._width, self._height, self._scale)

        # populate the deck sprites dictionary
        self._deck_sprites["not empty"] = card_back_sprite
        self._deck_sprites["empty"] = empty_deck_sprite

    def toggle_sprite(self):
        """Switches the sprite from empty to full or from full to empty."""
        x, y = self.get_pos()

        if self._image == self._deck_sprites["not empty"]:
            self._image = self._deck_sprites["empty"]
        else:
            self._image = self._deck_sprites["not empty"]

        self._rect = self._image.get_rect()
        self.set_pos(x, y)
        
    def create_deck(self):
        """Creates all cards and adds them to the deck."""

        cards_sprite_sheet = SpriteSheet('images/cards.png')

        for suit in range(0, 4):
            x_coord = 0
            y_coord = self._height * suit

            for card_value in range(0, 13):
                sprite = cards_sprite_sheet.get_sprite(x_coord, y_coord, self._width, self._height, self._scale)
                card = Card(suit + 1, card_value + 1, sprite)

                # add card to list
                self.add_card(card)

                # increment x coordinate by the width of a card
                x_coord += self._width

    def draw_card(self):
        """Pops a card off the top of the deck."""

        card = self._cards.pop()

        # make sure new top card is set to moveable
        new_top_card = self.get_top_card()
        new_top_card.set_to_moveable()

        return card
    
    def add_card(self, card):
        """Adds a card to the top of the deck."""

        self._cards.append(card)
    
    def is_empty(self):
        """Returns True if the deck is empty, otherwise returns False."""

        return len(self._cards) == 0

    def shuffle(self):
        """Shuffles the deck."""

        random.shuffle(self._cards)
        # flag top card as moveable
        self._cards[-1].set_to_moveable()
