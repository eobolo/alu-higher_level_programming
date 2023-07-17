#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as err_message:
        print("Exception: {}".format(err_message), file=sys.stderr)
        return None
