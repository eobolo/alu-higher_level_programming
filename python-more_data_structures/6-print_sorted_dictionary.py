#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    for key, value in sorted(a_dictionary.items()):
        print("{0:s}: {1}".format(key, value), end="\n")
    return 0
