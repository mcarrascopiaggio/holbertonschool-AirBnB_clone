#!/usr/bin/python3
"""
Module for creating a Amenity class that inherits from BaseModel
"""
from models.base_model import BaseModel
import models  # if we put: from models import storage -> error:circular import


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel.
    """

    name = ""
