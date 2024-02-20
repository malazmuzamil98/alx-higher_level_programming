#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


class MyInt(int):
    """_summary_

    Args:
        int (_type_): _description_
    """

    def __eq__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        return not super().__ne__(other)
