#!/usr/bin/env python3
"""
class BasicCache
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Class representing a basic cache implementation.

    Inherits from BasicCaching class.

    Methods:
    - put(self, key, item): Add an item to the cache with the given key.
    - get(self, key): Retrieve the value given key from the cache.

    Attributes:
    - cache_data (dict): A dictionary to store key-value pairs in the cache."""

    def put(self, key, item):
        """
        Add an item to the cache with the given key.

        Parameters:
        key (str): The key to associate the item with in the cache.
        item (any): The item to be stored in the cache.

        Returns:
        None"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from the cache.

        Parameters:
        key (str): The key to look up in the cache.

        Returns:
        The value associated with the key, or None
        """
        return self.cache_data.get(key)
