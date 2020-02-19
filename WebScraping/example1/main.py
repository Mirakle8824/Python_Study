import requests
from bs4 import BeautifulSoup

# res = requests.get('http://v.media.daum.net/v/20170615203441266')
# # res.content
#
# soup = BeautifulSoup(res.content, 'html.parser')
# mydata = soup.find('title')
# print(mydata.get_text())


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#
# html = "<html> \
# <body> \
# <h1 id='title'> [1] 크롤링이란?</h1>\
# <p class=cssstyle'> 웹페이지에서 필요한 데이터를 추출하는 것</p> \
# <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> \
# </body> \
# </html>"
#
# soup = BeautifulSoup(html, "html.parser")
# data = soup.find('p')
#
# # data = soup.find('p', class_='cssstyle')
# # data = soup.find('p', 'cssstyle')
# # data = soup.find('p', attrs = {'id': 'body', 'align': 'center'})
# # data = soup.find(id='body')
#
# data = soup.find_all('p')
# for item in data:
#     print(item.string)
#
# # print(data.string)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# res = requests.get('http://v.media.daum.net/v/20170615203441266')
#
# soup = BeautifulSoup(res.content, 'html.parser')
# # mydata = soup.find('h3', 'tit_view')
#
#
# # mydata = soup.find_all('span', 'txt_info')
# # for item in mydata:
# #     print(item.string)
#
# mydata = soup.find('div', 'layer_util layer_summary')
# print(mydata.get_text())


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# res = requests.get('https://www.daum.net/')
#
# soup = BeautifulSoup(res.content, 'html.parser')
#
# mydata = soup.find_all('a', attrs={'class':'link_issue', 'tabindex':'-1'})
# for item in mydata:
#     print(item.string)



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# res = requests.get('https://www.nvaer.com/')
# soup = BeautifulSoup(res.content, 'html.parser')
# 
# mydata = soup.find('div', 'ah_roll_area PM_CL_realtimeKeyword_rolling')
# items = mydata.find_all('li', 'ah_item')
# for item in items:
#     data = item.get_text().split('\n')
#     print(data[2] + '위:', data[3])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -