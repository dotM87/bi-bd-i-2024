import scrapy
from datetime import datetime
from clasificados_scraper.items import ClasificadosItem

class ClasificadosSpider(scrapy.Spider):
    name = 'clasificados_spider'
    allowed_domains = ['clasificados.lostiempos.com']
    start_urls = ['https://clasificados.lostiempos.com/inmuebles']

    def parse(self, response):
        # Extraer los datos de los anuncios

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for ad in response.css('div.views-row'):
            item = ClasificadosItem()
            item['title'] = ad.css('div.title a::text').get()
            item['date'] = ad.css('div.publish-date span.field-content::text').get()
            item['description'] = ad.css('div.body span.field-content::text').get()
            item['location'] = ad.css('div.description span.field-content::text').get()
            item ['request_date'] = current_date
            yield item

        # Seguir a la siguiente página si existe
        next_page = response.css('li.pager-next a::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
