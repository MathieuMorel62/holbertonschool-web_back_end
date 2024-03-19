#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
