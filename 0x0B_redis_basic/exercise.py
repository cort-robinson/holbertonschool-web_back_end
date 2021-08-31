#!/usr/bin/env python3
from functools import wraps
from typing import Callable, Union
from uuid import uuid4

import redis


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of Cache are called"""
    @wraps(method)
    def wrapper(self, *args):
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


class Cache:
    """Caching class"""

    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
