"""
UNIT TESTING STRATEGY – reviewable_item_hierarchy.py

Purpose:
Confirms reviewable items can store and track reviews.

Coverage Rationale:
Reviewable items form the backbone of the review system. Review tracking
must be correct for analytics and display.
"""

import unittest
from reviewable_item_hierarchy import AbstractMediaItem
from media_review_manager import Review


class DummyMedia(AbstractMediaItem):
    def display(self):
        pass


class TestReviewableItemUnit(unittest.TestCase):
    """Coverage: Review storage"""

    def test_add_review(self):
        item = DummyMedia("Test")
        review = Review("user", 5, "Nice")
        item.add_review(review)
        self.assertEqual(len(item.reviews), 1)
