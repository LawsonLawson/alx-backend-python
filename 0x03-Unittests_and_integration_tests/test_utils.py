#!/usr/bin/env python3
"""
Unit Test Suite for Utility Functions

This module contains unit tests for the utility functions `access_nested_map`,
`get_json`, and `memoize`. It uses the `unittest` framework along with
`parameterized` for parameterized testing and `unittest.mock`for mocking HTTP
requests and object methods.

Classes:
    TestAccessNestedMap: Contains tests for the `access_nested_map` function.
    TestGetJson: Contains tests for the `get_json` function.
    TestMemoize: Contains tests for the `memoize` decorator.

Functions:
    TestAccessNestedMap.test_access_nested_map: Tests the correct return values
    of `access_nested_map`.
    TestAccessNestedMap.test_access_nested_map_exception: Tests that `KeyError`
    is raised correctly in `access_nested_map`.
    TestGetJson.test_get_json: Tests that `get_json` returns the correct JSON
    payload.
    TestMemoize.test_memoize: Tests that a method is only called once when
    memoized.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Case for `access_nested_map` function.

    This class tests the functionality of the `access_nested_map` function by
    providing different input maps and paths, and checking the function's
    return value or whether it raises a KeyError.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """
        Test that `access_nested_map` returns the expected value.

        Args:
            nested_map (dict): The dictionary to be accessed.
            path (tuple): The sequence of keys to retrieve the value.
            answer: The expected result of accessing the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that `access_nested_map` raises KeyError for invalid paths.

        Args:
            nested_map (dict): The dictionary to be accessed.
            path (tuple): The sequence of keys to retrieve the value.

        Raises:
            KeyError: If the path does not exist in the dictionary.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Test Case for `get_json` function.

    This class tests the `get_json` function by mocking the HTTP GET request
    and checking that the function returns the expected JSON response.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that `get_json` returns the correct JSON payload.

        Args:
            test_url (str): The URL to send the GET request to.
            test_payload (dict): The expected JSON response.
            mock_get (Mock): The mock object for `get_json`.
        """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test Case for `memoize` decorator.

    This class tests the `memoize` decorator to ensure that a method is only
    called once even when accessed multiple times via a memoized property.
    """

    def test_memoize(self):
        """
        Test that a method is only called once when accessed via a memoized
        property.

        This method patches the `a_method` of `TestClass` and checks that it is
        only called once when the `a_property` is accessed multiple times.
        """

        class TestClass:
            """
            A simple test class for memoization.
            """

            def a_method(self):
                """
                A method that returns a constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that calls `a_method`.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()

            # First access, should call a_method
            test_class.a_property

            # Second access, should not call a_method
            test_class.a_property

            # Ensure a_method was only called once
            mockMethod.assert_called_once()
