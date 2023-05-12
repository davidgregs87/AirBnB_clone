#!/usr/bin/env python3
from models.base_model import BaseModel
class City(BaseModel):
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
