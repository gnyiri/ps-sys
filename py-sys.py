#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import DirStat
from ps_utils.py_proc_stat import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.m_process_query_button = QPushButton("Get process id-s")
        self.m_process_ids = QListWidget()
        self.m_browser = QTextBrowser()

        l_layout = QVBoxLayout()
        l_layout.addWidget(self.m_process_query_button)
        l_layout.addWidget(self.m_process_ids)
        l_layout.addWidget(self.m_browser)

        self.setLayout(l_layout)
        self.connect(self.m_process_query_button, SIGNAL("clicked()"), self.update_ui)
        self.setWindowTitle("py-sys")

    def update_ui(self):
        l_process_ids = get_process_ids()

        assert isinstance(l_process_ids, list)

        for l_process_id in l_process_ids:
            l_item = QListWidgetItem(QString(str(l_process_id)))
            self.m_process_ids.addItem(l_item)


def main():
    l_app = QApplication(sys.argv)
    l_form = Form()
    l_form.show()
    l_app.exec_()


if __name__ == '__main__':
    main()
