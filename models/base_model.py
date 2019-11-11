#!/usr/bin/python3
""" model base """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'update_at':
                    self.update_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.update_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        """" return de representation of the instance """
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        """ save the changes and update the date """
        storage.save()
        self.update_at = datetime.now()

    def to_dict(self):
        """ return a dictionary """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = str(datetime.isoformat(self.created_at))
        dictionary['update_at'] = str(datetime.isoformat(self.update_at))
        return dictionary
