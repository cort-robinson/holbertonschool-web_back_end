#!/usr/bin/env python3
"""Module for basic flask application
"""
from flask import Flask, jsonify

from auth import Auth

app = Flask(__name__)


@app.route('/')
def index():
    """Index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def create_user(email: str, password: str):
    """Create user route
    """
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
