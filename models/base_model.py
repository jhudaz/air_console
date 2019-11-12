#!/usr/bin/python3
""" model base """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """ constructor """
        
        if len(kwargs) > 0:
            """ dictionary representation """
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
            """ new instance """
            self.id = str(uuid4())
            self.update_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """" return de representation of the instance """
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        """ save the changes and update the date """
        self.update_at = datetime.now()
        self.update_at = self.update_at.isoformat()
        storage.save()
        

    def to_dict(self):
        """ return a dictionary """
        dictionary = self.__dict__
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': str(datetime.isoformat(self.created_at))})
        dictionary.update({'update_at': str(datetime.isoformat(self.update_at))})
        #dictionary['__class__'] = self.__class__.__name__
        #dictionary['created_at'] = str(datetime.isoformat(self.created_at))
        #dictionary['update_at'] = str(datetime.isoformat(self.update_at))
        return dictionary
