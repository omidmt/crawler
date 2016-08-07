# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from readability import Document
from utils import strip_tags
from scrapy.exceptions import DropItem
import pymongo
import hashlib


class ClearancePipeline(object):
    def process_item(self, article, spider):
        
        doc = Document(article['text'])
        article['text'] = strip_tags(doc.summary())
        article['hash'] = hashlib.sha256(article['url']).hexdigest()
        
        return article



class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['hash'] in self.ids_seen:
            raise DropItem("Duplicate url found: %s" % item)
        else:
            self.ids_seen.add(item['hash'])
            return item


class MongoPipeline(object):

    collection_name = 'article_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


