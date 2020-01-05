import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy, QSlider, QGraphicsRectItem, QGraphicsScene, QGraphicsItem, \
    QGraphicsView, QVBoxLayout
from PyQt5.QtGui import QTransform, QColor
from PyQt5.QtCore import Qt

class Rectangle(QGraphicsRectItem):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.setBrush(QColor(250, 50, 0))
        self.setPen(QColor(0, 0, 0, 0))
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.tx = x+w/2
        self.ty = y+h/2

    def doRotate(self, alfa):
        tr = QTransform()
        tr.translate(self.tx, self.ty)
        tr.rotate(alfa)
        tr.translate(-self.tx, -self.ty)
        self.r, self.g, self.b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.setBrush(QColor(self.r, self.g, self.b))
        self.setTransform(tr)

class View(QGraphicsView):
    def __init__(self):
        super(View, self).__init__()

        self.scene = QGraphicsScene()
        self.setSceneRect(0, 0, 400, 400)

        self.rect1 = Rectangle(150, 150, 100, 100)
        self.rect2 = Rectangle(150, 150, 100, 100)
        self.scene.addItem(self.rect1)
        self.scene.addItem(self.rect2)

        self.setScene(self.scene)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rotation")
        self.setGeometry(150, 150, 425, 450)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.view = View()
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(-180, 180)

        self.sld.valueChanged.connect(self.changeValue)

        vbox.addWidget(self.view)
        vbox.addWidget(self.sld)
        self.setLayout(vbox)

    def changeValue(self):
        self.view.rect1.doRotate(self.sld.value())
        self.view.rect2.doRotate(self.sld.value())

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())