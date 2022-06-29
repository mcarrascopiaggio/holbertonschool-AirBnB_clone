#!/usr/bin/python3
"""
Module for creating a user class that inherits from BaseModel: User
"""
from models.base_model import BaseModel
import models  # if we put: from models import storage -> error:circular import


class User(BaseModel):
    """
    class User that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
