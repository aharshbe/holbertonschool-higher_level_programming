#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unit test for max int function
    """
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
