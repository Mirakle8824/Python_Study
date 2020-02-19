import sys, Gui

from Serial_set import serialThreadClass
from PyQt5.QtWidgets import QApplication, QDialog

class MainClass(QDialog, Gui.Ui_Dialog):

    BAUDRATES = (
        '1200',
        '2400',
        '4800',
        '9600',
        '19200',
        '38400',
        '57600',
        '115200',

    )

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.serial_th = serialThreadClass()

        self.seri_buad_set.insertItems(0, [str(x) for x in self.BAUDRATES])
        self.seri_port_set.insertItems(0, self.serial_th.port_list)

        self.seri_buad_set.currentTextChanged.connect(self.serial_setting)
        self.seri_port_set.currentTextChanged.connect(self.serial_setting)
        self.Btn_open_port.clicked.connect(self.serial_th_start)

        self.Btn_Receive_Code.clicked.connect(self.Receive_Code)
        self.Btn_Send_Code.clicked.connect(self.Send_Code)

        f = open("C:\Temp\ps14.txt", 'r')
        self.data = f.read()
        f.close()
        print(len(self.data))

    def serial_setting(self):
        self.serial_th.seriport.baudrate = self.seri_buad_set.currentText()
        self.serial_th.seriport.port = self.seri_port_set.currentText()

        print(self.serial_th.seriport.baudrate)
        print(self.serial_th.seriport.port)

    def serial_th_start(self):
        self.serial_th.seriport.open()
        self.serial_th.start()

    def Send_Code(self):
        self.serial_th.sendSerial(self.data)

    def Receive_Code(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = MainClass()
    main_dialog.show()
    app.exec()

