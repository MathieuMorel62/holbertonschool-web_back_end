#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int):
    """ Return a tuple of size 2 containing a start index and an end index """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
