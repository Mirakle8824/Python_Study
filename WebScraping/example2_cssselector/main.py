import requests
from bs4 import BeautifulSoup

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



#
# res = requests.get('http://v.media.daum.net/v/20170615203441266')
# soup = BeautifulSoup(res.content, 'html.parser')
# items = soup.select('h3.tit_view')
# for item in items:
#     print(item.get_text())
#
# items1 = soup.find_all('h3', 'tit_view')
# for item in items1:
#     print(item.get_text())



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


res = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')
# items = soup.select('html head title')
# items = soup.select('html title')
# items = soup.select('html > title')  # >는 html 바로 밑에 태그를 의미하므로 중간에 여러 태그가 포함되어있어 아무것도 나타나지 않음
# items = soup.select('.tit_view') # 클래스를 표기하는 법은 .으로 표기
# items = soup.select('div#harmonyContainer') # 클래스를 표기하는 법은 .으로 표기  id 표기는 #으로
# items = soup.select('#harmonyContainer') # 클래스를 표기하는 법은 .으로 표기
items = soup.select('div#mArticle div#harmonyContainer') # 복합 사용 가능


for item in items:
    print(item.get_text())