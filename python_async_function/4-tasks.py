#!/usr/bin/env python3
""" Asynchronous coroutine """

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for random delays and returns a
    sorted list of delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A sorted list of delays.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
