#!/usr/bin/env python3
"""Contains insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a school document into a mongo collection"""
    mongo_collection.insert_one(kwargs)
