"""module for tile class for game tile"""
import pygame as pg

FRESH = pg.image.load("Assets\\Tile.png")
HOVER = pg.image.load("Assets\\TileHover.png")
SAFE = pg.image.load("Assets\\acorn.png")
MINE = pg.image.load("Assets\\grenade.png")

TILE_WIDTH = FRESH.get_width()
TILE_HEIGHT = FRESH.get_height()
TILE_BUFFER = TILE_WIDTH // 10


class Tile:
    """class for game tile"""

    def __init__(self, x_pos, y_pos):
        self.img = FRESH

        self.x_pos = x_pos
        self.x_upper = x_pos + TILE_WIDTH
        self.y_pos = y_pos
        self.y_upper = y_pos + TILE_HEIGHT
        self.text_mid_point = [
            self.x_pos + (TILE_WIDTH / 2),
            self.y_pos + (TILE_HEIGHT / 2),
        ]

        self.is_mine = False
        self.is_flagged = False
        self.mine_count = 0
        self.is_clicked = False
        self.is_over = False

    def hovered(self, x_mouse, y_mouse):
        """check if mouse is currently hovering over self"""
        return (self.x_pos + TILE_BUFFER <= x_mouse <= self.x_upper - TILE_BUFFER) and (
            self.y_pos + TILE_BUFFER <= y_mouse <= self.y_upper - TILE_BUFFER
        )

    def clicked(self, mine_count):
        """change the img if the tile has been clicked"""
        self.is_clicked = True

        if self.is_mine:
            self.img = MINE
        else:
            self.mine_count = mine_count

    def right_clicked(self):
        """change the image if the tile has been right clicked"""
        self.is_flagged = True
        self.img = SAFE

    def change_image(self):
        """change to the hover img"""
        if self.is_over:
            self.img = HOVER
        else:
            self.img = FRESH

    def make_mine(self):
        """set tile as mine"""
        self.is_mine = True
