import os
import scrapy
import w3lib.html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from directions.point2 import AbsoluteProjectRoot
from ..items import *

chrome_options = Options()

chrome_options.add_argument("--headless")

##

class GetWorldData(scrapy.Spider):
    name = 'GetWorldData'
    start_urls = [
        'https://www.worldometers.info/coronavirus/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        Wo_Data = Raw_WorldData()

        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(5,231):
            
            Country = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[2]/a/text()")
            TotalCases = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[3]")
            NewCases = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[4]")
            TotalDeaths = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[5]")
            NewDeaths = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[6]")
            TotalRecovery = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[7]")
            NewRecovery = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[8]")
            ActiveCases = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[9]")
            TotalTests = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[13]")
            Population = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[" + str(i) + "]/td[15]")

            Wo_Data['Country'] = w3lib.html.remove_tags(str(Country.extract_first()))
            Wo_Data['TotalCases'] = w3lib.html.remove_tags(TotalCases.extract_first())
            Wo_Data['NewCases'] = w3lib.html.remove_tags(NewCases.extract_first())
            Wo_Data['TotalDeaths'] = w3lib.html.remove_tags(TotalDeaths.extract_first())
            Wo_Data['NewDeaths'] = w3lib.html.remove_tags(NewDeaths.extract_first())
            Wo_Data['TotalRecovery'] = w3lib.html.remove_tags(TotalRecovery.extract_first())
            Wo_Data['NewRecovery'] = w3lib.html.remove_tags(NewRecovery.extract_first())
            Wo_Data['ActiveCases'] = w3lib.html.remove_tags(ActiveCases.extract_first())
            Wo_Data['TotalTests'] = w3lib.html.remove_tags(TotalTests.extract_first())
            Wo_Data['Population'] = w3lib.html.remove_tags(Population.extract_first())

            yield Wo_Data

class GetWorldDailyData(scrapy.Spider):
    name = 'GetWorldDailyData'
    start_urls = [
        'https://www.worldometers.info/coronavirus/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        WD_Data = Raw_WorldDailyData()

        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)
        
        NewCases = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[4]")
        TotalDeaths = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[5]")
        NewDeaths = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[6]")
        TotalRecovery = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[7]")
        NewRecovery = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[8]")
        ActiveCases = response.xpath("/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[9]")

        WD_Data['NewCases'] = w3lib.html.remove_tags(NewCases.extract_first())
        WD_Data['TotalDeaths'] = w3lib.html.remove_tags(TotalDeaths.extract_first())
        WD_Data['NewDeaths'] = w3lib.html.remove_tags(NewDeaths.extract_first())
        WD_Data['TotalRecovery'] = w3lib.html.remove_tags(TotalRecovery.extract_first())
        WD_Data['NewRecovery'] = w3lib.html.remove_tags(NewRecovery.extract_first())
        WD_Data['ActiveCases'] = w3lib.html.remove_tags(ActiveCases.extract_first())

        yield WD_Data