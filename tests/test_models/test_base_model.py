#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing setting up with new attribute instances"""
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()
        cls.base1.name = "Ngozi Nwamanna"
        cls.base2.name = "Amaka Nwamanna"
        cls.base1.number = 89
        cls.base2.number = 56

    @classmethod
    def tearDownClass(cls):
        """Testing for removing file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing attribute Instatiation"""
        self.assertTrue(self.base1.name, "Ngozi Nwamanna")
        self.assertTrue(self.base2.name, "Amaka Nwamanna")
        self.assertTrue(self.base1.number, 89)
        self.assertTrue(self.base2.number, 56)
        assert self.base1.id != self.base2.id

    def test_save(self):
        """Testing the save method"""
        self.base1.save()
        self.base2.save()
        assert self.base1.created_at != self.base1.updated_at
        assert self.base2.created_at != self.base2.updated_at

    def test_to_dict(self):
        """Testing the to_dict method"""
        b1_dict = self.base1.to_dict()
        b2_dict = self.base2.to_dict()
        self.assertTrue(type(b1_dict), dict)
        self.assertTrue(type(b2_dict), dict)
        self.assertTrue(type(b1_dict["created_at"]), str)
        self.assertTrue(type(b2_dict["updated_at"]), str)
        assert ("__class__" in b1_dict.keys()) is True
        base3 = BaseModel(**b1_dict)
        assert self.base1 != base3
