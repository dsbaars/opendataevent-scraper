from ics import Calendar, Event
import time

class IcsExporter:
    def __init__(self, crawl_started_at, filename):
        self.c = Calendar()
        self.filename = filename

    def save(self, item):
        e = Event()
        e.name = item['title'][0].strip()
        e.begin = time.strftime('%Y%m%dT%H%M00Z', time.strptime(item['startDate'][0].strip() + ' ' + item['startTime'][0].strip(), "%d-%m-%Y %H:%M"))
        e.end = time.strftime('%Y%m%dT%H%M00Z',time.strptime(item['startDate'][0].strip() + ' ' + item['endTime'][0].strip(), "%d-%m-%Y %H:%M"))
        self.c.events.append(e)

    def close(self):
        with open(self.filename, 'w') as f:
            f.writelines(self.c)
