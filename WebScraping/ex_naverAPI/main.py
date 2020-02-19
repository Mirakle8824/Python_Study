import json
import requests
import pprint
import openpyxl

client_id = 'mFl820NR7x7Dr6t2vq5V'
client_secret = 'hK19p06onM'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=갤럭시'
# header_params = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
# res = requests.get(naver_open_api, headers=header_params) ## 서버로 Head 정보 전달
#
# if(res.status_code == 200):
#     data = res.json()
#     # pprint.pprint(data[items])
#     for index, item in enumerate(data['items']):
#         print(index + 1, item['title'], item['link'])
# else:
#     print("Error Code:", res.status_code)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_Sheet = excel_file.active
excel_Sheet.column_dimensions['B'].width = 100
excel_Sheet.column_dimensions['C'].width = 100
excel_Sheet.append(['랭킹', '제목', '링크'])


for index in range(10):
    start_number = start + (index * 100)
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + str(start_number)

    header_params = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    res = requests.get(naver_open_api, headers=header_params) ## 서버로 Head 정보 전달

    if res.status_code == 200:
        data = res.json()
        # pprint.pprint(data[items])
        for item in data['items']:
            num += 1
            excel_Sheet.append([num, item['title'], item['link']])


    else:
        print("Error Code:", res.status_code)

excel_file.save('shopping_with_xiaomi.xlsx')
excel_file.close()