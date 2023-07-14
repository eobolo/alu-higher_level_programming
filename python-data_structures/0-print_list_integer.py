#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("An empty list of length {0:d} \
                was given.".format(len(my_list)))
        return 1
    for i in my_list:
        print("{0:d}".format(i))
    return 0
