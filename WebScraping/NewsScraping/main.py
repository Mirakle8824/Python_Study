import sys, requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QUrl as gd
from bs4 import BeautifulSoup as bs, element

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.qf = QFrame(self)
        self.btn1 = QPushButton('모바일', self)
        self.btn2 = QPushButton('컴퓨터', self)
        self.btn3 = QPushButton('게임/리뷰', self)
        self.dte = QDateEdit(QDate.currentDate(), self)
        self.lv = QListView(self.qf)
        self.model = QStandardItemModel()
        self.subTitle = QLabel(self)
        self.subCont = QPlainTextEdit(self)
        self.lst = []
        self.category = {'모바일': 731, '컴퓨터': 283, '게임/리뷰': 229}
        self.curCat = ''
        self.setUi()
        self.setSlot()


    def setUi(self):
        self.setGeometry(300, 300, 400, 500)
        self.qf.setGeometry(0, 30, 600, 500)
        self.lv.setGeometry(0, 0, 600, 500)
        self.lv.setMode(self.model)
        self.btn1.move(0, 0)
        self.btn2.move(80, 0)
        self.btn3.move(160, 0)
        self.dte.move(510, 5)
        self.subTitle.move(610, 15)
        self.subTitle.setFixedsize(590, 50)
        self.subTitle.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.subCont.move(610, 50)
        self.subCOnt.setFixedSize(590, 480)
        self.subCOnt.SetSytleSheet("font-size: 13px;")

    def setSlot(self):
        self.lv.doubleClicked.connect(self.visit)
        self.btn1.clicked.connect(self.catSel)
        self.btn2.clicked.connect(self.catSel)
        self.btn3.clicked.connect(self.catSel)

    def visit(self):
        qd.openUrl(QUrl(self.lst[self.lv.currentIndex().row())[0])


    def catSel(self):
        self.curCat = self.sender().text()
        self.urlSet()

    def artSel(self):
        self.subTitle.setText(self.lv.currentIndex().data())
        url = self.lst[self.lv.currentIndex().row()][0]
        html = bs(requests.get(url).content, "html.parser", from_encoding="utf-8")
        tag = html.select("#articleBodyContents")
        joinTxt = ''

        for a in range(9, len(tag[0].contents)-2):
            if isinstance(tag[0].contents[a], element.NavigableString):
                joinTxt += str(tag[0].contents[a])+ '\n\n'

        joinTxt.replay('&apos', "'")
        self.subCOnt.setPlainText(joinTxt)

    def urlSet(self):
        page = 1
        date = self.dte.text().replace('-', '')
        self.lst.clear()
       # "https://news.naver.com/main/list.nhn?mode=LS2D&mid=sec&sid2={0}&sid1=105&date={1}&page={2}"
        baseUrl = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2={0}&sid1=105&mid=shm&date={1}&page={2}"
        url = baseUrl.format(self.category[self.category[self.curCat], date, page])
        html = bs(requests.get(url).content, "html.parser", from_encoding = "utf-8")
        page = len(html.select("#main_content > div.paging > a")) + 1
        for i in range(1, page+1):
            url = baseUrl.format(self.category[self.curCat], date, i)
            html = bs(requests.get(url).content, "html.parser", from_encoding="utf-8")
            tag = html.select("#main_content > div > ul > li")

            for s in tag:
                li = s.find_all('a')
                self.lst.append([])
                self.lst[-1].append(li[0].attrs['href'])
                if len(li) == 2:
                    self.lst[-1].append(li[1].string.strip().replace('&apos', "'"))
                else:
                    self.lst[-1].append(li[0].string.strip().replace('&apos', "'"))

        self.model.clear()
        for s in self.lst:
            self.model.appendRow(QStandardItem(s[1])


app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())