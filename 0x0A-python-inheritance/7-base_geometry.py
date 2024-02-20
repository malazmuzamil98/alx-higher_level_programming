#!/usr/bin/python3
"""_summary_
"""


class BaseGeometry:
    """
    This is the base class for all geometric shapes
    """

    def area(self):
        """
        This is the area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
