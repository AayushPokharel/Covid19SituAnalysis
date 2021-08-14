import sys
from matplotlib.backends.backend_qt5 import FigureCanvasQT
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from PySide2.QtWidgets import QApplication, QWidget
import csv
import pandas as pd

class Seriousness_of_Symptoms(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        plt.style.use('fivethirtyeight')

        with open('Resources/Seriousness_of_Symptoms.csv', newline='') as csvfile: #purpose of newline?; works without it also
            data = csv.DictReader(csvfile)

            for row in data:
                mild = row['MILD']
                severe = row['SEVERE']
                critical = row['CRITICAL']

        slices = [mild, severe, critical]
        index = ['MILD', 'SEVERE', 'CRITICAL']
        slice_colors = ['#6d904f', '#e5ae37', '#fc4f30']

        plt.pie(slices, labels = index, colors = slice_colors, wedgeprops = {'edgecolor':  'black'}, shadow = True, autopct = '%1.1f%%')
        plt.title('Seriousness of Symptoms\nThe Majority of Infections are Mild')

        # plt.legend(loc = (-0.4, -0.2))

        plt.tight_layout() # works for small screen; solves padding issues




class Agewise_Risk_Analysis(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        plt.style.use('fivethirtyeight')

        age = []
        italy = []
        uk = []

        bar_width = 0.33

        data = pd.read_csv('Resources/Agewise_Risk_Analysis.csv')

        age = data['Age'].tolist()
        italy = data['Italy'].tolist()
        uk = data['UK'].tolist()

        x_indexes = np.arange(len(age))

        plt.bar(x_indexes - bar_width, italy, width = bar_width, label = 'Italy')
        plt.bar(x_indexes + bar_width, uk, width = bar_width, label = 'UK')

        plt.xticks(ticks = x_indexes, labels = age) #fixes x-axis label issue

        plt.title('% of deceased')
        plt.xlabel('Age')
        plt.ylabel('')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues




class Best_Household_Materials_For_a_Mask(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        plt.style.use('fivethirtyeight')

        household_materials = []
        percent_microns_captured = []
        
        data = pd.read_csv('Resources/Best_Household_Materials_for_a_Mask.csv')

        household_materials = data['Household Materials'].tolist()
        percent_microns_captured = data['Percent of 0.02-microns captured'].tolist()

        plt.barh(household_materials, percent_microns_captured)


        plt.title('Best Household Materials for a Mask')
        plt.xlabel('Household Materials')
        plt.ylabel('Percent of 0.02-microns captured when coughing')

        # plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues