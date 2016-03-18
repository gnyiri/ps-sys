#!/usr/bin/env python

import sys
from ps_utils.file_stat import FileStat


def main():
    fs = FileStat(sys.argv[1])
    fs.lookup()

if __name__ == '__main__':
    main()