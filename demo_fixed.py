from media_system import MediaItem
from cattaloglibrary import Library, LibraryItem

def demonstrate_polymorphism():
    print("\n" + "=" * 60)
    print("Polymorphism & Media Demonstration")
    print("=" * 60)

    print("\nMedia item polymorphism demonstration:\n")

    items = [
        MediaItem("m1", "The Great Gatsby", "book"),
        MediaItem("m2", "Now You See Me", "movie"),
        MediaItem("m3", "Jazz Classics", "album")
    ]

    for i, item in enumerate(items):
        item._reviews = [{"stars": 5}] * (i + 1)

    for item in items:
        print(f"{item.title} ({item._media_type}):")
        avg = sum(r["stars"] for r in item._reviews) / len(item._reviews)
        print(f" Review Count: {len(item._reviews)}")
        print(f" Average Rating: {avg:.1f}")
        print()

    print("=" * 60)
    print("Library Container Demonstration")
    print("=" * 60)

    library = Library("Campus Library")

    for item in items:
        lib_item = LibraryItem(item.title, "Unknown Author", 2025)
        library.add_item(lib_item)

    print("\nLibrary Catalog:")
    library.list_items()

    print("\nOptional: Add a new item via LibraryItem.from_user_input():")
    new_item = LibraryItem.from_user_input()
    library.add_item(new_item)

    print("\nUpdated Library Catalog:")
    library.list_items()


if __name__ == "__main__":
    demonstrate_polymorphism()
