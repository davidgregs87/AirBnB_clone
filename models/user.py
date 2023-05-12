#!/usr/bin/env python3
"""Write a class User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """Created my User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
