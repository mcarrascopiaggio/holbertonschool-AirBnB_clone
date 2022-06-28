#!/usr/bin/python3
"""
__init__.py can just be an empty file, but it can also execute initialization
code for the package.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
