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

class GetHospitalData(scrapy.Spider):
    name = 'GetHospitalData'
    start_urls = [
        'https://covidnepal.org/',

    ]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"), options=chrome_options)


    @staticmethod
    def get_selenium_response(driver,url):
        driver.get(url)
        selenium_response_text = driver.page_source.encode('utf-8')
        return selenium_response_text

    def parse(self,response):
        HR_Data = Raw_HospitalData()

        newSelector = self.get_selenium_response(self.driver, response.url)
        response = scrapy.Selector(text= newSelector)

        for i in range(1,11):
            HospitalNameXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[1]/div[1]/text()"
            HospitalAddressXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[1]/div[2]/span/text()"
            HospitalContactXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[3]/a/text()[1]"
            TotalBedXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[5]/text()"
            ICUBedXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[6]/text()"
            VentilatorsXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[7]/text()"
            IsolationBedXpath = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[8]/text()"
            
            HospitalRecord = response.xpath(HospitalNameXpath).extract_first()
            HospitalAddress = response.xpath(HospitalAddressXpath).extract_first()
            HospitalContact = response.xpath(HospitalContactXpath).extract_first()
            TotalBed = response.xpath(TotalBedXpath).extract_first()
            ICUBed = response.xpath(ICUBedXpath).extract_first()
            Ventilators = response.xpath(VentilatorsXpath).extract_first()
            IsolationBed = response.xpath(IsolationBedXpath).extract_first()

            HR_Data['HospitalName'] = HospitalRecord
            HR_Data['Location'] = HospitalAddress
            HR_Data['ContactNumber'] = HospitalContact
            HR_Data['TotalBeds'] = TotalBed
            HR_Data['ICUBeds'] = ICUBed
            HR_Data['Ventilators'] = Ventilators
            HR_Data['IsolationBeds'] = IsolationBed

            yield HR_Data

        