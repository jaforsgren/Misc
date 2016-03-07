# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Imports
import os
import sys
import subprocess
import threading
import time
import shutil

sys.path.append(r'\shared-fs1\imagetools\tools\Python27\Lib\site-packages')
from PySide import QtGui
from PySide import QtCore
from PySide.QtGui import*
from PySide.QtCore import *

class FunctionThread(QThread):
    """
    Qthread class with target
    """
    def __init__(self, target=None, parent=None):
            QThread.__init__(self, parent)
            self.function = target

    def run(self):
        if self.function != None:
            self.function()

r = FunctionThread()
