#!/usr/bin/env python3
"""
class LRUCache
Inherits from BasCaching
"""
from typing import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    This class represents LRU cache implementation

    Attributes:
        - cache_data: A dictionary to store key-value pairs in the cache.
        - keys: A list to maintain the insertion order of keys in the cache.

    Methods:
        - __init__(self): Initializes an instance of the FIFOCache class.
        - put(self, key, item): Adds or updates an item .
        - get(self, key): Retrieves the value from the cache.
    """

    def __init__(self):
        """
        Initialize instance of the class
        """
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache with the given key.

        Args:
            key: The key to associate the item with.
            item: The item to be stored in the cache.

        Returns:
            The key of the item that was added or updated in the cache.
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discard = next(iter(self.lru_order))
            del self.cache_data[item_discard]
            print("DISCARD:", item_discard)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        """
        Retrieve item from cache given key
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
