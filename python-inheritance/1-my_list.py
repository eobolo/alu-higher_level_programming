#!/usr/bin/python3
# 1-my_list.py
"""This is a python module
that inherits from th built-in
class List and creates a sorted
function to sort the list not
in-place
"""


class MyList(list):
    """This is my class
    MyList that inherits from
    the built in class list
    an creates a sorted function
    """
    # An initialization method of an empty list is done by the parent class
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """This is the sorted function
        that sorts the the the instance
        of the list mylist which inherits
        the abilities of the class list
        and the method .sort() and sorts
        the instance not in place
        """
        print(sorted(self))
