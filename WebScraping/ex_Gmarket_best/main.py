import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01')
soup = BeautifulSoup(res.content, 'html.parser')
titles = soup.select('div.best-list li a.itemname')

# 해당 권한을 파일로 가져옴
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Crawling-b221df05298a.json', scope)
client = gspread.authorize(creds)

worksheet = client.open('Report1').get_worksheet(0)

# telemedicine = sheet.get_all_records()
# print(telemedicine)
#
# row = ["I'm", "inserting", "a", "new", "row", "into", "a", "Spreadsheet", "using", "Python"]
# index = 3
# sheet.insert_row(row, index)

for index, title in enumerate(titles):
    if len(title.get_text()) > 0:
        # print(title.get_text(), title['href'])
        res_sub = requests.get(title['href'])
        soup_sub = BeautifulSoup(res_sub.content, 'html.parser')
        contact_name = soup_sub.select_one('#vip-tab_detail > div.vip-detailarea_productinfo.box__product-notice.js-toggle-content > div.box__product-notice-list > table:nth-child(1) > tbody > tr:nth-child(4) > td')
        worksheet.insert_row([title.get_text(), title['href'], contact_name.get_text()], index+1)

