#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    key_name = ""
    largest_value_so_far = -10
    for key in a_dictionary.keys():
        if a_dictionary.get(key) > largest_value_so_far:
            largest_value_so_far = a_dictionary.get(key)
            key_name = key
        else:
            continue
    return key_name
