#!/usr/bin/python3
"""_summary_"""


def add_attribute(obj, name, value):
    """_summary_

    Args:
        obj (_type_): _description_
        name (_type_): _description_
        value (_type_): _description_
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
