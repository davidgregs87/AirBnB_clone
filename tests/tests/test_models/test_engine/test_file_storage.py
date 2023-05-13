#!/usr/bin/env python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def teardownClass(cls):
       file_path = store._FileStorage__file_path
       os.remove(file_path)
       print("Tearing down")

    def test_init(self):
        self.assertTrue(isinstance(self.store, FileStorage), True)

    def test_all(self):
        obj_dict = self.store.all()
        self.assertTrue(type(obj_dict), dict)

    def test_new(self):
        self.store.new(self.base)
        obj_dict = self.store.all()
        obj_list = list(obj_dict.values())
        self.assertTrue(isinstance(obj_list[0], BaseModel))

    def test_save(self):
        self.store.save()
        self.assertTrue(os.path.exists(self.store._FileStorage__file_path), True)

    def test_reload(self):
        obj_dict1 = self.store.all()
        print(obj_dict1)
        self.store.new(self.base)
        self.store.save()
        self.store.reload()
        obj_dict2 = self.store.all()
        print(obj_dict2)
        assert obj_dict1 == obj_dict2
