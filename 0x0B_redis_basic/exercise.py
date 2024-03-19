#!/usr/bin/env python3
""" Redis exercise """

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ Initialize the Cache instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the data in Redis using a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """ Get the data from Redis """
        value = self._redis.get(key)
        if fn and value is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ Get a string from Redis """
        value = self.get(key, fn=lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> Optional[int]:
        """ Get an int from Redis """
        value = self.get(key, fn=int)
        return value

    def replay(method: Callable):
        """ Display the history of calls of a particular function. """
        qualified_name = method.__qualname__
        redis_instance = method.__self__._redis

        inputs = redis_instance.lrange(f"{qualified_name}:inputs", 0, -1)
        outputs = redis_instance.lrange(f"{qualified_name}:outputs", 0, -1)

        print(f"{qualified_name} was called {len(inputs)} times:")

        for input_, output in zip(inputs, outputs):
            input_key = input_.decode('utf-8')
            output_key = output.decode('utf-8')
            print(f"{qualified_name}(*{input_key}) -> {output_key}")
