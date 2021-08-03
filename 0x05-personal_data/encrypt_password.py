#!/usr/bin/env python3
"""
Implement a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
"""
from bcrypt import hashpw, gensalt


def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())
