#!/usr/bin/python3
'''
Test files for file_storage
'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''
    Tests Filestorage class
    '''
    def test_FileStorage(self):