import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 901, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 901, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 370, 431, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 370, 431, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название сорта"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Прожарка"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Вкус"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Вкус"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Обьем"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Информация о кофе</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Добавить новый вид "))
        self.pushButton_2.setText(_translate("MainWindow", "Редактировать"))


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = []
        self.id, self.sort, self.degree, self.tip, self.taste, self.price, self.volume = 4, "", 0, "", "", 0, 0
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM info").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.id = len(result)
        for i in range(len(result)):
            for j in range(7):
                self.tableWidget.setItem(i, j,  QTableWidgetItem(str(result[i][j])))
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        p = False

        ks = Second(self)

        self.w.append(ks)

        ks.setGeometry(300, 300, 800, 462)
        ks.lineEdit = QLineEdit(ks)
        ks.lineEdit_2 = QLineEdit(ks)
        ks.lineEdit_3 = QLineEdit(ks)
        ks.lineEdit_4 = QLineEdit(ks)
        ks.lineEdit_5 = QLineEdit(ks)
        ks.lineEdit_6 = QLineEdit(ks)
        ks.button = QPushButton('Готово', ks)
        ks.label = QLabel(ks)
        ks.label_2 = QLabel(ks)
        ks.label_3 = QLabel(ks)
        ks.label_4 = QLabel(ks)
        ks.label_7 = QLabel(ks)
        ks.label_5 = QLabel(ks)
        ks.label_6 = QLabel(ks)

        ks.lineEdit.setGeometry(QtCore.QRect(200, 120, 161, 22))
        ks.lineEdit_2.setGeometry(QtCore.QRect(200, 190, 161, 22))
        ks.lineEdit_3.setGeometry(QtCore.QRect(200, 260, 161, 22))
        ks.lineEdit_4.setGeometry(QtCore.QRect(600, 120, 161, 22))
        ks.lineEdit_5.setGeometry(QtCore.QRect(600, 190, 161, 22))
        ks.lineEdit_6.setGeometry(QtCore.QRect(600, 260, 161, 22))
        ks.label.setGeometry(QtCore.QRect(250, 30, 200, 22))
        ks.label.setText("Редактирование / Новый вид")
        ks.label_2.move(40, 120)
        ks.label_2.setText("Название сорта")
        ks.label_3.move(44, 185)
        ks.label_3.setText("Обжарка")
        ks.label_4.move(50, 255)
        ks.label_4.setText("Вид")
        ks.label_5.move(480, 110)
        ks.label_5.setText("Вкус")
        ks.label_6.move(480, 185)
        ks.label_6.setText("Цена")
        ks.label_7.move(480, 250)
        ks.label_7.setText("Обьем")
        ks.button.setGeometry(QtCore.QRect(270, 350, 251, 41))
        ks.button.clicked.connect(self.run2)

        if self.sender() == self.pushButton_2:
            i, okBtnPressed = QInputDialog.getInt(self, "Изменение обьекта",
                                                  "Введите номер id")
            if okBtnPressed:
                self.id = i
                result = cur.execute("SELECT * FROM info WHERE id=?", (self.id, )).fetchall()
                cur.execute("DELETE from info WHERE id=?", (self.id, ))
                con.commit()
                p = True

                ks.lineEdit.setText(str(result[0][1]))
                ks.lineEdit_2.setText(str(result[0][2]))
                ks.lineEdit_3.setText(str(result[0][3]))
                ks.lineEdit_4.setText(str(result[0][4]))
                ks.lineEdit_5.setText(str(result[0][5]))
                ks.lineEdit_6.setText(str(result[0][6]))
            else:
                self.w = self.w[:-1]

        else:
            p = True
            result = cur.execute("SELECT * FROM info").fetchall()
            self.id = result[-1][0] + 1
        if p:
            ks.show()

    def run2(self):
        al = [self.id, self.w[-1].lineEdit.text(), self.w[-1].lineEdit_2.text(), self.w[-1].lineEdit_3.text(),
              self.w[-1].lineEdit_4.text(), int(self.w[-1].lineEdit_5.text()), int(self.w[-1].lineEdit_6.text())]
        for i in self.w:
            i.close()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        cur.execute("INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ?)", al)
        result = cur.execute("SELECT * FROM info").fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())