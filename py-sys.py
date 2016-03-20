#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import FileStat


def main():
    l_file_stat = FileStat(sys.argv[1])

    l_file_extensions = l_file_stat.get_file_extensions()

    print 'File extensions: '

    for l_ext, l_count in l_file_extensions.iteritems():
        print l_ext, ' -> ', l_count

    print 'Directory size: '

    print l_file_stat.get_directory_size() / (1024 * 1024), ' mbytes'

if __name__ == '__main__':
    main()