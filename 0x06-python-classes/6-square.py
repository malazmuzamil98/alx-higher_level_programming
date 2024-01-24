#!/usr/bin/python3
"""A module for a square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """Gets the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value (int): square position

        Raises:
            TypeError: If value is not a tuple or not of length 2.
            ValueError: If value is not a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print the square"""

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + "#" * self.__size)
