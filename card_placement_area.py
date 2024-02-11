from mappable_sprite import MappableSprite
from sprite_sheet import SpriteSheet


class CardPlacementArea(MappableSprite):
    """Represents an area where cards can be placed."""

    def __init__(self, border_type):
        """Takes in a string border_type which determines which sprite is used. Valid strings for border types are
        'dashed' or 'solid'."""

        # base width and height before scaling
        self._width = 48
        self._height = 64

        # scale multiplier for a card area
        self._scale = 2

        # takes the border_type and creates an image to be passed to the parent class init method
        self.on_init(border_type)

        # starts out empty
        self._cards = []

    def on_init(self, border_type):
        """Sets the image depending on the passed in border_type and passes it to super()."""

        cards_sprite_sheet = SpriteSheet('images/cards.png')

        if border_type == "dashed":
            image = cards_sprite_sheet.get_sprite(48, 256, self._width, self._height, self._scale)
        elif border_type == "solid":
            image = cards_sprite_sheet.get_sprite(96, 256, self._width, self._height, self._scale)

        super().__init__(image)

    def get_cards(self):
        """Returns the current cards in the card area."""

        return self._cards
    
    def get_last_card(self):
        """Return the top card on the stack."""

        if not self.is_empty():
            return self._cards[-1]
        else:
            return False
    
    def add_card(self, card):
        """Add a card onto the top of the stack."""

        self._cards.append(card)

    def draw_card(self):
        """Pop a card from the top of the stack and return it."""
    
        return self._cards.pop()
    
    def is_empty(self):
        """Returns true if there are no available cards, otherwise returns false."""

        if self._cards:
            return False
        
        return True