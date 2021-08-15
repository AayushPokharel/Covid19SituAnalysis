import os
from directions import point2
import sys
import shutil

def move(a_file):
    shutil.move(a_file, os.path.join(point2.AbsoluteProjectRoot,"Resources",a_file))


def Scrape(a_spiderName,a_FileName):
    command = "scrapy crawl "
    spiderName = a_spiderName
    flag = " -o "
    outputLocation = point2.AbsoluteProjectRoot
    outputName = a_FileName

    final = str(command) + str(spiderName) + str(flag) + str(outputName)
    print(final)

    os.system(final)
    move(a_FileName)

if __name__ == "__main__":
    Scrape(sys.argv[1],sys.argv[2])
    pass
