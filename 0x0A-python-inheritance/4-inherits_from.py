#!/usr/bin/python3
"""_summary_
"""


def inherits_from(obj, a_class):
    """_summary_"""
    return isinstance(obj, a_class)


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))