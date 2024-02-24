#!/usr/bin/env python3
""" Session authentication view """

from flask import request, jsonify
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle user login.

    Retrieves the email and password from the request form.
    Checks if the email and password are provided.
    Searches for a user with the given email.
    Verifies if the password is correct for the user.
    Creates a session for the user.
    Returns the user information as a JSON response with a session cookie.

    Returns:
        A JSON response containing the user information and a session cookie.

    Raises:
        400: If the email or password is missing.
        404: If no user is found for the given email.
        401: If the password is incorrect.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    user_json = jsonify(user.to_json())
    user_json.set_cookie(getenv('SESSION_NAME'), session_id)

    return user_json
