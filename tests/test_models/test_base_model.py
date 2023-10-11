#!/usr/bin/python3
"""Module to test BaseModel class
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel"""

    def test_id_uniquness(self):
        """Test that the instances ids are different
        """
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

    def test_model_uniquness(self):
        """Test that the instances are different entities
        """

        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1, model2)

    def test_id_type(self):
        """Test that the id attribute is a string
        """

        model1 = BaseModel()
        self.assertEqual(type(model1.id), str)

    def test_id_length(self):
        """Test that the id attribute using UUID4 is a length of 36 chars
        """

        model1 = BaseModel()
        self.assertEqual(len(model1.id), 36)

    def test_instance_type(self):
        """Test that the instance class is BaseModel
        """

        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)

    def test_instance_str(self):
        """Test that the string representaion of the instance is
        in the correct format
        """

        model1 = BaseModel()
        modelstr = "[BaseModel] ({}) {}".format(model1.id, model1.__dict__)
        self.assertEqual(str(model1), modelstr)

    def test_save_method(self):
        """Test that the save method has changed the updated_at attribute
        """

        model1 = BaseModel()
        olddate = model1.updated_at
        model1.save()
        self.assertTrue(olddate < model1.updated_at)

    def test_create_time(self):
        """Test that the object created_at attribute is less than the current
        actual time
        """

        model1 = BaseModel()
        date_now = datetime.now()
        self.assertTrue(model1.created_at < date_now)

    def test_to_dict(self):
        """Test that the dictionary returned from to_dict method has
        the correct keys and values
        """

        model1 = BaseModel()
        dct = model1.__dict__
        newdct = model1.to_dict()
        for key in dct:
            self.assertIn(key, newdct)

        self.assertIn("__class__", newdct)
        self.assertEqual(newdct["__class__"], "BaseModel")
        self.assertEqual(newdct["created_at"], dct["created_at"].isoformat())
        self.assertEqual(newdct["updated_at"], dct["updated_at"].isoformat())

    def test_copy_model(self):
        """Test the behavior of creating a model from another
        """

        model1 = BaseModel()
        dct = model1.to_dict()

        model2 = BaseModel(**dct)
        self.assertNotEqual(model1, model2)
        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.created_at, model2.created_at)

    def test_copy_model_with_empty_dict(self):
        """Test the behavior of passing an empty dictionary
        """

        dct = {}
        model1 = BaseModel(**dct)
        self.assertIn("id", model1.__dict__)

    def test_copy_model_time_type(self):
        """Test that the created_at and updated_at attributes are a datetime
        objects after copying
        """

        model1 = BaseModel()
        dct = model1.to_dict()
        model2 = BaseModel(**dct)
        self.assertIsInstance(model2.created_at, datetime)
        self.assertIsInstance(model2.updated_at, datetime)
