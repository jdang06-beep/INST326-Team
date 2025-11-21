lass FavoritesContainer(AbstractReviewContainer):
    """Lst of favorite media items from the user."""

    def add_item(self, media_item):
        # makes sure there are no duplicates 
        if media_item not in self.media_items:
            self.media_items.append(media_item)

    def remove_item(self, media_item):
        if media_item in self.media_items:
            self.media_items.remove(media_item)

    def get_items(self):
        return self.media_items

    def get_container_type(self):
        return "Favorites"


class WatchlistContainer(AbstractReviewContainer):
    """A container representing items a user plans to watch/read."""

    def add_item(self, media_item):
        # Duplicates allowed because of the different behavior
        self.media_items.append(media_item)

    def remove_item(self, media_item):
        # Gets rid of the first occurrence
        if media_item in self.media_items:
            self.media_items.remove(media_item)

    def get_items(self):
        return self.media_items

    def get_container_type(self):
        return "Watchlist"
