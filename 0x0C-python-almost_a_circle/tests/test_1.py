#!/usr/bin/python3

import unittest
from models.base import Base


class tests(unittest.TestCase):
    to_test = Base()

    def isint(self):
        self.assertTrue(tests.to_test.id is int)

if __name__ == "__main__":
    unittest.main()
