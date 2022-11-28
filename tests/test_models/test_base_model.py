#!/usr/bin/python3
'''
Creates a unittest for the base_model
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Test case for BaseModel class'''

    def test_base_model(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
    
    def test_base_model_docs(self):
        bm = BaseModel()
        self.assertIsNotNone(bm.__doc__)
        self.assertIsNotNone(bm.__init__.__doc__)
        self.assertIsNotNone(bm.__Str__.__doc__)
        self.assertIsNotNone(bm.save.__doc__)
        self.assertIsNotNone(bm.to_dict.__doc__)

    def test_base_model_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertIsInstance(bm1.id, str)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertIsInstance(bm2.id, str)
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_updated_at(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertEqual(bm.created_at, bm.updated_at)


if __name__ == '__main__':
    unittest.main()
