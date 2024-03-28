import scrapy

class ClasificadosItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    request_date = scrapy.Field()
