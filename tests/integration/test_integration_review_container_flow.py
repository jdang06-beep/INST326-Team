"""
INTEGRATION TEST 5
Review ↔ Multiple Containers

Strategy:
Tests review moving between user and global containers.

Coverage Rationale:
Validates consistency across multiple collection dependencies.
"""

import unittest
from media_review_manager import User, Review
from containers import UserReviewList


class TestReviewContainerFlow(unittest.TestCase):

    def test_review_moves_between_containers(self):
        user = User("sam")
        review = Review("sam", 3, "Okay")
        container = UserReviewList()

        user.save_review(review)
        container.add_saved_review(review)

        self.assertIn(review, user.saved_reviews)
        self.assertIn(review, container.saved_reviews)
