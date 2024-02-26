#!/usr/bin/env python3
""" User authentication service """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
