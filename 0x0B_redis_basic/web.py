#!/usr/bin/env python3
"""Module containing get_page"""
from functools import wraps
from typing import Callable

import redis
import requests

r = redis.Redis()


def count_access(func: Callable) -> Callable:
    """Counts the number of times a function is called with redis"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        r.incr('access')
        return func(*args, **kwargs)
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Use requests to to return HTML content of a URL"""
    response = requests.get(url)
    return response.text
