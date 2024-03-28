import sys
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from .items import ClasificadosItem

class MongoDBPipeline:
    collection_name = 'inmuebles'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        if not self.mongo_uri: sys.exit("No se ha especificado la URI de MongoDB")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(ClasificadosItem(item))
        self.db[self.collection_name].insert_one(data)
        return item
