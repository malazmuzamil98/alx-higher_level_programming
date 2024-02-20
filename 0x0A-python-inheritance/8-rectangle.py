#!/usr/bin/python3
"""Module that contains the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""_summary_"""


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class
    """

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This is the area method
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        This is the string method
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
