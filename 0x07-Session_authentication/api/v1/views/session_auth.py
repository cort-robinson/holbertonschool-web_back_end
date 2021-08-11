#!/usr/bin/env python3
""" Module of Session Auth views
"""
from os import getenv

from api.v1.app import auth
from api.v1.views import app_views
from flask import jsonify, request
from flask.helpers import make_response
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ Login Session
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400
    user = User.search(email=email)
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    session_id = auth.create_session(user_id=user.id)
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
