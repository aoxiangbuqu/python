# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    title  = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    houseType = scrapy.Field()
    allPrice = scrapy.Field()
    avePrice = scrapy.Field()
    area = scrapy.Field()