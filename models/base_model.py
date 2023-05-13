#!/usr/bin/python3

"""
models/base_model.py:
Defines the BaseModel class, serving as the base class for other
classes.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    defines common attributes and methods for the other classes.
    """
    def __init__(self, *args, **Kwargs):
        """
        Initializes a new instance of the BaseModel class
        If Kwargs is not empty set attributes base on key-value
        If Kwargs is empty generate a new id and set and update.
        """
        if Kwargs:
            for key, value in Kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        Calls the save(self) method of storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing al keys/values of the instance.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        data['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return data

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
