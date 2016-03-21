#!/usr/bin/env python

import unittest
import re
from ps_utils.py_utils import *
from ps_utils.py_file_stat import *
from ps_utils.py_proc_stat import *


class TestUtils(unittest.TestCase):
    def test_get_file_extension(self):
        self.assertEqual(get_file_extension('file.txt'), 'txt')
        self.assertEqual(get_file_extension('file.txt.csv'), 'csv')
        self.assertEqual(get_file_extension('.dummy'), '')
        self.assertEqual(get_file_extension(''), '')


class TestFileStat(unittest.TestCase):
    def test_get_file_extensions(self):
        l_dir_stat = DirStat('/tmp/')
        l_file_extensions = l_dir_stat.get_file_extensions()
        self.assertLess(0, len(l_file_extensions.items()))

    def test_get_directory_size(self):
        l_dir_stat = DirStat('/tmp/')
        self.assertLess(0, l_dir_stat.get_directory_size())

    def test_get_process_ids(self):
        l_process_ids = get_process_ids()
        self.assertLess(0, len(l_process_ids))

        for l_process_id in l_process_ids:
            if not re.search('\d+', l_process_id):
                self.fail("Wrong process id")


if __name__ == '__main__':
    unittest.main()

