#!/usr/bin/env python3
""" Asynchronous coroutine """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio Task that calls the wait_random
    function with the given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: An asyncio Task object that represents the execution
        of the wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
