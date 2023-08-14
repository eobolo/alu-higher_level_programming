#!/usr/bin/python3
"""
This is the testfile

for the module base.py

in the models/ directory
"""


import unittest
from models.base import Base


# test_object1 = Base()
# test_object2 = Base()
# test_object3 = Base(89)


class TestBase(unittest.TestCase):
    """
    This is the unittest class

    for the base.py class

    in the models directory
    """
    def test_base_with_or_without_args(self):
        """
        This test for the instance

        of the Base class without

        arguement to see if the id are

        given consecutively after initialization
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(89).id, 89)
