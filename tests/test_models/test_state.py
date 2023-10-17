#!/usr/bin/python3
"""Unittests for the State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_attributes_updating(self):
        """Test that assigning a value for the attributes and
        checks the value against the object attributes values
        """

        new_state = State()

        self.assertEqual(new_state.name, "")

        new_state.name = "Kafr al-Sheikh"

        self.assertEqual(new_state.name, "Kafr al-Sheikh")
