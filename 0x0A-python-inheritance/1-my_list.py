#!/usr/bin/python3
"""A class that inherits from the list class"""


class MyList(list):
    """A class that inherits from the list class"""

    def print_sorted(self):
        """Prints the list in sorted order"""
        print(sorted(self))
