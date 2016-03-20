#!/usr/bin/env python

from py_utils import *


# FileStat class
class FileStat:
    # CTOR
    def __init__(self, p_directory):
        self.m_directory = p_directory

    # get directory size (recursive)
    def get_directory_size_r(self, p_directory):
        l_file_size = 0

        for l_root, l_dir, l_files in os.walk(p_directory):
            for l_file in l_files:
                l_full_path = l_root + '/' + l_file
                if os.path.isfile(l_full_path):
                    l_file_size += os.path.getsize(l_full_path)
                else:
                    l_file_size += self.get_directory_size_r(l_full_path)

        return l_file_size

    # get directory size
    def get_directory_size(self):
        assert isinstance(self.m_directory, str)

        return self.get_directory_size_r(self.m_directory)

    # get file extensions dictionary
    def get_file_extensions(self):
        assert isinstance(self.m_directory, str)

        l_file_extensions = {}

        if len(self.m_directory) < 1:
            print 'Wrong directory name! Exit!'
        else:
            print 'Starting lookup ' + self.m_directory
            for l_root, l_dir, l_files in os.walk(self.m_directory):
                for l_file in l_files:
                    l_file_ext = get_file_extension(l_file)
                    if l_file_extensions.has_key(l_file_ext):
                        l_file_extensions[l_file_ext] += 1
                    else:
                        l_file_extensions[l_file_ext] = 1

        return l_file_extensions
