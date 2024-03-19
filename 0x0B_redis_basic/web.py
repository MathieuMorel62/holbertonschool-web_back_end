#!/usr/bin/env python3
""" Redis exercise """

import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_url(method: Callable) -> Callable:
    """ Cache wrapper """
    @wraps(method)
    def wrapper(url) -> str:
        """ Wrapper function """
        redis_client.incr(f"count:{url}")
        cached = redis_client.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        html = method(url)
        redis_client.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@cache_url
def get_page(url: str) -> str:
    """ Get page """
    response = requests.get(url)
    return response.text
