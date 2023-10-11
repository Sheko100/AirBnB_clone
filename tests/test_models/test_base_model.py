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
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_model_uniquness(self):
        """Test that the instances are different entities
        """

        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1, obj2)

    def test_id_type(self):
        """Test that the id attribute is a string
        """

        obj1 = BaseModel()
        self.assertEqual(type(obj1.id), str)

    def test_id_length(self):
        """Test that the id attribute using UUID4 is a length of 36 chars
        """

        obj1 = BaseModel()
        self.assertEqual(len(obj1.id), 36)

    def test_instance_type(self):
        """Test that the instance class is BaseModel
        """

        obj1 = BaseModel()
        self.assertIsInstance(obj1, BaseModel)

    def test_instance_str(self):
        """Test that the string representaion of the instance is
        in the correct format
        """

        obj1 = BaseModel()
        objstr = "[BaseModel] ({}) {}".format(obj1.id, obj1.__dict__)
        self.assertEqual(str(obj1), objstr)

    def test_save_method(self):
        """Test that the save method has changed the updated_at attribute
        """

        obj1 = BaseModel()
        olddate = obj1.updated_at
        obj1.save()
        self.assertTrue(olddate < obj1.updated_at)

    def test_create_time(self):
        """Test that the object created_at attribute is less than the current
        actual time
        """

        obj1 = BaseModel()
        date_now = datetime.now()
        self.assertTrue(obj1.created_at < date_now)

    def test_to_dict(self):
        """Test that the dictionary returned from to_dict method has
        the correct keys and values
        """

        obj1 = BaseModel()
        dct = obj1.__dict__
        newdct = obj1.to_dict()
        for key in dct:
            self.assertIn(key, newdct)

        self.assertIn("__class__", newdct)
        self.assertEqual(newdct["__class__"], "BaseModel")
        self.assertEqual(newdct["created_at"], dct["created_at"].isoformat())
        self.assertEqual(newdct["updated_at"], dct["updated_at"].isoformat())
