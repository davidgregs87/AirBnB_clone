#!/usr/bin/env python3
""" Contains a base model """
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        if kwargs:
            keys = list(kwargs.keys())
            if "id" in keys:
                self.id = kwargs['id']
            if "created_at" in keys:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if "updated_at" in keys:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            if "name" in keys:
                self.name = kwargs['name']
            if "number" in keys:
                self.number = kwargs['number']
        else:
             self.id = str(uuid.uuid4())
             self.created_at = datetime.now()
             self.updated_at = self.created_at
             storage.new(self)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
        

