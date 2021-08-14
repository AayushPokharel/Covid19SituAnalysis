import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# from splashScreen import SplashScreen
from statistics import Canvas
from ui_functions import *
from infographics import Seriousness_of_Symptoms, Agewise_Risk_Analysis, Best_Household_Materials_For_a_Mask

# # SET AS GLOBAL WIDGETS
# # ///////////////////////////////////////////////////////////////
# widgets = None

## ==> SPLASH SCREEN
from ui_SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

from qt_material import *

## ==> GLOBALS
counter = 0


# MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ## SET MAIN BACKGROUND TO TRANSPARENT
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)


        ## STACKED PAGES NAVIGATION

        ## DEFAULT PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))


        ## LEFT MENU BUTTON CLICKED
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_nationalStatistics.clicked.connect(self.buttonClick)
        self.ui.btn_worldStatistics.clicked.connect(self.buttonClick)
        self.ui.btn_hospitals.clicked.connect(self.buttonClick)
        self.ui.btn_infographics.clicked.connect(self.buttonClick)
        ## EXIT WINDOW CLICKED
        self.ui.btn_exit.clicked.connect(lambda: UIFunctions.warningMessage(self))

        
        ## SET DEFAULT TAB
        # self.ui.tabWidget.setCurrentWidget(tabwidget.findChild(QWidget, self.ui.tableWidget_symptoms))





        ## ADD CLICK EVENT/MOUSE MOVE EVENT/DRAG EVENT TO THE TOP HEADER TO MOVE THE WINDOW
        # self.ui.leftBox.mouseMoveEvent = UIFunctions.moveWindow(self)


        ## LEFT MENU TOGGLE BUTTON
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.slideLeftMenu(self))

        ## SETTINGS BUTTON CLICKED
        self.ui.btn_Settings.clicked.connect(lambda: UIFunctions.slideExtraLeftBox(self))
        self.ui.extraCloseColumnBtn.clicked.connect(lambda: UIFunctions.slideExtraLeftBox(self))


        


        ##TABLE WIDGET CUSTOM SETTINGS
        # self.ui.tableWidget_symptoms.setColumnWidth(0, 175)
        # self.ui.tableWidget_symptoms.setColumnWidth(1, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(2, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(3, 120)
        # self.ui.tableWidget_symptoms.setColumnWidth(4, 120)
        UIFunctions.loadSymptoms(self)


        ######################################
        ############### GRAPH  ###############
        ##### IMPORTED FROM statistics.py ####
        ######################################

        ##AGE
        self.graph1 = Canvas(self)
        self.graph2 = Canvas(self)
        self.graph3 = Canvas(self)
        self.graph4 = Canvas(self)

        self.ui.graph1.addWidget(self.graph1)
        self.ui.graph2.addWidget(self.graph2)
        self.ui.graph3.addWidget(self.graph3)
        self.ui.graph4.addWidget(self.graph4)

        #GENDER
        self.graph1_2 = Canvas(self)
        self.graph2_2 = Canvas(self)
        self.graph3_2 = Canvas(self)
        self.graph4_2 = Canvas(self)

        self.ui.graph1_2.addWidget(self.graph1_2)
        self.ui.graph2_2.addWidget(self.graph2_2)
        self.ui.graph3_2.addWidget(self.graph3_2)
        self.ui.graph4_2.addWidget(self.graph4_2)

        
        #REGION
        self.graph1_3 = Canvas(self)
        self.graph2_3 = Canvas(self)
        self.graph3_3 = Canvas(self)
        self.graph4_3 = Canvas(self)

        self.ui.graph1_3.addWidget(self.graph1_3)
        self.ui.graph2_3.addWidget(self.graph2_3)
        self.ui.graph3_3.addWidget(self.graph3_3)
        self.ui.graph4_3.addWidget(self.graph4_3)


        ######################################
        ############### GRAPH  ###############
        ##### IMPORTED FROM infographics.py ####
        ######################################
        self.graph5 = Seriousness_of_Symptoms(self)
        self.ui.graph5.addWidget(self.graph5)


        self.graph6 = Agewise_Risk_Analysis(self)
        self.ui.graph6.addWidget(self.graph6)


        self.graph7 = Best_Household_Materials_For_a_Mask(self)
        self.ui.graph7.addWidget(self.graph7)



        ##DATE SELECTED
        self.ui.btn_select.clicked.connect(lambda: UIFunctions.getDate(self))



        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()


        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        ## NAVIGATE TO HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO NATIONAL STATISTICS PAGE
        if btnName == "btn_nationalStatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.national_Statistics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

         ## NAVIGATE TO WORLD STATISTICS PAGE
        if btnName == "btn_worldStatistics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.world_statistics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO HOSPITALS PAGE
        if btnName == "btn_hospitals":
            self.ui.stackedWidget.setCurrentWidget(self.ui.hospitals)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        ## NAVIGATE TO INFOGRAPHICS PAGE
        if btnName == "btn_infographics":
            self.ui.stackedWidget.setCurrentWidget(self.ui.infographics)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



    ## ADD MOUSE EVENTS TO THE WINDOW
    def mousePressEvent(self, event):
        ## GET THE CURRENT POSTITION OF THE MOUSE
        self.clickPosition = event.globalPos() 
        ## WE USE THIS VALUT TO MOVE THE WINDOW   







# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        # global widgets
        # widgets = self.ui
        

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>COVID-19</strong> Situation Analysis Application")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()
    sys.exit(app.exec_())