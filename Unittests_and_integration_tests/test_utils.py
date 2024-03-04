#!/usr/bin/env python3
""" Unittests for utils module """

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    """Class testing access_nested_map fn"""
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map fn """
        self.assertEqual(access_nested_map(nested_map, path), expected)
