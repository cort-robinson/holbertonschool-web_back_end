#!/usr/bin/env python3
"""Unittests for client.py
"""
import unittest
from unittest.mock import PropertyMock, patch

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

    def test_public_repos_url(self):
        """Test public_repos_url returns the correct value.
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as mock_method:
            mock_method.return_value = {'repos_url': 'test_url'}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, 'test_url')
