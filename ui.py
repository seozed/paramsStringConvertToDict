# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 422)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 241, 321))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 171))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_input = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_input.setGeometry(QtCore.QRect(0, 20, 521, 141))
        self.textEdit_input.setObjectName("textEdit_input")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 521, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_output = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_output.setGeometry(QtCore.QRect(0, 20, 521, 141))
        self.textEdit_output.setObjectName("textEdit_output")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 816, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "convert params string to dict object"))
        self.pushButton.setText(_translate("MainWindow", "Convert To"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output"))

