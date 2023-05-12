#!/usr/bin/env python3
from models.base_model import BaseModel
class State(BaseModel):
    name = ""
    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
