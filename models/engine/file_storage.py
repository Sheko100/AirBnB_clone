#!/usr/bin/python3
"""Module to define FileStorage class"""

import importlib
import json
import os


class FileStorage:
    """Defines a FileStorage class

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gets the __objects attribute

        Returns:
            __objects attribute
        """

        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects attribute

        Args:
            obj (object): an instance of the BaseModel class
        """
        cls_name = obj.__class__.__name__
        key = "{}.{}".format(cls_name, obj.id)
        objects = self.all()
        objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file with __file_path path
        """

        objects = self.all()
        objects_to_save = {}

        for id, obj in objects.items():
            objects_to_save[id] = obj.to_dict()

        jsons = json.dumps(objects_to_save)

        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            file.write(jsons)

    def reload(self):
        """Deserializes the JSON file into the __objects attribute
        """

        modules = {"BaseModel": "base_model",
                   "User": "user",
                   "State": "state",
                   "City": "city",
                   "Amenity": "amenity",
                   "Place": "place",
                   "Review": "review"
                   }
        file_path = self.__file_path
        if os.path.isfile(file_path):
            with open(file_path, encoding="utf-8") as file:
                jsons = file.read()

            objects_to_load = json.loads(jsons)
            for id, dct in objects_to_load.items():
                cls_name = dct["__class__"]
                model_path = "..{}".format(modules[cls_name])
                module = importlib.import_module(model_path, "models.engine")
                cls = getattr(module, dct["__class__"])
                obj = cls(**dct)
                self.new(obj)
