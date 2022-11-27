#!/usr/bin/python3
'''
Test files for amenity
'''
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    Tests Amenity class
    '''
    def test_amenity(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)
        self.assertTrue("name" in new_amenity.__dir__())
    
    def test_amenity_attribute(self):
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)


if __name__ == '__main__':
    unittest.main()