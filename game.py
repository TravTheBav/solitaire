import pygame as pg
from settings import Settings
from display import Display
from deck import Deck


class Game:
    """A class for a game of standard solitaire. Controls the state of the game and coordinates the various
    classes necessary for a game of solitaire."""

    def __init__(self):
        self._settings = Settings()
        self._display_surface = None
        self._running = True
        self._clock = pg.time.Clock()
        self._card_dragging = False
        self._offset_x = None
        self._offset_y = None
        self._deck = None

    def on_init(self):
        # initialize pygame, the display, the deck of cards, and set game state to running
        pg.init()
        self._display_surface = Display(self._settings.get_screen_size())
        self._deck = Deck()
        self._running = True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

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


if __name__ == "__main__":
    solitaireGame = Game()
    solitaireGame.on_execute()