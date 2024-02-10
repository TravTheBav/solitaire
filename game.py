import pygame as pg
from settings import Settings
from display import Display
from deck import Deck
from card_placement_area import CardPlacementArea


class Game:
    """A class for a game of standard solitaire. Controls the state of the game and coordinates the various
    classes necessary for a game of solitaire."""

    def __init__(self):
        self._settings = Settings()
        self._display_surface = None
        self._running = True
        self._clock = pg.time.Clock()

        # used for moving cards around
        self._card_dragging = False
        self._offset_x = None
        self._offset_y = None

        # holds a deck instance as well as other card areas
        self._deck = None
        self._available_cards = None

    def on_init(self):
        # initialize pygame, the display, the deck of cards, and set game state to running
        pg.init()
        self._display_surface = Display(self._settings.get_screen_size())
        self.setup_new_deck()
        self.setup_available_cards_area()
        self._running = True

    def setup_new_deck(self):
        """Makes a new deck object for the game."""

        self._deck = Deck()
        x, y = self._settings.get_screen_width() - (self._deck.get_scaled_width() + 10), 10
        self._deck.set_pos(x, y)
        self._deck.shuffle()

    def setup_available_cards_area(self):
        """Sets up the area where cards are placed when they are drawn from the deck."""

        self._available_cards = CardPlacementArea("dashed")
        x, y = self._settings.get_screen_width() - (self._deck.get_scaled_width() * 2 + 20), 10
        self._available_cards.set_pos(x, y)

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

        # Left mouse button
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            
            # When the deck is clicked, move a card from the deck into available cards area
            if self.check_deck_clicked(event.pos):
                self.deck_clicked()

        # Checks for the start of a 'card drag'
        #elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        #    if self._test_card.get_rect().collidepoint(event.pos):
        #        self._card_dragging = True
        #        mouse_x, mouse_y = event.pos
        #        self._offset_x = self._test_card.get_x() - mouse_x
        #        self._offset_y = self._test_card.get_y() - mouse_y

        # Stop card dragging
        #elif event.type == pg.MOUSEBUTTONUP:
        #    self._card_dragging = False

        # Update card position when dragged by the mouse
        #elif event.type == pg.MOUSEMOTION:
        #    if self._card_dragging:
        #        mouse_x, mouse_y = event.pos
        #        x = mouse_x + self._offset_x
        #        y = mouse_y + self._offset_y
        #        self._test_card.set_pos(x, y)

    def on_loop(self):
        pass

    def on_render(self):
        # fills background color
        self._display_surface.fill_background(self._settings.get_background_color())

        # display deck
        self._display_surface.draw(self._deck.get_image(), self._deck.get_pos())

        # display available cards; only need to draw the last card that was put down
        if not self._available_cards.is_empty():
            card = self._available_cards.get_last_card()
            x, y = self._available_cards.get_pos()
            self._display_surface.draw(card.get_image(), (x, y))

        # updates the screen
        self._display_surface.update()
        

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self._clock.tick(60)
        self.on_cleanup()

    def check_deck_clicked(self, event_pos):
        """Returns true if the deck was clicked, otherwise returns false."""

        if self._deck.get_rect().collidepoint(event_pos):
            return True
        
        return False

    def deck_clicked(self):
        """Handles the game logic for when the deck is clicked."""

        if self._deck.is_empty():
            # add all cards back to deck in the same order
            while not self._available_cards.is_empty():
                card = self._available_cards.draw_card()
                self._deck.add_card(card)

            # toggle the deck image to indicate it has cards
            self._deck.toggle_sprite()

        else:
            # draw a card from the deck
            card = self._deck.draw_card()
                
            # update that cards position to the available cards area position and add card to available cards
            x, y = self._available_cards.get_pos()
            card.set_pos(x, y)
            self._available_cards.add_card(card)

            # if the last card has been drawn, then the sprite for the deck must be updated to reflect its empty state
            if self._deck.is_empty():
                self._deck.toggle_sprite()
        

if __name__ == "__main__":
    solitaireGame = Game()
    solitaireGame.on_execute()