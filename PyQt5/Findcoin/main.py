import sys, random, os, shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData

class btn(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        ex.x, ex.y = e.x(), e.y()
        super().mousePressEvent(e)

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.sel = None
        self.x = 0
        self.y = 0
        self.cnt = 0
        self.btnList = []
        self.f = QFrame(self)
        for i in range(8):
            self.btnList.append(btn("동전" + str(i+1), self))
        self.btn1 = QPushButton("무게 재기(횟수: 0)", self)
        self.btn2 = QPushButton("초기화", self)
        self.lbl = QLabel('동전을 드래그하고 무게 재기 클릭!', self)
        self.cmb1 = QComboBox(self)
        self.cmb1.addItems(["불량동전은?", '1', '2', '3', '4', '5', '6', '7', '8'])
        self.cmb2 = QComboBox(self)
        self.cmb2.addItems(['무게는?', '무겁다', '가볍다'])
        self.lblRes = QLabel('정답여부', self)

        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setWindowTitle(("불량 동전 찾기"))
        self.setGeometry(300, 300, 500, 400)
        for i in range(8):
            self.btnList[i].move(20+(i%4)*80, 20+(i//4)*40)
        self.lbl.move(150, 100)
        self.f.setFrameShape(QFrame.VLine)
        self.f.setLineWidth(2)
        self.f.setStyleSheet("background-color:rgb(150,170,180)")
        self.f.setGeometry(0, 120, 500, 200)
        self.btn1.move(50, 350)
        self.btn2.move(400, 30)
        self.cmb1.move(200, 350)
        self.cmb2.move(300, 350)
        self.lblRes.move(420, 350)
        self.coinList = [0, 10, 10, 10, 10, 10, 10, 10, 10]
        self.coinList[random.randint(1, 8)] = random.choice([9, 11])
        self.cmb1.setCurrentIndex(0)
        self.cmb2.setCurrentIndex(0)
        self.lbl.setText('동전을 드래그하고 무게 재기 클릭!')
        self.lblRes.setText('정답여부')
        self.btn1.setText("무게 재기(횟수: 0)")
        self.cnt = 0

    def setSlot(self):
        self.setAcceptDrops(True)
        self.btn1.clicked.connect(self.chk)
        self.btn2.clicked.connect(self.setUi)
        self.cmb2.currentIndexChanged.connect(self.res)
        for i in range(8):
            self.btnList[i].pressed.connect(self.btnSel)

    def btnSel(self):
        self.sel = self.sender()

    def chk(self):
        self.cnt += 1
        x1, y1 = 0, 120
        x2, y2 = 250, 320
        x3, y3 = 250, 120
        x4, y4 = 500, 320
        L, R = 0, 0
        for i in self.btnList:
            if (x1 <i.x() and y1 < i.y()) and (x2 > i.x() and y2 > i.y()):
                L += self.coinList[int(i.text()[-1])]
            if (x3 < i.x() and y3 < i.y()) and (x4 > i.x() and y4 > i.y()):
                R += self.coinList[int(i.text()[-1])]
        if L > R:
            self.lbl.setText("왼쪽 저울이 더 무겁습니다.")
        elif L < R:
            self.lbl.setText("오른쪽 저울이 더 무겁습니다.")
        else:
            self.lbl.setText("양쪽 저울이 균형을 이룹니다!")

        self.btn1.setText("무게 측정(횟수 : {0}".format(self.cnt))

    def res(self):
        if self.cmb2.currentText() == "가볍다" and self.coinList[int(self.cmb1.currentText())] < 10:
            self.lblRes.setText("정답!!!!")
        elif self.cmb2.currentText() == "무겁다" and self.coinList[int(self.cmb1.currentText())] > 10:
            self.lblRes.setText("정답!!!!")
        else:
            self.lblRes.setText("땡!!!!")

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        self.sel.move(pos.x()-self.x, pos.y()-self.y)
        e.accept()

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())