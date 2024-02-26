#!/usr/bin/env python3
""" User authentication service """

import bcrypt
import uuid
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generates a UUID """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database. """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user with the given email and password """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if the user is valid """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
