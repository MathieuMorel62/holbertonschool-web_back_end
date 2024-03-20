#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis


redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Get a page with caching and counting functionality.
    """
    cached_key = f"cached:{url}"
    count_key = f"count:{url}"

    redis_client.incr(count_key)

    cached_response = redis_client.get(cached_key)
    if cached_response:
        return cached_response.decode()

    response = requests.get(url)
    page_content = response.text

    redis_client.setex(cached_key, 10, page_content)

    return page_content
