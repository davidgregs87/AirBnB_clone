#!/usr/bin/python3

"""
BaseModel module that defines all the common attributes/methods
for other classes
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """
        Instance Attributes
        """
        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints ==> [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        """Get a copy of the object's __dict__ so that changes
        can be made
        """
        dic_obj = self.__dict__.copy()
        dic_obj["__class__"] = type(self).__name__
        dic_obj["created_at"] = dic_obj["created_at"].isoformat()
        dic_obj["updated_at"] = dic_obj["updated_at"].isoformat()
        return dic_obj
