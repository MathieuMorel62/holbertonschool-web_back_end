#!/usr/bin/env python3
""" Module for implementing a filter_datum function """

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """Custom formatter for redacting sensitive information in log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message.
        """
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """
    Redact sensitive information from a log message.

    Args:
        fields (List[str]): List of fields to be redacted.
        redaction (str): The string to replace the sensitive information with.
        message (str): The log message to be redacted.
        separator (str): The separator used to separate fields in the log mess

    Returns:
        str: The redacted log message.
    """
    for field in fields:
        pattern = f"{field}=.*?{separator}"
        message = re.sub(pattern, (
            f" {field}={redaction}{separator}"), message)
    return message
