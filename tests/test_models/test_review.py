#!/usr/bin/python
"""
test Class Review
"""


import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class TestCity(unittest.TestCase):
    """
    Test Review
    """

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(Review.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = Review()
        self.assertEqual(test.place_id, "")
        self.assertEqual(test.user_id, "")
        self.assertEqual(test.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = Review()
        self.assertEqual(type(test.place_id), str)
        self.assertEqual(type(test.user_id), str)
        self.assertEqual(type(test.text), str)


if __name__ == "__main__":
    unittest.main()
