#!/usr/bin/env python3
"""
Session authentication for the API.
"""
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session authentication class
        * validate if everything inherits correctly without overloading
        * valide the switch by using environment variables
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a a session id for a user_id:
            * Return None if user_id is None
            * Return None if user_id is not a string
            * Otherwise:
                * Generate a Session ID using uuid module and uuid4() like id
                  in Base
                * Use this Session ID as key of the dictionary
                  user_id_by_session_id - the value for this key must be
                  user_id
                * Return the Session ID
            * The same user_id can have multiple sesssion id - indeed, the
              user_id is the value in the dictionary user_id_by_session_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
