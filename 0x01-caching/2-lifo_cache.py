#!/usr/bin/env python3
"""LIFOCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a
    LIFO (Last-In, First-Out) cache system.

    Args:
        BaseCaching (class): The parent class providing
        the `cache_data` dictionary and `MAX_ITEMS` constant.
    """

    def __init__(self):
        """
        Initializes the `LIFOCache` instance.
        """
        super().__init__()  # Call the parent class constructor

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following
        the LIFO (Last-In, First-Out) strategy.

        Args:
            key (Any): The key to store the item under.
            item (Any): The value to associate with the key.

        Raises:
            TypeError: If either key or item is None.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LIFO eviction: remove the most recently added item
            discarded_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with a key from the cache.

        Args:
            key (Any): The key to look up.

        Returns:
            Any: The value stored under the key, or None if not found.
        """
        return self.cache_data.get(key)
