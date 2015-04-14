data.overheid.nl event-scraper
==============================

Mijn data-verzoek aan de open data-portal (data.overheid.nl):
> Kunnen de Evenementen ook als ICS (iCal)-feed worden aangeboden?

Werd helaas beantwoord met:
> Dank voor uw bericht. Het is niet mogelijk om de kalender via ICS-feed aan te bieden.

... nou dan maak ik 'm zelf wel

Hoe werkt dit?
--------------

1. Installer scrapy

Maak er een JSON van: `scrapy crawl data_overheid -o <output.json>`<br>
of uncomment `opendataevent.pipelines.OpenDataEventPipeline` in opendataevent/settings.py voor een simpele ICS-export.
