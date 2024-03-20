#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis


redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Get a page and cache it for 10 seconds"""
    count_key = f"count:{url}"
    cached_key = f"cached:{url}"

    redis_client.incr(count_key)

    cached_response = redis_client.get(cached_key)
    if cached_response:
        return cached_response.decode()

    response = requests.get(url)
    redis_client.setex(cached_key, 10, response.text)
    return response.text
