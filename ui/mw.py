# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(322, 409)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(322, 409))
        MainWindow.setMaximumSize(QtCore.QSize(322, 409))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_1 = QtWidgets.QPushButton(MainWindow)
        self.btn_1.setGeometry(QtCore.QRect(10, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(MainWindow)
        self.btn_2.setGeometry(QtCore.QRect(80, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(MainWindow)
        self.btn_3.setGeometry(QtCore.QRect(150, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(MainWindow)
        self.btn_4.setGeometry(QtCore.QRect(10, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(MainWindow)
        self.btn_5.setGeometry(QtCore.QRect(80, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(MainWindow)
        self.btn_6.setGeometry(QtCore.QRect(150, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(MainWindow)
        self.btn_7.setGeometry(QtCore.QRect(10, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(MainWindow)
        self.btn_8.setGeometry(QtCore.QRect(80, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(MainWindow)
        self.btn_9.setGeometry(QtCore.QRect(150, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_0 = QtWidgets.QPushButton(MainWindow)
        self.btn_0.setGeometry(QtCore.QRect(10, 340, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_equal = QtWidgets.QPushButton(MainWindow)
        self.btn_equal.setGeometry(QtCore.QRect(80, 340, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_equal.setFont(font)
        self.btn_equal.setObjectName("btn_equal")
        self.btn_div = QtWidgets.QPushButton(MainWindow)
        self.btn_div.setGeometry(QtCore.QRect(220, 130, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_multi = QtWidgets.QPushButton(MainWindow)
        self.btn_multi.setGeometry(QtCore.QRect(220, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_multi.setFont(font)
        self.btn_multi.setObjectName("btn_multi")
        self.btn_minus = QtWidgets.QPushButton(MainWindow)
        self.btn_minus.setGeometry(QtCore.QRect(220, 270, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_clear = QtWidgets.QPushButton(MainWindow)
        self.btn_clear.setGeometry(QtCore.QRect(10, 100, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_back = QtWidgets.QPushButton(MainWindow)
        self.btn_back.setGeometry(QtCore.QRect(160, 100, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.btn_plus = QtWidgets.QPushButton(MainWindow)
        self.btn_plus.setGeometry(QtCore.QRect(220, 340, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.lbl_screen = QtWidgets.QLabel(MainWindow)
        self.lbl_screen.setGeometry(QtCore.QRect(10, 20, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_screen.setFont(font)
        self.lbl_screen.setStyleSheet("background-color: rgb(158, 255, 189);\n"
"border: 1px solid black;\n"
"")
        self.lbl_screen.setObjectName("lbl_screen")
        self.lbl_screen_2 = QtWidgets.QLabel(MainWindow)
        self.lbl_screen_2.setGeometry(QtCore.QRect(10, 0, 301, 20))
        self.lbl_screen_2.setText("")
        self.lbl_screen_2.setObjectName("lbl_screen_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_multi.setText(_translate("MainWindow", "x"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_clear.setText(_translate("MainWindow", "c"))
        self.btn_back.setText(_translate("MainWindow", "<X"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.lbl_screen.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"></p></body></html>"))
