feature/media-review-display-class.py
class MediaReviewDisplay:

    def __init__(self, title, average_rating, reviews=None):
        """Initialize a media review display with validation."""
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if not isinstance(average_rating, (int, float)) or not (0 <= average_rating <= 5):
            raise ValueError("Average rating must be a number between 0 and 5")
        if reviews is None:
            reviews = []
        elif not isinstance(reviews, list):
            raise ValueError("Reviews must be a list of dictionaries")

        self._title = title
        self._average_rating = float(average_rating)
        self._reviews = reviews

    @property
    def title(self):
        """str: Get or set the media title."""
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def average_rating(self):
        """float: Get the average rating (read-only)."""
        return self._average_rating

    @property
    def reviews(self):
        """list: Get the list of reviews (read-only)."""
        return self._reviews

    def add_review(self, user, rating, comment=""):
        """Add a new review and update average rating."""
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
        review = {"user": user, "rating": rating, "comment": comment}
        self._reviews.append(review)
        self._update_average_rating()

    def _update_average_rating(self):
        """Recalculate the average rating based on reviews."""
        if not self._reviews:
            self._average_rating = 0
        else:
            total = sum(r["rating"] for r in self._reviews)
            self._average_rating = round(total / len(self._reviews), 2)

    def display(self):
        """Print a nicely formatted review section."""
        print("=" * 60)
        print(f"🎬  {self._title.upper()}  🎬".center(60))
        print("=" * 60)
        print(f"⭐ Average Rating: {self._average_rating:.2f}/5")
        print("-" * 60)

        if not self._reviews:
            print("No reviews available.")
        else:
            for i, review in enumerate(self._reviews, start=1):
                user = review.get("user", "Anonymous")
                rating = review.get("rating", "N/A")
                comment = review.get("comment", "(No comment)")
                print(f"\n🧾 Review #{i}")
                print(f"👤 User: {user}")
                print(f"⭐ Rating: {rating}/5")
                print(f"💬 Comment: {comment}")
                print("-" * 60)

        print("End of Reviews".center(60, "="))
        print("\n")

    def __str__(self):
        return f"{self._title} - Avg Rating: {self._average_rating:.2f}/5"

    def __repr__(self):
        return f"MediaReviewDisplay(title={self._title!r}, average_rating={self._average_rating}, reviews={self._reviews!r})"


if __name__ == "__main__":
    reviews = [
        {"user": "Alice", "rating": 4.8, "comment": "Amazing!"},
        {"user": "Bob", "rating": 3.5, "comment": "Good but long."}
    ]
    media = MediaReviewDisplay("Inception", 4.33, reviews)
    media.display()
    media.add_review("Charlie", 5, "Masterpiece!")
    print(media)
    print(repr(media))

git commit -m "Add MediaReviewDisplay class with validation, encapsulation, and Project 1 integration"
git push origin feature/media-review-display-class
