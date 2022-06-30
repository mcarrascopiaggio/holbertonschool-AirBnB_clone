#!/usr/bin/python
"""
test Class Review
"""


import unittest
import models
from models.review import Review


class TestCity(unittest.TestCase):
    """
    Test Review
    """

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


if __name__ == "__main__":
    unittest.main()
