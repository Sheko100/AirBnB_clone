#!/usr/bin/python3
"""Module to define the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class that defines a place

    Args:
        city_id (str): the id of the City
        user_id (str); the id of the User
        name (str): the place name
        description (str): the place description
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): the price of the night
        latitude (float): the place latitude
        longitude (float): the place longitude
        amenity_ids (list): list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

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
