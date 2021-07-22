import os
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from directions.point2 import AbsoluteProjectRoot
from ..items import *

chrome_options = Options()

chrome_options.add_argument("--headless")

##

class GetDailyData(scrapy.Spider):
    name = 'GetDailyData'
    start_urls = [
        'https://covid19.mohp.gov.np/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        DD_item = Raw_DailyData()
        x = 1
        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(0,3):
            temp_files = response.css('div.ant-card-body')[i]
            files = temp_files.css('p::text')
            value = files.extract()

            DD_item['indicator'] = value[1]
            DD_item['value'] = value[0]

            yield DD_item

###

class GetOverallData(scrapy.Spider):
    name = 'GetOverallData'
    start_urls = [
        'https://covid19.mohp.gov.np/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        OD_item = Raw_OverallData()
        x = 1
        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(3,7):
            temp_files = response.css('div.ant-card-body')[i]
            files = temp_files.css('p::text')
            value = files.extract()

            OD_item['value'] = value[0]
            OD_item['indicator'] = value[1]

            yield OD_item

##

class GetStatusData(scrapy.Spider):
    name = 'GetStatusData'
    start_urls = [
        'https://covid19.mohp.gov.np/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        SD_item = Raw_StatusData()
        x = 1
        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(7,10):
            temp_files = response.css('div.ant-card-body')[i]
            files = temp_files.css('span.ant-typography::text')
            value = files.extract()

            SD_item['value'] = value[0]
            SD_item['indicator'] = value[1]

            yield SD_item 


#######################################

class GetAllData(scrapy.Spider):
    name = 'GetAllData'
    start_urls = [
        'https://covid19.mohp.gov.np/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        DD_item = Raw_DailyData()
        OD_item = Raw_OverallData()
        SD_item = Raw_StatusData()
        x = 1
        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(0,3):
            temp_DailyDataFiles = response.css('div.ant-card-body')[i]
            DailyDataFiles = temp_DailyDataFiles.css('p::text')
            DailyDataValue = DailyDataFiles.extract()

            DD_item['indicator'] = DailyDataValue[1]
            DD_item['value'] = DailyDataValue[0]

            yield DD_item
        
        for i in range(3,7):
            temp_OverallFiles = response.css('div.ant-card-body')[i]
            OverallFiles = temp_OverallFiles.css('p::text')
            OverallValue = OverallFiles.extract()

            OD_item['indicator'] = OverallValue[1]
            OD_item['value'] = OverallValue[0]

            yield OD_item
        
        for i in range(7,10):
            temp_StatusFiles = response.css('div.ant-card-body')[i]
            Statusfiles = temp_StatusFiles.css('span.ant-typography::text')
            StatusValue = Statusfiles.extract()

            SD_item['indicator'] = StatusValue[1]
            SD_item['value'] = StatusValue[0]

            yield SD_item 
