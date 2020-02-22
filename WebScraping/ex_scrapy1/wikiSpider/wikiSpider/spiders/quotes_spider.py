import scrapy
import re
# from wikiSpider.wikiSpider.items import WikispiderItem
from ..items import WikispiderItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['corners.gmarket.co.kr']
    start_urls = ['https://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        # print(response.url)
        # print(response.css('head > title').get())
        # print(response.css('head > title::text').get())
        # print(response.css('div.best-list li a::text').getall())
        # print(response.css('div.best-list li a::text')[1].get())
        # print(response.css('div.best-list li a::text')[1].re('(\w+)'))
        titles = response.css('div.best-list li a::text').getall()
        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()

        for num, title in enumerate(titles):
            doc = WikispiderItem()
            doc['title'] = title
            doc['price'] = prices[num]
            yield doc
            print(title)