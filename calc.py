# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import sys
from ui.mw import Ui_MainWindow

class Calc(QtWidgets.QMainWindow):

    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\asus\Desktop\py_projets\calculator_gui\images\calculator.png'))
        self.ui.btn_0.clicked.connect(self.edit_screen)
        self.ui.btn_1.clicked.connect(self.edit_screen)
        self.ui.btn_2.clicked.connect(self.edit_screen)
        self.ui.btn_3.clicked.connect(self.edit_screen)
        self.ui.btn_4.clicked.connect(self.edit_screen)
        self.ui.btn_5.clicked.connect(self.edit_screen)
        self.ui.btn_6.clicked.connect(self.edit_screen)
        self.ui.btn_7.clicked.connect(self.edit_screen)
        self.ui.btn_8.clicked.connect(self.edit_screen)
        self.ui.btn_9.clicked.connect(self.edit_screen)


    def edit_screen(self):
        sender = self.sender().text()
        result = str()
        if sender == '0':
            result = self.ui.lbl_screen.text() + '0'
        if sender == '1':
            result = self.ui.lbl_screen.text() + '1'
        elif sender == '2':
            result = self.ui.lbl_screen.text() + '2'
        elif sender == '3':
            result = self.ui.lbl_screen.text() + '3'
        elif sender == '4':
            result = self.ui.lbl_screen.text() + '4'
        elif sender == '5':
            result = self.ui.lbl_screen.text() + '5'
        elif sender == '6':
            result = self.ui.lbl_screen.text() + '6'
        elif sender == '7':
            result = self.ui.lbl_screen.text() + '7'
        elif sender == '8':
            result = self.ui.lbl_screen.text() + '8'
        elif sender == '9':
            result = self.ui.lbl_screen.text() + '9'

        print(result)

        self.ui.lbl_screen.setText(result)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Calc()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()    