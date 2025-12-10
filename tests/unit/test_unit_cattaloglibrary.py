"""
UNIT TESTING STRATEGY – cattaloglibrary.py

Purpose:
Verifies core LibraryItem behavior independently of full Library system.

Coverage Rationale:
LibraryItem represents stored media in the catalog. If these fail,
persistence and querying will fail.
"""

import unittest
from cattaloglibrary import LibraryItem


class TestLibraryItemUnit(unittest.TestCase):
    """Coverage: LibraryItem initialization"""

    def test_library_item_creation(self):
        item = LibraryItem("Test", "Movie", 2020)
        self.assertEqual(item.title, "Test")
        self.assertEqual(item.media_type, "Movie")
        self.assertEqual(item.year, 2020)
