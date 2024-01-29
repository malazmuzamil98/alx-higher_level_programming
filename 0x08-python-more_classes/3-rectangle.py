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

    def __str__(self):
        """prints the Rectangle

        Returns:
            str: a string
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += ("#" * self.width) + "\n"
        return string[:-1]

    def __repr__(self):
        """

        Returns:
            str: a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

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

    def area(self):
        """ calculate the Rectangle area

        Returns:
            int: Rectagle area
        """
        return self.width * self.height

    def perimeter(self):
        """ Rectangle perimeter

        Returns:
            int: Rectagle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
