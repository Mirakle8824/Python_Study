import sys, GUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtTest import QTest

class main(QWidget, GUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn = []
        self.gridLayout.setSpacing(5)
        for r in range(3):
            self.btn.append([])
            for c in range(3):
                self.btn[r].append(QPushButton(""))
                self.btn[r][c].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.btn[r][c].setStyleSheet("background-color:rgb(150, 170, 180)")
                self.btn[r][c].setCheckable(True)
                self.btn[r][c].clicked.connect(self.test)
                self.gridLayout.addWidget(self.btn[r][c], r, c)

        self.QRbtn1.setChecked(True)
        self.QRbtn1.clicked.connect(self.changeMode)
        self.QRbtn2.clicked.connect(self.changeMode)
        self.sldR.valueChanged.connect(self.setRgb)
        self.sldG.valueChanged.connect(self.setRgb)
        self.sldB.valueChanged.connect(self.setRgb)

    def changeMode(self):
        if self.QRbtn2.isChecked():
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

        self.pushButton_3.setStyleSheet(tmp)
        if self.QRbtn1.isChecked():
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
    win = main()
    win.show()
    sys.exit(app.exec_())