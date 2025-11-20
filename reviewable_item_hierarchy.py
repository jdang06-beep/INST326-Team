"""
Inheritance hierarchy for reviews of media/library items.

This module contains...
- A base class (abstract) that defines the common interface all items must follow 
- 3 subclasses that specialize the base class
- Method overriding with super()
"""

from abc import ABC, abstractmethod

class ReviewableItem(ABC): # Base class
    def __init__(self, title):
        self.title = title
        self.reviews = []  # list of (rating, text)

    def add_review(self, rating, text):
        # Shared method: all items support adding reviews.
        self.reviews.append((rating, text))

    @abstractmethod
    def display_review_summary(self):
        # Each subclass displays its review summary differently.
        pass


class LibraryItem(ReviewableItem): # First subclass
    def __init__(self, title, author, year):
        super().__init__(title)  # calls base constructor
        self.author = author
        self.year = year

    def display_review_summary(self):
        # Override with book-specific details.
        base_avg = (
            sum(r[0] for r in self.reviews) / len(self.reviews)
            if self.reviews else "No reviews yet"
        )
        return (f"Book: {self.title} by {self.author} ({self.year})\n"
                f"Average Rating: {base_avg}")
    

class MediaItem(ReviewableItem): # Second subclass
    def __init__(self, title, media_type, duration):
        super().__init__(title)
        self.media_type = media_type
        self.duration = duration  # minutes or equivalent

    def display_review_summary(self):
        # Override with media-specific formatting.
        avg = (
            sum(r[0] for r in self.reviews) / len(self.reviews)
            if self.reviews else "No ratings"
        )
        return (f"{self.media_type}: {self.title} ({self.duration} min)\n"
                f"Avg User Rating: {avg}")


class UserReviewList(ReviewableItem): # Third subclass
    def __init__(self, username):
        super().__init__(username)
        self.username = username
        self.saved = []

    def add_saved_review(self, item_title, rating):
        self.saved.append((item_title, rating))

    def display_review_summary(self):
        # Override with user-focused summary.
        count = len(self.saved)
        return (f"User: {self.username}\n"
                f"Saved Reviews: {count}")