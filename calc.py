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

    def clear_one(self):
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        lbl_screen = self.ui.lbl_screen.text()
        soup = BeautifulSoup(lbl_screen, 'html.parser')
        self.ui.lbl_screen.setText(text_1 + soup.p.get_text()[:-1] + text_2)

    def clear_screen(self):
        result = ''
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        self.ui.lbl_screen.setText(text_1 +  result + text_2)


    def edit_screen(self):
        sender = self.sender().text()
        result = str()
        text_1 = '<html><head/><body><p align="right">'
        text_2 = '</p></body></html>'
        lbl_screen = self.ui.lbl_screen.text()
        soup = BeautifulSoup(lbl_screen, 'html.parser')
        print(sender)

        print('buraya bak: ', soup.p.get_text())
        if soup.p.get_text() == '0':
            print('buraya girildi')
            self.ui.lbl_screen.setText(text_1 + '' + text_2)

        if sender in '/x+-':
            try:
                if sender == '+':
                    if soup.p.get_text()[-1] != '+':
                        result = soup.p.get_text() + '+'
                    else:
                        result = soup.p.get_text()

                if sender == '-':
                    if soup.p.get_text()[-1] != '-':
                        result = soup.p.get_text() + '-'
                    else:
                        result = soup.p.get_text()

                if sender == 'x':
                    if soup.p.get_text()[-1] != 'x':
                        result = soup.p.get_text() + 'x'
                    else:
                        result = soup.p.get_text()

                if sender == '/':
                    if soup.p.get_text()[-1] != '/':
                        result = soup.p.get_text() + '/'
                    else:
                        result = soup.p.get_text()
            except IndexError as err:
                pass

        elif sender in '0123456789':
            if sender == '0':
                result = soup.p.get_text() + '0'
            elif sender == '1':
                result = soup.p.get_text() + '1'
            elif sender == '2':
                result = soup.p.get_text() + '2'
            elif sender == '3':
                result = soup.p.get_text() + '3'
            elif sender == '4':
                result = soup.p.get_text() + '4'
            elif sender == '5':
                result = soup.p.get_text() + '5'
            elif sender == '6':
                result = soup.p.get_text() + '6'
            elif sender == '7':
                result = soup.p.get_text() + '7'
            elif sender == '8':
                result = soup.p.get_text() + '8'
            elif sender == '9':
                result = soup.p.get_text() + '9'

        self.ui.lbl_screen.setText(text_1 +  result + text_2)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Calc()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()    