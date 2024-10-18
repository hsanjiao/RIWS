import scrapy
from  MueiRiws.items import AcapellasItem

class AcapellasSpider(scrapy.Spider):
    name = "acapellas"
    #allowed_domains = []
    
    # Start url
    start_urls = ["https://www.looperman.com/acapellas"]

    # Parse method to extract acapellas
    def parse(self, response):
        a = 0
        item = None
        for div in response.xpath('//div[contains(@class,"player-wrapper") or contains(@class, "tag-wrapper") or contains(@class, "desc-wrapper")]'):
            if a == 200:
                return
            className = div.css('::attr(class)').get()
            if "player-wrapper" in className:
                item = AcapellasItem()
                item["title"] = div.css('a.player-title::text').get()
                item["date"] = div.css('div.ms-1 span::text').get()
                item["author"] = div.css('span.text-nowrap a::text').get()
                item["duration"] = div.css('div.player-buttons div.jp-timer span::attr(data-bs-title)').get()
            elif "tag-wrapper" in className:
                item["other_tags"] = []
                for tag in div.css('a'):
                    attr_dataBsTitle = tag.css('::attr(data-bs-title)').get()
                    if "Genre" in attr_dataBsTitle:
                        item["genre"] = tag.css('::text').get()
                    elif "Time Signature" in attr_dataBsTitle:
                        item["time_signature"] = tag.css('::text').get()
                    elif "is in the key of" in attr_dataBsTitle:
                        item["key"] = tag.css('::text').get() #extract only value remove 'Key : '
                    elif "bpm" in attr_dataBsTitle:
                        item["bpm"] = tag.css('::text').get()
                    elif "Male" in attr_dataBsTitle or "Female" in attr_dataBsTitle:
                        item["gender"] = tag.css('::text').get()
                    elif "File Size" in attr_dataBsTitle:
                        item["file_size"] = tag.css('::text').get()
                    elif "Commercial" in attr_dataBsTitle:
                        item["usage"] = tag.css('::text').get()
                    else:
                        item["other_tags"].append(tag.css('::text').get())
            elif "desc-wrapper" in className:
                item["description"] = " ".join(list(map(str.strip, div.css('::text').getall()))) 
                yield item       
            a+=1 
        
        next_page = response.css('li.page-item span.page-link a[rel*="next"]::attr(href)').get()
        next_page_url = response.urljoin(next_page)
        print(f"Following next unvisited page: {next_page_url}")
        yield scrapy.Request(next_page_url, callback=self.parse)

