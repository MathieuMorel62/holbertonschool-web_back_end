#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis
from typing import Callable
from functools import wraps

redis_client = redis.Redis()


def cache_and_count(method: Callable) -> Callable:
    """
    Decorator to count the number of requests to a URL
    """

    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        """
        count_key = "count:{}".format(*args)
        cached_key = "cached:{}".format(*args)
        redis_client.incr(count_key)
        result = method(*args)
        redis_client.setex(cached_key, 10, result)
        return result
    return wrapper


@cache_and_count
def get_page(url: str) -> str:
    """ Retrieves HTML content from a URL """
    response = requests.get(url)
    return response.text
