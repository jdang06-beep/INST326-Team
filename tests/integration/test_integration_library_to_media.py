"""
INTEGRATION TEST 3
LibraryItem ↔ ReviewableItem

Strategy:
Ensures reviewable media can successfully wrap library catalog items.

Coverage Rationale:
Validates compatibility between catalog storage and review system.
"""

import unittest
from cattaloglibrary import LibraryItem
from reviewable_item_hierarchy import AbstractMediaItem


class DummyMedia(AbstractMediaItem):
    def display(self):
        pass


class TestLibraryMediaIntegration(unittest.TestCase):

    def test_library_item_to_reviewable(self):
        lib_item = LibraryItem("Inception", "Movie", 2010)
        media = DummyMedia(lib_item.title)

        self.assertEqual(media.title, lib_item.title)
