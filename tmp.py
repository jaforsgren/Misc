# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class FunctionThread(QThread):
    """
    Qthread class with target
    """
        def __init__(self, target=None, parent=None):
                QThread.__init__(self, parent)
                self.function = function

        def run(self):
            if self.function != None:
                self.function()
