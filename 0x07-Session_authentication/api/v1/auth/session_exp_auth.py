#!/usr/bin/env python3
"""
Session expiration authentication module
"""
from datetime import datetime, timedelta
from os import getenv

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Session expiration authentication class
    """
    def __init__(self):
        """ Initialize SessionExpAuth
        """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create a Session ID
        """
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                "user_id": user_id,
                "created_at": datetime.now()
            }
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """ Return User ID for Session ID
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        if 'created_at' not in session_dict:
            return None
        if (session_dict.get('created_at') +
                timedelta(seconds=self.session_duration)) < datetime.now():
            return None
        return session_dict.get('user_id')
