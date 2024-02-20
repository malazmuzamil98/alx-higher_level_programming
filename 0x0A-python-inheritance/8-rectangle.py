#!/usr/bin/python3
"""_summary_
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""_summary_
"""


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class
    """

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        __width = width
        __height = height
