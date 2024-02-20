#!/usr/bin/python3
"""_summary_
"""


Rectangle = __import__("9-rectangle").Rectangle

"""_summary_
"""


class Square(Rectangle):
    """
    This is the Square class
    """

    def __init__(self, size):
        """_summary_

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This is the area method
        """
        return super().area()

    def __str__(self):
        """_str_

        Returns:
            _type_: _description_
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
