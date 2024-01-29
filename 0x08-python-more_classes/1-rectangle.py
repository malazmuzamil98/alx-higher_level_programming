#!/usr/bin/python3
"""a Rectangle class"""


class Rectangle:
    """a Rectangle class"""

    def __init__(self, width=0, height=0):
        """ A constructor method

        Args:
            width (int): width. Defaults to 0.
            height (int): height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter

        Returns:
            int: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter

        Args:
            value (int): width value

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter

        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter

        Args:
            value (int): height value

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
