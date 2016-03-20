#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import FileStat


def main():
    l_f = FileStat(sys.argv[1])
    print sys.argv[1], ':', l_f.get_directory_size()

if __name__ == '__main__':
    main()