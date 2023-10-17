#!/usr/bin/python3
"""Unittests for the Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_attributes_updating(self):
        """Test that assigning a value for the attributes and
        checks the value against the object attributes values
        """

        new_amenity = Amenity()

        self.assertEqual(new_amenity.name, "")

        new_state.name = "test amenity name"

        self.assertEqual(new_state.name, "test amenity name")
