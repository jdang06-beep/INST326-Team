"""
INTEGRATION TEST 1
User ↔ Review ↔ UserReviewList

Strategy:
Tests full interaction between user, review creation, and container storage.

Coverage Rationale:
Ensures review data properly propagates between core subsystems.
"""

import unittest
from media_review_manager import User, Review
from containers import UserReviewList


class TestUserReviewFlow(unittest.TestCase):

    def test_user_review_saved_and_stored(self):
        user = User("alice")
        review = Review("alice", 5, "Excellent")
        container = UserReviewList()

        user.save_review(review)
        container.add_saved_review(review)

        self.assertEqual(len(user.saved_reviews), 1)
        self.assertEqual(len(container.saved_reviews), 1)
