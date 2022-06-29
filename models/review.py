#!/usr/bin/python3
"""
Module for creating a Review class that inherits from BaseModel
"""
from models.base_model import BaseModel
import models  # if we put: from models import storage -> error:circular import


class Review(BaseModel):
    """
    class Review that inherits from BaseModel.
    """

    place_id = ""
    user_id = ""
    text = ""
