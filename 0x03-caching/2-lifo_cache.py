#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching
and is a caching system:

    * You must use self.cache_data - dictionary from
      the parent class BaseCaching
    * You can overload def __init__(self): but don’t
      forget to call the parent init: super().__init__()
    * def put(self, key, item):
        * Must assign to the dictionary self.cache_data
          the item value for the key key.
        * If key or item is None, this method should not
          do anything.
        * If the number of items in self.cache_data is
          higher that BaseCaching.MAX_ITEMS:
            * you must discard the last item put in
              cache (LIFO algorithm)
            * you must print DISCARD: with the key
              discarded and following by a new line
    * def get(self, key):
        * Must return the value in self.cache_data linked to key.
        * If key is None or if the key doesn’t exist in
          self.cache_data, return None.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Put item in cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data.keys())[-2]))
            self.cache_data.pop(list(self.cache_data.keys())[-2])

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        return None
