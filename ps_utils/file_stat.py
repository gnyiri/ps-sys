#!/usr/bin/env python

import sys
import os


class FileStat:
    def __init__(self, directory):
        self.m_directory = directory
        self.m_file_count = 0
        self.m_file_extensions = {}

    def lookup(self):
        assert isinstance(self.m_directory, str)

        if len(self.m_directory) < 1:
            print 'Wrong directory name! Exit!'
        else:
            print 'Starting lookup ' + self.m_directory
            for root, dir, files in os.walk(self.m_directory):
                for file in files:
                    print file
                    self.m_file_count += 1
                    file_ext = os.path.basename(file)
                    if self.m_file_extensions.has_key(file_ext):
                        self.m_file_extensions[file_ext] += 1
                    else:
                        self.m_file_extensions[file_ext] = 0

            print self.m_file_count

            for key in self.m_file_extensions:
                print key, ' => ', self.m_file_extensions[key]
