#!/usr/bin/env python3
"""
Function to list students sorted by average score
"""


def top_students(mongo_collection):
    """ Return list of students sorted by average score """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
