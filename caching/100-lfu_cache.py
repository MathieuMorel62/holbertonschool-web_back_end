#!/usr/bin/python3
"""
This module contains the LFUCache class, which is a
subclass of BaseCaching.
It implements a Least Frequently Used (LFU) caching algorithm.
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class represents a Least Frequently Used (LFU) cache.

    Attributes:
        freq: A dictionary that keeps track of the frequency of each key.
        freq_items: A dictionary that stores the items for each frequency.
        min_freq: An integer representing the minimum frequency in the cache.

    Methods:
        __init__: Initializes an instance of LFUCache.
        put: Adds an item to the cache with the given key.
        get: Retrieves the item associated with the given key from the cache.
    """
    def __init__(self):
        """Initialize an instance of LFUCache."""
        super().__init__()
        self.freq = defaultdict(int)
        self.freq_items = defaultdict(OrderedDict)
        self.min_freq = 0

    def put(self, key, item):
        """
        Add an item to the cache with the given key.
        If the cache is full, remove the least frequently used item.

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq_items[self.freq[key]].pop(key)
            if not self.freq_items[self.freq[key]]:
                del self.freq_items[self.freq[key]]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq_key, _ = self.freq_items[
                self.min_freq].popitem(last=False)
            if not self.freq_items[self.min_freq]:
                del self.freq_items[self.min_freq]
            self.cache_data.pop(min_freq_key)
            self.freq.pop(min_freq_key)
            print("DISCARD: " + min_freq_key)

        self.cache_data[key] = item
        self.freq[key] += 1
        self.freq_items[self.freq[key]][key] = None
        self.min_freq = 1

    def get(self, key):
        """
        Retrieve the item associated with the given key from the cache.
        If the key is not found in the cache, return None.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the given key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_items[self.freq[key]].pop(key)
        if not self.freq_items[self.freq[key]]:
            del self.freq_items[self.freq[key]]
        self.freq[key] += 1
        self.freq_items[self.freq[key]][key] = None
        if not self.freq_items[self.min_freq]:
            self.min_freq += 1

        return self.cache_data[key]
