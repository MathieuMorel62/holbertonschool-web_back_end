#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis
from functools import wraps


redis_client = redis.Redis()


def count_requests(func):
    """ Decorator to count the number of requests to a URL """
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)
    return wrapper


def cache_response(func):
    """ Decorator to cache the answer """
    @wraps(func)
    def wrapper(url):
        cache_key = f"cached:{url}"
        cached = redis_client.get(cache_key)

        if cached:
            return cached.decode('utf-8')

        response = func(url)
        redis_client.setex(cache_key, 10, response)
        return response
    return wrapper


@count_requests
@cache_response
def get_page(url: str) -> str:
    """ Retrieves HTML content from a URL """
    response = requests.get(url)
    return response.text
