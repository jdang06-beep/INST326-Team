"""
UNIT TESTING STRATEGY – media_review_manager.py

Purpose:
Tests core user and review logic in isolation without persistence.
Ensures Review objects store data correctly and Users can save reviews.

Coverage Rationale:
media_review_manager.py contains core business logic for user-generated
reviews. If this fails, recommendations and displays will be incorrect.
"""

import unittest
from media_review_manager import Review, User


class TestReviewUnit(unittest.TestCase):
    """Coverage: Review object attribute storage"""

    def test_review_creation(self):
        r = Review("alice", 5, "Great movie")
        self.assertEqual(r.username, "alice")
        self.assertEqual(r.rating, 5)
        self.assertEqual(r.text, "Great movie")


class TestUserUnit(unittest.TestCase):
    """Coverage: User saving reviews"""

    def test_user_saves_review(self):
        user = User("bob")
        review = Review("bob", 4, "Good")
        user.save_review(review)
        self.assertEqual(len(user.saved_reviews), 1)
