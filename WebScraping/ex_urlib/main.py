from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 사이트에서 인코딩이 데이터가 깨짐 (의도적으로 크롤링 막아둠)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.remove('Sheet')
excel_sheet = excel_file.creat_sheet('IT뉴스')

excel_sheet.column_dimensions['B'].width = 100
num = 0

res = urlopen('https://seeko.earlyadopter.co.kr/bbs/board.php?bo_table=mainnews')       # res에 String으로 들어옴
soup = BeautifulSoup(res, 'html.parser')

items = soup.find_all('a', 'item-subject')
excel_sheet.append(['번호', '제목'])

for item in items:
    data = item.get_text().replace('\t','').replace('\n','')
    print(data)
    excel_sheet.append([num, item.get_text()])
    num += 1

cell_A1 = excel_sheet['A1']
cell_A1.alignment = openpyxl.styles.Alignment(horizontal='center')
cell_B1 = excel_sheet['B1']
cell_B1.alignment = openpyxl.styles.Alignment(horizontal='center')

excel_file.save('test.xlsx')
excel_file.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



