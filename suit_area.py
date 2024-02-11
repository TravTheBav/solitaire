from card_placement_area import CardPlacementArea


class SuitArea(CardPlacementArea):
    """A child class of CardPlacementArea. Represents an area where cards are stacked by suit from Ace to King.
    Once placed, cards cannot be removed from a suit area."""

    def __init__(self, border_type):
        super().__init__(border_type)

        # does not have an associated suit until a card is placed
        self._suit = None

        # current value starts at 1 (Ace) and gets incremented everytime a card is added
        self._current_value = 1

    def draw_card(self):
        """Overrides the draw card method from the parent class so that a card cannot be drawn once placed."""

        return
    
    

    