#!/usr/bin/python
"""
test Class Amenity
"""


import unittest
import models
from models.amenity import Amenity


class Test  Amenity(unittest.TestCase):
    """
    Test amenity
    """

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = Amenity()
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
