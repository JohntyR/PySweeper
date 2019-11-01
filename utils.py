"""Utility function module"""
import random
import pygame as pg
import tile
from tile import Tile
import button
from button import Button

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 400
DIFFICULTY = (10, 10)
TILE_COUNT = DIFFICULTY[0] * DIFFICULTY[1]
SIDE_GAP = (WINDOW_WIDTH - (DIFFICULTY[0] * tile.TILE_WIDTH)) // 2
BOTTOM_GAP = WINDOW_HEIGHT - (DIFFICULTY[1] * tile.TILE_HEIGHT)

MINE_COUNT = (TILE_COUNT) // 5
NAME = "PySweeper"
ICON = "Assets\\MineIcon.png"
LEFT_ADJ_LIST = [-10, -9, 1, 10, 11]
RIGHT_ADJ_LIST = [-11, -10, -1, 9, 10]
ADJ_LIST = [-11, -10, -9, -1, 1, 9, 10, 11]

BUTTON_X_POS = (WINDOW_WIDTH - button.BUTTON_WIDTH) // 2
BUTTON_Y_POS = WINDOW_HEIGHT - button.BUTTON_HEIGHT - 5

BACKGROUND_COLOUR = (85, 65, 95)
BACKGROUND_COLOUR_TILE = (0, 0, 0)

# set fonts
pg.font.init()
FONT = pg.font.SysFont("TAHOMA", 12)
FONT_COLOUR = (255, 255, 255)
GAME_OVER_FONT = pg.font.SysFont("TAHOMA", 36)
GAME_OVER_FONT_COLOUR = (255, 0, 0)
MINE_FONT_COLOURS = [
    (220, 245, 255),
    (230, 200, 110),
    (100, 185, 100),
    (80, 140, 215),
    (215, 115, 85),
    (85, 65, 95),
    (100, 105, 100),
    (0, 0, 0),
]


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
            tile_set.append(
                Tile(SIDE_GAP + (j * tile.TILE_WIDTH), i * tile.TILE_HEIGHT)
            )
    return tile_set


def generate_mine_sequence(i):
    """generate random list of unique integers for mines that doesnt include passed in number"""
    while True:
        mine_seq = random.sample(range(TILE_COUNT), (MINE_COUNT))
        if i not in mine_seq:
            break
    return mine_seq


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


def generate_mine_counter_text(mines):
    """Create new surface with count"""
    return FONT.render(f"{mines}", True, FONT_COLOUR)


def generate_mine_text(mines):
    """create new surface with text"""
    if mines == 0:
        return FONT.render("", True, FONT_COLOUR)

    return FONT.render(f"{mines}", True, MINE_FONT_COLOURS[mines])


def mine_count_coords(font, tile_mids):
    """returns co-ordinates needed to fit text in bottom corner"""
    font_obj = font.get_rect(center=(tile_mids[0], tile_mids[1]))
    return (font_obj[0], font_obj[1])


def mines_left_coords(mines_left):
    """returns co-ordinates needed to fit text in bottom corner"""
    x_pos = WINDOW_WIDTH - SIDE_GAP - FONT.size(f"{mines_left}")[0] - 5
    y_pos = (
        DIFFICULTY[1] * tile.TILE_HEIGHT
        + (BOTTOM_GAP - FONT.size(f"{mines_left}")[1]) // 2
    )
    return (x_pos, y_pos)


def add_button():
    """add button to screen"""

    return Button(BUTTON_X_POS, BUTTON_Y_POS)


def draw_tile_background(screen):
    """draw rectangle behind tiles"""
    return pg.draw.rect(
        screen,
        BACKGROUND_COLOUR_TILE,
        (SIDE_GAP, 0, (WINDOW_WIDTH - (SIDE_GAP * 2)), (WINDOW_HEIGHT - SIDE_GAP)),
    )
