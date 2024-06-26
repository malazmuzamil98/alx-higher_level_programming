#!/usr/bin/python3
"""_summary_"""


from base import Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.__width

    @width.setter
    def width(self, width_value):
        """_summary_

        Args:
            width_value (_type_): _description_
        """

        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")
        if width_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_value

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.__height

    @height.setter
    def height(self, height_value):
        """_summary_

        Args:
            height_value (_type_): _description_
        """

        if not isinstance(height_value, int):
            raise TypeError("height must be an integer")
        if height_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_value

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.__x

    @x.setter
    def x(self, x_value):
        """_summary_

        Args:
            x_value (_type_): _description_
        """

        if not isinstance(x_value, int):
            raise TypeError("x must be an integer")
        if x_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.__y

    @y.setter
    def y(self, y_value):
        """_summary_

        Args:
            y_value (_type_): _description_
        """

        if not isinstance(y_value, int):
            raise TypeError("y must be an integer")
        if y_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value

    def area(self):
        """_summary_"""

        return self.__height * self.__width

    def display(self):
        """_summary_"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -" \
            "{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """_summary_"""

        if args is not None:
            self.__width = kwargs.get("width", self.__width)
            self.__height = kwargs.get("height", self.__height)
            self.__x = kwargs.get("x", self.__x)
            self.__y = kwargs.get("y", self.__y)
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

    def to_dictionary(self):
        """_summary_"""

        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())