#!/usr/bin/env python3
"""Unittests for utils.py
"""
import unittest
from unittest.mock import patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
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
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json
        """
        mock_get().json.return_value = test_payload
        mock_get.assert_called_once
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoize
    """
    @parameterized.expand([
        (1, 1),
        (2, 2),
        (3, 3),
    ])
    @patch("utils.memoize")
    def test_memoize(self, test_input, expected, mock_memoize):
        """Test memoize
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, mock_method.return_value)
            self.assertEqual(test_obj.a_property, mock_method.return_value)
            mock_method.assert_called_once
