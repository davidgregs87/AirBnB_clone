#!/usr/bin/env python3
"""A file that defines our file storage module"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json
from os.path import exists


class FileStorage():
    """our file storage module"""
    __file_path = "new.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_fmt = {}
#        dict_fmt = {k: v=v.to_dict() for k, v in dict_fmt.items()}
        for k, v in FileStorage.__objects.items():
            v = v.to_dict()
            dict_fmt[k] = v
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_fmt, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file does
        not exist, no exception should be raised)"""

        try:
            if exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    json_obj = json.load(f)
                for key in json_obj.values():
                    cls_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            pass
