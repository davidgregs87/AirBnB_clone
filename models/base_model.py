#!/usr/bin/python3
"""a file that include defined modules """
import uuid
from datetime import datetime


class BaseModel:
    """This defines all common attributes/methods for other classes """
    def __init__(self, *arg, **kwargs):
        """Initializes all attributes"""
        """Importing storage from models"""
        date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs or len(kwargs) == 0:
            # Checking if dictionary is empty
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Store the classname.id
            from models import storage
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_fmt)
# Remove the key "__class__" from kwargs
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self) -> str:
        """Returns a string"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      (self.__dict__)))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
