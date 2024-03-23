#!/usr/bin/env python
"""
Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    """
    return mongo_collection.find()
