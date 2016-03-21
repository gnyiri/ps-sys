#!/usr/bin/env python

import re
from py_utils import *


def get_process_ids():
    l_process_path = '/proc/'
    l_process_ids = []
    l_all_files = os.listdir(l_process_path)

    for l_file in l_all_files:
        if re.search('(\d+)', l_file):
            l_file = l_process_path + l_file

            if os.path.isdir(l_file):
                l_process_ids.append(l_file)

    return l_process_ids
