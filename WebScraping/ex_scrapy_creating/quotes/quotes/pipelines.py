# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class QuotesPipeline(object):
    def process_item(self, item, spider):
        print(item)
        if int(item['price']) > 10000:
            return item
        else:
            raise DropItem("drop item having lower price than 10,000")
