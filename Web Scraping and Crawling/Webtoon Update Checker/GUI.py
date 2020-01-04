# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Temp\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 253)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 171, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 611, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 16))
        self.label_2.setObjectName("label_2")
        self.rb_10min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_10min.setGeometry(QtCore.QRect(20, 140, 71, 19))
        self.rb_10min.setObjectName("rb_10min")
        self.rb_5min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_5min.setGeometry(QtCore.QRect(110, 140, 71, 19))
        self.rb_5min.setObjectName("rb_5min")
        self.rb_1min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_1min.setGeometry(QtCore.QRect(190, 140, 71, 19))
        self.rb_1min.setObjectName("rb_1min")
        self.rb_30sec = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_30sec.setGeometry(QtCore.QRect(270, 140, 81, 19))
        self.rb_30sec.setObjectName("rb_30sec")
        self.rb_5sec = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_5sec.setGeometry(QtCore.QRect(360, 140, 71, 19))
        self.rb_5sec.setObjectName("rb_5sec")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(450, 130, 93, 28))
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(540, 130, 93, 28))
        self.btn_stop.setObjectName("btn_stop")
        self.lbl_print = QtWidgets.QLabel(self.centralwidget)
        self.lbl_print.setGeometry(QtCore.QRect(20, 180, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_print.setFont(font)
        self.lbl_print.setText("")
        self.lbl_print.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_print.setObjectName("lbl_print")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rb_10min.clicked.connect(MainWindow.setCycle)
        self.rb_5min.clicked.connect(MainWindow.setCycle)
        self.rb_1min.clicked.connect(MainWindow.setCycle)
        self.rb_30sec.clicked.connect(MainWindow.setCycle)
        self.rb_5sec.clicked.connect(MainWindow.setCycle)
        self.btn_start.clicked.connect(MainWindow.startChk)
        self.btn_stop.clicked.connect(MainWindow.stopChk)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update detector"))
        self.label.setText(_translate("MainWindow", "주소를 입력하세요"))
        self.label_2.setText(_translate("MainWindow", "주기를 선택하세요"))
        self.rb_10min.setText(_translate("MainWindow", "10min"))
        self.rb_5min.setText(_translate("MainWindow", "5min"))
        self.rb_1min.setText(_translate("MainWindow", "1min"))
        self.rb_30sec.setText(_translate("MainWindow", "30sec"))
        self.rb_5sec.setText(_translate("MainWindow", "5sec"))
        self.btn_start.setText(_translate("MainWindow", "체크 시작"))
        self.btn_stop.setText(_translate("MainWindow", "체크 종료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

