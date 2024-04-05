#!/usr/bin/env python3
"""LRUCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    mainn class
    """

    def __init__(self):
        super().__init__()
        self.lru_queue = []

    def put(self, key, item):
        if key is None or item is None:
            return

        # If cache is full, discard least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.__evict_lru()

        self.cache_data[key] = item
        self.__update_lru(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update LRU queue
        self.__update_lru(key)
        return self.cache_data[key]

    def __update_lru(self, key):
        if key in self.lru_queue:
            self.lru_queue.remove(key)
        self.lru_queue.append(key)

    def __evict_lru(self):
        if self.lru_queue:
            lru_key = self.lru_queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)
