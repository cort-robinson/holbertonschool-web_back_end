#!/usr/bin/env python3
"""Module for basic flask application
"""
from flask import Flask, abort, jsonify, request
from flask.helpers import make_response

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """Index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Create user route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Login route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        response = make_response(jsonify({"email": email,
                                          "message": "logged in"}), 200)
        response.set_cookie('session_id', AUTH.get_session_id(email))
        return response
    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
