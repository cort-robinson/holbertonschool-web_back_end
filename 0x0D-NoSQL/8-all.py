#!/usr/bin/env python3
"""Contains list_all function"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    count = mongo_collection.count()
    if count == 0:
        return []
    return mongo_collection.find()
