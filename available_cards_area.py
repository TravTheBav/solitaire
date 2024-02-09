import pygame as pg


class AvailableCardsArea(pg.Rect):
    """Represents the area where cards drawn from the deck are put for the player to select from."""

    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

        # starts out empty
        self._cards = []

    def get_cards(self):
        """Returns the current cards in the card area."""

        return self._cards
    
    def get_last_card(self):
        """Return the top card on the stack."""

        return self._cards[-1]
    
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