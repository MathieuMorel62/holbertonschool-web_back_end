#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document in a collection """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
