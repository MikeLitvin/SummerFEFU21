import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calc_ui import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 512, 512)
        self.setWindowTitle('Calculator')
        self.setupUi(self)

        self.exp = ''

        self.btn0.clicked.connect(lambda: self.add_symbol('0'))
        self.btn1.clicked.connect(lambda: self.add_symbol('1'))
        self.btn2.clicked.connect(lambda: self.add_symbol('2'))
        self.btn3.clicked.connect(lambda: self.add_symbol('3'))
        self.btn4.clicked.connect(lambda: self.add_symbol('4'))
        self.btn5.clicked.connect(lambda: self.add_symbol('5'))
        self.btn6.clicked.connect(lambda: self.add_symbol('6'))
        self.btn7.clicked.connect(lambda: self.add_symbol('7'))
        self.btn8.clicked.connect(lambda: self.add_symbol('8'))
        self.btn9.clicked.connect(lambda: self.add_symbol('9'))
        self.btn_open.clicked.connect(lambda: self.add_symbol('('))
        self.btn_close.clicked.connect(lambda: self.add_symbol(')'))
        self.btn_point.clicked.connect(lambda: self.add_symbol('.'))
        self.btn_div.clicked.connect(lambda: self.add_symbol('/'))
        self.btn_mult.clicked.connect(lambda: self.add_symbol('*'))
        self.btn_minus.clicked.connect(lambda: self.add_symbol('-'))
        self.btn_plus.clicked.connect(lambda: self.add_symbol('+'))
        self.btn_eval.clicked.connect(lambda: self.get_eval())
        self.btn_ac.clicked.connect(lambda: self.clear_screen())
        self.btn_back.clicked.connect(lambda: self.pop_back())

    def add_symbol(self, value):
        self.exp += value
        self.expression.setText("{}".format(self.exp))

    def pop_back(self):
        self.exp = self.exp[0:-1]
        self.expression.setText("{}".format(self.exp))

    def get_eval(self):
        try:
            self.expression.setText("{}".format(eval(self.exp)))
            self.exp = ''
        except:
            self.expression.setText("{}".format("Error"))
            self.exp = ''

    def clear_screen(self):
        self.exp = ''
        self.expression.setText("{}".format(self.exp))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
