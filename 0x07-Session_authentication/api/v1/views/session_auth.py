#!/usr/bin/env python3
""" Module of Session Auth views
"""
from os import getenv

from api.v1.views import app_views
from flask import jsonify, request, abort
from flask.helpers import make_response
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ Login Session
    """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({'error': 'no user found for this email'}), 404
    user = None
    for _ in users:
        if _.is_valid_password(password):
            user = _
    if not user:
        return jsonify({'error': 'wrong password'}), 401
    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout():
    """ Logout Session
    """
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
