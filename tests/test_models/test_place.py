#!/usr/bin/python
"""
test Class Place
"""


import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class TestCity(unittest.TestCase):
    """
    Test Place
    """

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """
        test instance of place
        """
        test = Place()
        self.assertEqual(test.name, "")
        self.assertEqual(test.user_id, "")
        self.assertEqual(test.city_id, "")
        self.assertEqual(test.description, "")
        self.assertEqual(test.number_rooms, 0)
        self.assertEqual(test.number_bathrooms, 0)
        self.assertEqual(test.max_guest, 0)
        self.assertEqual(test.price_by_night, 0)
        self.assertEqual(test.latitude, 0.0)
        self.assertEqual(test.longitude, 0.0)
        self.assertEqual(test.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
