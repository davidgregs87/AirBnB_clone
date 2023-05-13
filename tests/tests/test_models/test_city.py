#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage

class TestCity(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city2 = City()
        cls.city1.name = "Utako"
        cls.city2.name = "Ikeja"
        cls.city1.state_id = "89"
        cls.city2.state_id = "56"

    @classmethod
    def tearDownClass(cls):
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        self.assertTrue(self.city1.name, "Utako")
        self.assertTrue(self.city2.name, "Ikeja")
        self.assertTrue(self.city1.state_id, "89")
        self.assertTrue(self.city2.state_id, "56")
        assert self.city1.id != self.city2.id

    def test_save(self):
        self.city1.save()
        self.city2.save()
        assert self.city1.created_at != self.city1.updated_at
        assert self.city2.created_at != self.city2.updated_at

    def test_to_dict(self):
        c1_dict = self.city1.to_dict()
        c2_dict = self.city2.to_dict()
        self.assertTrue(type(c1_dict), dict)
        self.assertTrue(type(c2_dict), dict)
        self.assertTrue(type(c1_dict["created_at"]), str)
        self.assertTrue(type(c2_dict["updated_at"]), str)
        assert ("__class__" in c1_dict.keys()) == True
        city3 = City(**c1_dict)
        assert self.city1 != city3

    def test_class_attribute_exists(self):
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))

    def test_class_attribute_type(self):
        self.assertTrue(type(self.city1.state_id), str)
        self.assertTrue(type(self.city1.name), str)

