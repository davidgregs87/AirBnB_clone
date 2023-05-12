#!/usr/bin/env python3
"""My review file"""

from models.base_model import BaseModel

class Review(BaseModel):
    """My review class that is inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
