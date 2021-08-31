#!/usr/bin/env python3
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Caching class"""

    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key