import requests
from bs4 import BeautifulSoup

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# site_list = ['https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000', 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000001']
#
# for site in site_list:
#     res = requests.get(site)
#     soup = BeautifulSoup(res.content, 'html.parser')
#
#     items = soup.select('#productListArea > ul > li > p > a')
#     print(site)
#     for item in items:
#         print(item.get_text())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


site_list = ['https://finance.naver.com/sise/']

for site in site_list:
    res = requests.get(site)
    soup = BeautifulSoup(res.content, 'html.parser')

    # items = soup.select('#popularItemList > li > a')
    # items = soup.select('div.rgt > ul.lst_major > li > a')
    items = soup.select('div.rgt > ul.lst_major > li')

    for item in items:
        print("지수이름:", item.find('a').get_text(), "현재지수:", item.find('span').get_text(), item.find('em').get_text())
