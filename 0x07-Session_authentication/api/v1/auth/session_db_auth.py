#!/usr/bin/env python3
"""
Session DB Authentication Module
"""
from datetime import datetime, timedelta

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Session DB Authentication Class
    """
    def create_session(self, user_id=None):
        """ Create a session ID
        """
        session_id = super().create_session(user_id)
        if session_id:
            new_session = UserSession(session_id=session_id, user_id=user_id)
            new_session.save()
            return session_id

    def user_id_for_session_id(self, session_id):
        """ Get the user ID for a given session ID
        """
        if session_id is None:
            return None
        users = UserSession.search(session_id=session_id)
        if not users:
            return
        user = users[0]
        if self.session_duration <= 0:
            return user.user_id
        if (user.created_at +
                timedelta(seconds=self.session_duration)) < datetime.now():
            return None
        return user.user_id

    def destroy_session(self, request) -> bool:
        """ Destroys UserSession based on Session ID
        """
        session_id = super().destroy_session(request)
        if session_id:
            UserSession.delete(session_id=session_id)
            return True
        return False
