#!/usr/bin/python3
"""Unittests for the Place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_attributes_updating(self):
        """Test that assigning a value for the email attribute and
        checks the value against the object attribute value
        """

        new_place = Place()

        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertIsInstance(new_place.amenity_ids, list)

        new_place.city_id = "asd5as25a4"
        new_place.user_id = "jdk4as664dok"
        new_place.name = "test place"
        new_place.description = "test description"
        new_place.number_rooms = 3
        new_place.number_bathrooms = 1
        new_place.max_guest = 2
        new_place.price_by_night = 50
        new_place.latitude = 4.54
        new_place.longitude = 8.67
        new_place.amenity_ids.append("udyw5qv25a4")

        self.assertEqual(new_place.city_id, "asd5as25a4")
        self.assertEqual(new_place.user_id, "jdk4as664dok")
        self.assertEqual(new_place.name, "test place")
        self.assertEqual(new_place.description, "test description")
        self.assertEqual(new_place.number_rooms, 3)
        self.assertEqual(new_place.number_bathrooms, 1)
        self.assertEqual(new_place.max_guest, 2)
        self.assertEqual(new_place.price_by_night, 50)
        self.assertEqual(new_place.latitude, 4.54)
        self.assertEqual(new_place.longitude, 8.67)
        self.assertEqual(new_place.amenity_ids[0], "udyw5qv25a4")
