#!/usr/bin/env python3
"""
Session authentication for the API.
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class
        * validate if everything inherits correctly without overloading
        * valide the switch by using environment variables
    """
