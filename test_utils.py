"""testing"""
import unittest
import pygame as pg
import utils
from tile import Tile
from button import Button


class TestUtils(unittest.TestCase):
    """Test cases for utils.py"""

    def setUp(self):
        """init pygame and font"""
        pg.init()

    def test_init_game(self):
        """Check caption has been set correctly"""
        utils.init_game()
        self.assertEqual(pg.display.get_caption()[0], utils.NAME)

    def test_init_game_2(self):
        """Check surface is returned"""
        surface = utils.init_game()
        self.assertIsInstance(surface, pg.Surface)

    def test_generate_tiles(self):
        """Test if list of appropriate length is returned """
        tile_list = utils.generate_tiles()
        self.assertEqual(len(tile_list), utils.TILE_COUNT)

    def test_generate_tiles_2(self):
        """Test if list contains Tile objects"""
        tile_list = utils.generate_tiles()
        self.assertIsInstance(tile_list[0], Tile)

    def test_generate_mine_sequence(self):
        """Test if a list of appropriate length is returned"""
        mine_list = utils.generate_mine_sequence(1)
        self.assertEqual(len(mine_list), utils.MINE_COUNT)

    def test_generate_mine_sequence_2(self):
        """Test if provided index is not included in sequence"""
        i = 1
        mine_list = utils.generate_mine_sequence(i)
        self.assertNotIn(i, mine_list)

    def test_game_over(self):
        """Test if font object created"""
        pg.font.init()
        font_surface = utils.game_over(True)
        self.assertIsInstance(font_surface, pg.Surface)

    def test_game_over_coordinates(self):
        """test if rect instance is returned"""
        pg.font.init()
        font = utils.FONT.render("test", True, utils.FONT_COLOUR)
        game_over_coords = utils.game_over_coords(font)
        self.assertIsInstance(game_over_coords, pg.Rect)

    def test_adjacent_bomb_count(self):
        """Test first case tile on left side"""
        index = 0
        adj_list = utils.adjacent_bomb_count(index)
        adj_list_2 = [
            index + x
            for x in utils.LEFT_ADJ_LIST
            if 0 <= index + x <= (utils.TILE_COUNT - 1)
        ]
        self.assertEqual(adj_list, adj_list_2)

    def test_adjacent_bomb_count_2(self):
        """Test second case, tile on the right side"""
        index = 9
        adj_list = utils.adjacent_bomb_count(index)
        adj_list_2 = [
            index + x
            for x in utils.RIGHT_ADJ_LIST
            if 0 <= index + x <= (utils.TILE_COUNT - 1)
        ]
        self.assertEqual(adj_list, adj_list_2)

    def test_adjacent_bomb_count_3(self):
        """Test third case, tile not on any side"""
        index = 17
        adj_list = utils.adjacent_bomb_count(index)
        adj_list_2 = [
            index + x
            for x in utils.ADJ_LIST
            if 0 <= index + x <= (utils.TILE_COUNT - 1)
        ]
        self.assertEqual(adj_list, adj_list_2)

    def test_generate_mine_text(self):
        """Test if font object created"""
        pg.font.init()
        font_surface = utils.generate_mine_text(1)
        self.assertIsInstance(font_surface, pg.Surface)

    def test_mine_count_text_coordinates(self):
        """Test if Rect instance is returned"""
        pg.font.init()
        font = utils.FONT.render("test", True, utils.FONT_COLOUR)
        mine_count_text_coords = utils.mine_count_coords(font, (10, 10))
        self.assertIsInstance(mine_count_text_coords, tuple)

    def test_mines_left_coordinates(self):
        """Test if coord tuple is returned"""
        pg.font.init()
        mines_coords = utils.mines_left_coords(1)
        self.assertIsInstance(mines_coords, tuple)

    def test_add_button(self):
        """Test if button object returned"""
        btn = utils.add_button()
        self.assertIsInstance(btn, Button)


if __name__ == "__main__":
    unittest.main()
