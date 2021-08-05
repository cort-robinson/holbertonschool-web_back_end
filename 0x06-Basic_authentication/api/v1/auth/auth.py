#!/usr/bin/env python3
""" authorization module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ decorator to require authentication
        """
        if path is None or not excluded_paths or path.strip('/') not in [
                path.strip('/') for path in excluded_paths]:
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
