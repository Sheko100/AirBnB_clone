#!/usr/bin/python3
"""Unittest for FileStorage class
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class attributes and methods
    """

    def test_all_method(self):
        """Test that the all method returning a dictionary
        """

        fs = FileStorage()

        objs = fs.all()

        self.assertIsInstance(objs, dict)

    def test_new_method(self):
        """Test that checks the normal behavior of new method
        """

        fs = FileStorage()
        model1 = BaseModel()

        cls_name = model1.__class__.__name__
        model_key = "{}.{}".format(cls_name, model1.id)

        fs.new(model1)
        models_dct = fs.all()

        self.assertIn(model_key, models_dct)
        self.assertEqual(models_dct[model_key], model1)

    def test_save_method(self):
        """Test that checks the normal behavior of the save method
        """
        file_path = "file.json"

        if os.path.isfile(file_path):
            os.remove(file_path)

        fs = FileStorage()

        fs.save()
        fs.reload()

        self.assertTrue(os.path.isfile(file_path))

        os.remove(file_path)

    def test_reload_method(self):
        """Test that checks the normal behavior of the reload method
        """

        fs = FileStorage()
        model1 = BaseModel()
        model2 = BaseModel()

        fs.save()
        fs.reload()
        objects = fs.all()
        cls_name = model1.__class__.__name__
        model1_key = "{}.{}".format(cls_name, model1.id)

        self.assertIn(model1_key, objects)
        model1_id = objects[model1_key].id
        self.assertEqual(model1_id, model1.id)

        model2_key = "{}.{}".format(cls_name, model2.id)
        self.assertIn(model2_key, objects)
        model2_id = objects[model2_key].id
        self.assertEqual(model2_id, model2.id)

        file_path = "file.json"
        if os.path.isfile(file_path):
            os.remove(file_path)
