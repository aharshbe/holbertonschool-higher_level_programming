#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestBase):
	totest = Base()
	def test_id_isnum(self):
		self.assertTrue(totest.id is int)
	def test_isnotnull(self):
		self.assertFalse(totest.id is not None)

if __name__ == "__main__":
	unittest.main()

