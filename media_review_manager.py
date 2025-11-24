"""
This module demonstrates "has-a" relationships (composition) between objects
without using inheritance.

Composition is chosen over inheritance because:
- A Review is not a type of MediaItem, so a MediaItem cannot inherit from Review.
- A User is not a type of Review or MediaItem.
- MediaReviewDisplay is not a type of MediaItem or User.
- We want flexible relationships
"""
# demo of classes
class Review:
    # represents a review for a media item
    def __init__(self, media_item_id, user, stars, comment=""):
        self.media_item_id = media_item_id
        self.user = user
        self.stars = stars
        self.comment = comment


class MediaItem:
    # represents a media item 

    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self._reviews = []  # composition: MediaItem "has-a" list of Review objects

    def add_review(self, review):
        # attach a Review instance to this MediaItem
        if review.media_item_id != self.item_id:
            raise ValueError("Review does not belong to this MediaItem")
        self._reviews.append(review)  # composition: linking MediaItem to Review

    def average_rating(self):
        # return the average star rating or None if no reviews
        if not self._reviews:
            return None
        total = sum(r.stars for r in self._reviews)
        return total / len(self._reviews)

    def review_count(self):
        return len(self._reviews)


class User:
    # represents a user in the system

    def __init__(self, username):
        self.username = username
        self.saved_reviews = []  # composition: User "has-a" collection of saved Review objects

    def save_review(self, review):
        self.saved_reviews.append(review)  # composition: storing Review in User


class MediaReviewDisplay:
    # represents a display for reviews of a MediaItem

    def __init__(self, media_item):
        self.media_item = media_item      # composition: Display "has-a" MediaItem
        self.display_reviews = media_item._reviews  # composition: Display "has-a" list of Review objects

    def show_reviews(self):
        print(f"\n=== Reviews for {self.media_item.title} ===")
        if not self.display_reviews:
            print("No reviews yet.")
            return
        for r in self.display_reviews:
            print(f"User: {r.user}, Stars: {r.stars}, Comment: {r.comment}")
        print(f"Average Rating: {self.media_item.average_rating():.2f} ({self.media_item.review_count()} reviews)")

# demo of composition
def demonstrate_composition():
    print("\n--- Composition Demonstration ---\n")

    # create a media item
    movie = MediaItem("m1", "Movie1")

    # create users
    ali = User("Ali")
    bob = User("Bob")

    # create reviews (composition: MediaItem "has-a" Review)
    review1 = Review("m1", ali.username, 5, "Amazing movie!")
    review2 = Review("m1", bob.username, 4, "Really enjoyed it!")

    # add reviews to media item (composition: linking MediaItem to its Reviews)
    movie.add_review(review1)
    movie.add_review(review2)

    # users save reviews (composition: User "has-a" Review)
    ali.save_review(review1)
    bob.save_review(review2)

    # create display (composition: Display "has-a" MediaItem and its Reviews)
    display = MediaReviewDisplay(movie)

    # show results
    display.show_reviews()

    print("\n--- End of Composition Demonstration ---\n")

# running demo
if __name__ == "__main__":
    demonstrate_composition()
