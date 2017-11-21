# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!


from ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *
from urllib.parse import parse_qsl
import json

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.convertToDict)

    def convertToDict(self):
        item = dict()
        input_text = self.textEdit_input.toPlainText()
        item.update(parse_qsl(input_text))
        self.textEdit_output.setText(json.dumps(item, indent=2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())