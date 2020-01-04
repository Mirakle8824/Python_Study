from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy
import sys, time, random
from PyQt5.QtGui import QFont
from PyQt5.QtTest import QTest

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = []
        self.frt = ["a", "b", "c", "d", "e", "f", "g", "h", "a", "b", "c", "d", "e", "f", "g", "h"]
        self.cnt = 0
        self.a = 0
        self.b = 0

        for x in range(300):
            rnd = random.randint(0, 15)
            self.frt[rnd], self.frt[0] = self.frt[0], self.frt[rnd]

        self.grid = QGridLayout()
        self.grid.setSpacing(15)

        fnt = QFont()
        fnt.setBold(True)
        fnt.setPixelSize(50)

        for r in range(4):
            self.btn.append([])
            for c in range(4):
                self.btn[r].append(QPushButton(self.frt[r * 4 + c]))
                self.btn[r][c].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.btn[r][c].setFont(fnt)
                self.btn[r][c].setToolTip(str(r * 4 + c))
                self.btn[r][c].setToolTipDuration(1)
                self.btn[r][c].clicked.connect(self.test)
                self.grid.addWidget(self.btn[r][c], r, c)
            self.setLayout(self.grid)
            self.setGeometry(100, 100, 500, 500)

    def hidePzl(self):
        QTest.qWait(2000)
        for r in range(0, 4):
            for c in range(0, 4):
                self.btn[r][c].setText("?")


    def test(self):
        e = self.sender()
        if e.text() != "?":
            return
        if self.cnt == 0:
            self.cnt = 1
            e.setText(self.frt[int(e.toolTip())])
            self.a = int(e.toolTip())
        else:
            self.cnt = 0
            e.setText(self.frt[int(e.toolTip())])
            self.b = int(e.toolTip())
            self.chk(self.a, self.b)

    def chk(self, a, b):
        if self.frt[a] != self.frt[b]:
            QTest.qWait(100)
            self.btn[a // 4][a % 4].setText("?")
            self.btn[b // 4][b % 4].setText("?")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    win.show()
    win.hidePzl()
    sys.exit(app.exec_())