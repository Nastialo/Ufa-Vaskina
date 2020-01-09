import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor("yellow"))
        x = randint(4, 495)
        y = randint(4, 435)
        a = randint(4, 435)
        qp.drawEllipse(x, y, a, a)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())