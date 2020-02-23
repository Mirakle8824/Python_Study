# -*- coding: utf-8 -*-
import scrapy
from quotes.items import QuotesItem


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list > ul > li > a::text').getall()
        prices = response.css('div.best-list > ul > li > div.item_price > div.s-price > strong > span > span::text').getall()



        for num, title in enumerate(titles):
            doc = QuotesItem()
            doc['price'] = prices[num].strip().replace("원", "").replace(",", "")
            doc['title'] = title
            yield doc

