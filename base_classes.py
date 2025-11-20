"""
Abstract base classes for the Media Review Library 

This module defines the abstract interfaces that all concrete media item
and review classes must implement.
"""
from abc import ABC, abstractmethod


class AbstractMediaItem(ABC):
    """Abstract base class for all media items.
    
    This class defines the interface that all media item types must implement,
    ensuring consistent behavior across different media formats.
    """
    
    def __init__(self, item_id, title, creator, genre, release_year):
        """Initialize a media item.
        
        Args:
            item_id (str): Unique identifier for the media item
            title (str): Title of the media (e.g., book title, film title)
            creator (str): Primary creator (e.g., author, director, producer)
            genre (str): Media genre
            release_year (int): Year the media item was released
        """
        self.item_id = item_id
        self.title = title
        self.creator = creator
        self.genre = genre
        self.release_year = release_year
        self.reviews = []
        
    @abstractmethod
    def get_media_type(self):
        """Return the type of media.
        
        Returns:
            str: Description of the media type (e.g., "Book", "Film")
        """
        pass
    
    @abstractmethod
    def get_default_review_scale(self):
        """Return the rating scale used for this media type.
        
        Returns:
            str: Description of the rating scale (e.g., "1–5", "1–10")
        """
        pass
    
    @abstractmethod
    def get_summary(self):
        """Return a short description or summary of the media.
        
        Returns:
            str: Summary text
        """
        pass
    
    @abstractmethod
    def calculate_engagement_score(self):
        """Calculate a media-specific engagement score.
        
        Returns:
            float: Engagement score based on format-specific criteria
        """
        pass
    
    def add_review(self, review):
        """Add a review to this media item.
        
        Args:
            review: Review object to associate with this media item
        """
        self.reviews.append(review)
    
    def __str__(self):
        """String representation of the media item."""
        return f"{self.title} ({self.release_year}) by {self.creator}"


class AbstractReviewContainer(ABC):
    """Abstract base class for all review containers.
    
    Defines the interface that any class holding collections of media items
    and their reviews must implement to ensure polymorphic behavior across
    different container types.
    """
    
    def __init__(self, container_id, name, description=None):
        """Initialize a review container.
        
        Args:
            container_id (str): Unique identifier for the container
            name (str): Name of the container (e.g., "Favorites", "Watchlist")
            description (str, optional): Optional description of the container
        """
        self.container_id = container_id
        self.name = name
        self.description = description
        self.media_items = []
        
    @abstractmethod
    def add_item(self, media_item):
        """Add a media item to this container.
        
        Args:
            media_item: Media item object to add
        """
        pass
    
    @abstractmethod
    def remove_item(self, media_item):
        """Remove a media item from this container.
        
        Args:
            media_item: Media item object to remove
        """
        pass
    
    @abstractmethod
    def get_items(self):
        """Return all media items in this container.
        
        Returns:
            list: List of media item objects
        """
        pass
    
    @abstractmethod
    def get_container_type(self):
        """Return the type of container.
        
        Returns:
            str: Description of the container type
        """
        pass
    
    def __str__(self):
        """String representation of the container."""
        return f"{self.name} ({self.container_id})"
