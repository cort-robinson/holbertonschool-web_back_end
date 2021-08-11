#!/usr/bin/env python3
"""Basic authentication module for API"""
import base64
from typing import TypeVar, Tuple

from api.v1.auth.auth import Auth
from models.base import DATA
from models.user import User


class BasicAuth(Auth):
    """ Basic authentication class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the base64 encoded authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.replace('Basic ', '', 1)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes the base64 encoded authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64encode(base64.b64decode(base64_authorization_header))
        except Exception:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Extracts the user credentials from the decoded base64
            authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if decoded_base64_authorization_header.count(':') < 1:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(':', 1)
        return user_credentials[0], user_credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Creates a user object from the user email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        if not DATA.get('User'):
            return None
        for user in User.search({'email': user_email}):
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user
        """
        auth_header = self.authorization_header(request)
        extracted_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_auth_header = self.decode_base64_authorization_header(
            extracted_auth_header)
        user_credentials = self.extract_user_credentials(decoded_auth_header)
        return self.user_object_from_credentials(
            user_credentials[0], user_credentials[1])
