#!/usr/bin/python3
import math

"""magic class
"""


class MagicClass:
    """Class that stores the properties
    of a circumference
    """

    def __init__(self, radius=0):
        """Initialize the class with a radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Method that calculates the area of a circumference"""
        return (self.__radius**2) * math.pi

    def circumference(self):
        """Method that calculates the perimeter of a circumference"""
        return 2 * math.pi * self.__radius
