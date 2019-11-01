"""Testing module for tile class"""
import unittest
import tile
from tile import Tile


class TestTile(unittest.TestCase):
    """test cases for tile.py"""

    def test_hovered(self):
        """Check if true if mouse pos inside tile pos"""
        test_tile = Tile(10, 10)
        hovered = test_tile.hovered(15, 15)
        self.assertEqual(hovered, True)

    def test_hovered_2(self):
        """Check if false if x mouse pos is inside but y outside tile pos"""
        test_tile = Tile(10, 10)
        hovered = test_tile.hovered(15, 150)
        self.assertEqual(hovered, False)

    def test_hovered_3(self):
        """Check if false if x mouse pos outside but y inside tile pos"""
        test_tile = Tile(10, 10)
        hovered = test_tile.hovered(150, 15)
        self.assertEqual(hovered, False)

    def test_hovered_4(self):
        """check if false if both mouse pos are outside tile pos"""
        test_tile = Tile(10, 10)
        hovered = test_tile.hovered(150, 150)
        self.assertEqual(hovered, False)

    def test_clicked(self):
        """Check if tile.is_clicked is set"""
        test_tile = Tile(10, 10)
        test_tile.clicked(1)
        self.assertEqual(test_tile.is_clicked, True)

    def test_clicked_2(self):
        """Check if tile is a mine, that the image is changed to mine"""
        test_tile = Tile(10, 10)
        test_tile.is_mine = True
        img = tile.MINE
        test_tile.clicked(1)
        self.assertEqual(test_tile.img, img)

    def test_clicked_3(self):
        """Check if mine_count is set correctly"""
        test_tile = Tile(10, 10)
        test_tile.clicked(1)
        self.assertEqual(test_tile.mine_count, 1)

    def test_right_clicked(self):
        """Check if is_flagged is set"""
        test_tile = Tile(10, 10)
        test_tile.right_clicked()
        self.assertEqual(test_tile.is_flagged, True)

    def test_right_clicked_2(self):
        """Check if image is set"""
        test_tile = Tile(10, 10)
        test_tile.right_clicked()
        img = tile.SAFE
        self.assertEqual(test_tile.img, img)

    def test_right_clicked_3(self):
        """Check flag is reversed"""
        test_tile = Tile(10, 10)
        test_tile.is_flagged = True
        test_tile.right_clicked()
        self.assertEqual(test_tile.is_flagged, False)

    def test_change_image(self):
        """Check if image is changed to HOVER"""
        test_tile = Tile(10, 10)
        test_tile.is_over = True
        test_tile.change_image()
        img = tile.HOVER
        self.assertEqual(test_tile.img, img)

    def test_change_image_2(self):
        """Check if image is changed to FRESH"""
        test_tile = Tile(10, 10)
        test_tile.change_image()
        img = tile.FRESH
        self.assertEqual(test_tile.img, img)

    def test_make_mine(self):
        """Check tile is_mine is set"""
        test_tile = Tile(10, 10)
        test_tile.make_mine()
        self.assertEqual(test_tile.is_mine, True)

    def test_make_mine_2(self):
        """Check if false if tile has not been made a mine"""
        test_tile = Tile(10, 10)
        self.assertEqual(test_tile.is_mine, False)


if __name__ == "__main__":
    unittest.main()
