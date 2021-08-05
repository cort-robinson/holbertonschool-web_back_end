#!/usr/bin/env python3
""" authorization module for the API
"""
import re
from typing import List, TypeVar

from flask import request


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ decorator to require authentication
        """
        if path is None or not excluded_paths:
            return True
        for word in [path.strip('/') for path in excluded_paths]:
            if word.endswith('*'):
                if not re.search('^' + word[:-1], path):
                    return True
            elif word == path:
                return True
        return False

    def authorization_header(self, request=None) -> str:
        """ returns the authorization header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns the current user
        """
        return None
