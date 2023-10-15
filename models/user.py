#!/usr/bin/python3
"""Module to define the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a User

    Args:
    email (str): the user email
    password (str): the user password
    first_name (str): the user first name
    last_name (str): the user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the instance

        Args:
            args: positional arguments
            kwargs: named arguments
        """
        if len(kwargs) < 1:
            super().__init__()
        else:
            super().__init__(**kwargs)
