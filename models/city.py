#!/usr/bin/python3
"""
Module for creating a City class that inherits from BaseModel
"""
from models.base_model import BaseModel
import models  # if we put: from models import storage -> error:circular import


class City(BaseModel):
    """
    class City that inherits from BaseModel.
    """

    state_id = ""
    name = ""
