#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage

class TestCity(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing class attribute assignment"""
        cls.amen1 = Amenity()
        cls.amen2 = Amenity()
        cls.amen1.name = "Water Heater"
        cls.amen2.name = "AC"

    @classmethod
    def tearDownClass(cls):
        """Testing for removing file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing class attribute assignment"""
        self.assertTrue(self.amen1.name, "Water Heater")
        self.assertTrue(self.amen2.name, "AC")
        assert self.amen1.id != self.amen2.id

    def test_save(self):
        """Testing save method"""
        self.amen1.save()
        self.amen2.save()
        assert self.amen1.created_at != self.amen1.updated_at
        assert self.amen2.created_at != self.amen2.updated_at

    def test_to_dict(self):
        """Testing to_dict method"""
        a1_dict = self.amen1.to_dict()
        a2_dict = self.amen2.to_dict()
        self.assertTrue(type(a1_dict), dict)
        self.assertTrue(type(a2_dict), dict)
        self.assertTrue(type(a1_dict["created_at"]), str)
        self.assertTrue(type(a2_dict["updated_at"]), str)
        assert ("__class__" in a1_dict.keys()) == True
        amen3 = Amenity(**a1_dict)
        assert self.amen1 != amen3

    def test_class_attribute_exists(self):
        """Testing if class attribute exists"""
        self.assertTrue(hasattr(Amenity, 'name'))
