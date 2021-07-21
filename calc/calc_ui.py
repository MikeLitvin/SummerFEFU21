# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.expression = QtWidgets.QLabel(self.centralwidget)
        self.expression.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(24)
        font.setItalic(False)
        self.expression.setFont(font)
        self.expression.setStyleSheet("padding: 5%;")
        self.expression.setText("")
        self.expression.setScaledContents(True)
        self.expression.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.expression.setObjectName("expression")
        self.verticalLayout_2.addWidget(self.expression)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 1, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 1, 1, 1, 1)
        self.btn_eval = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eval.setObjectName("btn_eval")
        self.gridLayout.addWidget(self.btn_eval, 4, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 3, 0, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 3, 3, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 1, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 3, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 4, 3, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 4, 1, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 4, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 1, 3, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 3, 2, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setMaximumSize(QtCore.QSize(199, 32))
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 0, 1, 1, 1)
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setObjectName("btn_open")
        self.gridLayout.addWidget(self.btn_open, 0, 0, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 0, 2, 1, 1)
        self.btn_ac = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setObjectName("btn_ac")
        self.gridLayout.addWidget(self.btn_ac, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn_eval.setText(_translate("MainWindow", "="))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_close.setText(_translate("MainWindow", ")"))
        self.btn_open.setText(_translate("MainWindow", "("))
        self.btn_back.setText(_translate("MainWindow", "<-"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
