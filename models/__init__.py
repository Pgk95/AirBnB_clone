#!/usr/bin/python3
"""initializes the storage package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
