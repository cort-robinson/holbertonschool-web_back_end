#!/usr/bin/env python3
"""contains hash_password and is_valid"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Implement a hash_password function that expects one string argument name
    password and returns a salted, hashed password, which is a byte string.

    Use the bcrypt package to perform the hashing (with hashpw).
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
