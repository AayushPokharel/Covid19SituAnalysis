import os
import csv
import wget
from directions import point2
import datetime
import pandas as pd

#####################

url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
file = os.path.join(point2.AbsoluteProjectRoot,"Resources","owid-covid-data.csv")
###########################

cleanup4Nepal_Keep = [
    "date",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_tests",
    "new_tests",
    "positive_rate",
    "tests_per_case",
    "total_vaccinations",
    "people_vaccinated",
    "people_fully_vaccinated",
]

cleanup4Continent_Keep = [
    "location",
    "date",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_tests",
    "new_tests",
    "positive_rate",
    "tests_per_case",
    "total_vaccinations",
    "people_vaccinated",
    "people_fully_vaccinated",
]
###########################


def FileUptoDate(a_fileName):
    file = os.path.join(point2.AbsoluteProjectRoot,"Resources",a_fileName)
    currentDate = datetime.date.today()
    fileDate = datetime.datetime.fromtimestamp(os.path.getctime(file)).date()

    if os.path.exists(file):
        if os.path.getsize(file) > 0:
            if fileDate == currentDate:
                print("File UptoDate")
                return True
    return False


def DownloadCommand():
    print("Downloading")
    wget.download(url, file)


def Download():
    if os.path.exists(file):
        print("File Exists")
        if FileUptoDate(file) == False:
            print("File Outdated")
            os.remove(file)
            DownloadCommand()
    else:
        print("File Doesn't Exists")
        DownloadCommand()


def cleanupRows(a_file,a_rows2keep):
    dataframe = pd.read_csv(a_file,usecols=a_rows2keep)
    dataframe.to_csv(a_file,index=False)


def FilterNepal():
    print("Opening Filter for Nepal")
    f = 0
    outfile = os.path.join(point2.AbsoluteProjectRoot,"Resources","CovidDataNepal.csv")
    with open(file,'r') as fin:
        with open(outfile,'w') as fout:
            writer = csv.writer(fout, delimiter=',')
            for row in csv.reader(fin, delimiter=','):
                if f == 0:
                    writer.writerow(row)
                    f = 1
                if row[2] == 'Nepal':
                    writer.writerow(row)

    cleanupRows(outfile,cleanup4Nepal_Keep)


def FilterSingleContinent(a_Continent):
    print("Opening Filter for "+ a_Continent)
    f = 0
    ofileName = "CovidData" + str(a_Continent) +".csv" 
    outfile = os.path.join(point2.AbsoluteProjectRoot,"Resources",ofileName)
    with open(file,'r') as fin:
        with open(outfile,'w') as fout:
            writer = csv.writer(fout, delimiter=',')
            for row in csv.reader(fin, delimiter=','):
                if f == 0:
                    writer.writerow(row)
                    f = 1
                if row[1] == a_Continent:
                    writer.writerow(row)

    cleanupRows(outfile,cleanup4Continent_Keep)


def FilterAllContinents():
    Continents = [
        "Asia",
        "Africa",
        "Europe",
        "North America",
        "South America",
        "Oceania"
    ]  
    for i in Continents:
        FilterSingleContinent(i)

def ScrapeKaggleData():
    Download()
    FilterNepal()
    FilterAllContinents()

##################################

##################################
if __name__ =='__main__':
    ScrapeKaggleData()