# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    headline = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    imageUrl = scrapy.Field()
    cacheDateTime = scrapy.Field()
    hash = scrapy.Field()
