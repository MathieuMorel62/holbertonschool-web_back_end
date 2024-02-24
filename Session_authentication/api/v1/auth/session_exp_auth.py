#!/usr/bin/env python3
""" Session expiration authentication """

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Session expiration authentication """
    def __init__(self):
        """ Constructor """
        session_duration = os.getenv("SESSION_DURATION")
        try:
            self.session_duration = int(
                session_duration) if session_duration else 0
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create a session for the given user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID if the session was successfully created,
                None otherwise.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        if not user_id:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieves the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The user ID associated with the session ID, or None
                if the session ID is invalid or expired.
        """
        if session_id is None or session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        if 'created_at' not in session_dict:
            return None
        expiration_date = session_dict['created_at'] + timedelta(
            seconds=self.session_duration)
        if expiration_date < datetime.now():
            return None
        return session_dict.get('user_id')
