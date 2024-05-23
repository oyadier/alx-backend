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
            Nothing
        """
        if key is not None or item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Get the value using key
            Args:
                key(int): the key to retrieve the item
        Return:
            item(any): item of a key
        """
        return self.cache_data.get(key, None)
