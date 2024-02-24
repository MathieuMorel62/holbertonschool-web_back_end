#!/usr/bin/env python3
""" Session authentication module """

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session for the given user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID associated with the session ID,
            or None if the session ID is invalid or not provided.
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
