#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class GraphWidget(QWidget):
    XMARGIN = 12.0
    YMARGIN = 5.0
    WSTRING = "999"

    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))

    def sizeHint(self):
        return self.minimumSizeHint()

    def minimumSizeHint(self):
        return QSize(10, 200)



