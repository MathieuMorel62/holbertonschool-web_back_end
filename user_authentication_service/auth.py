#!/usr/bin/env python
""" User authentication service """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
