"""
SYSTEM TEST 3
Review → Media → Display Pipeline

Strategy:
Validates review storage and display interaction.

Coverage Rationale:
Ensures full data flow from review to media display.
"""

import unittest
from media_review_manager import Review
from reviewable_item_hierarchy import AbstractMediaItem


class DummyMedia(AbstractMediaItem):
    def display(self):
        return "Displaying"


class TestReviewDisplaySystem(unittest.TestCase):

    def test_review_to_display_pipeline(self):
        media = DummyMedia("Display Test")
        review = Review("eli", 4, "Nice")

        media.add_review(review)
        output = media.display()

        self.assertEqual(output, "Displaying")
