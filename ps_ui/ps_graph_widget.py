#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))

