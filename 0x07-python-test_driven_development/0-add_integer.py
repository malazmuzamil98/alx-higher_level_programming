#!/usr/bin/python3
"""
this module to add two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
    a (int): The first integer to be added.
    b (int): The second integer to be added. Default is 98.
    Returns:
    int: The sum of the two input integers.
    Raises:
    TypeError: If either 'a' or 'b' are not integers.
    """

    vars = [a, b]
    for v in vars:
        if not isinstance(v, int) and not isinstance(v, float):
            raise TypeError("{} must be an integer".format(v))
        a = int(a)
        b = int(b)

        return a + b
