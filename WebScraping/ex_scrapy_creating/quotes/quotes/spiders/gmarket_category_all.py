# -*- coding: utf-8 -*-
import scrapy
import time


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse)
        # yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers111', callback=self.parse2)

    def parse(self, response):
        category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()
        # best_100s = response.css('div.best-list ul li a::text').getall()
        #
        # print(category_links, category_names, best_100s)

        for index, category_link in enumerate(category_links):
            # print('http://corners.gmarket.co.kr' + category_link, category_names[index])
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_maincategory,
                                 meta={'maincategory_name': category_names[index]})
        #     time.sleep(2)

        # yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01', callback=self.parse_maincategory)

    def parse_maincategory(self, response):
        # print("parse_maincategory", response.meta['maincategory_name'])

        best_items = response.css('div.best-list ul')
        print(best_items.css('li a.itemname::text').get)

        # title = best_items.css('a.itemname::text').getall()
        # ori_price = best_items.css('div.o-price span span::text').getall()
        # dis_price = best_items.css('div.s-price strong span span::text').getall()
        # discount_percent = best_items.css('div.s-price em::text').getall()
        # print(title, ori_price, dis_price, discount_percent)


        # for index, item in enumerate(best_items.css('li')):
        #     title = item.css('a.itemname::text').get()
        #     ori_price = item.css('div.o-price span span::text').get()
        #     dis_price = item.css('div.s-price strong span span::text').get()
        #     discount_percent = item.css('div.s-price em::text').get()
        # print(title, ori_price, dis_price, discount_percent)

    # def parse2(self, response):
    #     pass
