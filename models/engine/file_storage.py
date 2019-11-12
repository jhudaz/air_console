#!/usr/bin/python3
""" storage model """
from json import dump, load
from datetime import datetime
from os import path


class FileStorage():
    """FileStorage class"""

    """private class attributes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ """
        return self.__objects

    def new(self, obj):
        """ set the dictionary """
        nameClass = obj.__class__.__name__
        idClass = obj.id
        key = nameClass+'.'+idClass
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """ serialize the object to a JSON file"""
        data = self.__objects
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            dump(data, file)

    def reload(self):
        """ deserialize the JSON file into a python object"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8')as file:
                self.__objects = load(file)
