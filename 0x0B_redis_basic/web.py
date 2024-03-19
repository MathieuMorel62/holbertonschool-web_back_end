#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis
from functools import wraps
from typing import Callable, Any


redis_client = redis.Redis()


def count_requests(func: Callable) -> Callable:
    """ function that will count how many times a request has been made """
    @wraps(func)
    def wrapper(url: str, *args, **kwargs) -> Any:
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url, *args, **kwargs)

    return wrapper


def cache_response(func: Callable) -> Callable:
    """ function that will cache the response of a request """
    @wraps(func)
    def wrapper(url: str, *args, **kwargs) -> Any:
        cache_key = f"cache:{url}"
        cached_response = redis_client.get(cache_key)

        if cached_response:
            return cached_response.decode()

        response = func(url, *args, **kwargs)
        redis_client.setex(cache_key, 10, response)
        return response

    return wrapper


@count_requests
@cache_response
def get_page(url: str) -> str:
    """ function that will call get_page """
    response = requests.get(url)
    return response.text
