#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing class attribute instantiation"""
        cls.state1 = State()
        cls.state2 = State()
        cls.state1.name = "Abuja"
        cls.state2.name = "Lagos"

    @classmethod
    def tearDownClass(cls):
        """Testing for removing file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing class attribute instantiation"""
        self.assertTrue(self.state1.name, "Abuja")
        self.assertTrue(self.state2.name, "Lagos")
        assert self.state1.id != self.state2.id

    def test_save(self):
        """Testing save method"""
        self.state1.save()
        self.state2.save()
        assert self.state1.created_at != self.state1.updated_at
        assert self.state2.created_at != self.state2.updated_at

    def test_to_dict(self):
        """Testing to_dict method"""
        s1_dict = self.state1.to_dict()
        s2_dict = self.state2.to_dict()
        self.assertTrue(type(s1_dict), dict)
        self.assertTrue(type(s2_dict), dict)
        self.assertTrue(type(s1_dict["created_at"]), str)
        self.assertTrue(type(s2_dict["updated_at"]), str)
        assert ("__class__" in s1_dict.keys()) == True
        state3 = State(**s1_dict)
        assert self.state1 != state3

    def test_class_attribute_exists(self):
        """Testing if attribute exists"""
        self.assertTrue(hasattr(State, 'name'))

    def test_class_attribute_type(self):
        """Testing attribute type"""
        self.assertTrue(type(self.state1.name), str)
