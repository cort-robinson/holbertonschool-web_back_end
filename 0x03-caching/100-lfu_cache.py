#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a caching system:
    * You must use self.cache_data - dictionary from the parent class
      BaseCaching
    * You can overload def __init__(self): but don’t forget to call the parent
      init: super().__init__()
    * def put(self, key, item):
        * Must assign to the dictionary self.cache_data the item value for the
          key key.
        * If key or item is None, this method should not do anything.
        * If the number of items in self.cache_data is higher that
          BaseCaching.MAX_ITEMS:
            * you must discard the least frequency used item (LFU algorithm)
            * if you find more than 1 item to discard, you must use the LRU
              algorithm to discard only the least recently used
            * you must print DISCARD: with the key discarded and following by
              a new line
    * def get(self, key):
        * Must return the value in self.cache_data linked to key.
        * If key is None or if the key doesn’t exist in self.cache_data,
          return None.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache"""

    def __init__(self):
        """Initialize LFU Cache"""
        super().__init__()
        self.accessCount = {}

    def LFUKey(self, key=None):
        """Return the key with the least frequency"""
        if key is None:
            return min(self.accessCount, key=self.accessCount.get)
        else:
            evalDict = self.accessCount.copy()
            evalDict.pop(key)
            return min(evalDict, key=evalDict.get)

    def access(self, key):
        """Increase access count of key in accessCount"""
        if key in self.accessCount:
            self.accessCount[key] += 1
        else:
            self.accessCount[key] = 1

    def put(self, key, item):
        """Put item in cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.access(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.LFUKey(key)))
            self.cache_data.pop(self.LFUKey(key))
            self.accessCount.pop(self.LFUKey(key))

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        if key in self.cache_data:
            self.put(key, self.cache_data[key])
            return self.cache_data[key]
        return None
