#!/usr/bin/python
"""
test Class Amenity
"""


import unittest
from models.base_model import BaseModel
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test amenity
    """

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = Amenity()
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
