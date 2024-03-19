#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator to count the number of requests to a URL """
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper function """
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return method(url)
    return wrapper


def cache_response(method: Callable) -> Callable:
    """ Decorator to cache the answer """
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper function """
        cache_key = f"cached:{url}"
        cached = redis_client.get(cache_key)

        if cached:
            return cached.decode('utf-8')

        response = method(url)
        redis_client.setex(cache_key, 11, response)
        return response
    return wrapper


@count_requests
@cache_response
def get_page(url: str) -> str:
    """ Retrieves HTML content from a URL """
    response = requests.get(url)
    return response.text
