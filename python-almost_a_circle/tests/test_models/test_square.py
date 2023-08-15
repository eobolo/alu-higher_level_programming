#!/usr/bin/python3
"""unittest for the models/square.py
"""

import unittest
from models.square import Square


class TesSquare(unittest.TestCase):
    """
    Our unittest class

    inheriting from the unittest.TestCase

    class.
    """
    def test_square_with_incomplete_correct_args(self):
        self.assertEqual(Square(1).id, 4)
        self.assertEqual(Square(1, 2).id, 5)
        self.assertEqual(Square(1, 2, 3).id, 6)
        
    def test_square_for_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_with_complete_correct_args(self):
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_square_for_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_string_display(self):
        self.assertEqual(Square(5).__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(Square(2, 2).__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(Square(3, 1, 3).__str__(), "[Square] (3) 1/3 - 3")
        self.assertEqual(Square(3, 1, 3, 6).__str__(), "[Square] (6) 1/3 - 3")
