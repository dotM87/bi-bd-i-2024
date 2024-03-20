from pymongo import MongoClient
from scrapy.exceptions import DropItem
from clasificados_scraper.items import ClasificadosItem

class MongoDBPipeline:
    collection_name = 'inmuebles'

    def open_spider(self, spider):
        # Conectar a MongoDB Atlas
        uri = "mongodb+srv://mbenjaminzr:51fS6hMejs8fInPx@m87-bi-bd.crrwcre.mongodb.net/?retryWrites=true&w=majority&appName=m87-bi-bd"
        self.client = MongoClient(uri)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, ClasificadosItem):
            # Obtener el siguiente índice disponible para el nuevo documento
            db = self.client['clasificados-los-tiempos']
            index = db[self.collection_name].count_documents({}) + 1
            item['id'] = index

            # Guardar el item en la colección 'inmuebles'
            db[self.collection_name].insert_one(dict(item))
            return item
        else:
            raise DropItem("Item no válido: %s" % item)

