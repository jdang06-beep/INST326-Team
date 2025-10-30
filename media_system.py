media_system/media_item.py
class MediaItem:
    """Represents a media item (movie, book, album, etc.)

    Attributes:
        item_id (str): unique identifier (read-only)
        title (str): human title
        media_type (str): e.g., 'book', 'movie'
        tags (List[str]): topical tags
        metadata (dict): arbitrary metadata like 'year', 'genre' etc.

    Example:
        >>> m = MediaItem("m1", "Dune", "book", tags=["sci-fi", "classic"])
        >>> m.title
        'Dune'
    """

    def __init__(self, item_id: str, title: str, media_type: str, tags: Optional[List[str]] = None,
                 metadata: Optional[Dict[str, Any]] = None):
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("item_id must be a non-empty string")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        if media_type not in {"book", "movie", "album", "game", "other"}:
            raise ValueError("media_type must be one of: 'book', 'movie', 'album', 'game', 'other'")

        self._item_id = item_id.strip()
        self._title = title.strip()
        self._media_type = media_type
        self._tags = list(tags) if tags else []
        self._metadata = dict(metadata) if metadata else {}
        self._reviews: List["Review"] = []

    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new: str):
        if not new or not isinstance(new, str):
            raise ValueError("title must be a non-empty string")
        self._title = new.strip()

    @property
    def tags(self) -> List[str]:
        return list(self._tags)

    @property
    def metadata(self) -> Dict[str, Any]:
        return dict(self._metadata)

    def add_tag(self, tag: str):
        if not tag or not isinstance(tag, str):
            raise ValueError("tag must be non-empty string")
        if tag not in self._tags:
            self._tags.append(tag)

    def add_review(self, review: "Review"):
        """Attach a Review instance to this MediaItem."""
        if not isinstance(review, Review):
            raise TypeError("review must be a Review instance")
        if review.media_item_id != self._item_id:
            raise ValueError("Review.media_item_id does not match this MediaItem.item_id")
        self._reviews.append(review)

    def average_rating(self) -> Optional[float]:
        """Return the average star rating or None if no reviews."""
        if not self._reviews:
            return None
        s = sum(r.stars for r in self._reviews)
        return s / len(self._reviews)

    def review_count(self) -> int:
        return len(self._reviews)

    def normalized_title(self) -> str:
        """Integration point: use Project 1 normalization function."""
        return project1_normalize_title(self._title)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self._item_id,
            "title": self._title,
            "media_type": self._media_type,
            "tags": list(self._tags),
            "metadata": dict(self._metadata),
            "avg_rating": self.average_rating(),
            "review_count": self.review_count()
        }

    def __str__(self):
        avg = self.average_rating()
        avg_str = f"{avg:.2f}/5" if avg is not None else "No ratings"
        return f"{self._title} ({self._media_type}) — {avg_str}"

    def __repr__(self):
        return f"MediaItem({self._item_id!r}, {self._title!r}, {self._media_type!r})"
      git add media_system/media_system.py
git commit -m "Add MediaItem class with validation, encapsulation, and Project 1 integration"
git push origin feature/mediaitem-class
