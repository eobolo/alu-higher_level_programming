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
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(89)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 89)


if __name__ == '__main__':
    unittest.main()
