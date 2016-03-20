#!/usr/bin/env python

import unittest
from ps_utils.py_utils import *


class TestUtils(unittest.TestCase):
    def test_get_file_extension(self):
        self.assertEqual(get_file_extension('file.txt'), 'txt')
        self.assertEqual(get_file_extension('file.txt.csv'), 'csv')
        self.assertEqual(get_file_extension('.dummy'), '')
        self.assertEqual(get_file_extension(''), '')

if __name__ == '__main__':
    unittest.main()

