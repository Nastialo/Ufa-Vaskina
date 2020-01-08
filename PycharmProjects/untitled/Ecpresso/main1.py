import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        self.tableWidget.setRowCount(4)
        con = sqlite3.connect("coffee(1).db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM info").fetchall()
        for i in range(4):
            for j in range(7):
                self.tableWidget.setItem(i, j,  QTableWidgetItem(str(result[i][j])))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())