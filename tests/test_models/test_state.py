#!/usr/bin/python
"""
test Class State
"""


import unittest
import models
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test state
    """

    def test_documentation(self):
        """
        check if class has documentation
        """
        self.assertIsNotNone(State.__doc__)

    def test_class(self):
        """
        test class & test subclass
        """
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """
        test instance of state
        """
        test = State()
        self.assertEqual(test.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributetype(self):
        """
        test attribute test
        """
        test = State()
        self.assertEqual(type(test.name), str)


if __name__ == "__main__":
    unittest.main()
