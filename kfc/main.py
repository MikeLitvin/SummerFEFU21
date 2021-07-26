import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore, QtWidgets

import json

with open('products.json') as file:
    products = json.load(file)


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 580, 210))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 250, 200, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setText("Купить")

    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle("Терминал")


class UiSetValue(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(210, 80)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 40, 130, 35))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 190, 30))
        self.spinBox.setObjectName("spinBox")

        self.retranslate_ui(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, Dialog):
        Dialog.setWindowTitle("Выберите количество")


class UiCheque(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 580, 230))
        self.textBrowser.setObjectName("textBrowser")

    def retranslate_ui(self, Form):
        Form.setWindowTitle("Чек")


value = 0


class Cheque(QWidget, UiCheque):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


class SetValue(QDialog, UiSetValue):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.buttonBox.accepted.connect(self.get_value)

    def get_value(self):
        global value
        value = self.spinBox.value()


class Terminal(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.cheque = Cheque()
        self.setup_ui(self)
        self.listWidget.setViewMode(QListWidget.IconMode)
        for item in products:
            pixmap = QPixmap(item['src'])
            item = QListWidgetItem(QIcon(pixmap), item['name'] + ' - ' + item['cost'])
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
        self.listWidget.itemChanged.connect(self.changed)
        self.order = dict()
        self.prices = dict()
        self.pushButton.clicked.connect(self.get_cheque)

    def changed(self, item):
        pos, price = item.text().split(' - ')
        self.prices[pos] = int(price)
        if item.checkState():
            window = SetValue()
            window.show()
            window.exec()
            self.order[pos] = value
        else:
            self.order[item.text()] = 0

    def get_cheque(self):
        total_price = 0
        cheque_text = str()
        for name in self.order.keys():
            if self.order[name] > 0:
                current_price = self.prices[name] * self.order[name]
                if 1 == current_price % 10:
                    rubles = 'рубль'
                elif 2 <= current_price % 10 <= 4:
                    rubles = 'рубля'
                else:
                    rubles = 'рублей'
                cheque_text += '"{}" в количестве {} шт., \t {} {}.\n'.format(name,
                                                                              self.order[name], current_price, rubles)
                total_price += current_price
        if 1 == total_price % 10:
            rubles = 'рубль'
        elif 2 <= total_price % 10 <= 4:
            rubles = 'рубля'
        else:
            rubles = 'рублей'
        cheque_text += "Сумма к оплате: {} {}".format(total_price, rubles)
        self.cheque.textBrowser.setText(cheque_text)
        self.cheque.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Terminal()
    ex.show()
    sys.exit(app.exec())
