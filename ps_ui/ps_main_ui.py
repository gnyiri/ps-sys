#!/usr/bin/env python

import sys
from ps_utils.py_file_stat import DirStat
from ps_utils.py_proc_stat import *
from ps_ui.ps_graph_widget import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainForm(QDialog):
    def __init__(self, p_parent=None):
        super(MainForm, self).__init__(p_parent)
        self.m_btn_process_query = QPushButton('Get process id-s')
        self.m_list_process = QListWidget()
        self.m_combo_status_section = QComboBox()
        self.m_browser_details = QTextBrowser()
        self.m_graph_widget = GraphWidget()

        l_layout = QGridLayout()
        l_layout.addWidget(self.m_btn_process_query, 0, 0)
        l_layout.addWidget(self.m_list_process, 1, 0)
        l_layout.addWidget(self.m_combo_status_section, 0, 1)
        l_layout.addWidget(self.m_browser_details, 1, 1)
        l_layout.addWidget(self.m_graph_widget)

        self.setLayout(l_layout)
        self.connect(self.m_btn_process_query, SIGNAL('clicked()'), self.update_process_ids)
        self.connect(self.m_list_process, SIGNAL('itemClicked(QListWidgetItem *)'), self.update_process_details)
        self.setWindowTitle('py-sys')

    def update_process_ids(self):
        l_process_ids = get_process_ids()

        assert isinstance(l_process_ids, list)

        for l_process_id in l_process_ids:
            l_process_name = parse_process_status(l_process_id, 'Name')
            l_item = QListWidgetItem(QString(str(l_process_id) + ' (' + l_process_name + ')'))
            self.m_list_process.addItem(l_item)

        self.m_combo_status_section.addItem('VmPeak')
        self.m_combo_status_section.addItem('VmSize')

    def update_process_details(self, p_item):
        l_process_id = str(p_item.text())
        l_process_id = l_process_id.split(' ')

        self.m_browser_details.clear()
        l_process_status = get_process_status(l_process_id[0])

        self.m_browser_details.append(l_process_status)

        parse_process_status(l_process_id[0], 'Cpus_allowed')
