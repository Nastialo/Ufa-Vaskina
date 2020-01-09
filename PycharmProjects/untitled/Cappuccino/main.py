import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
import sqlite3


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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
        if self.sender() == self.pushButton_2:
            i, okBtnPressed = QInputDialog.getInt(self, "Изменение обьекта",
                                                  "Введите номер id")
            if okBtnPressed:
                self.id = i
                result = cur.execute("SELECT * FROM info WHERE id=?", (self.id, )).fetchall()
                cur.execute("DELETE from info WHERE id=?", (self.id, ))
                con.commit()

                uic.loadUi('addEditCoffeeForm.ui', self)
                self.lineEdit.setText(str(result[0][1]))
                self.lineEdit_2.setText(str(result[0][2]))
                self.lineEdit_3.setText(str(result[0][3]))
                self.lineEdit_4.setText(str(result[0][4]))
                self.lineEdit_5.setText(str(result[0][5]))
                self.lineEdit_6.setText(str(result[0][6]))
        else:
            result = cur.execute("SELECT * FROM info").fetchall()
            self.id = result[-1][0] + 1
            uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.run2)

    def run2(self):
        al = [self.id, self.lineEdit.text(), str(self.lineEdit_2.text()), self.lineEdit_3.text(),
              self.lineEdit_4.text(), int(self.lineEdit_5.text()), int(self.lineEdit_6.text())]
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        cur.execute("INSERT INTO info VALUES(?, ?, ?, ?, ?, ?, ?)", al)
        uic.loadUi('main.ui', self)
        result = cur.execute("SELECT * FROM info").fetchall()
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