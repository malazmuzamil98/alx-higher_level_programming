#!/usr/bin/python3
"""_summary_
"""


def inherits_from(obj, a_class):
    """_summary_"""
    if type(obj) is a_class:
        print(type(obj))
        return False
    return isinstance(obj, a_class)
