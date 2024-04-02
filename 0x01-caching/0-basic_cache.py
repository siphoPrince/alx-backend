#!/usr/bin/env python3
"""Defines a BasicCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A BasicCache class"""

    def put(self, key, item):
        """Assigns item to self.cache_data for the given key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
