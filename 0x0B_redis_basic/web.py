#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis


redis_client = redis.Redis()


def get_page(url: str) -> str:
    """ Use the requests module to obtain the HTML content of a particular URL """

    count_key = f"count:{url}"
    redis_client.incr(count_key)

    cache_key = f"cache:{url}"
    cached_response = redis_client.get(cache_key)

    if cached_response:
        return cached_response.decode()

    response = requests.get(url)
    response_text = response.text

    redis_client.setex(cache_key, 10, response_text)
    return response_text
