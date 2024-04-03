#!/usr/bin/env python3
"""LRUCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class Node:
    """
    Node class for the doubly linked list used in LRU Cache.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    and implements a LRU (Least Recently Used) cache system.

    Args:
        BaseCaching (class): The parent class providing
        the `cache_data` dictionary and `MAX_ITEMS` constant.
    """

    def __init__(self):
        """
        Initializes the `LRUCache` instance.
        """
        super().__init__()  # Call the parent class constructor
        self.head = None
        self.tail = None

    def _remove(self, node):
        """
        Removes a node from the doubly linked list.

        Args:
            node (Node): The node to remove.
        """
        if self.head == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def _add_to_head(self, node):
        """
        Adds a node to the head of the doubly linked list.

        Args:
            node (Node): The node to add.
        """
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def _move_to_head(self, node):
        """
        Moves a node to the head of the doubly linked list, updating its position.

        Args:
            node (Node): The node to move.
        """
        self._remove(node)
        self._add_to_head(node)

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, following
        the LRU (Least Recently Used) strategy.

        Args:
            key (Any): The key to store the item under.
            item (Any): The value to associate with the key.

        Raises:
            TypeError: If either key or item is None.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self._move_to_head(self.cache_data[key])
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU eviction: remove the least recently used item (tail)
                discarded_key = self.tail.key
                self._remove(self.tail)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            new_node = Node(key, item)
            self.cache_data[key] = new_node
            self._add_to_head(new_node)

    def get(self, key):
        """
        Retrieves the value associated with a key
        from the cache, updating its position to head (LRU).

        Args:
            key (Any): The key to look up.

        Returns:
            Any: The value stored under the key, or None if not found.
        """
        if key in self.cache_data:
            self._move_to_head(self.cache_data[key])
            return self.cache_data[key].value
        return None
