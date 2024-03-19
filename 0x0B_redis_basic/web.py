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
        
        try:
            result = method(url)
            if result:
                redis_client.setex(f"cached:{url}", 10, result.encode('utf-8'))
            return result
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return "An error occurred while fetching the URL"
    return wrapper


@cache_url
def get_page(url: str) -> str:
    """ Get page """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: HTTPStatus {response.status_code}"
