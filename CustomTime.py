from datetime import datetime

def getCurrentYear():
    today = datetime.today()
    datem = today.year
    return datem

def getCurrentMonth():
    today = datetime.today()
    datem = today.month
    return datem

def getCurrentDay():
    today = datetime.today()
    datem = today.day
    return datem

def getYear(a_Val):
    Mnth = datetime.strptime(a_Val,"%Y-%m-%d")
    datem = Mnth.year
    return datem

def getMonth(a_Val):
    Mnth = datetime.strptime(a_Val,"%Y-%m-%d")
    datem = Mnth.month
    return datem

def getDay(a_Val):
    Mnth = datetime.strptime(a_Val,"%Y-%m-%d")
    datem = Mnth.day
    return datem

if __name__ == '__main__':
    pass