#!/usr/bin/python3
"""
BASE MODEL
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BASE MODEL"""

    def __init__(self, *arg, **kwargs):
        """Initializes all attributes"""
        from models import storage
        date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_fmt)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns string representation of Base Model"""
        className = '[{}] '.format(self.__class__.__name__)
        self_id = '({}) '.format(self.id)
        self_dict = str(self.__dict__)
        return className + self_id + self_dict

    def save(self):
        """Updates the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of the attributes"""
        date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        dic = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.strftime(date_fmt)
            if key != '__class__':
                key = key.split('__')
                key = key[-1]
                dic.update({key: value})
        if '__class__' not in self.__dict__.items():
            dic.update({'__class__': self.__class__.__name__})
        return dic
