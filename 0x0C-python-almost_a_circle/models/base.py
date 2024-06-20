#!/usr/bin/python3
"""_summary_"""


import json
class Base:
    """_summary_"""

    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """

        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        file_name = class_name + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(dict_list))
