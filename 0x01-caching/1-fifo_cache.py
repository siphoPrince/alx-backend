#!/usr/bin/env python3
""" inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements a FIFO (First-In, First-Out) cache system.

    Args:
        BaseCaching (class): The parent class providing the `cache_data` dictionary and `MAX_ITEMS` constant.
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key.
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pop_off = sorted(self.cache_data)[0]
            self.cache_data.pop(pop_off)
            print('DISCARD: {}'.format(pop_off))

    def get(self, key):
        """
        Return value of cache_data linked to key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
