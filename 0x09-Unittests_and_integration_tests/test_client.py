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
        """Test _public_repos_url
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as mock_method:
            mock_method.return_value = {'repos_url': 'test_url'}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, 'test_url')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos
        """
        mock_get_json.return_value = [{'name': 'test_repo'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            client = GithubOrgClient('google')
            mock_url.return_value = 'test_url'
            self.assertEqual(client.public_repos(), ['test_repo'])
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()
