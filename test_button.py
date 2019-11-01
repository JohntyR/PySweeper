"""Testing module for button class"""
import unittest

# import button
from button import Button


class TestButton(unittest.TestCase):
    """Test cases for button.py"""

    def test_hovered(self):
        """Check if true if mouse pos inside button pos"""
        test_btn = Button(10, 10)
        hovered = test_btn.hovered(20, 20)
        self.assertEqual(hovered, True)

    def test_hovered_2(self):
        """Check if false if x mouse pos is inside but y outside tile pos"""
        test_btn = Button(10, 10)
        hovered = test_btn.hovered(15, 150)
        self.assertEqual(hovered, False)

    def test_hovered_3(self):
        """Check if false if x mouse pos outside but y inside tile pos"""
        test_btn = Button(10, 10)
        hovered = test_btn.hovered(150, 15)
        self.assertEqual(hovered, False)

    def test_hovered_4(self):
        """check if false if both mouse pos are outside tile pos"""
        test_btn = Button(10, 10)
        hovered = test_btn.hovered(150, 150)
        self.assertEqual(hovered, False)

    def test_clicked(self):
        """check if property changed correctly"""
        test_btn = Button(10, 10)
        test_btn.clicked()
        self.assertEqual(test_btn.is_clicked, True)


if __name__ == "__main__":
    unittest.main()
