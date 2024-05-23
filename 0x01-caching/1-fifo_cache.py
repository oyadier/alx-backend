#!/usr/bin/python3
"""FiFO Caching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implement FIFO caching"""

    def __init__(self):
        """Initialice the obj"""
        super().__init__()
        self.cache_data

    def put(self, key, item):
        """Add item to FIFO block
        Args:
                key(integer): key of the item block
                item(str): item of the block
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            key, val = next(iter(self.cache_data.items()))
            print("DISCARD: {}".format(key))
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """Get the value given the key
        Args:
                key(integer): Value fo the item
        Retrun:
                item(intefer): item linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
