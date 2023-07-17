#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as err_message:
        print("Exception: {}".format(err_message), file=sys.stderr)
        return None
