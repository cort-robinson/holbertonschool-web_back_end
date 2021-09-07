#!/usr/bin/env python3
"""Contains update_topics function"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school
        document based on the name
    """
    mongo_collection.update(
        {'name': name},
        {'$set': {'topics': topics}},
        multi=True
    )
