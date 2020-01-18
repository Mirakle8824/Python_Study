# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\82109\Desktop\Project\Python_Study\PyQt5\Send_E-Mail\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(652, 448)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 631, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtAtt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtAtt.setObjectName("txtAtt")
        self.gridLayout.addWidget(self.txtAtt, 2, 1, 1, 1)
        self.txtTitle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtTitle.setObjectName("txtTitle")
        self.gridLayout.addWidget(self.txtTitle, 1, 1, 1, 1)
        self.txtTo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtTo.setObjectName("txtTo")
        self.gridLayout.addWidget(self.txtTo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnAtt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAtt.setObjectName("btnAtt")
        self.gridLayout.addWidget(self.btnAtt, 2, 0, 1, 1)
        self.txtCont = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtCont.setObjectName("txtCont")
        self.gridLayout.addWidget(self.txtCont, 3, 1, 1, 1)
        self.btnSend = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout.addWidget(self.btnSend, 4, 1, 1, 1)
        self.btnReset = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout.addWidget(self.btnReset, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Title"))
        self.label_2.setText(_translate("Form", "To"))
        self.btnAtt.setText(_translate("Form", "File"))
        self.btnSend.setText(_translate("Form", "Send"))
        self.btnReset.setText(_translate("Form", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

