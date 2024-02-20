#!/usr/bin/python3
"""A class that inherits from the list class"""


class MyList(list):
    """A class that inherits from the list class"""

    def print_sorted(self):
        """Prints the list in sorted order"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
