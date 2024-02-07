#!/usr/bin/env python3
""" Measure the runtime of a coroutine """

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime(n: int = 5) -> float:
    """ Measure the runtime of a coroutine

    Args:
        n (int, optional): Number of times to measure the runtime.
        Defaults to 5.

    Returns:
        float: Average runtime of the coroutine.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(n)))
    end = time.time()

    return (end - start) / n
