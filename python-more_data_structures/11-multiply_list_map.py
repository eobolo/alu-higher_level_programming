#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    copy_list = list(my_list)
    new_list = list(map(lambda x: x * number, copy_list))
    return new_list
