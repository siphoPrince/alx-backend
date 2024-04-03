#!/usr/bin/env python3
"""MRUCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements a MRU (Most Recently Used) cache system.

    Args:
        BaseCaching (class): The parent class providing the `cache_data` dictionary and `MAX_ITEMS` constant.
    """

    def __init__(self):
        """
        Initializes the `MRUCache` instance.
        """
        super().__init__()  # Call the parent class constructor
        self.cache_data = {}  # Use the inherited dictionary for cache data
        self.lru_head = None  # Head of the linked list for tracking MRU

    def _remove_from_linked_list(self, node):
        """
        Removes a node from the linked list.

        Args:
            node (dict): The node (key-value pair) to remove.
        """
        if node == self.lru_head:
            self.lru_head = node.get('next')
            if self.lru_head:
                self.lru_head['prev'] = None
        elif node.get('next'):
            node['next']['prev'] = node['prev']
        if node.get('prev'):
            node['prev']['next'] = node['next']

    def _add_to_linked_list(self, node):
        """
        Adds a node to the head of the linked list, making it the MRU item.

        Args:
            node (dict): The node (key-value pair) to add.
        """
        node['next'] = self.lru_head
        if self.lru_head:
            self.lru_head['prev'] = node
        self.lru_head = node
        node['prev'] = None

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following the MRU (Most Recently Used) strategy.

        Args:
            key (Any): The key to store the item under.
            item (Any): The value to associate with the key.

        Raises:
            TypeError: If either key or item is None.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self._remove_from_linked_list(self.cache_data[key])

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # MRU eviction: remove the most recently used item (head of linked list)
            discarded_key = self.lru_head['key']
            self._remove_from_linked_list(self.lru_head)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = {'key': key, 'value': item, 'next': None, 'prev': None}
        self._add_to_linked_list(self.cache_data[key])

    def get(self, key):
        """
        Retrieves the value associated with a key from the cache, updating its position as MRU.

        Args:
            key (Any): The key to look up.

        Returns:
            Any: The value stored under the key, or None if not found.
        """
        if key in self.cache_data:
            node = self.cache_data[key]
            self._remove_from_linked_list(node)
            self._add_to_linked_list(node)
            return node['value']
        return None

# Example usage (assuming BaseCaching is defined elsewhere)
my_cache = MRUCache()
# ... (follow the test cases from 4-main.py)

