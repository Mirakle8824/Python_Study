from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer
from bs4 import BeautifulSoup as bs
import urllib.request as req, sys, time
from GUI import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.chk)
        self.timer.setInterval(5 * 60 * 1000)
        self.rb_10min.setChecked(True)
        self.show()

    def setCycle(self):
        if self.rb_10min.isChecked():
            self.timer.setInterval(10 * 60 * 1000)
        elif self.rb_5min.isChecked():
            self.timer.setInterval(5 * 60 * 1000)
        elif self.rb_1min.isChecked():
            self.timer.setInterval(1 * 60 * 1000)
        elif self.rb_30sec.isChecked():
            self.timer.setInterval(1 * 10 * 1000)
        elif self.rb_5sec.isChecked():
            self.timer.setInterval(1 * 5 * 1000)


    def startChk(self):
        self.lineEdit.setEnabled(False)
        self.timer.start()

    def stopChk(self):
        self.lineEdit.setEnabled(True)
        self.timer.stop()

    def chk(self):
        self.rsp = req.urlopen(self.lineEdit.text())
        self.html = bs(self.rsp, "html.parser")
        try:
            self.test = self.html.find(alt="UP").attrs['alt']
        except:
            self.test = "XX"
        self.t = time.localtime()
        self.lbl_print.setText("{}:{}:{} 체크결과:{}".format(self.t.tm_hour, self.t.tm_min, self.t.tm_sec, self.test))

app = QApplication([])
ex = Example()
sys.exit(app.exec_())




