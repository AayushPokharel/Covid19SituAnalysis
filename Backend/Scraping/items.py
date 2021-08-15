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

class Raw_RegionData(scrapy.Item):
    dateStart = scrapy.Field()
    dateEnd = scrapy.Field()
    region = scrapy.Field()
    Male = scrapy.Field()
    Female = scrapy.Field()

class Raw_HospitalData(scrapy.Item):
    HospitalName = scrapy.Field()
    Location = scrapy.Field()
    ContactNumber = scrapy.Field()
    TotalBeds = scrapy.Field()
    ICUBeds = scrapy.Field()
    Ventilators = scrapy.Field()
    IsolationBeds = scrapy.Field()

class Raw_WorldData(scrapy.Item):
    TotalCases = scrapy.Field()
    Country = scrapy.Field()
    TotalCases = scrapy.Field()
    NewCases = scrapy.Field()
    TotalDeaths = scrapy.Field()
    NewDeaths = scrapy.Field()
    TotalRecovery = scrapy.Field()
    NewRecovery = scrapy.Field()
    ActiveCases = scrapy.Field()
    TotalTests = scrapy.Field()
    Population = scrapy.Field()

class Raw_WorldDailyData(scrapy.Item):
    NewCases = scrapy.Field()
    TotalDeaths = scrapy.Field()
    NewDeaths = scrapy.Field()
    TotalRecovery = scrapy.Field()
    NewRecovery = scrapy.Field()
    ActiveCases = scrapy.Field()

class TestItem(scrapy.Item):
    value = scrapy.Field()