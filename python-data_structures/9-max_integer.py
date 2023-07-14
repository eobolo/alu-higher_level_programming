#!/usr/bin/python3
def max_integer(my_list=[]):
    # let maximum be first set to an negative number specifically
    # since we want to find the maximum of a list
    # we don't want a value for maximum to be larger than max in a list
    maximum = -10
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if maximum > i:
                continue
            maximum = i
        return maximum
