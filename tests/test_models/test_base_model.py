#!/usr/bin/python3
"""
Test suite for Base class --> Unittest
--> run with python3 -m unittest discover tests
or --> run with python3 -m unittest tests/test_models/test_base_model.py
- All your test files and folders should start with test_
"""
import models
import unittest
import json
from datetime import datetime
from models.base_model import BaseModel


class test_Base(unittest.TestCase):
    """
    Test suite for Base class.
    """
    def test_documentation(self):
        """
        Test if there is documentation
        """
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)

    def test_id_assignment(self):
        """
        Test assignment of UUID is of type string and len is equal to 36
        A UUID is made up of hex digits  (4 chars each) along with 4 “-”
        symbols, which make its length equal to 36 characters.
        """
        test = BaseModel()
        self.assertIsInstance(test.id, str)
        self.assertEqual(len(test.id), 36)

    def test_instance_of_BaseModel(self):
        """
        Test instantiation of a BaseModel class
        """
        test = BaseModel()
        self.assertEqual(type(test), BaseModel)
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))

    def test_instance_with_kwarg(self):
        """
        Test instantation with kwarg
        """
        test = BaseModel(name="Marce y Agus")
        self.assertTrue(hasattr(test, "name"))

    def test_created_at(self):
        """
        Test that when creating an instance of BaseModel "datetime" is assigned
        correctly to the public instance attribute: "created_at" and is of type
        "datetime".
        Use of function "hasattr" to check if the attribute was created as it
        should be.
        """
        test = BaseModel()
        self.assertTrue(hasattr(test, "created_at"))
        self.assertEqual(type(test.created_at), datetime)

    def test_updated_at(self):
        """
        Test that when creating an instance of BaseModel "datetime" is assigned
        correctly to the public instance attribute: "updated_at" and is of type
        "datetime".
        Use of function "hasattr" to check if the attribute was created as it
        should be.
        """
        test = BaseModel()
        self.assertTrue(hasattr(test, "updated_at"))
        self.assertEqual(type(test.updated_at), datetime)

    def test_save(self):
        """
        Test save model: storage created time and updated time
        """
        test = BaseModel()
        test.save()
        self.assertNotEqual(test.created_at, test.updated_at)

    def test_to_dict(self):
        """
        test to dict method
        """
        test = BaseModel()
        test_dict = test.to_dict()
        self.assertIsInstance(test_dict, dict)

    # test prueba checker:

    def test_id(self):
        """2 instancias deben tener diferente id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertFalse(obj1.id == obj2.id)

    def test_format_date(self):
        """chequeamos el formato de date"""
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)

    def test_kwarg(self):
        """test que valida que se llene mediante un diccionario"""
        dic = {'id': '12', 'created_at': '2017-09-28T21:03:54.052302',
               'updated_at': '2017-09-28T21:03:54.052302'}
        obj1 = BaseModel(**dic)
        data1 = '%Y-%m-%dT%H:%M:%S.%f'
        data2 = '2017-09-28T21:03:54.052302'

        self.assertEqual(obj1.id, "12")
        self.assertEqual(obj1.created_at, datetime.strptime(data2, data1))
        self.assertEqual(obj1.updated_at, datetime.strptime(data2, data1))
        self.assertEqual(type(dic["created_at"]), str)

    def test_str(self):
        """chequeo de la str function"""
        obj = BaseModel()
        self.assertEqual(type(str(obj)), str)
        # self.assertEqual(type(__str__(obj)), str)

    if __name__ == '__main__':
        unittest.main()
