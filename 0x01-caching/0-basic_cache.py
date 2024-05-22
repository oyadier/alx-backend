#!/usr/bin/env python3
"""Implementing Caching algorithm"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching implementations"""

    def put(self, key, item):
        """
        Add item to the cache system block
            Args:
                key(int): key of the block item
                value(int): item of the block
            Return:
                """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        Get the value using key
            Args:
                key(int): the key to retrieve the item
            Return:
                item(any): item of a key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
