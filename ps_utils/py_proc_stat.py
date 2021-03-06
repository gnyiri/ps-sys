#!/usr/bin/env python

import re
from py_utils import *


def get_process_ids():
    l_process_path = '/proc/'
    l_process_ids = []
    l_all_files = os.listdir(l_process_path)

    for l_file in l_all_files:
        if re.search('(\d+)', l_file):
            l_file_path = l_process_path + l_file

            if os.path.isdir(l_file_path):
                l_process_ids.append(l_file)

    return l_process_ids


def get_process_status(p_process_id):
    l_process_path = '/proc/'
    l_process_status = ""

    try:
        l_file = open(l_process_path + str(p_process_id) + '/status', "r")
    except IOError as l_e:
        return ""

    l_process_status = l_file.read()
    l_file.close()

    return l_process_status


def parse_process_status(p_process_id, p_section):
    assert isinstance(p_section, str)

    l_process_status = get_process_status(p_process_id)

    l_ret_val = ''

    for l_line in l_process_status.splitlines():
        l_value = l_line.split(':')

        if len(l_value) > 1:
            if l_value[0].strip() == p_section:
                l_ret_val = l_value[1]
                break

    return l_ret_val.strip()
