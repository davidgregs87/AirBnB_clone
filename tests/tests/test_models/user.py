#!/bin/usr/env python3
import unittest
from models.user import User
class TestUser(unittest.TestCase):
    def classSetUp(self):
        self.user1 = User()
        self.user2 = User()

    def ClassTeardown(self):
         os.rm.
