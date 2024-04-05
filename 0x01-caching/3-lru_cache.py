#!/usr/bin/env python3
"""LRUCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    mainn class
    """

    def __init__(self):
        """
        Init
        """
        self.queued_item = deque()
        self.lru_item = []
        super().__init__()

    def put(self, key, item):
        """
        print put
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru_item.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del self.cache_data[self.lru_item[0]]
                    print("DISCARD:", self.lru_item[0])
                    self.lru_item.pop(0)
                self.cache_data[key] = item
            self.lru_item.append(key)

    def get(self, key):
        """
        get cache_data
        """
        if key in self.cache_data:
            self.lru_item.remove(key)
            self.lru_item.append(key)
            return self.cache_data.get(key)
        else:
            return None
