# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenDataEventItem(scrapy.Item):
    title = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    startTime = scrapy.Field()
    endTime = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    moreInfoLink = scrapy.Field()
    pass
