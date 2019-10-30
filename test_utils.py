"""testing"""
import unittest
import pygame as pg
import utils


class TestUtils(unittest.TestCase):
    """Test cases for Utils.py"""

    def setUp(self):
        """init pygame and font"""
        pg.init()

    def tearDown(self):
        """quit the initiated pygame"""
        # pg.quit()

    def test_initialise_game(self):
        """Check caption has been set correctly"""
        utils.initialise_game()
        self.assertEqual(pg.display.get_caption()[0], utils.NAME)

    def test_create_screen(self):
        """Check if screen has been created"""
        utils.create_screen()
        self.assertIsNotNone(pg.display.get_surface())

    def test_return_mine_count(self):
        """Test if mine count is correct"""
        mine_count = utils.return_mine_count()
        self.assertEqual(mine_count, utils.MINE_COUNT)

    def test_generate_text(self):
        """Test if font object is created"""
        pg.font.init()
        font_surface = utils.generate_text(100, 200)
        self.assertIsInstance(font_surface, pg.Surface)

    # def test_current_coordinates(self):
    #     """test if tuple of coords is created"""

    def test_generate_tiles(self):
        """test if list of appropriate length is returned """
        tile_list = utils.generate_tiles()
        self.assertEqual(len(tile_list), utils.TILE_COUNT)

    def test_generate_mine_sequence(self):
        """test if a list of appropriate length is returned"""
        mine_list = utils.generate_mine_sequence()
        self.assertEqual(len(mine_list), utils.MINE_COUNT)

    def test_game_over(self):
        """Test if font object created"""
        pg.font.init()
        font_surface = utils.game_over()
        self.assertIsInstance(font_surface, pg.Surface)

    def test_game_over_coordinates(self):
        """test if rect instance is returned"""
        pg.font.init()
        font = utils.FONT.render("test", True, utils.FONT_COLOUR)
        game_over_coords = utils.game_over_coordinates(font)
        self.assertIsInstance(game_over_coords, pg.Rect)

    # def test_adjacent_bomb_count(self):
    #     """Test first case"""

    def test_generate_mine_count_text(self):
        """Test if font object created"""
        pg.font.init()
        font_surface = utils.generate_mine_count_text(1)
        self.assertIsInstance(font_surface, pg.Surface)

    def test_mine_count_text_coordinates(self):
        """Test if Rect instance is returned"""
        pg.font.init()
        font = utils.FONT.render("test", True, utils.FONT_COLOUR)
        mine_count_text_coords = utils.mine_count_text_coordinates(font, (10, 10))
        self.assertIsInstance(mine_count_text_coords, pg.Rect)

    def test_generate_mines_left_text(self):
        """Test if font object created"""
        pg.font.init()
        font_surface = utils.generate_mines_left_text(1)
        self.assertIsInstance(font_surface, pg.Surface)

    # def test_mines_left_coordinates(self):
    #     """Test if coord tuple is returned"""


if __name__ == "__main__":
    unittest.main()
