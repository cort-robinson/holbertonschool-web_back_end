#!/usr/bin/env python3
"""Module for redis exercises"""
from functools import wraps
from typing import Callable, Union
from uuid import uuid4

import redis


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of Cache are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Prints call history of methods of Cache"""
    input_list_key = method.__qualname__ + ':inputs'
    output_list_key = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a function"""
    method_redis = method.__self__._redis
    inputs = method_redis.lrange(method.__qualname__ + ':inputs', 0, -1)
    outputs = method_redis.lrange(method.__qualname__ + ':outputs', 0, -1)

    print('{} was called {} times:'.format(method.__qualname__,
                                           method_redis.get(
                                               method.__qualname__).decode))
    for input, output in zip(inputs, outputs):
        print('{}(*{},) -> {}'.format(method.__qualname__,
                                      input.decode(), output.decode()))


class Cache:
    """Caching class"""

    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """Modified get function for redis"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Get a string from the cache."""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get an integer from the cache."""
        return self.get(key, int)
