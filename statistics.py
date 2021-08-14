import sys
from matplotlib.backends.backend_qt5 import FigureCanvasQT
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from PySide2.QtWidgets import QApplication, QWidget
import csv
import pandas as pd

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5, 4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        plt.style.use('fivethirtyeight')

        age = []
        infected = []
        recovered = []

        data = pd.read_csv('Resources/ScrapedData/Agewise_Data.csv')
        
        age = data['Age'].tolist()
        infected = data['Infected'].tolist()
        plt.bar(age, infected, label = 'Infected')

        # print(age)
        # print(infected)

        plt.title('Covid Cases by Age')
        plt.xlabel('Age')
        plt.ylabel('Total Cases')

        plt.legend()
        plt.grid(True)

        plt.tight_layout() # works for small screen; solves padding issues