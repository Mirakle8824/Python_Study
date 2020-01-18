import sys, random, os, GUI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP_SSL
from PyQt5.QtWidgets import *

class main(QWidget, GUI):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        # https://myaccount.google.com/security -> 보안 수준이 낮은 앱 허용
        self.server = "smtp.gmail.com"
        self.port = 465
        self.id =
        self.pw =
        self.setUi()
        self.setSlot()


    def setUi(self):
        self.txtAtt.setTreadOnly(True)


    def setSlot(self):
        self.bttAtt.clicked.connect(self.selectFile)
        self.btnReset.clicked.connect(self.reset)
        self.btnSend.clicked.connect(self.send)


    def selectFile(self):
        att = QFileDialog.getOpenFileName(self, "파일 선택")[0]
        if not att == '':
            self.txtAtt.setText(att)

    def reset(self):
        self.txtAtt.setText('')
        self.txtCont.setText('')
        self.txtTile.setText('')
        self.txtTo.setText('')

    def send(self):
        add = self.txtTo.text()
        title = self.txtTitle.text()
        cont = self.txtCont.toPlainText()
        att = False if self.txtAtt.text() == '' else self.txtAtt.text()
        msg = MIMEMultipart('mixed') if att else MIMEMultipart('alternative')
        msg['From'] = 'AAA'
        msg['To'] = add
        msg['subject'] = title
        msg.attach(MIMEText(cont))

        if att:
            file_data = MIMEBase('application', 'octet-stream')
            f = open(att, 'rb')
            file_contents = f.read()
            file_data.set_payload(file_contents)
            encoders.encode_base64(file_data)

            file_data.add_header('Content-Disposition', 'attachment', filename = os.path.basename(att))
            msg.attach(file_data)

        smtp = SMTP_SSL(self.server, self.port)
        smtp.login(self.id, self.pw)
        smtp.sendmail(self.id + "@gmail.com", add, msg.as_string())
        smtp.close()


app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())