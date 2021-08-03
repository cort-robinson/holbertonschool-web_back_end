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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Implement an is_valid function that expects two arguments: hashed_password,
    which is a byte string, and password, which is a string.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
