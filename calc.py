# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import sys
from ui.mw import Ui_MainWindow
from bs4 import BeautifulSoup

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
        self.ui.btn_plus.clicked.connect(self.edit_screen)
        self.ui.btn_div.clicked.connect(self.edit_screen)
        self.ui.btn_minus.clicked.connect(self.edit_screen)
        self.ui.btn_multi.clicked.connect(self.edit_screen)
        self.ui.btn_clear.clicked.connect(self.clear_screen)
        self.ui.btn_back.clicked.connect(self.clear_one)
        self.ui.btn_equal.clicked.connect(self.calculate)

    def calculate(self):
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        result = str()
        lbl_screen = self.ui.lbl_screen.text()
        soup = BeautifulSoup(lbl_screen, 'html.parser')

        if soup.p.get_text() and soup.p.get_text()[-1] not in '+-/x':
            result = soup.p.get_text().replace('x','*')    
            try:
                result = eval(result)
                if isinstance(result, float):
                    result = round(result, 6)
            except ZeroDivisionError:
                result = 'error'
            except NameError:
                result = ''
            self.ui.lbl_screen.setText(text_1 + str(result) + text_2)


    def clear_one(self):
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        lbl_screen = self.ui.lbl_screen.text()
        soup = BeautifulSoup(lbl_screen, 'html.parser')
        self.ui.lbl_screen.setText(text_1 + soup.p.get_text()[:-1] + text_2)

        if len(soup.p.get_text()) <= 11: 
            font = QtGui.QFont()
            font.setPointSize(36)
            self.ui.lbl_screen.setFont(font)
        elif len(soup.p.get_text()) <= 17:
            font = QtGui.QFont()
            font.setPointSize(24)
            self.ui.lbl_screen.setFont(font)
        else:
            pass

    def clear_screen(self):
        result = ''
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        self.ui.lbl_screen.setText(text_1 +  result + text_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.ui.lbl_screen.setFont(font)

    def edit_screen(self):
        sender = self.sender().text()
        result = str()
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        lbl_screen = self.ui.lbl_screen.text()
        soup = BeautifulSoup(lbl_screen, 'html.parser')
        print(sender)

        if len(soup.p.get_text()) == 25:
            result == soup.p.get_text()
            self.ui.lbl_screen.setText(text_1 + result + text_2)
            #TODO add max range on the 2. screen 
            

        if len(soup.p.get_text()) == 11: 
            font = QtGui.QFont()
            font.setPointSize(24)
            self.ui.lbl_screen.setFont(font)
        elif len(soup.p.get_text()) >= 17:
            font = QtGui.QFont()
            font.setPointSize(16)
            self.ui.lbl_screen.setFont(font)
        else:
            pass

        if sender in '/x+-':
            try:
                last_sign = soup.p.get_text()[-1]
                if (last_sign != '+') and (last_sign != '-') and (last_sign != '/') and (last_sign != 'x'):
                    result = soup.p.get_text() + sender
                else:
                    result = soup.p.get_text()
            except IndexError as err:
                pass

        elif sender in '0123456789':
            result = soup.p.get_text() + sender

        self.ui.lbl_screen.setText(text_1 +  result + text_2)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Calc()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()    