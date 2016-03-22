#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import DirStat
from ps_utils.py_proc_stat import *
from ps_ui.ps_main_ui import *


def main():
    l_app = QApplication(sys.argv)
    l_form = MainForm()
    l_form.show()
    l_app.exec_()


if __name__ == '__main__':
    main()
