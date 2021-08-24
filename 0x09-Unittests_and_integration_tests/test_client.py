#!/usr/bin/env python3
"""Unittests for client.py
"""
import unittest
from unittest.mock import PropertyMock, patch

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([{
    'org_payload': TEST_PAYLOAD[0][0],
    'repos_payload': TEST_PAYLOAD[0][1],
    'expected_repos': TEST_PAYLOAD[0][2],
    'apache2_repos': TEST_PAYLOAD[0][3]
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test integration of GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """Setup class method
        """
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()
        cls.get.side_effect = cls.side_effect

    @classmethod
    def side_effect(cls, *args):
        """Checks if the url is correct and returns the payload
        """

        if args[0] == 'https://api.github.com/orgs/google':
            return cls.org_payload
        elif args[0] == 'https://api.github.com/orgs/google/repos':
            return cls.repos_payload
        else:
            raise ValueError('Wrong url')

    def test_public_repos(self):
        """Test public_repos
        """
        pass

    def test_public_repos_with_license(self):
        """Test public_repos with a license
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """Teardown class method
        """
        cls.get_patcher.stop()
