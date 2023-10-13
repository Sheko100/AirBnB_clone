#!/usr/bin/python3
"""Module to initialize variables
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
