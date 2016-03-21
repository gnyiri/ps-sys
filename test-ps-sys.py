#!/usr/bin/env python

import unittest
from ps_utils.py_utils import *
from ps_utils.py_file_stat import *


class TestUtils(unittest.TestCase):
    def test_get_file_extension(self):
        self.assertEqual(get_file_extension('file.txt'), 'txt')
        self.assertEqual(get_file_extension('file.txt.csv'), 'csv')
        self.assertEqual(get_file_extension('.dummy'), '')
        self.assertEqual(get_file_extension(''), '')


class TestFileStat(unittest.TestCase):
    def test_get_file_extensions(self):
        l_f = DirStat('/tmp/')
        l_file_extensions = l_f.get_file_extensions()
        self.assertLess(0, len(l_file_extensions.items()))

    def test_get_directory_size(self):
        l_f = DirStat('/tmp/')
        self.assertLess(0, l_f.get_directory_size())

if __name__ == '__main__':
    unittest.main()

