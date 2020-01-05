# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 376)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 161, 201))
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
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 310, 161, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 10, 351, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 161, 80))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.QRbtn1.setText(_translate("Form", "수정모드"))
        self.QRbtn2.setText(_translate("Form", "지정모드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

