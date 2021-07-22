# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Raw_DailyData(scrapy.Item):
    indicator = scrapy.Field()
    value = scrapy.Field()

class Raw_OverallData(scrapy.Item):
    indicator = scrapy.Field()
    value = scrapy.Field()

class Raw_StatusData(scrapy.Item):
    indicator = scrapy.Field()
    value = scrapy.Field()