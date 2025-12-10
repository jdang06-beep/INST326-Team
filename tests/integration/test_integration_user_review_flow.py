"""
INTEGRATION TESTING STRATEGY – User <-> Review <-> ReviewList

Purpose:
Verifies interaction between User, Review, and UserReviewList.

Coverage Rationale:
If these components do not integrate correctly, user-facing review
features will fail even if individual units pass.
"""

import unittest
from media_review_manager import User, Review
from containers import UserReviewList


class TestUserReviewIntegration(unittest.TestCase):

    def test_user_saves_and_lists_review(self):
        user = User("alice")
        review = Review("alice", 5, "Excellent")
        review_list = UserReviewList()

        user.save_review(review)
        review_list.add_saved_review(review)

        self.assertEqual(len(user.saved_reviews), 1)
        self.assertEqual(len(review_list.saved_reviews), 1)
