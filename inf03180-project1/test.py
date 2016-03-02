#! /usr/bin/env python

import unittest
from app import app

class TestApp(unittest, TestCase):
    
    def setup(self):
        self.app = app.test_client()


if __name__ == '__main__':
    unittest.main()
