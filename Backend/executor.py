from scrapy import cmdline
from directions import point2
import sys

def done(a_spiderName,a_FileName):
    command = "scrapy crawl "
    spiderName = a_spiderName
    flag = " -o "
    #outputLocation = point2.AbsoluteProjectRoot
    outputLocation = ""
    outputName = a_FileName

    final = str(command) + str(spiderName) + str(flag) + str(outputLocation) + str(outputName)
    print(final)

    cmdline.execute(final.split())

if __name__ == "__main__":
    done(sys.argv[1],sys.argv[2])
    pass
