# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 110, 161, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sldR = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.sldR.setOrientation(QtCore.Qt.Vertical)
        self.sldR.setObjectName("sldR")
        self.horizontalLayout.addWidget(self.sldR)
        self.sldG = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.sldG.setOrientation(QtCore.Qt.Vertical)
        self.sldG.setObjectName("sldG")
        self.horizontalLayout.addWidget(self.sldG)
        self.sldB = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.sldB.setOrientation(QtCore.Qt.Vertical)
        self.sldB.setObjectName("sldB")
        self.horizontalLayout.addWidget(self.sldB)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 20, 351, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 161, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QRbtn1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.QRbtn1.setObjectName("QRbtn1")
        self.verticalLayout.addWidget(self.QRbtn1)
        self.QRbtn2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.QRbtn2.setObjectName("QRbtn2")
        self.verticalLayout.addWidget(self.QRbtn2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 320, 161, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QRbtn1.setText(_translate("MainWindow", "수정모드"))
        self.QRbtn2.setText(_translate("MainWindow", "지정모드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

