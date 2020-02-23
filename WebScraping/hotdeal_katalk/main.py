import requests
from bs4 import BeautifulSoup
import time
import json

KAKAO_TOKEN = "e5YSYjr69Pj6aIUlcAl8OqAURAQ8cCu3utL7Awo9c04AAAFwcTtZRg"

# 텍스트 템플릿 보내기 참고
def send_to_kakao():
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": "Data from Python project",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def search_slickdeals(keyword):
    keyword = "apple ipad"
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&searcharea=deals&searchin=first".format(keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.content, "lxml")
    divs = bs.select("div.resultRow")

    for d in divs:
        images = d.select("img.lazyimg")
        alink = d.select("a.dealTitle")[0]
        href = "https://slickdeals.net" + alink.get("href")
        title = alink.text
        price = d.select("span.price")[0].text.replace("$", "").replace("Free", "0")
        fire = len(d.select("span.icon-fire"))

if __name__ == "__main__":
    condition = {
        "keyword": "apple ipad",
        "min_price": 100,
        "max_price": 250,
    }
    search_slickdeals("apple ipad")

    while True:
        send_to_kakao()
        time.sleep(10)
