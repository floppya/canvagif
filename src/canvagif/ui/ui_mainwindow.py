# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\canvagif\ui\mainwindow.ui'
#
# Created: Mon Apr 01 16:48:28 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AppMainWindow(object):
    def setupUi(self, AppMainWindow):
        AppMainWindow.setObjectName(_fromUtf8("AppMainWindow"))
        AppMainWindow.resize(985, 572)
        AppMainWindow.setAcceptDrops(False)
        AppMainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(AppMainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtUrl = QtGui.QLineEdit(self.centralwidget)
        self.txtUrl.setObjectName(_fromUtf8("txtUrl"))
        self.horizontalLayout.addWidget(self.txtUrl)
        self.butReload = QtGui.QPushButton(self.centralwidget)
        self.butReload.setObjectName(_fromUtf8("butReload"))
        self.horizontalLayout.addWidget(self.butReload)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        AppMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AppMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AppMainWindow.setStatusBar(self.statusbar)
        self.canvagifDockWidget = QtGui.QDockWidget(AppMainWindow)
        self.canvagifDockWidget.setObjectName(_fromUtf8("canvagifDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.butSelect = QtGui.QPushButton(self.dockWidgetContents)
        self.butSelect.setCheckable(True)
        self.butSelect.setObjectName(_fromUtf8("butSelect"))
        self.horizontalLayout_2.addWidget(self.butSelect)
        self.lblSelected = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSelected.sizePolicy().hasHeightForWidth())
        self.lblSelected.setSizePolicy(sizePolicy)
        self.lblSelected.setObjectName(_fromUtf8("lblSelected"))
        self.horizontalLayout_2.addWidget(self.lblSelected)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.spinFps = QtGui.QSpinBox(self.dockWidgetContents)
        self.spinFps.setMinimum(1)
        self.spinFps.setProperty("value", 10)
        self.spinFps.setObjectName(_fromUtf8("spinFps"))
        self.horizontalLayout_3.addWidget(self.spinFps)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinOutWidth = QtGui.QSpinBox(self.dockWidgetContents)
        self.spinOutWidth.setMaximum(1024)
        self.spinOutWidth.setProperty("value", 64)
        self.spinOutWidth.setObjectName(_fromUtf8("spinOutWidth"))
        self.horizontalLayout_4.addWidget(self.spinOutWidth)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinOutHeight = QtGui.QSpinBox(self.dockWidgetContents)
        self.spinOutHeight.setMaximum(1024)
        self.spinOutHeight.setProperty("value", 64)
        self.spinOutHeight.setObjectName(_fromUtf8("spinOutHeight"))
        self.horizontalLayout_4.addWidget(self.spinOutHeight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.butSelectOutputLocation = QtGui.QPushButton(self.dockWidgetContents)
        self.butSelectOutputLocation.setObjectName(_fromUtf8("butSelectOutputLocation"))
        self.verticalLayout.addWidget(self.butSelectOutputLocation)
        self.butRecord = QtGui.QPushButton(self.dockWidgetContents)
        self.butRecord.setCheckable(True)
        self.butRecord.setObjectName(_fromUtf8("butRecord"))
        self.verticalLayout.addWidget(self.butRecord)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.canvagifDockWidget.setWidget(self.dockWidgetContents)
        AppMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.canvagifDockWidget)

        self.retranslateUi(AppMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AppMainWindow)

    def retranslateUi(self, AppMainWindow):
        AppMainWindow.setWindowTitle(_translate("AppMainWindow", "Canvagif", None))
        self.butReload.setText(_translate("AppMainWindow", "Reload", None))
        self.canvagifDockWidget.setWindowTitle(_translate("AppMainWindow", "Recording", None))
        self.butSelect.setText(_translate("AppMainWindow", "Select element", None))
        self.lblSelected.setText(_translate("AppMainWindow", "None selected", None))
        self.label.setText(_translate("AppMainWindow", "Sample rate (fps)", None))
        self.label_2.setText(_translate("AppMainWindow", "Output size", None))
        self.label_3.setText(_translate("AppMainWindow", "x", None))
        self.butSelectOutputLocation.setText(_translate("AppMainWindow", "Select output location", None))
        self.butRecord.setText(_translate("AppMainWindow", "Record", None))

