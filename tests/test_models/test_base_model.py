#!/usr/bin/python3
"""Unit test for the Base class"""
import unittest
import pep8
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """ Test_BaseModel class"""

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_modal.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

