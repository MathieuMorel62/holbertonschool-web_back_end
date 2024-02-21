#!/usr/bin/env python3
""" Auth module """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that
                are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        authorization_header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user method
        """
        return None
