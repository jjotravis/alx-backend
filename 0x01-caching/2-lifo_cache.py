#!/usr/bin/env python3
"""
class LIFOCache
Inherits from BasCaching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    This class represents LIFO cache implementation

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
        self.keys = []

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
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.keys.remove(key)
                else:
                    del self.cache_data[self.keys[self.MAX_ITEMS - 1]]
                    item_discard = self.keys.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discard)

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Get the value associated with the given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key if it exists.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
