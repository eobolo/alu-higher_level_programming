#!/usr/bin/python3
"""unittest for the models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Our unittest class

    inheriting from the unittest.TestCase

    class.
    """

    def test_rectangle_with_incomplete_correct_args(self):
        self.assertEqual(Rectangle(1, 2).id, 9)
        self.assertEqual(Rectangle(1, 2, 3).id, 10)
        self.assertEqual(Rectangle(1, 2, 3, 4).id, 11)
        self.assertEqual(Rectangle(1, 2, -3).id, 12)
        self.assertEqual(Rectangle(1, 2, 3, -4).id, 13)

    def test_rectangle_for_type_error(self):
        self.assertEqual(Rectangle("1", 2).width, None)
        self.assertEqual(Rectangle(1, "2").height, None)
        self.assertEqual(Rectangle(1, 2, "3").x, None)
        self.assertEqual(Rectangle(1, 2, 3, "4").y, None)

    def test_reactangle_with_complete_correct_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_rectangle_for_value_error(self):
        self.assertEqual(Rectangle(-1, 2).width, None)
        self.assertEqual(Rectangle(1, -2).height, None)
        self.assertEqual(Rectangle(0, 2).width, None)
        self.assertEqual(Rectangle(1, 0).height, None)
