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

"""
---------------------------------------------------------------------------------------------------------------------------------
Eli's code below 
class LibraryItem:
    def __init__(self, title, author, year, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year}) — Copies: {self.copies}"
    @classmethod
    def from_user_input(cls):
        print("\n Add a New Library Item ")
        title = input("Enter the title: ").strip()
        author = input("Enter the author: ").strip()
        year = input("Enter the publication year: ").strip()
        try:
            copies = int(input("Enter number of copies: ").strip())
        except ValueError:
            copies = 1
            print("Invalid input for copies — defaulting to 1.")
        return cls(title, author, year, copies)

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            year=data.get("year"),
            copies=data.get("copies", 1)
        )
class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = []

    def add_item(self, item: LibraryItem):
        self.catalog.append(item)
        print(f"\n'{item.title}' has been added to {self.name} Library!")

    def list_items(self):
        if not self.catalog:
            print("\nThe library catalog is currently empty.")
        else:
            print(f"\n {self.name} Library Catalog ")
            for i, item in enumerate(self.catalog, start=1):
                print(f"{i}. {item}")

    @classmethod
    def from_list(cls, name, items_data):
        lib = cls(name)
        for data in items_data:
            item = LibraryItem.from_dict(data)
            lib.add_item(item)
        return lib
def main():
    my_lib = Library("Campus Library")
    print(f" Welcome to the {my_lib.name} Management System!")

    while True:
        print("\nMenu:")
        print("1. Add a new item")
        print("2. View catalog")
        print("3. Exit")
        choice = input("Enter your choice (1–3): ").strip()

        if choice == "1":
            new_item = LibraryItem.from_user_input()
            my_lib.add_item(new_item)
        elif choice == "2":
            my_lib.list_items()
        elif choice == "3":
            print("\n Exiting the Library Management System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
items = [
    {"title": "Nervous Conditions", "author": "Tsitsi Dangarembga", "year": 1988, "copies": 2},
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year": 1958, "copies": 1},
]

my_lib_2 = Library.from_list("Campus Library", items)
print(my_lib_2.list_items())"""
