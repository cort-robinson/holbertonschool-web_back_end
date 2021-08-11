#!/usr/bin/env python3
"""
Session authentication for the API.
"""
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a a session id for a user_id:
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
