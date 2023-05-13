#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage

class TestPlace(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing class attribute instatiation"""
        cls.rev1 = Review()
        cls.rev2 = Review()
        cls.rev1.text = "Excellent"
        cls.rev2.text = "Average"
        cls.rev1.place_id = "7648"
        cls.rev2.place_id = "0293"

    @classmethod
    def tearDownClass(cls):
        """Testing for removing file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing class attribute instatiation"""
        self.assertTrue(self.rev1.text, "Excellent")
        self.assertTrue(self.rev2.text, "Average")
        self.assertTrue(self.rev1.place_id, "7648")
        self.assertTrue(self.rev2.place_id, "0293")
        assert self.rev1.id != self.rev2.id

    def test_save(self):
        """Testing save method"""
        self.rev1.save()
        self.rev2.save()
        assert self.rev1.created_at != self.rev1.updated_at
        assert self.rev2.created_at != self.rev2.updated_at

    def test_to_dict(self):
        """Testing to_dict method"""
        r1_dict = self.rev1.to_dict()
        r2_dict = self.rev2.to_dict()
        self.assertTrue(type(r1_dict), dict)
        self.assertTrue(type(r2_dict), dict)
        self.assertTrue(type(r1_dict["created_at"]), str)
        self.assertTrue(type(r2_dict["updated_at"]), str)
        assert ("__class__" in r1_dict.keys()) == True
        rev3 = Review(**r1_dict)
        assert self.rev1 != rev3

    def test_class_attribute_exists(self):
        """Testing if class attribute exists"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_class_attribute_type(self):
        """Testing attribute type"""
        self.assertTrue(type(self.rev1.place_id), str)
        self.assertTrue(type(self.rev1.user_id), str)
        self.assertTrue(type(self.rev1.text), str)
