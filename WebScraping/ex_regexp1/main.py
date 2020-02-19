import openpyxl
import re

regex = re.compile(' [A-Za-z]+\.')

work_book = openpyxl.load_workbook('train.xlsx')

work_sheet = work_book.active

# for each_row in work_sheet.rows:
    # print(each_row[3].value)
    # print(regex.findall(each_row[3].value))

# pattern = re.compile('D.A')
# print(pattern.search("DAA"))

pattern = re.compile('D\.A')
print(pattern.search("DAA"))
print(pattern.search("D.A"))
print(type(pattern.search("D.A")))

string = "DDA D1A DDA DA"
print(re.sub('D.A', 'Dave', string))

work_book.close()
