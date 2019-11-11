#!/usr/bin/python3
""" storage model """
from json import dump, load
from datetime import datetime


class FileStorage():
    """FileStorage class"""

    """private class attributes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects

    def new(self, obj):
        """"""
        nameClass = obj.__class__.__name__
        idClass = obj.id
        key = nameClass+'.'+idClass
        dataDict = obj.__dict__.copy()
        created_date = dataDict['created_at']
        update_date = dataDict['update_at']
        dataDict['created_at'] = str(datetime.isoformat(created_date))
        dataDict['update_at'] = str(datetime.isoformat(update_date))
        FileStorage.__objects.update({key: dataDict})
        print("\n\ndata {}\n\n".format(dataDict))

       
    def save(self):
        """ serialize the object to a JSON file"""
        with open(FileStorage.__file_path, 'a', encoding='utf-8') as file:
            dataJson = FileStorage.__objects
            dump(dataJson, file)

    def reload(self):
        """ """
        """with open(FileStorage.__file_path, 'r', encoding='utf-8')as file:
            load(file)"""
