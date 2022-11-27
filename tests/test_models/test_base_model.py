#!/usr/bin/python3
'''
Creates a unittest for the base_model
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Test case for BaseModel class'''

    def test_base_model_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertIsInstance(bm1.id, str)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertIsInstance(bm2.id, str)

if __name__ == '__main__':
    unittest.main()
