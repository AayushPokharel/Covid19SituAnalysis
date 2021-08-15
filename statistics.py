import sys
from matplotlib.backends.backend_qt5 import FigureCanvasQT
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from PySide2.QtWidgets import QApplication, QWidget
import csv
import pandas as pd
from datetime import datetime
from CustomTime import *
from dateutil.relativedelta import relativedelta

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        #plt.style.use('fivethirtyeight')

        infected = []
        recovered = []

        data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_cases'])
        data['date'] = pd.to_datetime(data['date']) 

        lastMnth = datetime.now()+relativedelta(months=-1)

        start_date = datetime.strftime(lastMnth,"%Y-%m-%d")
        end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

        #latestMonthData = data.loc([start_date:end_date])

        mask = (data['date'] > start_date) & (data['date'] <= end_date) 

        LatestMonthData = data.loc[mask]

        #currentMonthData = data[getMonth(data["date"]) > getCurrentMonth]
        
        Date = matplotlib.dates.date2num(LatestMonthData['date'].tolist())
        newCases = matplotlib.dates.date2num(LatestMonthData['new_cases'].tolist())
        plt.plot(Date, newCases, label = 'NewCases')

        # print(age)
        # print(infected)

        plt.title('Covid Cases latest Month')
        plt.xlabel('Date')
        plt.ylabel('New Cases')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues