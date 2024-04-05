#!/usr/bin/env python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """main cahce fclass"""
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.lru_queue = []

    def put(self, key, item):
        if key is None or item is None:
            return

        # If cache is full, discard least frequency used item (LFU)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.__evict_lfu()

        self.cache_data[key] = item
        self.__update_frequency(key)
        self.__update_lru(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and LRU queue
        self.__update_frequency(key)
        self.__update_lru(key)
        return self.cache_data[key]

    def __update_frequency(self, key):
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def __update_lru(self, key):
        if key in self.lru_queue:
            self.lru_queue.remove(key)
        self.lru_queue.append(key)

    def __evict_lfu(self):
        min_frequency = min(self.frequency.values())
        lfu_keys = [key for key, freq in self.frequency.items() if freq == min_frequency]

        if len(lfu_keys) > 1:
            # If more than 1 LFU item, use LRU to break tie
            lfu_keys.sort(key=lambda k: self.lru_queue.index(k))

        lfu_key = lfu_keys[0]
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        self.lru_queue.remove(lfu_key)
        print("DISCARD:", lfu_key)
