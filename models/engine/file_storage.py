#!/usr/bin/python3
""" storage model """
import json
from os import path


class FileStorage():
    """FileStorage class"""

    """private class attributes"""
    __file_path = ''
    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects;

    def new(self, obj):
        """ """
        return ''

    def save(self):
        """ serialize the object to a JSON file"""
        
        return ''

    def reload(self):
        """ """
        return ''
