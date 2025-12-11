"""
INTEGRATION TEST 2
Review ↔ ReviewableMediaItem

Strategy:
Verifies that reviews attach correctly to reviewable media items.

Coverage Rationale:
Critical for ensuring user reviews connect to actual media objects.
"""

import unittest
from media_review_manager import Review
from reviewable_item_hierarchy import AbstractMediaItem


class DummyMedia(AbstractMediaItem):
    def display(self):
        pass


class TestReviewToMediaIntegration(unittest.TestCase):

    def test_review_attaches_to_media(self):
        media = DummyMedia("Movie")
        review = Review("bob", 4, "Good")

        media.add_review(review)

        self.assertEqual(len(media.reviews), 1)
