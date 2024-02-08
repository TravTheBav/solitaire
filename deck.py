from mappable_sprite import MappableSprite
from card import Card
from sprite_sheet import SpriteSheet


class Deck(MappableSprite):
    """A class representing a standard 52 playing card deck."""

    def __init__(self):
        # set up the images first so it can be passed to the parent class initializer
        self._deck_sprites = {}
        self.init_deck_sprites()

        # get the image first and pass it to super
        super().__init__(self._deck_sprites["not empty"])

        # fill deck with cards
        self._cards = []
        self.create_deck()
        
    def create_deck(self):
        """Creates all cards and adds them to the deck."""

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

    def init_deck_sprites(self):
        """Set the sprites for an empty deck and a non-empty deck."""

        # TO DO - NEED TO MAKE A SPRITE FOR AN EMPTY DECK AND MAKE SELF._IMAGE INTO A DICTIONARY
        cards_sprite_sheet = SpriteSheet('images/cards.png')

        # set sprite for a card back
        width, height = 48, 64
        card_back_sprite = cards_sprite_sheet.get_sprite(0, 256, width, height, 2)

        # set sprite for an empty deck
        empty_deck_sprite = cards_sprite_sheet.get_sprite(48, 256, width, height, 2)

        # populate the deck sprites dictionary
        self._deck_sprites["not empty"] = card_back_sprite
        self._deck_sprites["empty"] = empty_deck_sprite

        # set image to card back to start
        self._image = self._deck_sprites["not empty"]

    def draw_card(self):
        """Pops a card off the top of the deck."""

        return self._cards.pop()