"""Class for buttons"""
import pygame as pg


RESTART = pg.image.load("Assets\\restart.png")

BUTTON_WIDTH = RESTART.get_width()
BUTTON_HEIGHT = RESTART.get_height()
BUTTON_BUFFER = BUTTON_WIDTH // 10


class Button:
    """Button class"""

    def __init__(self, x_pos, y_pos):
        """init"""
        self.x_pos = x_pos
        self.x_upper = x_pos + BUTTON_WIDTH
        self.y_pos = y_pos
        self.y_upper = y_pos + BUTTON_HEIGHT

        self.img = RESTART
        self.is_over = False
        self.is_clicked = True

    def hovered(self, x_mouse, y_mouse):
        """check if mouse is currently hovering over self"""
        return (
            self.x_pos + BUTTON_BUFFER <= x_mouse <= self.x_upper - BUTTON_BUFFER
        ) and (self.y_pos + BUTTON_BUFFER <= y_mouse <= self.y_upper - BUTTON_BUFFER)

    def clicked(self):
        """do stuff if clicked"""
        self.is_clicked = True
