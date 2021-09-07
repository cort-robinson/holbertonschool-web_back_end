#!/usr/bin/env python3
"""Contains insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a school document into a mongo collection"""
    new_doc = {key: value for key, value in kwargs.items()}
    insert_obj = mongo_collection.insert_one(new_doc)
    return insert_obj.inserted_id
