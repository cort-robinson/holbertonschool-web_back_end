#!/usr/bin/env python3
"""Unittests for utils.py
"""
import unittest
from unittest.mock import patch, MockResponse

from parameterized import parameterized

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")],
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json
    """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests):
        """Test get_json
        """
        mock_requests.return_value = MockResponse(json_data=test_payload)

        self.assertEqual(get_json(test_url), test_payload)
        mock_requests.assert_called_once_with(test_url)
