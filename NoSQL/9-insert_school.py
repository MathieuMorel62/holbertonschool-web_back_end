#!/usr/bin/env python3
""" """


def insert_school(mongo_collection, **kwargs):
    """"""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id