import os
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from directions.point2 import AbsoluteProjectRoot
from ..items import *




class GetHospitalDatav2(scrapy.Spider):
    name = "GetHospitalDatav2"
# Using a dummy website to start scrapy request
    def start_requests(self):
        url = "https://covidnepal.org/"
        yield scrapy.Request(url=url, callback=self.parse_countries)


    def parse_countries(self, response):
        HR_Data = Raw_HospitalData()

        driver = webdriver.Chrome(executable_path= os.path.join(AbsoluteProjectRoot,"Driver","chromedriver.exe"))


        driver.get("https://covidnepal.org/")
        wait = WebDriverWait(driver, 5)

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

        driver.quit()