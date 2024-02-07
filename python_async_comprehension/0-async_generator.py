#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """ Asynchronous generator that yields random floats between 0 and 10. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
