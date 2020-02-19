import json

data = """
{
    "lastBuildDate": "Wed, 12 Feb 2020 15:36:00 +0900",
    "total": 683517,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "파인디지털 파인드라이브 Q300",
            "link": "https://search.shopping.naver.com/gate.nhn?id=19490416717",
            "image": "https://shopping-phinf.pstatic.net/main_1949041/19490416717.20191231183104.jpg",
            "lprice": "229000",
            "hprice": "328400",
            "mallName": "네이버",
            "productId": "19490416717",
            "productType": "1"
        },
        {
            "title": "파인디지털 파인드라이브 Q30",
            "link": "https://search.shopping.naver.com/gate.nhn?id=18711239261",
            "image": "https://shopping-phinf.pstatic.net/main_1871123/18711239261.20190415105108.jpg",
            "lprice": "209000",
            "hprice": "294320",
            "mallName": "네이버",
            "productId": "18711239261",
            "productType": "1"
        },
        {
            "title": "범용 <b>안드로이드</b> 올인원 매립 네비게이션 PX6 익스트림 에디션 유니버셜 7인치 / 10인치",
            "link": "https://search.shopping.naver.com/gate.nhn?id=82113730741",
            "image": "https://shopping-phinf.pstatic.net/main_8211373/82113730741.jpg",
            "lprice": "399000",
            "hprice": "0",
            "mallName": "모터스밸류",
            "productId": "82113730741",
            "productType": "2"
        },
        {
            "title": "팅크웨어 아이나비 LS700",
            "link": "https://search.shopping.naver.com/gate.nhn?id=21722358232",
            "image": "https://shopping-phinf.pstatic.net/main_2172235/21722358232.20200109155648.jpg",
            "lprice": "209000",
            "hprice": "239000",
            "mallName": "네이버",
            "productId": "21722358232",
            "productType": "1"
        },
        {
            "title": "파인디지털 파인드라이브 T",
            "link": "https://search.shopping.naver.com/gate.nhn?id=19551877065",
            "image": "https://shopping-phinf.pstatic.net/main_1955187/19551877065.20191011170126.jpg",
            "lprice": "179000",
            "hprice": "319000",
            "mallName": "네이버",
            "productId": "19551877065",
            "productType": "1"
        },
        {
            "title": "파인디지털 파인드라이브 Q100 Black",
            "link": "https://search.shopping.naver.com/gate.nhn?id=13854813056",
            "image": "https://shopping-phinf.pstatic.net/main_1385481/13854813056.20180326121103.jpg",
            "lprice": "226590",
            "hprice": "534000",
            "mallName": "네이버",
            "productId": "13854813056",
            "productType": "1"
        },
        {
            "title": "파인디지털 파인드라이브 AI",
            "link": "https://search.shopping.naver.com/gate.nhn?id=19895890826",
            "image": "https://shopping-phinf.pstatic.net/main_1989589/19895890826.20200120144426.jpg",
            "lprice": "189000",
            "hprice": "234000",
            "mallName": "네이버",
            "productId": "19895890826",
            "productType": "1"
        },
        {
            "title": "[PX6 / 4+32GB] 세계 최초 FHD 1080P 12인치 범용 유니버설 <b>안드로이드</b> 올인원",
            "link": "https://search.shopping.naver.com/gate.nhn?id=82061276586",
            "image": "https://shopping-phinf.pstatic.net/main_8206127/82061276586.1.jpg",
            "lprice": "539000",
            "hprice": "0",
            "mallName": "클라이드코리아",
            "productId": "82061276586",
            "productType": "2"
        },
        {
            "title": "<b>안드로이드</b>OS 내비게이션!! E-ACE E03 Car GPS Na",
            "link": "https://search.shopping.naver.com/gate.nhn?id=20825652490",
            "image": "https://shopping-phinf.pstatic.net/main_2082565/20825652490.jpg",
            "lprice": "173630",
            "hprice": "0",
            "mallName": "인터파크",
            "productId": "20825652490",
            "productType": "2"
        },
        {
            "title": "팅크웨어 아이나비 M500",
            "link": "https://search.shopping.naver.com/gate.nhn?id=15140462505",
            "image": "https://shopping-phinf.pstatic.net/main_1514046/15140462505.20191231194102.jpg",
            "lprice": "256990",
            "hprice": "500000",
            "mallName": "네이버",
            "productId": "15140462505",
            "productType": "1"
        }
    ]
}
"""

json_data = json.loads(data)
print(json_data)
