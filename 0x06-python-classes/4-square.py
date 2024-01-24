#!/usr/bin/python3
"""A module for a square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """initialization point of instunces

        Args:
            size : size of the square
        Raises:
            TypeError : if size is not an integer
            ValueError : if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            integer: returns the area of the square which is hight * width
            in the square case they are equal and equals the size
        """

        return self.__size * self.__size
    @property
    def size(self):
        """Gets the square size"""

        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): square size

        Raises:
            TypeError: if the value is integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
