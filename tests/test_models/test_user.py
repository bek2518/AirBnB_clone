#!/usr/bin/python3
'''
Test files for user
'''
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    '''
    Test cases for User
    '''

    def test_user(self):
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
    
    def test_user_email(self):
        new_user = User()
        email = getattr(new_user, "email")
        self.assertIsInstance(email, str)
    
    def test_user_password(self):
        new_user = User()
        password = getattr(new_user, "password")
        self.assertIsInstance(password, str)
    
    def test_user_first_name(self):
        new_user = User()
        first_name = getattr(new_user, "first_name")
        self.assertIsInstance(first_name, str)
    
    def test_user_first_name(self):
        new_user = User()
        last_name = getattr(new_user, "lasrt_name")
        self.assertIsInstance(last_name, str)


if __name__ == '__main__':
    unittest.main()
