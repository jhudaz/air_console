#!/usr/bin/python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from json import loads, dumps
from datetime import datetime, date


class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key is 'update_at':
                    self.update_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key is 'created_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key is '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.update_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['update_at'] = str(datetime.isoformat(self.update_at))
        dictionary['created_at'] = str(datetime.isoformat(self.created_at))
        return dictionary
