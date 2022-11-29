#!/usr/bin/python3
'''
Test files for file_storage
'''
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    '''
    Tests Filestorage class
    '''
    @classmethod
    def setup(cls):
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Bog"
        cls.user.email = "airbnb@mail.com"
        cls.user.password = "root"
    def test_FileStorage(self):
        '''
        Test for attributes of FileStorage
        '''
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_FileStorage_all(self):
        '''
        Tests return type of the method all
        '''
        fs = FileStorage()
        dictionary = fs.all()
        self.assertIsInstance(dictionary, dict)
    
    def test_FileStorage_new(self):
        '''
        Tests new() method
        '''
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        self.assertIsNotNone(fs.all())

    def test_FileStorage_save(self):
        '''
        Tests save() method'''
        bm = BaseModel
        fs = FileStorage
        fs.new(bm)
        fs.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_FileStorage_reload(self):
        '''
        Tests reload() method
        '''
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        fs.save()
        dictionary = fs.reload()
        self.assertTrue(dictionary is fs.reload())

if __name__ == '__main__':
    unittest.main()