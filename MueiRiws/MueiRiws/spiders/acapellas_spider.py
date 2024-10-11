import scrapy
from  MueiRiws.items import AcapellasItem

class AcapellasSpider(scrapy.Spider):
    name = "acapellas"

    # Start url
    start_urls = ["https://www.looperman.com/acapellas"]

    # Parse method to extract acapellas
    def parse(self, response):
        n = 0
        for acapella in response.css('div.player-wrapper'):
            if n == 200:
                return
            
            item = AcapellasItem()
            item["title"] = acapella.css('a.player-title::text').get()
            item["date"] = acapella.css('div.ms-1 span::text').get()
            item["author"] = acapella.css('span.text-nowrap a::text').get()
            n+=1
            
            yield item

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
