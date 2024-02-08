#!/usr/bin/python3
""" Module for implementing a FIFO cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that represents a First-In-First-Out (FIFO) cache """

    def __init__(self):
        """ Initializes a FIFO cache object. """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item to the cache """
        self.cache_data[key] = item

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            print("DISCARD: " + first_item)
            del self.cache_data[first_item]
