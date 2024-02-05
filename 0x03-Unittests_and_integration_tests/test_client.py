#!/usr/bin/env python3
""" test client"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test git hub"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        mock_get_json.return_value = {}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {})

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        org = GithubOrgClient("test")
        org._public_repos_url = (
            'https://api.github.com/orgs/test/repos'
        )
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        self.assertEqual(
            org._public_repos_url,
            'https://api.github.com/orgs/test/repos'
        )

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_public_repos_url.return_value = (
            'https://api.github.com/orgs/test/repos'
        )
        org = GithubOrgClient("test")
        self.assertEqual(
            org.public_repos(),
            [{'name': 'repo1'}, {'name': 'repo2'}]
        )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        org = GithubOrgClient("test")
        self.assertEqual(
            org.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
        ({}, {}, [], []),
        ({"repos_url": "https://api.github.com/orgs/test/repos"}, {}, [], []),
        ({}, {"name": "repo1"}, [{"name": "repo1"}], []),
        ({}, {"name": "repo1", "license":
                {"key": "apache-2.0"}}, [], [{"name": "repo1"}]),

    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        org = GithubOrgClient("test")
        org.org_payload = self.org_payload
        org.repos_payload = self.repos_payload
        self.mock_get().json.side_effect = [org.org_payload, org.repos_payload]
        self.assertEqual(org.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        org = GithubOrgClient("test")
        org.org_payload = self.org_payload
        org.repos_payload = self.repos_payload
        self.mock_get().json.side_effect = [org.org_payload, org.repos_payload]
        self.assertEqual(
            org.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
