#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import DirStat
from ps_utils.py_proc_stat import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, p_parent=None):
        super(Form, self).__init__(p_parent)
        self.m_btn_process_query = QPushButton("Get process id-s")
        self.m_list_process = QListWidget()
        self.m_browser_details = QTextBrowser()

        l_layout = QVBoxLayout()
        l_layout.addWidget(self.m_btn_process_query)
        l_layout.addWidget(self.m_list_process)
        l_layout.addWidget(self.m_browser_details)

        self.setLayout(l_layout)
        self.connect(self.m_btn_process_query, SIGNAL("clicked()"), self.update_process_ids)
        self.connect(self.m_list_process, SIGNAL("itemClicked(QListWidgetItem *)"), self.update_process_details)
        self.setWindowTitle("py-sys")

    def update_process_ids(self):
        l_process_ids = get_process_ids()

        assert isinstance(l_process_ids, list)

        for l_process_id in l_process_ids:
            l_item = QListWidgetItem(QString(str(l_process_id)))
            self.m_list_process.addItem(l_item)

    def update_process_details(self, p_item):
        l_item = p_item.text()
        self.m_browser_details.clear()
        l_process_status = get_process_status(l_item)
        self.m_browser_details.append(l_process_status)

        parse_process_status(l_process_status, "VmStat")


def main():
    l_app = QApplication(sys.argv)
    l_form = Form()
    l_form.show()
    l_app.exec_()


if __name__ == '__main__':
    main()
