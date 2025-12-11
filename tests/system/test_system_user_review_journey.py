"""
SYSTEM TEST 2
User Review Journey

Strategy:
Simulates full user lifecycle from creation → review → storage.

Coverage Rationale:
Verifies real-world workflow works end-to-end.
"""

import unittest
from media_review_manager import User, Review
from containers import UserReviewList


class TestUserJourneySystem(unittest.TestCase):

    def test_user_review_journey(self):
        user = User("mia")
        review = Review("mia", 5, "Loved it")
        container = UserReviewList()

        user.save_review(review)
        container.add_saved_review(review)

        self.assertEqual(len(user.saved_reviews), 1)
        self.assertEqual(len(container.saved_reviews), 1)
