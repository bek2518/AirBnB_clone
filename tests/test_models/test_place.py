#!/usr/bin/python3
'''
Test files for place
'''
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    '''
    Test cases for User
    '''

    def test_place(self):
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)
        self.assertTrue("city_id" in new_place.__dir__())
        self.assertTrue("user_id" in new_place.__dir__())
        self.assertTrue("description" in new_place.__dir__())
        self.assertTrue("name" in new_place.__dir__())
        self.assertTrue("number_rooms" in new_place.__dir__())
        self.assertTrue("max_guest" in new_place.__dir__())
        self.assertTrue("price_by_night" in new_place.__dir__())
        self.assertTrue("latitude" in new_place.__dir__())
        self.assertTrue("longitude" in new_place.__dir__())
        self.assertTrue("amenity_ids" in new_place.__dir__())

    def test_place_city_id(self):
        new_place = Place()
        city_id = getattr(new_place, "city_id")
        self.assertIsInstance(city_id, str)
    
    def test_place_user_id(self):
        new_place = Place()
        user_id = getattr(new_place, "user_id")
        self.assertIsInstance(user_id, str)
    
    def test_place_name(self):
        new_place = Place()
        name = getattr(new_place, "name")
        self.assertIsInstance(name, str)
    
    def test_place_city_id(self):
        new_place = Place()
        description = getattr(new_place, "description")
        self.assertIsInstance(description, str)
    
    def test_place_number_rooms(self):
        new_place = Place()
        number_rooms = getattr(new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)
    
    def test_place_number_bathrooms(self):
        new_place = Place()
        number_bathrooms = getattr(new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)
    
    def test_place_max_guest(self):
        new_place = Place()
        max_guest = getattr(new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_place_price_by_night(self):
        new_place = Place()
        price_by_night = getattr(new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_place_latitude(self):
        new_place = Place()
        latitude = getattr(new_place, "latitude")
        self.assertIsInstance(latitude, float)
    
    def test_place_amenity_ids(self):
        new_place = Place()
        amenity_ids = getattr(new_place, "amenity_ids")
        self.assertIsInstance(amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
