#!/usr/bin/env python3
"""Create a class MRUCache that inherits
from BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_keys:
                self.used_keys.append(key)
            else:
                self.used_keys.append(
                    self.used_keys.pop(self.used_keys.index(key)))
            if len(self.used_keys) > BaseCaching.MAX_ITEMS:
                mostUsed = self.used_keys.pop(-2)
                del self.cache_data[mostUsed]
                print('DISCARD: {:s}'.format(mostUsed))

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is not None and key in self.cache_data.keys():
            self.used_keys.append(
                self.used_keys.pop(self.used_keys.index(key)))
            return self.cache_data.get(key)
        return None
