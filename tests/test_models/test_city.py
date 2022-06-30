#!/usr/bin/python
"""
test Class City
"""


import unittest
from models.base_model import BaseModel
import models
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test City
    """

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """
        test instance of City
        """
        test = City()
        self.assertEqual(test.state_id, "")
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
