#!/usr/bin/env python3
import json
import os
class FileStorage():
    __file_path = "file.json"
    __object = {}
    def all(self):
        return type(self).__object

    def new(self, obj):
        c_name = obj.__class__.__name__
        c_id = obj.id
        object_dict = obj
        type(self).__object[c_name+"."+c_id] = object_dict

    def save(self):
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
            with open(type(self).__file_path, "w", encoding="utf-8") as f:
                for key, value in type(self).__object.items():
                     json_dict[key] = value.to_dict()
                json.dump(json_dict, f)
        else:
            json_dict = {}
            with open(type(self).__file_path, "w", encoding="utf-8") as f:
                for key, value in type(self).__object.items():
                     json_dict[key] = value.to_dict()
                json.dump(json_dict, f)


    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.exists(type(self).__file_path) and os.path.getsize(type(self).__file_path) > 0:
             with open(type(self).__file_path, encoding="utf-8") as f:
                json_dict = json.load(f)
                for values in json_dict.values():
                    class_name = values['__class__']
                    del values['__class__']
                    self.new(eval(class_name)(**values)) 
