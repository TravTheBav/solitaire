import pygame as pg
from card import Card


class App:
    def __init__(self):
        self._running = True
        self._display_surface = None
        self._bg_color = 'green'
        self._width = 800
        self._height = 640
        self._size = self._width, self._height
        self._clock = pg.time.Clock()
        self._card_dragging = False
        self._offset_x = None
        self._offset_y = None

    def on_init(self):
        pg.init()
        self._display_surface = pg.display.set_mode(self._size)
        self._running = True
        self._test_card = Card(100, 125, 0, 0)

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

        # Checks for the start of a 'card drag'
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self._test_card.get_rect().collidepoint(event.pos):
                self._card_dragging = True
                mouse_x, mouse_y = event.pos
                self._offset_x = self._test_card.get_x() - mouse_x
                self._offset_y = self._test_card.get_y() - mouse_y

        # Stop card dragging
        elif event.type == pg.MOUSEBUTTONUP:
            self._card_dragging = False

        # Update card position when dragged by the mouse
        elif event.type == pg.MOUSEMOTION:
            if self._card_dragging:
                mouse_x, mouse_y = event.pos
                x = mouse_x + self._offset_x
                y = mouse_y + self._offset_y
                self._test_card.set_pos(x, y)

    def on_loop(self):
        pass

    def on_render(self):
        # fills background color
        self._display_surface.fill(self._bg_color)

        # draws one card to the screen, for testing purposes
        self._display_surface.blit(self._test_card.get_scaled_image(), self._test_card.get_pos())

        # updates the screen
        pg.display.flip()

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
    theApp = App()
    theApp.on_execute()