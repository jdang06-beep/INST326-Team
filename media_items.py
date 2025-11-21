# media_items.py

from abc import ABC, abstractmethod


class AbstractMediaItem(ABC):
    """Abstract base class for all media items."""

    def __init__(self, item_id, title, creator, genre, release_year):
        self.item_id = item_id
        self.title = title
        self.creator = creator
        self.genre = genre
        self.release_year = release_year
        self.reviews = []

    @abstractmethod
    def get_media_type(self):
        pass

    @abstractmethod
    def get_default_review_scale(self):
        pass

    @abstractmethod
    def get_summary(self):
        pass

    @abstractmethod
    def calculate_engagement_score(self):
        pass

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        return f"{self.title} ({self.release_year}) by {self.creator}"

#Concrete media subclasses

class Book(AbstractMediaItem):
    """Concrete media item representing a book."""

    def get_media_type(self):
        return "Book"

    def get_default_review_scale(self):
        return "1–5"

    def get_summary(self):
        return f"'{self.title}' is a book written by {self.creator}."

    def calculate_engagement_score(self):
        """Simple engagement score: number of reviews * 1.2"""
        return len(self.reviews) * 1.2


class Film(AbstractMediaItem):
    """Concrete media item representing a film."""

    def get_media_type(self):
        return "Film"

    def get_default_review_scale(self):
        return "1–10"

    def get_summary(self):
        return f"{self.title} is a film directed by {self.creator}."

    def calculate_engagement_score(self):
        """Reviews are higher weight for movies."""
        return len(self.reviews) * 2.5


class AudioRecording(AbstractMediaItem):
    """Media object that symbolizes podcasts, music, etc."""

    def get_media_type(self):
        return "Audio Recording"

    def get_default_review_scale(self):
        return "1–7"

    def get_summary(self):
        return f"{self.title} is an audio recording by {self.creator}."

    def calculate_engagement_score(self):
        """Engagement is measured differently in audio recordings."""
        return len(self.reviews) * 0.9
