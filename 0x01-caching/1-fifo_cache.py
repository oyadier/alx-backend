#!/usr/bin/python3
"""FiFO Caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implement FIFO caching"""

    def __init__(self):
        super().__init__(self)
        self.cache_data

    def put(self, key, item):
        """
        Add item to FIFO block
            Args:
                key(integer): key of the item block
                item(str): item of the block
        Retrun:
            Nothing
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[0]
            for key, vl in self.cache_data.items():
                if vl == self.cache_data[0]:
                    print("DISCARD: {}".format(key))
        self.cache_data[key] = item

    def get(self, key):
        """
        Get the value given the key
            Args:
                key(integer): Value fo the item
        Retrun:
            item(intefer): item linked to key
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
