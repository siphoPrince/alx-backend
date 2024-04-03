#!/usr/bin/env python3
""" inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the first item (FIFO)
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        # Add the new item
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

    def print_cache(self):
        """Print the cache"""
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
