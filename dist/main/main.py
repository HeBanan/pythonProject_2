import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import csv
import traceback


def exception_hook(exctype, value, traceback):
    traceback_formated = traceback.format_exception(exctype, value, traceback)
    traceback_string = "".join(traceback_formated)
    print(traceback_string, file=sys.stderr)
    sys.exit(1)


sys.excepthook = exception_hook


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow")
        MainWindow_2.resize(284, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(50, 230, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.update_label = QtWidgets.QLabel(self.centralwidget)
        self.update_label.setGeometry(QtCore.QRect(10, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.update_label.setFont(font)
        self.update_label.setObjectName("update_label")
        self.nazad = QtWidgets.QPushButton(self.centralwidget)
        self.nazad.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nazad.setFont(font)
        self.nazad.setObjectName("nazad")
        self.update_name_label = QtWidgets.QLabel(self.centralwidget)
        self.update_name_label.setGeometry(QtCore.QRect(10, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_name_label.setFont(font)
        self.update_name_label.setObjectName("update_name_label")
        self.update_kurs_label = QtWidgets.QLabel(self.centralwidget)
        self.update_kurs_label.setGeometry(QtCore.QRect(10, 150, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_kurs_label.setFont(font)
        self.update_kurs_label.setObjectName("update_kurs_label")
        self.update_value_name = QtWidgets.QTextEdit(self.centralwidget)
        self.update_value_name.setGeometry(QtCore.QRect(10, 100, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.update_value_name.setFont(font)
        self.update_value_name.setObjectName("update_value_name")
        self.update_kurs = QtWidgets.QTextEdit(self.centralwidget)
        self.update_kurs.setGeometry(QtCore.QRect(10, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_kurs.setFont(font)
        self.update_kurs.setObjectName("update_kurs")
        self.dobavit_image = QtWidgets.QLabel(self.centralwidget)
        self.dobavit_image.setGeometry(QtCore.QRect(230, 20, 71, 71))
        self.dobavit_image.setText("")
        self.dobavit_image.setPixmap(QtGui.QPixmap("dobavit_transformed.png"))
        self.dobavit_image.setObjectName("dobavit_image")
        MainWindow_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.update_button.setText(_translate("MainWindow", "Обновить"))
        self.update_label.setText(_translate("MainWindow", "Добавление валюты"))
        self.nazad.setText(_translate("MainWindow", "Назад"))
        self.update_name_label.setText(_translate("MainWindow", "Валюта в 3-х буквенном формате"))
        self.update_kurs_label.setText(_translate("MainWindow", "Её курс к USD"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow_2")
        MainWindow.resize(361, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.valuta = QtWidgets.QTextEdit(self.centralwidget)
        self.valuta.setGeometry(QtCore.QRect(90, 120, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.valuta.setFont(font)
        self.valuta.setObjectName("valuta")
        self.kolichestvo = QtWidgets.QTextEdit(self.centralwidget)
        self.kolichestvo.setGeometry(QtCore.QRect(90, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.kolichestvo.setFont(font)
        self.kolichestvo.setObjectName("kolichestvo")
        self.vvalytu = QtWidgets.QTextEdit(self.centralwidget)
        self.vvalytu.setGeometry(QtCore.QRect(90, 200, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.vvalytu.setFont(font)
        self.vvalytu.setObjectName("vvalytu")
        self.konvert = QtWidgets.QPushButton(self.centralwidget)
        self.konvert.setGeometry(QtCore.QRect(60, 280, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.konvert.setFont(font)
        self.konvert.setObjectName("konvert")
        self.project_name = QtWidgets.QLabel(self.centralwidget)
        self.project_name.setGeometry(QtCore.QRect(70, 40, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.project_name.setFont(font)
        self.project_name.setObjectName("project_name")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(260, 40, 81, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo-transformed.png"))
        self.logo.setObjectName("logo")
        self.valuta_label = QtWidgets.QLabel(self.centralwidget)
        self.valuta_label.setGeometry(QtCore.QRect(0, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valuta_label.setFont(font)
        self.valuta_label.setObjectName("valuta_label")
        self.kolichestvo_label = QtWidgets.QLabel(self.centralwidget)
        self.kolichestvo_label.setGeometry(QtCore.QRect(0, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kolichestvo_label.setFont(font)
        self.kolichestvo_label.setObjectName("kolichestvo_label")
        self.vvalytu_label = QtWidgets.QLabel(self.centralwidget)
        self.vvalytu_label.setGeometry(QtCore.QRect(0, 200, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vvalytu_label.setFont(font)
        self.vvalytu_label.setObjectName("vvalytu_label")
        self.itog_label = QtWidgets.QLabel(self.centralwidget)
        self.itog_label.setGeometry(QtCore.QRect(10, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.itog_label.setFont(font)
        self.itog_label.setObjectName("itog_label")
        self.itog = QtWidgets.QLabel(self.centralwidget)
        self.itog.setGeometry(QtCore.QRect(96, 243, 261, 39))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.itog.setFont(font)
        self.itog.setObjectName("itog")
        self.primer_valuta = QtWidgets.QLabel(self.centralwidget)
        self.primer_valuta.setGeometry(QtCore.QRect(280, 120, 81, 41))
        self.primer_valuta.setObjectName("primer_valuta")
        self.primer_kolichestvo = QtWidgets.QLabel(self.centralwidget)
        self.primer_kolichestvo.setGeometry(QtCore.QRect(280, 160, 71, 41))
        self.primer_kolichestvo.setObjectName("primer_kolichestvo")
        self.primer_vvalyru = QtWidgets.QLabel(self.centralwidget)
        self.primer_vvalyru.setGeometry(QtCore.QRect(280, 200, 81, 41))
        self.primer_vvalyru.setObjectName("primer_vvalyru")
        self.dobavit_value = QtWidgets.QPushButton(self.centralwidget)
        self.dobavit_value.setGeometry(QtCore.QRect(100, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dobavit_value.setFont(font)
        self.dobavit_value.setObjectName("dobavit_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project конвертор валют"))
        self.konvert.setText(_translate("MainWindow", "Конвертировать"))
        self.project_name.setText(_translate("MainWindow", "Конвертор валют"))
        self.valuta_label.setText(_translate("MainWindow", "Валюта:"))
        self.kolichestvo_label.setText(_translate("MainWindow", "Кол-во:"))
        self.vvalytu_label.setText(_translate("MainWindow", "В валюту:"))
        self.itog_label.setText(_translate("MainWindow", "Итог:"))
        self.itog.setText(_translate("MainWindow", "-"))
        self.primer_valuta.setText(_translate("MainWindow", "(RUB/USD/CNY)"))
        self.primer_kolichestvo.setText(_translate("MainWindow", "(Число)"))
        self.primer_vvalyru.setText(_translate("MainWindow", "(RUB/USD/CNY)"))
        self.dobavit_value.setText(_translate("MainWindow", "Обновить валюты"))


class MyProject_dialogue(Ui_MainWindow_2, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.nazad.clicked.connect(self.nazad_func)
        self.update_button.clicked.connect(self.insert_func)
        self.show()

    def nazad_func(self):
        self.close()

    def insert_func(self):
        db = sqlite3.connect("Database_cursValut")
        dbcur = db.cursor()
        new_value = self.update_value_name.toPlainText()
        new_value_kurs = self.update_kurs.toPlainText()
        old_value = list(i[0] for i in dbcur.execute("""SELECT value FROM exchange_rates""").fetchall())
        if new_value in old_value:
            dbcur.execute(f"""UPDATE exchange_rates SET kurs_k_USD={float(new_value_kurs)} 
            WHERE value LIKE '{new_value}'""")
        else:
            dbcur.execute(f"""INSERT INTO exchange_rates (value, kurs_k_USD) 
            VALUES ('{new_value}', '{float(new_value_kurs)}')""")
            dbcur.execute(f"""INSERT INTO dobavlenie_value (dobav_value, kurs_new_value) 
            VALUES ('{new_value}', '{float(new_value_kurs)}')""")
        db.commit()
        dbcur.close()


class MyProject(Ui_MainWindow, QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.konvert.clicked.connect(self.func)
        self.dobavit_value.clicked.connect(self.dobav_func)

    def func(self):
        db = sqlite3.connect("Database_cursValut")
        dbcur = db.cursor()

        value = self.valuta.toPlainText()
        kolvo = self.kolichestvo.toPlainText()
        value2 = self.vvalytu.toPlainText()

        kurs = dbcur.execute(f"""SELECT kurs_k_USD FROM exchange_rates WHERE value LIKE '{value}' """).fetchall()
        kurs2 = dbcur.execute(f"""SELECT kurs_k_USD FROM exchange_rates WHERE value LIKE '{value2}' """).fetchall()

        value_itog = round((float(kolvo) * float(kurs[0][0])) / float(kurs2[0][0]), 3)
        self.itog.setText(str(value_itog))
        with open("popular_value.csv", "a", encoding="utf8") as popular:
            popular.write(value + "\n")

    def dobav_func(self):
        self.dialogue_window = MyProject_dialogue()
        self.dialogue_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyProject()
    ex.show()
    sys.exit(app.exec_())