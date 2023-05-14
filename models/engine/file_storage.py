#!/usr/bin/python3

"""
file_storage Module.
All objects are stored here
"""
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Adds objects to the dictionary with the key
        being classname.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)

        Create a json_obj that would have __object[key] as key
        and value == dictionary form of the objects

        N.B: val == obj

        Created a new obj to be saved in the file.
        Because saving the self.__objects directly would cause
        an object not serializable error
        """
        json_obj = {}
        for key, val in self.__objects.items():
            json_obj[key] = val.to_dict()
        with open(self.__file_path, 'w') as a_file:
            json.dump(json_obj, a_file)

    def reload(self):
        """
        Derializes json object from file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as a_file:
                py_obj = json.load(a_file)
            for key, val in py_obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)
        else:
            pass
