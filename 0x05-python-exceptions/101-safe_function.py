#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exeption: {}\n".format(e))
        result = None

    return result
