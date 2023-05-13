#!/usr/bin/env python3
""" Test for BaseModel Class """
import os
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """ unit test for all methods in BaseModel """
    @classmethod
    def setUpClass(cls):
        """Testing attribute assignment"""
        cls.place1 = Place()
        cls.place2 = Place()
        cls.place1.name = "Water Park"
        cls.place2.name = "Max Cinema"
        cls.place1.city_id = "7648"
        cls.place2.city_id = "0293"

    @classmethod
    def tearDownClass(cls):
        """Testing for removing file path"""
        file_path = storage._FileStorage__file_path
        os.remove(file_path)
        print("Tearing down")

    def test_init(self):
        """Testing class attribute assignment"""
        self.assertTrue(self.place1.name, "Water Park")
        self.assertTrue(self.place2.name, "Max Cinema")
        self.assertTrue(self.place1.city_id, "7648")
        self.assertTrue(self.place2.city_id, "0293")
        assert self.place1.id != self.place2.id

    def test_save(self):
        """Testing save method"""
        self.place1.save()
        self.place2.save()
        assert self.place1.created_at != self.place1.updated_at
        assert self.place2.created_at != self.place2.updated_at

    def test_to_dict(self):
        """Testing to_dict method"""
        p1_dict = self.place1.to_dict()
        p2_dict = self.place2.to_dict()
        self.assertTrue(type(p1_dict), dict)
        self.assertTrue(type(p2_dict), dict)
        self.assertTrue(type(p1_dict["created_at"]), str)
        self.assertTrue(type(p2_dict["updated_at"]), str)
        assert ("__class__" in p1_dict.keys()) == True
        place3 = Place(**p1_dict)
        assert self.place1 != place3

    def test_class_attribute_exists(self):
        """Testing if class attribute exists"""
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_class_attribute_type(self):
        """Testing attribute type"""
        self.assertTrue(type(self.place1.city_id), str)
        self.assertTrue(type(self.place1.user_id), str)
        self.assertTrue(type(self.place1.name), str)
        self.assertTrue(type(self.place1.description), str)
        self.assertTrue(type(self.place1.number_rooms), int)
        self.assertTrue(type(self.place1.number_bathrooms), int)
        self.assertTrue(type(self.place1.max_guest), int)
        self.assertTrue(type(self.place1.price_by_night), int)
        self.assertTrue(type(self.place1.latitude), float)
        self.assertTrue(type(self.place1.longitude), float)
        self.assertTrue(type(self.place1.amenity_ids), list)
