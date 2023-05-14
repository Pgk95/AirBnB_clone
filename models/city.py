#!/usr/bin/python3
"""creates the class user attribute."""

from models.base_model import BaseModel


class City(BaseModel):
    """manages city objects."""
    state_id = ""
    name = ""
