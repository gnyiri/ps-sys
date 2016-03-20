#!/usr/bin/env python

import os


def get_file_extension(p_file_name):
    l_file_name, l_file_ext = os.path.splitext(p_file_name)
    l_file_ext = l_file_ext[1:]
    return l_file_ext

