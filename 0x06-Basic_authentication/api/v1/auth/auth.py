#!/usr/bin/env python3
""" authorization module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def __init__(self, app):
        """ constructor
        """
        self.app = app

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ decorator to require authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ returns the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns the current user
        """
        return None
