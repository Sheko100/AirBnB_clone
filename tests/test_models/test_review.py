#!/usr/bin/python3
"""Unittests for the Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_attributes_updating(self):
        """Test that assigning a value for the attributes and
        checks the value against the object attributes values
        """

        new_review = Review()

        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")

        new_review.place_id = "asjkas545aska5"
        new_review.user_id = "65shjas46ajs"
        new_review.text = "test text"

        self.assertEqual(new_review.place_id, "asjkas545aska5")
        self.assertEqual(new_review.user_id, "65shjas46ajs")
        self.assertEqual(new_review.text, "test text")
