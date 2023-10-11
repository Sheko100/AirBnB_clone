#!/usr/bin/python3
"""Module to define a BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """A class to define a base model
    """

    def __init__(self):
        """initializes the instance of the BaseModel
        """

        date_now = datetime.now()
        self.id = str(uuid4())
        self.created_at = date_now
        self.updated_at = date_now

    def __str__(self):
        cls_name = self.__class__.__name__

        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary for the instance
        """

        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = dct["created_at"].isoformat()
        dct["updated_at"] = dct["updated_at"].isoformat()

        return dct
