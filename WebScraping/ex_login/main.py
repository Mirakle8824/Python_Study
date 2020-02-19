import requests
from bs4 import BeautifulSoup

login_url = 'https://www.hanbit.co.kr/member/login_proc.php'
crawl_url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'

session = requests.session()

params = dict()
params['m_id'] = 'nargo8824'
params['m_passwd'] = 'skrmsp12'

res = session.post(login_url, data=params)
res.raise_for_status()          # 200 안될시 fail

print(res.headers)              # set_Cookie 서버로 부터 넘어온 세션
print(session.cookies.get_dict())

res = session.get(crawl_url)        # session이 ID, PW를 대체함, 특정 사이트를 크롤링

soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('dl.mileage_section1 > dd > span')

for item in data:
    print(item.get_text())