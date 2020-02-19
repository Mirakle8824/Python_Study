import sys, serial, glob
import Gui
from PyQt5.QtCore import pyqtSignal, QThread

__platform__ = sys.platform

class serialThreadClass(QThread, Gui.Ui_Dialog):
    pysig = pyqtSignal(str)
    Temp = 0

    def __init__(self, parent = None):
        super(serialThreadClass, self).__init__(parent)
        self.Temp_Buff = []
        self.port_list = []

        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i +1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsuported platform')

        for port in ports:
            try:
                self.seriport = serial.Serial(port)
                self.seriport.close()
                self.port_list.append(port)
            except (OSError, serial.SerialException):
                pass

    def run(self):
        while True:
            if self.seriport.in_waiting:
                buf = self.seriport.readline()

                buf_decode = (buf.decode('utf-8'))[:-1]
                print(buf_decode)


    def sendSerial(self, data):
        print(len(data))
        self.seriport.write(data.encode('utf-8'))




