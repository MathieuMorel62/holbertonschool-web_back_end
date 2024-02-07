#!/usr/bin/env python3
""" Asynchronous Comprehension """

from typing import List
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
  """ Asynchronous comprehension that returns a list of random floats. """
  async_numbers = [number async for number in generator()]
  return async_numbers
