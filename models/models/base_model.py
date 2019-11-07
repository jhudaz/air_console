#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import uuid4
from json import loads
from datetime import datetime

class BaseModel:
    """Base Class"""

    def __init__(self, id=None):
        id = uuid4()
        created_at = datetime.now()
        update_at = datetime.now()

    def __str__(self):
        print("[{}] ({}) {}".format(self.__name__(), self.id, self.__dict__()))

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        return self.__dict__()
