#!/usr/bin/env python

from PyQt4 import QtGui
from canvagif.mainwindow import CanvagifMainWindow


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = CanvagifMainWindow()
    app.setActiveWindow(window)
    window.show()
    app.exec_()
