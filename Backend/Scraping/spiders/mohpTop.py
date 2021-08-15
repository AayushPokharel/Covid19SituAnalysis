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

###################################################################################
#VVVVVV Yo partVVVVVV garna aayena
##############################################################################
class GetRegionalData(scrapy.Spider):
    name = 'GetRegionalData'
    start_urls = [
        'https://covid19.mohp.gov.np/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        testVal = driver.find_element(By.XPATH, RegionPtr)
        print("Here: "+testVal)
        return selenium_response_text

    def parse(self,response):
        R_item = Raw_RegionData()
        T_item = TestItem()
        #StartDateXpath = "/html/body/div[2]/div[4]/div[2]/div/div/div[1]/div/div/h4/text()[3]"
        #EndDateXpath = "/html/body/div[2]/div[4]/div[2]/div/div/div[1]/div/div/h4/text()[5]"
        
        for district in range(1,5):
            #RegionXpath = '/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[3]/span/b/text()'
            #RegionPath = "div.ant-card-grid ant-card-grid-hoverable"
            #DemographicsXpath = "/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[{}]".format(district)

            RegionPtr = response.css('div.ant-cardgrid ant-card-grid-hoverable')
            RegionDataValue = RegionPtr.css('span.b::text').extract()
            
            #MaleDataValue = response.xpath(DemographicsXpath + "/div[1]/text()[3]")
            #FemaleDataValue = response.xpath(DemographicsXpath + "/div[2]/text()[3]")

            #R_item['dateStart'] = response.xpath(StartDateXpath).extract()
            #R_item['dateEnd'] = response.xpath(EndDateXpath).extract()
            #R_item['region'] = RegionDataValue.extract()
            #R_item['male'] = MaleDataValue.extract()
            #R_item['female'] = FemaleDataValue.extract()

            
            #T_item['value'] = testVal

#######################################################

class MySpider(scrapy.Spider):

    name = 'Myspider'
    allowed_domains = ['.gov.np']
    start_urls = [
        'https://covid19.mohp.gov.np/'
    ]

    def parse(self, response):

        headers = {'Referer': 'https://covid19.mohp.gov.np/',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                   'Accept': 'application/json, text/plain, */*',
                   'Accept-Language': 'en-US,en;q=0.9',
                   'Accept-Encoding': 'gzip, deflate, br',
                   #'Content-Type': 'application/json; charset=utf-8',
                   #'X-Requested-With': 'XMLHttpRequest',
                   #'Content-Length': 246,
                   #'Connection': 'keep-alive',
                   }

        yield scrapy.Request(
            url='https://portal.edcd.gov.np/rest/api/fetch?filter=casesBetween&type=aggregate&sDate=2020-01-01&eDate=2021-08-14&disease=COVID-19',
            method='GET',
            headers=headers,
            callback=self.parse_ajax
        )

    def parse_ajax(self, response):
        yield {'data': response.text}