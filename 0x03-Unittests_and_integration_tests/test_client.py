#!/usr/bin/env python3
"""
Unit and Integration Tests for GithubOrgClient

This module contains unit and integration tests for the `GithubOrgClient` class
in the `client` module.
It uses the `unittest` framework, `parameterized` for parameterized testing,
and `unittest.mock` for mocking HTTP requests and object properties.

Classes:
    TestGithubOrgClient: Contains unit tests for the `GithubOrgClient` class.
    TestIntegrationGithubOrgClient: Contains integration tests for the
    `GithubOrgClient` class using mocked HTTP responses.

Functions:
    TestGithubOrgClient.test_org: Tests that the `org` property returns the
    expected organization data.
    TestGithubOrgClient.test_public_repos_url: Tests that `_public_repos_url`
    returns the correct URL.
    TestGithubOrgClient.test_public_repos: Tests that `public_repos` returns
    the expected list of repository names.
    TestGithubOrgClient.test_has_license: Tests that `has_license` correctly
    identifies repositories with a given license.
    TestIntegrationGithubOrgClient.setUpClass: Sets up the necessary mocks for
    integration testing.
    TestIntegrationGithubOrgClient.tearDownClass: Cleans up the mocks after
    integration testing.
    TestIntegrationGithubOrgClient.test_public_repos: Tests that `public_repos`
    returns the expected repositories using integration.
    TestIntegrationGithubOrgClient.test_public_repos_with_license: Tests that
    `public_repos` filters repositories by license using integration.
"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit Test Case for `GithubOrgClient` class.

    This class tests the functionality of the `GithubOrgClient` class by
    providing different inputs and mocking the HTTP GET requests to check
    the behavior of various methods.
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        Test that the `org` property returns the expected organization data.

        Args:
            org (str): The name of the GitHub organization.
            expected (dict): The expected data returned by the `org` property.
            get_patch (Mock): The mock object for `get_json`.
        """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """
        Test that the `_public_repos_url` property returns the correct
        repository URL.

        This method mocks the `org` property to return a payload containing the
        `repos_url` and checks that `_public_repos_url` retrieves this URL
        correctly.
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """
        Test that `public_repos` returns the expected list of repository names.

        This method mocks the `_public_repos_url` property and `get_json`
        function to return a list of repositories, and checks the correct
        functionality of `public_repos`.
        """
        lawson = {"name": "Lawson", "license": {"key": "a"}}
        israel = {"name": "Israel", "license": {"key": "b"}}
        pascal = {"name": "Pascal"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [lawson, israel, pascal]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Lawson', 'Israel', 'Pascal'])
            self.assertEqual(x.public_repos("a"), ['Lawson'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """
        Test that `has_license` correctly identifies if a repository has the
        given license.

        Args:
            repo (dict): The repository data containing the license information
            license (str): The license key to check for. expected (bool): The
            expected boolean result indicating if the license matches.
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration Test Case for `GithubOrgClient` class.

    This class performs integration tests by mocking the HTTP GET requests and
    using predefined payloads to simulate API responses from GitHub. It checks
    the functionality of the `GithubOrgClient` class methods in a more
    comprehensive environment.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the necessary mocks before running the integration tests.

        This method prepares mock objects for the organization and repository
        payloads and patches the `requests.get` method to return these mocks.
        """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the mocks after running the integration tests.

        This method stops the patching of the `requests.get` method and
        removes the mocks.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that `public_repos` returns the expected repositories using
        integration.

        This method checks that the `public_repos` method of `GithubOrgClient`
        returns the correct repositories based on the mocked API responses.
        """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """
        Test that `public_repos` filters repositories by license using
        integration.

        This method checks that the `public_repos` method of `GithubOrgClient`
        correctly filters repositories based on the license key provided.
        """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
