#!/usr/bin/python3
"""
Module for creating a State class that inherits from BaseModel
"""
from models.base_model import BaseModel
import models  # if we put: from models import storage -> error:circular import


class State(BaseModel):
    """
    class State that inherits from BaseModel.
    """

    name = ""
