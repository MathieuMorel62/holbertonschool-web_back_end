#!/usr/bin/env python3
""" Redis exercise """

import redis
import requests
from functools import wraps


def cache_url(func):
    """ Cache wrapper """
    @wraps(func)
    def wrapper(url):
        """ Wrapper function """
        redis_client = redis.Redis()
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        redis_client.incr(count_key)

        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        html_content = func(url)
        redis_client.setex(cache_key, 10, html_content)
        return html_content

    return wrapper

@cache_url
def get_page(url: str) -> str:
    """ Get page """
    response = requests.get(url)
    return response.text
