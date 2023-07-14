#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return 1
    elif idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        c = list(my_list)
        c[idx] = element
    return c
