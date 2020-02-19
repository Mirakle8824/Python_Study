# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp\Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 290)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 171, 231))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 131, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.seri_port_set = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.seri_port_set.setObjectName("seri_port_set")
        self.verticalLayout.addWidget(self.seri_port_set)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.seri_buad_set = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.seri_buad_set.setObjectName("seri_buad_set")
        self.verticalLayout.addWidget(self.seri_buad_set)
        self.Btn_open_port = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_open_port.setObjectName("Btn_open_port")
        self.verticalLayout.addWidget(self.Btn_open_port)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 70, 131, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Send_Code = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Btn_Send_Code.setObjectName("Btn_Send_Code")
        self.verticalLayout_2.addWidget(self.Btn_Send_Code)
        self.Btn_Receive_Code = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Btn_Receive_Code.setObjectName("Btn_Receive_Code")
        self.verticalLayout_2.addWidget(self.Btn_Receive_Code)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Terminal Setting"))
        self.label.setText(_translate("Dialog", "Port"))
        self.label_2.setText(_translate("Dialog", "Buadrate"))
        self.Btn_open_port.setText(_translate("Dialog", "Open Port"))
        self.Btn_Send_Code.setText(_translate("Dialog", "Send Code"))
        self.Btn_Receive_Code.setText(_translate("Dialog", "Receive Code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

