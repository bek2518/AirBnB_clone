#!/usr/bin/python3
'''
Test files for review
'''
import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    '''
    Test cases for Reveiw
    '''

    def test_review(self):
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())
    
    def test_review_place_id(self):
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        self.assertIsInstance(place_id, str)
    
    def test_review_user_id(self):
        new_review = Review()
        user_id = getattr(new_review, "user_id")
        self.assertIsInstance(user_id, str)
    
    def test_review_text(self):
        new_review = Review()
        text = getattr(new_review, "text")
        self.assertIsInstance(text, str)


if __name__ == '__main__':
    unittest.main()
