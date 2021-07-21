import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QHBoxLayout,
                             QTextBrowser, QTextEdit, QVBoxLayout)


class Editor(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 512, 512)
        self.setWindowTitle('HTML Editor')

        main_layout = QVBoxLayout()
        additional_layout = QHBoxLayout()

        self.render_button = QPushButton('Get Text', clicked=self.generate_html)

        self.render_button.setStyleSheet('QPushButton {background-color: #75691A; '
                                         'color: #F7E780;}')
        
        self.text_browser = QTextBrowser()
        self.text_editor = QTextEdit()
        additional_layout.addWidget(self.text_editor)
        additional_layout.addWidget(self.text_browser)
        main_layout.addLayout(additional_layout)
        main_layout.addWidget(self.render_button)
        self.setLayout(main_layout)

    def generate_html(self):
        self.text_browser.clear()
        text = self.text_editor.toPlainText()
        self.text_browser.append('{}'.format(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Editor()
    ex.show()
    sys.exit(app.exec())
