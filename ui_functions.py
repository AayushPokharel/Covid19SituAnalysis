from main import *
import pandas as pd


symptoms = []
covid_19 = []
common_cold = []
flu = []
allergies = []


class UIFunctions(MainWindow):
    ## UPDATE RESTORE BUTTON ICON ON MAXIMIZINGOR MINIMIZING WINDOW
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            ## CHANGE ICON
            self.ui.maximizeRestoreAppBtn.setIcon(QtGui.QIcon(u":/icons/images/icons/icon_maximize.png"))
        else:
            self.showMaximized()
            ## CHANGE ICON
            self.ui.maximizeRestoreAppBtn.setIcon(QtGui.QIcon(u":/icons/images/icons/icon_restore.png"))


    ## EXPAND AND RESTORE LEFT MENU
    def slideLeftMenu(self):
        ## GET CURRENT LEFT MENU WIDTH
        width = self.ui.leftMenuBg.width()

        ## IF MINIMIZED
        if width == 60:
            newWidth = 240  ## EXPAND MENU      
        else: ## IF MAXIMIZED
            newWidth = 60  ## RESTORE MENU

        ## ANIMATE THE TRANSITION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth") ## ANIMATE MINIMUM WIDTH
        self.animation.setDuration(500)
        self.animation.setStartValue(width) ## START VALUE IS THE CURRENT MENU WIDTH
        self.animation.setEndValue(newWidth) ## END VALUE IS THE NEW MENU WIDTH
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    ## EXPAND AND RESTORE EXTRA LEFT BOX
    def slideExtraLeftBox(self):
        ## GET CURRENT LEFT MENU WIDTH
        width = self.ui.extraLeftBox.width()

        ## IF MINIMIZED
        if width == 0:
            newWidth = 240  ## EXPAND MENU      
        else: ## IF MAXIMIZED
            newWidth = 0  ## RESTORE MENU

        ## ANIMATE THE TRANSITION
        self.animation = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth") ## ANIMATE MINIMUM WIDTH
        self.animation.setDuration(500)
        self.animation.setStartValue(width) ## START VALUE IS THE CURRENT MENU WIDTH
        self.animation.setEndValue(newWidth) ## END VALUE IS THE NEW MENU WIDTH
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()



    ##SELECT/ DESELECT
    def selectMenu(getStyle):
        select = getStyle + """border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0)); background-color: rgb(40, 44, 52);"""
        return select

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("""border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0)); background-color: rgb(40, 44, 52);""", "")
        return deselect



    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        ## DRAG HANDLER - FUNCTION TO MOVE WINDOW ON MOUSE DRAG EVENT ON THE TITLE BAR
        def moveWindow(event):
            # DETECT IF THE WINDOW IS NORMAL SIZE 
            if self.isMaximized() == False: # (NOT MAXIMIZED - NORMAL SIZE) /// MOVE WINDOW ONLY WHEN WINDOW IS NORMAL SIZE
                ## ONLY ACCEPT LEFT MOUSE BUTTON CLICKS
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
                    # if self.isMaximized() == True:
                    #     self.showNormal()
        self.ui.leftBox.mouseMoveEvent = moveWindow


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(100)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.bgApp.setGraphicsEffect(self.shadow)


         ## WINDOW SIZE GRIP TO RESIZE WINDOW
        QSizeGrip(self.ui.frame_size_grip)

        ## MINIMIZE WINDOW
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        ## CLOSE WINDOW
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

        ## MAXIMIZE/RESTORE WINDOW
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.restore_or_maximize_window(self))


    ## SHOW WARNING MESSAGE BEFORE EXITING
    def warningMessage(self):
        msg = QMessageBox.warning(self, "Warning!!!", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            self.close()


    ##  LOAD SYMPTOMS FROM CSV TO THE TABLE IN INFROGRAPHICS
    def loadSymptoms(self):
        data = pd.read_csv('Resources/Symptoms.csv')

        symptoms = data['Symptoms'].tolist()
        covid_19 = data['COVID-19'].tolist()
        common_cold = data['Common Cold'].tolist()
        flu = data['Flu'].tolist()
        allergies = data['Allergies'].tolist()

        row = 0
        self.ui.tableWidget_symptoms.setRowCount(len(symptoms))
        for item in symptoms:    
            self.ui.tableWidget_symptoms.setItem(row, 0, QtWidgets.QTableWidgetItem(symptoms[row]))
            self.ui.tableWidget_symptoms.setItem(row, 1, QtWidgets.QTableWidgetItem(covid_19[row]))
            self.ui.tableWidget_symptoms.setItem(row, 2, QtWidgets.QTableWidgetItem(common_cold[row]))
            self.ui.tableWidget_symptoms.setItem(row, 3, QtWidgets.QTableWidgetItem(flu[row]))
            self.ui.tableWidget_symptoms.setItem(row, 4, QtWidgets.QTableWidgetItem(allergies[row]))
            row = row + 1

    ## GET START AND END DATE FROM THE USER
    def getDate(self):
        date_start = self.ui.comboBox_dateStart.currentText()
        month_start = self.ui.comboBox_monthStart.currentText()
        year_start =  self.ui.comboBox_yearStart.currentText()

        date_end = self.ui.comboBox_dateEnd.currentText()
        month_end = self.ui.comboBox_monthEnd.currentText()
        year_end =  self.ui.comboBox_yearEnd.currentText()
        
        print(date_start, month_start, year_start)
        print(date_end, month_end, year_end)
