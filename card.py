from mappable_sprite import MappableSprite


class Card(MappableSprite):
    """Represents a standard playing card."""

    def __init__(self, suit, value, image):
        super().__init__(image)

        self._visible = False
        self._suit = suit
        self._value = value

        # flag for enabling/preventing card movement
        self._moveable = False
    
    def __repr__(self):
        """Formats card data into a human readable string for console output purposes."""

        suits = {
            1: "Clubs",
            2: "Spades",
            3: "Diamonds",
            4: "Hearts"
        }
        values = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        return f"{values[self._value]} of {suits[self._suit]}"
