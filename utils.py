"""Utility function module"""
import random
import pygame as pg
from tile import Tile
from button import Button

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360
DIFFICULTY = (10, 10)
TILE_COUNT = DIFFICULTY[0] * DIFFICULTY[1]
MINE_COUNT = (TILE_COUNT) // 5
NAME = "PySweeper"
ICON = "Assets\\MineIcon.png"
LEFT_ADJ_LIST = [-10, -9, 1, 10, 11]
RIGHT_ADJ_LIST = [-11, -10, -1, 9, 10]
ADJ_LIST = [-11, -10, -9, -1, 1, 9, 10, 11]

BUTTON_X_POS = 400
BUTTON_Y_POS = 100

pg.font.init()

# set fonts
FONT = pg.font.SysFont("TAHOMA", 12)
FONT_COLOUR = (255, 255, 255)
GAME_OVER_FONT = pg.font.SysFont("TAHOMA", 36)
GAME_OVER_FONT_COLOUR = (255, 0, 0)


def init_game():
    """start up neccessary pg items and return a screen."""
    # load program logo image
    logo = pg.image.load(ICON)

    # init display settings
    pg.display.set_icon(logo)
    pg.display.set_caption(NAME)

    return pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def generate_tiles():
    """create tiles according to chosen difficulty"""
    tile_set = []
    for i in range(DIFFICULTY[0]):
        for j in range(DIFFICULTY[1]):
            tile_set.append(Tile(j * 32, i * 32))
    return tile_set


def generate_mine_sequence():
    """generate random list of unique integers for mines"""
    return random.sample(range(TILE_COUNT), (MINE_COUNT))


def game_over(lost):
    """Display text that game is finished"""
    if lost:
        text = "GAME OVER!"
    else:
        text = "YOU WON!"

    return GAME_OVER_FONT.render(text, True, GAME_OVER_FONT_COLOUR)


def game_over_coords(font):
    """return coords to position game over text"""
    return font.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


def adjacent_bomb_count(tile_i):
    """Calculate the number of bombs in the adjacent indexes of specified tile"""
    if tile_i == 0 or tile_i % 10 == 0:
        adjacent_tiles = LEFT_ADJ_LIST
    elif tile_i % 10 == 9:
        adjacent_tiles = RIGHT_ADJ_LIST
    else:
        adjacent_tiles = ADJ_LIST

    new_adjacent_tiles = [
        tile_i + x for x in adjacent_tiles if 0 <= tile_i + x <= (TILE_COUNT - 1)
    ]

    return new_adjacent_tiles


def generate_mine_text(mines):
    """create new surface with text"""
    if mines == 0:
        mines = ""
    return FONT.render(f"{mines}", True, FONT_COLOUR)


def mine_count_coords(font, tile_mids):
    """returns co-ordinates needed to fit text in bottom corner"""
    font_obj = font.get_rect(center=(tile_mids[0], tile_mids[1]))
    return (font_obj[0], font_obj[1])


def mines_left_coords(mines_left):
    """returns co-ordinates needed to fit text in bottom corner"""
    return (
        (WINDOW_WIDTH - FONT.size(f"{mines_left}")[0]) - 5,
        (5 + FONT.size(f"{mines_left}")[1]),
    )


def add_button():
    """add button to screen"""
    return Button(BUTTON_X_POS, BUTTON_Y_POS)
