#!/usr/bin/env python3
""" Stats about Nginx logs in MongoDB """


def log_stats(mongo_collection):
    """ Provide some stats about Nginx logs stored in MongoDB """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
