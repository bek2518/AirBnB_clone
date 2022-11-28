#!/usr/bin/python3
'''
Test files for city
'''
import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    '''
    Test cases for City
    '''

    def test_city(self):
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
    
    def test_city_name(self):
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)
    
    def test_city_state_id(self):
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)

if __name__ == '__main__':
    unittest.main()
