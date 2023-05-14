#!/usr/bin/python3
"""Creates the class Review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """manages the reviewing objects."""
    place_id = ""
    user_id = ""
    text = ""
