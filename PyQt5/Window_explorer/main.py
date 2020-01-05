import sys, random, os, shutil
from PyQt5.QtWidgets import QApplication, QTreeView, QWidget, QGridLayout, QPushButton, QSizePolicy, QSlider, QGraphicsRectItem, QGraphicsScene, QGraphicsItem, \
    QGraphicsView, QVBoxLayout, QFileSystemModel, QInputDialog, QLineEdit
from PyQt5.QtGui import QTransform, QColor
from PyQt5.QtCore import Qt

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.path = "C:"
        self.index = None

        self.tv = QTreeView(self)
        self.model = QFileSystemModel()
        self.btnRen = QPushButton("이름바꾸기")
        self.btnDel = QPushButton("파일삭제")
        self.layout = QVBoxLayout()

        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 700, 350)
        self.setWindowTitle("QFileSystemModel")
        self.model.setRootPath(self.path)
        self.tv.setModel(self.model)
        self.tv.setColumnWidth(0, 250)

        self.layout.addWidget(self.tv)
        self.layout.addWidget(self.btnDel)
        self.layout.addWidget(self.btnRen)
        self.setLayout(self.layout)

    def setSlot(self):
        self.tv.clicked.connect(self.setIndex)
        self.btnRen.clicked.connect(self.ren)
        self.btnDel.clicked.connect(self.rm)

    def setIndex(self, index):
        self.index = index

    def ren(self):
        os.chdir(self.model.filePath(self.model.parent(self.index)))
        fname = self.model.fileName(self.index)
        text, res = QInputDialog.getText(self, "이름 바꾸기", "바꿀 이름을 입력하세요.",
                                         QLineEdit.Normal, fname)

        if res:
            while True:
                self.ok = True
                for i in os.listdir(os.getcwd()):
                    print(i)
                    if i == text:
                        text, res = QInputDialog.getText(self, " 중복오류!",
                                                         "바꿀 이름을 입력하세요.", QLineEdit.Normal, text)
                if self.ok:
                    break
            os.rename(fname, text)

    def rm(self):
        os.chdir(self.model.filePath(self.model.parent(self.index)))
        fname = self.model.fileName(self.index)
        try:
            if not self.model.isDir(self.index):
                os.unlink(fname)
                print(fname + '폴더삭제')
        except:
            print("에러발생")


app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())