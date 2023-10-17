#!/usr/bin/python3
"""Unittests for the City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class"""

    def test_attributes_updating(self):
        """Test that assigning a value for the attributes and
        checks the value against the object attributes values
        """

        new_city = City()

        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")

        new_city.state_id = "askjd654ashj4a"
        new_city.name = "Kafr al-Sheikh"

        self.assertEqual(new_city.state_id, "askjd654ashj4a")
        self.assertEqual(new_city.name, "Kafr al-Sheikh")
