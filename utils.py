"""Utility function module"""
import random
import pygame as pg
from tile import Tile

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360
FONT_COLOUR = (255, 255, 255)
DIFFICULTY = (10, 10)
TILE_COUNT = DIFFICULTY[0] * DIFFICULTY[1]
MINE_COUNT = (TILE_COUNT) // 5
NAME = "PySweeper"
ICON = "Assets\\MineIcon.png"

pg.font.init()

# set font
FONT = pg.font.SysFont("TAHOMA", 12)
GAME_OVER_FONT = pg.font.SysFont("TAHOMA", 36)


def initialise_game():
    """start up neccessary pg items"""

    # load program logo image
    logo = pg.image.load(ICON)

    # init display settings
    pg.display.set_icon(logo)
    pg.display.set_caption(NAME)


def create_screen():
    """uses window width and height constants to create a surface"""
    return pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def return_mine_count():
    """number of starting mines"""
    return MINE_COUNT


def generate_text(x_pos, y_pos):
    """creates new surface with text stating the current co-ords"""
    return FONT.render(f"x: {x_pos} y: {y_pos}", True, FONT_COLOUR)


def current_coordinates(x_pos, y_pos):
    """returns co-ordinates needed to fit text in bottom corner"""
    return (
        (WINDOW_WIDTH - FONT.size(f"x: {x_pos} y: {y_pos}")[0]) - 5,
        (WINDOW_HEIGHT - FONT.size(f"x: {x_pos} y: {y_pos}")[1]) - 5,
    )


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


def game_over():
    """Display text that game is finished"""
    return GAME_OVER_FONT.render("GAME OVER", True, (255, 0, 0))


def game_over_coordinates(font):
    """return coords to position game over text"""
    return font.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


def adjacent_bomb_count(tile_i):
    """Calculate the number of bombs in the adjacent indexes of specified tile"""
    if tile_i == 0 or tile_i % 10 == 0:
        adjacent_tiles = [-10, -9, 1, 10, 11]
    elif tile_i % 10 == 9:
        adjacent_tiles = [-11, -10, -1, 9, 10]
    else:
        adjacent_tiles = [-11, -10, -9, -1, 1, 9, 10, 11]

    new_adjacent_tiles = [tile_i + x for x in adjacent_tiles if 0 <= tile_i + x <= 99]

    return new_adjacent_tiles


def generate_mine_count_text(mine_count):
    """creates new surface with text stating the number of mines"""
    if mine_count == 0:
        mine_count = ""
    return FONT.render(f"{mine_count}", True, FONT_COLOUR)


def mine_count_text_coordinates(font, tile_mids):
    """returns co-ordinates needed to fit text in bottom corner"""
    return font.get_rect(center=(tile_mids[0], tile_mids[1]))


def generate_mines_left_text(mines_left):
    """creates new surface with text stating the current co-ords"""
    return FONT.render(f"{mines_left}", True, FONT_COLOUR)


def mines_left_coordinates(mines_left):
    """returns co-ordinates needed to fit text in bottom corner"""
    return (
        (WINDOW_WIDTH - FONT.size(f"{mines_left}")[0]) - 5,
        (5 + FONT.size(f"{mines_left}")[1]),
    )
