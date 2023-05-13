#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing class attribute instatiation"""
        cls.user1 = User()
        cls.user2 = User()
        cls.user1.name = "Ngozi Nwamanna"
        cls.user2.name = "Amaka Nwamanna"
        cls.user1.number = 89
        cls.user2.number = 56

    @classmethod
    def tearDownClass(cls):
        """Testing to remove file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing attribute assignment"""
        self.assertTrue(self.user1.name, "Ngozi Nwamanna")
        self.assertTrue(self.user2.name, "Amaka Nwamanna")
        self.assertTrue(self.user1.number, 89)
        self.assertTrue(self.user2.number, 56)
        assert self.user1.id != self.user2.id

    def test_save(self):
        """Testing save method"""
        self.user1.save()
        self.user2.save()
        assert self.user1.created_at != self.user1.updated_at
        assert self.user2.created_at != self.user2.updated_at

    def test_to_dict(self):
        """Testing to_dict method"""
        u1_dict = self.user1.to_dict()
        u2_dict = self.user2.to_dict()
        self.assertTrue(type(u1_dict), dict)
        self.assertTrue(type(u2_dict), dict)
        self.assertTrue(type(u1_dict["created_at"]), str)
        self.assertTrue(type(u2_dict["updated_at"]), str)
        assert ("__class__" in u1_dict.keys()) == True
        user3 = User(**u1_dict)
        assert self.user1 != user3
