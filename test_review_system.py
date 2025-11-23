"""
Comprehensive test suite for review system.

Tests inheritance, abstract base classes, polymorphism, and composition.
"""

import unittest
from reviewable_items import (
    ReviewableItem,
    LibraryItem,
    MediaItem,
    UserReviewList
)
from media_item_classes import (
    AbstractMediaItem,
    Book,
    Film,
    AudioRecording
)
from abc import ABC


class TestReviewableInheritance(unittest.TestCase):
    """Test inheritance for ReviewableItem hierarchy."""

    def test_subclasses_inherit_from_reviewable_item(self):
        """Ensure all reviewable subclasses inherit from ReviewableItem."""
        book_item = LibraryItem("Dune", "Frank Herbert", 1965)
        media_item = MediaItem("Podcast Episode", "Podcast", 45)
        user_reviews = UserReviewList("jolina")

        self.assertIsInstance(book_item, ReviewableItem)
        self.assertIsInstance(media_item, ReviewableItem)
        self.assertIsInstance(user_reviews, ReviewableItem)


class TestReviewableAbstractMethods(unittest.TestCase):
    """Test abstract base behavior for ReviewableItem."""

    def test_cannot_instantiate_abstract_reviewable_item(self):
        """ReviewableItem should not instantiate because it has abstract methods."""
        with self.assertRaises(TypeError):
            ReviewableItem("test")

    def test_subclasses_implement_display_summary(self):
        """Check subclasses implement the abstract method display_review_summary."""

        book_item = LibraryItem("Dune", "Frank Herbert", 1965)
        media_item = MediaItem("Podcast Episode", "Podcast", 45)
        user_reviews = UserReviewList("jolina")

        for obj in (book_item, media_item, user_reviews):
            self.assertTrue(callable(obj.display_review_summary))



class TestMediaInheritance(unittest.TestCase):
    """Test inheritance relationships for media items."""

    def test_subclasses_inherit_from_abstract_media_item(self):
        """Ensure all concrete media types inherit from AbstractMediaItem."""

        book = Book("b1", "1984", "George Orwell", "Dystopian", 1949)
        film = Film("f1", "Inception", "Christopher Nolan", "Sci-Fi", 2010)
        audio = AudioRecording("a1", "The Daily", "NYT", "Podcast", 2024)

        self.assertIsInstance(book, AbstractMediaItem)
        self.assertIsInstance(film, AbstractMediaItem)
        self.assertIsInstance(audio, AbstractMediaItem)


class TestAbstractMediaItemBehavior(unittest.TestCase):
    """Test abstract base class rules & implementation requirements."""

    def test_cannot_instantiate_abstract_base_class(self):
        """AbstractMediaItem must not be instantiable because it has abstract methods."""

        with self.assertRaises(TypeError):
            AbstractMediaItem("x1", "Test", "Creator", "Genre", 2000)

    def test_concrete_classes_implement_all_abstract_methods(self):
        """Verify concrete subclasses implement required abstract methods."""

        book = Book("b1", "Dune", "Frank Herbert", "Sci-Fi", 1965)
        film = Film("f1", "The Matrix", "Wachowskis", "Sci-Fi", 1999)
        audio = AudioRecording("a1", "Podcast Ep 1", "Host", "Talk", 2023)

        for obj in (book, film, audio):
            self.assertTrue(callable(obj.get_media_type))
            self.assertTrue(callable(obj.get_default_review_scale))
            self.assertTrue(callable(obj.get_summary))
            self.assertTrue(callable(obj.calculate_engagement_score))

    def test_abstract_methods_return_unique_values(self):
        """Check polymorphic behavior: each subclass should respond differently."""

        book = Book("b1", "1984", "George Orwell", "Dystopian", 1949)
        film = Film("f1", "Inception", "Christopher Nolan", "Sci-Fi", 2010)
        audio = AudioRecording("a1", "The Daily", "NYT", "Podcast", 2024)

        self.assertEqual(book.get_media_type(), "Book")
        self.assertEqual(film.get_media_type(), "Film")
        self.assertEqual(audio.get_media_type(), "Audio Recording")

        self.assertEqual(book.get_default_review_scale(), "1–5")
        self.assertEqual(film.get_default_review_scale(), "1–10")
        self.assertEqual(audio.get_default_review_scale(), "1–7")

    def test_engagement_score_calculations(self):
        """Verify that engagement scoring formulas differ per subclass."""

        book = Book("b1", "Dune", "Frank Herbert", "Sci-Fi", 1965)
        film = Film("f1", "Interstellar", "Christopher Nolan", "Sci-Fi", 2014)
        audio = AudioRecording("a1", "Music Track", "Artist", "Pop", 2022)

        # Add simple review objects
        book.add_review("good")
        book.add_review("great")

        film.add_review("amazing")
        film.add_review("incredible")
        film.add_review("wow")

        audio.add_review("nice")

        self.assertEqual(book.calculate_engagement_score(), 2 * 1.2)
        self.assertEqual(film.calculate_engagement_score(), 3 * 2.5)
        self.assertEqual(audio.calculate_engagement_score(), 1 * 0.9)


if __name__ == "__main__":
    unittest.main()
