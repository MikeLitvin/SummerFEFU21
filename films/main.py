import sys
from itertools import groupby
from interface import Ui_Films

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QVBoxLayout, QLineEdit, QComboBox, \
    QLabel, QSpinBox
from PyQt5 import uic, QtCore
import sqlite3

con = sqlite3.connect("films.db")
cur = con.cursor()

# films = cur.execute("""SELECT * FROM Films""").fetchall()
all_genres = cur.execute("""SELECT title FROM genres""").fetchall()
all_genres_id = cur.execute("""SELECT id FROM genres""").fetchall()
genres = [el for el, _ in groupby(all_genres)]
genres_id = [el for el, _ in groupby(all_genres_id)]


def get_id_by_genre(genre):
    for i in range(len(genres)):
        if str(genres[i])[2:-3] == genre:
            return i


class AddFilm(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 256, 256)
        self.setWindowTitle('Add film')

        layout = QVBoxLayout()

        self.add_save_button = QPushButton('Сохранить', clicked=self.save_film)
        self.add_back_button = QPushButton('Отменить', clicked=self.close_window)
        self.film_name_field = QLineEdit()
        self.film_year_field = QSpinBox()
        self.film_year_field.setMaximum(2021)
        self.film_duration_field = QSpinBox()
        self.film_duration_field.setMaximum(1000)
        self.film_genre_box = QComboBox()
        self.film_name_label = QLabel('Название')
        self.film_year_label = QLabel('Год')
        self.film_duration_label = QLabel('Продолжительность')

        for elem in genres:
            self.film_genre_box.addItem(str(elem)[2:-3])

        layout.addWidget(self.film_name_label)
        layout.addWidget(self.film_name_field)
        layout.addWidget(self.film_year_label)
        layout.addWidget(self.film_year_field)
        layout.addWidget(self.film_duration_label)
        layout.addWidget(self.film_duration_field)
        layout.addWidget(self.film_genre_box)
        layout.addWidget(self.add_save_button)
        layout.addWidget(self.add_back_button)

        self.setLayout(layout)

        self.name = self.film_name_field.text()
        self.year = self.film_year_field.value()
        self.duration = self.film_duration_field.value()
        self.genre = self.film_genre_box.currentText()

    def save_film(self):
        current_film_id = list(cur.execute("""SELECT COUNT(*) FROM Films""").fetchone())[0] + 1000
        cur.execute(f"""INSERT INTO Films(id, title, year, genre, duration)
        VALUES(?, ?, ?, ?, ?)""", (current_film_id, self.name, self.year, get_id_by_genre(self.genre), self.duration))
        con.commit()
        self.close()

    def close_window(self):
        self.close()


class Films(QWidget, Ui_Films):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.genre_box.addItem('')
        self.setWindowTitle('Films')
        for elem in genres:
            self.genre_box.addItem(str(elem)[2:-3])
        self.search_button.clicked.connect(self.load_data)
        self.add_button.clicked.connect(self.add_film)

    def add_film(self):
        self.add_window = AddFilm()
        self.add_window.show()

    def load_data(self):
        self.tableWidget.setRowCount(0)
        current_genre = self.genre_box.currentText()
        current_name = self.film_name.text()
        current_year = self.film_year.text()
        current_duration = self.film_duration.text()
        print(current_genre)
        if current_genre == '' and current_duration and current_year:
            films = cur.execute("""SELECT * FROM Films WHERE 
            (title like "{}%") AND (duration = {}) AND (year = {})""".format(current_name, current_duration, current_year)).fetchall()
        elif current_genre == '' and current_year:
            films = cur.execute("""SELECT * FROM Films WHERE 
            (title like "{}%") AND (year = {})""".format(current_name, current_year)).fetchall()
        elif current_genre == '' and current_duration:
            films = cur.execute("""SELECT * FROM Films WHERE 
            (title like "{}%") AND (duration = {})""".format(current_name, current_duration)).fetchall()
        elif current_genre == '':
            films = cur.execute("""SELECT * FROM Films WHERE 
            (title like "{}%")""".format(current_name)).fetchall()
        elif current_duration and current_year:
            films = cur.execute("""SELECT * FROM Films WHERE genre=(
                            SELECT id FROM genres WHERE title = '{}') 
                            AND (title like "{}%") AND (duration = {}) AND (year = {})""".format(current_name, current_duration, current_year)).fetchall()
        elif current_year:
            films = cur.execute("""SELECT * FROM Films WHERE genre=(
                            SELECT id FROM genres WHERE title = '{}') 
                            AND (title like "{}%") AND (year = {})""".format(current_genre, current_name, current_year)).fetchall()
        elif current_duration:
            films = cur.execute("""SELECT * FROM Films WHERE genre=(
                            SELECT id FROM genres WHERE title = '{}') 
                            AND (title like "{}%") AND (duration = {})""".format(current_genre, current_name, current_duration)).fetchall()
        else:
            films = cur.execute("""SELECT * FROM Films WHERE genre=(
                SELECT id FROM genres WHERE title = '{}') AND (title like "{}%")""".format(current_genre, current_name)).fetchall()
        for row, film in enumerate(films):
            self.tableWidget.insertRow(row)
            for column, data in enumerate(film):
                if column == 3:
                    data = cur.execute("""SELECT title FROM genres WHERE id = {}""".format(data)).fetchone()
                    cell = QTableWidgetItem(str(data)[2:-3])
                    self.tableWidget.setItem(row, column, cell)
                elif column == 0:
                    cell = QTableWidgetItem(str(data))
                    cell.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(row, column, cell)
                else:
                    cell = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row, column, cell)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Films()
    ex.show()
    sys.exit(app.exec())

con.close()

