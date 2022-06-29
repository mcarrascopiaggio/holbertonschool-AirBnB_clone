#!/usr/bin/python3
"""
Unittest for FileStorage
"""
import models
from models.engine.file_storage import FileStorage
import unittest


class TestFile_Storage(unittest.TestCase):
    """
    File_Storage test
    """

    def test_documentation(self):
        """
        test documentation
        """
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_is_an_instance(self):
        """
        test instantation
        """
        test = FileStorage()
        self.assertIsInstance(test, FileStorage)
# method all
# method new
# method save
# method reload

    if __name__ == '__main__':
        unittest.main()
