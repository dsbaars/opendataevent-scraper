import scrapy
from opendataevent.items import OpenDataEventItem

class DataOverheidSpider(scrapy.Spider):
    name = "data_overheid"
    allowed_domains = ["data.overheid.nl"]
    start_urls = [
        "https://data.overheid.nl/contact/events/alle-evenementen"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[contains(@class, "views-row")]'):
            e = OpenDataEventItem()
            e['title'] = sel.xpath('div/span/a/text()').extract()
            e['startDate'] = sel.xpath('div/span/span[@class="date-display-single"]/text()').re("(\d{2}\-\d{2}\-\d{4})")
            e['startTime'] = sel.xpath('div/span/span[@class="date-display-single"]/span[@class="date-display-start"]/text()').extract()
            e['endTime'] = sel.xpath('div/span/span[@class="date-display-single"]/span[@class="date-display-end"]/text()').extract()
            e['link'] = 'https://data.overheid.nl' + sel.xpath('div/span/a/@href').extract()[0]
            yield e
