#!/usr/bin/python3
'''
Test files for state
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
    Test cases for State
    '''

    def test_state(self):
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)
        self.assertTrue("name" in new_state.__dir__())
    
    def test_state_name(self):
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
