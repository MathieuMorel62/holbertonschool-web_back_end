#!/usr/bin/env python3
""" Session expiration authentication """

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Session expiration authentication """
    def __init__(self):
        """ Constructor """
        self.session_duration = 0
        try:
            self.session_duration = int(os.getenv('session_duration'))
        except Exception:
            pass

    def create_session(self, user_id=None):
            """
            Create a session for the given user ID.

            Args:
                user_id (str): The ID of the user.

            Returns:
                str: The session ID if the session was successfully created,
                    None otherwise.
            """
            if not user_id:
                return None
            session_id = super().create_session(user_id)
            if not session_id:
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
        if not session_id:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary:
            user = session_dictionary.get("user_id")
            if user:
                if self.session_duration <= 0:
                    return user
                created_at = session_dictionary.get("created_at")
                if created_at is None:
                    return None
                if (datetime.now() - created_at) > timedelta(
                        seconds=self.session_duration):
                    return None
                return user
