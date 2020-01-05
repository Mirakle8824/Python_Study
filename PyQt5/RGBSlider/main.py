from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy
import sys, GUI
from PyQt5.QtGui import QFont
from PyQt5.QtTest import QTest

class window(QWidget, GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn = []
        self.grid.setSpacing(5)
        for r in range(3):
            self.btn.append([])
            for c in range(3):
                self.btn[r].append(QPushButton(""))
                self.btn[r][c].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.btn[r][c].setStyleSheet("background-color:rgb(150, 170, 180)")
                self.btn[r][c].setCheckable(True)
                self.btn[r][c].clicked.connect(self.test)
                self.grid.addWidget(self.btn[r][c], r, c)

        self.QRbtn1.setChecked(True)
        self.QRbtn1.clicked.connect(self.changeMode)
        self.QRbtn2.clickded.connect(self.changeMode)
        self.sldR.valueCHanged.connect(self.setRgb)
        self.sldG.valueCHanged.connect(self.setRgb)
        self.sldB.valueCHanged.connect(self.setRgb)

    def changeMode(self):
        if self.QRbtn1.isChecked():
            for r in range(3):
                for c in range(3):
                    self.btn[r][c].setCheckable(False)
                    self.btn[r][c].update()
        else:
            for r in range(3):
                for c in range(3):
                    self.btn[r][c].setCheckable(True)

    def setRgb(self):
        tmp = "background-color:rgb({}, {}, {})".format(self.sldR.value(), self.sldG.value(), self.sldB.value())

        self.pushButton_3.setStyleSheet()
        for r in range(3):
            for c in range(3):
                if self.btn[r][c].isChecked():
                    self.btn[r][c].setStyleSheet(tmp)

    def test(self):
        e = self.sender()
        if self.QRbtn2.isChecked():
            e.setStyleSheet(self.pushButton_3.StyleSheet())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())