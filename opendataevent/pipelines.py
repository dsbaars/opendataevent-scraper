# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from exporter import IcsExporter
from datetime import datetime
import pytz

class OpenDataEventPipeline(object):
    def __init__(self):
        self.scrape_started = datetime.utcnow().replace(tzinfo=pytz.utc)\
            .strftime('%Y-%m-%dT%H:%M:%SZ')
        self.items = []
        self.universal_items = {}

    def open_spider(self,spider):
        pass

    def process_item(self, item, spider):
        item_id = item['title']
        self.items.append(item)
        return item

    def close_spider(self, spider):
        exporter = IcsExporter(self.scrape_started, "test.ics")

        for item in self.items:
            exporter.save(item)
        exporter.close()
