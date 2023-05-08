#!/usr/bin/python3
"""a file that include defined modules"""
import uuid
import datetime

class BaseModel:
    """This defines all common attributes/methods for other classes """
    def __init__(self):
        """instantiating public instance attributes"""
        self.name = ""
        self.my_number = ""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self) -> str:
        """Returns a string"""
        return("[{}] ({}) {}".format(__class__.__name__, self.id, (self.__dict__)))
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        return self.__str__()
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__.update({"__class__":__class__.__name__})
        return self.__dict__
