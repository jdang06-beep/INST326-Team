

def demonstrate_polymorphism():
    print("\n" + "=" * 60)
    print("Polymorphism demonstration")
    print("=" * 60)

    # ---- MEDIA POLYMORPHISM ----
    print("\nMedia item polymorphism:\n")

    items = [
        Book("The Great Gatsby", "Here Comes The Sun", "Lord Of The Files", "Hunger Games", 1949),
        Film("Now You See Me", "Spy", "Wolf Of Walstreet", "Madea", 2010),
        AudioRecording("Jazz", "Blues", "Country", "Soul", 1959)
    ]

    # Pretend each item has some reviews
    for i, item in enumerate(items):
        for _ in range(i + 1):
            item.add_review("Sample Review")

    for item in items:
        print(f"{item.title} ({item.get_media_type()}):")
        print(f" Review Scale: {item.get_default_review_scale()}")
        print(f" Engagement Score: {item.calculate_engagement_score()}")
        print()

    # ---- CONTAINER POLYMORPHISM ----
    print("=" * 60)
    print("REVIEW CONTAINER POLYMORPHISM")
    print("=" * 60)

    containers = [
        FavoritesContainer("c1", "My Favorites"),
        WatchlistContainer("c2", "Weekend Watchlist"),
    ]

    # Add same items but behavior differs
    print("\nAdding media items to both containers...\n")
    for cont in containers:
        cont.add_item(items[0])
        cont.add_item(items[0])   # second add shows duplicate behavior difference

    for cont in containers:
        print(f"{cont.name} ({cont.get_container_type()}):")
        print(f"  Number of items: {len(cont.get_items())}")
        print(f"  Items: {[m.title for m in cont.get_items()]}")
        print()

if __name__ == "__main__":
    demonstrate_polymorphism()
