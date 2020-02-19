from openpyxl import *

filename = "C:\\Users\\82109\\Desktop\\Project\\Python_Study\\PyQt5\\openpyxl1\\a.xlsx"
book = load_workbook(filename)

# 새로운 시트 new_sheet 생성하기
sheet = book.create_sheet('new_sheet')

# 시트 Sheet2를 작업 대상으로 지정하기
sheet1 = book['Sheet1']
sheet2 = book['Sheet2']
sheet3 = book['Sheet3']

# 활성된 워크북의 시트를 선택하기
# sheet = book.active

# A1 셀에 문자열 쓰기
sheet2['A1'] = 'Python input test'
sheet3['A1'] = 'aaaaaa'

data = sheet1['A']
print(sheet1)
print(type(sheet1))
print(data)
print(type(data))
print(data[1].value)
print(data[2].value)
# 행 단위로 쓰기
sheet2.append(['A1 value', 'B1 value', 'C1 value'])
sheet3.merge_cells('A1:E3')
sheet3.

# 엑셀 파일로 저장
book.save('C:\\Users\\82109\\Desktop\\Project\\Python_Study\\PyQt5\\openpyxl1\\b.xlsx')

# # # 다른 시트의 값을 새로운 시트로 옮기기
# for row in old_sheet.iter_row():  # 한 행씩 데이터를 가져옴
#     row_data = []  # 행 값은 리스트 자료형을 사용
#     for cell in row:
#         row_data.append(cell.value)  # 각 열의 값을 리스트로 만듬
#     new_sheet.append(row_data)  # 완성된 리스트 값을 새로운 시트에 씀

#
# # A1 셀의 값
# val = xl_sheet['A1'].value
#
# # 1개 행을 가져와 각 열의 값 출력
# row = xl_sheet['1']  # 첫 번째 행 전체를 가져옴
# for cell in row:  # 각 열에 대해서
#     print(cell.value)
#
# # 1개 열을 가져와 각 행의 값 출력
# col = xl_sheet['A']  # 첫 번째 열 전체를 가져옴
# for cell in col:  # 각 행에 대해서
#     print(cell.value)
#
# # 여러 행의 데이터 출력
# rows = xl_sheet['1:2']  # 1~2행을 가져옴
# for row in rows  # 각 행에 대해서
#     for cell in row:  # 행의 각 셀에 대해서
#         print(cell.value)
#
# # 특정 영역의 데이터 출력
# rows = xl_sheet['A1:B2']  # 1~2행을 가져옴
# for row in rows  # 각 행에 대해서
#     for cell in row:  # 행의 각 셀에 대해서
#         print(cell.value)  # A1, B1, A2, B2 셀 값을 처리