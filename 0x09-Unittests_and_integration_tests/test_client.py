#!/usr/bin/env python3
"""Unittests for client.py
"""
import unittest
from unittest.mock import patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, org, mock_method):
        """Test org returns the correct value.
        """
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), mock_method())
