#!/usr/bin/env python3
""" Module for implementing a filter_datum function """

from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """ Function that returns the log message obfuscated """
    for field in fields:
        pattern = (f"{field}=.*?{separator}")
        message = re.sub(pattern, (f"{field}={redaction}{separator}"), message)
    return message
