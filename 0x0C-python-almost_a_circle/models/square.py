#!/usr/bin/python3
"""_summary_"""


from rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.width

    @size.setter
    def size(self, size_value):
        """_summary_

        Args:
            size_value (_type_): _description_
        """

        if not isinstance(size_value, int):
            raise TypeError("width must be an integer")
        if size_value <= 0:
            raise ValueError("width must be > 0")
        self.width = size_value
        self.height = size_value

    def update(self, *args, **kwargs):
        """_summary_"""

        super().update()
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.height = kwargs.get("size", self.height)
            self.width = kwargs.get("size", self.width)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
