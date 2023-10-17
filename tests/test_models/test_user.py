#!/usr/bin/python3
"""Unittests for the User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the City class"""

    def test_email_updating(self):
        """Test that assigning a value for the email attribute and
        checks the value against the object attribute value
        """

        new_user = User()

        self.assertEqual(new_user.email, "")
        new_user.email = "test@test.com"
        self.assertEqual(new_user.email, "test@test.com")

    def test_password_updating(self):
        """Test that assigning a value for the email attribute and
        checks the value against the object attribute value
        """

        new_user = User()
        self.assertEqual(new_user.password, "")
        new_user.password = "testpass"
        self.assertEqual(new_user.password, "testpass")


    def test_first_name_updating(self):
        """Test that assigning a value for the email attribute and
        checks the value against the object attribute value
        """

        new_user = User()
        self.assertEqual(new_user.first_name, "")
        new_user.first_name = "Ali"
        self.assertEqual(new_user.first_name, "Ali")

    def test_last_name_updating(self):
        """Test that assigning a value for the email attribute and
        checks the value against the object attribute value
        """

        new_user = User()
        self.assertEqual(new_user.last_name, "")
        new_user.last_name = "Akram"
        self.assertEqual(new_user.last_name, "Akram")



