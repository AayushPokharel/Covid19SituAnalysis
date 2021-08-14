# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-image: url(:/images/images/images/icon.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 2"
                        "49);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147,"
                        " 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px"
                        " solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid"
                        "; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255"
                        ", 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb("
                        "33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb"
                        "(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScroll"
                        "Bar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontro"
                        "l-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-"
                        "image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-p"
                        "osition: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: "
                        "10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButto"
                        "n {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 0, 160, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.topMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_7.addWidget(self.btn_home)

        self.btn_nationalStatistics = QPushButton(self.topMenu)
        self.btn_nationalStatistics.setObjectName(u"btn_nationalStatistics")
        sizePolicy.setHeightForWidth(self.btn_nationalStatistics.sizePolicy().hasHeightForWidth())
        self.btn_nationalStatistics.setSizePolicy(sizePolicy)
        self.btn_nationalStatistics.setMinimumSize(QSize(0, 45))
        self.btn_nationalStatistics.setFont(font)
        self.btn_nationalStatistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nationalStatistics.setLayoutDirection(Qt.LeftToRight)
        self.btn_nationalStatistics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_7.addWidget(self.btn_nationalStatistics)

        self.btn_worldStatistics = QPushButton(self.topMenu)
        self.btn_worldStatistics.setObjectName(u"btn_worldStatistics")
        sizePolicy.setHeightForWidth(self.btn_worldStatistics.sizePolicy().hasHeightForWidth())
        self.btn_worldStatistics.setSizePolicy(sizePolicy)
        self.btn_worldStatistics.setMinimumSize(QSize(0, 45))
        self.btn_worldStatistics.setFont(font)
        self.btn_worldStatistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_worldStatistics.setLayoutDirection(Qt.LeftToRight)
        self.btn_worldStatistics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_7.addWidget(self.btn_worldStatistics)

        self.btn_hospitals = QPushButton(self.topMenu)
        self.btn_hospitals.setObjectName(u"btn_hospitals")
        sizePolicy.setHeightForWidth(self.btn_hospitals.sizePolicy().hasHeightForWidth())
        self.btn_hospitals.setSizePolicy(sizePolicy)
        self.btn_hospitals.setMinimumSize(QSize(0, 45))
        self.btn_hospitals.setFont(font)
        self.btn_hospitals.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hospitals.setLayoutDirection(Qt.LeftToRight)
        self.btn_hospitals.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-medical-cross.png);")

        self.verticalLayout_7.addWidget(self.btn_hospitals)

        self.btn_infographics = QPushButton(self.topMenu)
        self.btn_infographics.setObjectName(u"btn_infographics")
        sizePolicy.setHeightForWidth(self.btn_infographics.sizePolicy().hasHeightForWidth())
        self.btn_infographics.setSizePolicy(sizePolicy)
        self.btn_infographics.setMinimumSize(QSize(0, 45))
        self.btn_infographics.setFont(font)
        self.btn_infographics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_infographics.setLayoutDirection(Qt.LeftToRight)
        self.btn_infographics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_7.addWidget(self.btn_infographics)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_7.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_Settings = QPushButton(self.bottomMenu)
        self.btn_Settings.setObjectName(u"btn_Settings")
        sizePolicy.setHeightForWidth(self.btn_Settings.sizePolicy().hasHeightForWidth())
        self.btn_Settings.setSizePolicy(sizePolicy)
        self.btn_Settings.setMinimumSize(QSize(0, 45))
        self.btn_Settings.setFont(font)
        self.btn_Settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_Settings.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.btn_Settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.home)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.home_frame = QFrame(self.home)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setStyleSheet(u"aQFrame{\n"
"background-image: url(:/images/images/images/logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}")
        self.home_frame.setFrameShape(QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.home_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_5 = QFrame(self.home_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-radius: 50px;\n"
"background-color: rgb(48, 70, 120);\n"
"font: 20px bold;\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setStyleSheet(u"border-radius: 15px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_16)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_13)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(50, 50))
        self.frame_17.setMaximumSize(QSize(60, 60))
        self.frame_17.setStyleSheet(u"border-image: url(:/images/images/images/world.png);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_17, 0, 0, 1, 1)

        self.label_56 = QLabel(self.frame_13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 40px bold;")
        self.label_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_56, 0, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_13, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_16)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_14)


        self.verticalLayout_25.addWidget(self.frame_16)

        self.frame_33 = QFrame(self.frame_15)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 175))
        self.frame_33.setStyleSheet(u"border-radius: 20px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(85, 170, 0);\n"
"font: 20px bold;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_34)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_39 = QFrame(self.frame_34)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_39)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 20pt \"Franklin Gothic Demi\";")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_16)


        self.verticalLayout_28.addWidget(self.frame_39)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_22.setSpacing(7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_38)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_13)

        self.label_12 = QLabel(self.frame_38)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_22.addWidget(self.label_12)


        self.verticalLayout_28.addWidget(self.frame_38)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_36)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_36)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_23.addWidget(self.label_15)


        self.verticalLayout_28.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_37)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_33)

        self.label_17 = QLabel(self.frame_37)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_28.addWidget(self.label_17)


        self.verticalLayout_28.addWidget(self.frame_37)


        self.horizontalLayout_21.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(85, 170, 0);\n"
"font: 20px bold;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_35)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_40 = QFrame(self.frame_35)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_40)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 20pt \"Franklin Gothic Demi\";")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_34)


        self.verticalLayout_29.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_35)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_30.setSpacing(7)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_41)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_30.addWidget(self.label_36)


        self.verticalLayout_29.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_35)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_42)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_42)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_31.addWidget(self.label_38)


        self.verticalLayout_29.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_35)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_43)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_43)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_32.addWidget(self.label_40)


        self.verticalLayout_29.addWidget(self.frame_43)


        self.horizontalLayout_21.addWidget(self.frame_35)


        self.verticalLayout_25.addWidget(self.frame_33)


        self.horizontalLayout_25.addWidget(self.frame_15)


        self.verticalLayout_26.addWidget(self.frame_5)

        self.frame_18 = QFrame(self.home_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_44 = QFrame(self.frame_18)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"border-radius: 50px;\n"
"background-color: rgb(48, 70, 120);\n"
"font: 20px bold;\n"
"\n"
"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_44)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 50))
        self.frame_45.setMaximumSize(QSize(16777215, 50))
        self.frame_45.setStyleSheet(u"border-radius: 15px;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_45)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_45)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self._2 = QGridLayout(self.frame_32)
        self._2.setObjectName(u"_2")
        self._2.setHorizontalSpacing(7)
        self._2.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_32)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(50, 50))
        self.frame_47.setMaximumSize(QSize(50, 50))
        self.frame_47.setStyleSheet(u"border-image: url(:/images/images/images/nepal_flag.png);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self._2.addWidget(self.frame_47, 0, 0, 1, 1)

        self.label_41 = QLabel(self.frame_32)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font: 40px bold;")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self._2.addWidget(self.label_41, 0, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_32, 0, Qt.AlignHCenter)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_46)


        self.verticalLayout_30.addWidget(self.frame_45)

        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 175))
        self.frame_49.setStyleSheet(u"border-radius: 20px;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(85, 170, 0);\n"
"font: 20px bold;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_50)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_51)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 20pt \"Franklin Gothic Demi\";")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_42)


        self.verticalLayout_31.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_35.setSpacing(7)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_52)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_52)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_35.addWidget(self.label_44)


        self.verticalLayout_31.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_53)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_53)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_36.addWidget(self.label_46)


        self.verticalLayout_31.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_54)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_54)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_37.addWidget(self.label_48)


        self.verticalLayout_31.addWidget(self.frame_54)


        self.horizontalLayout_33.addWidget(self.frame_50)

        self.frame_55 = QFrame(self.frame_49)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(85, 170, 0);\n"
"font: 20px bold;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_55)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_56)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 20pt \"Franklin Gothic Demi\";")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_49)


        self.verticalLayout_32.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_39.setSpacing(7)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_57)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_50)

        self.label_51 = QLabel(self.frame_57)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_39.addWidget(self.label_51)


        self.verticalLayout_32.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_55)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_58)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_52)

        self.label_53 = QLabel(self.frame_58)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_40.addWidget(self.label_53)


        self.verticalLayout_32.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_55)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_59)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_59)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_41.addWidget(self.label_55)


        self.verticalLayout_32.addWidget(self.frame_59)


        self.horizontalLayout_33.addWidget(self.frame_55)


        self.verticalLayout_30.addWidget(self.frame_49)


        self.verticalLayout_24.addWidget(self.frame_44)


        self.verticalLayout_26.addWidget(self.frame_18)


        self.horizontalLayout_14.addWidget(self.home_frame)

        self.stackedWidget.addWidget(self.home)
        self.national_Statistics = QWidget()
        self.national_Statistics.setObjectName(u"national_Statistics")
        self.national_Statistics.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.national_Statistics)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_19 = QFrame(self.national_Statistics)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setSpacing(20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 15, 0)
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_28)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 35))
        self.label_28.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_28)

        self.comboBox_dateStart = QComboBox(self.frame_26)
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.addItem("")
        self.comboBox_dateStart.setObjectName(u"comboBox_dateStart")
        self.comboBox_dateStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_dateStart)

        self.comboBox_monthStart = QComboBox(self.frame_26)
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.addItem("")
        self.comboBox_monthStart.setObjectName(u"comboBox_monthStart")
        self.comboBox_monthStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_monthStart)

        self.comboBox_yearStart = QComboBox(self.frame_26)
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.addItem("")
        self.comboBox_yearStart.setObjectName(u"comboBox_yearStart")
        self.comboBox_yearStart.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_12.addWidget(self.comboBox_yearStart)


        self.horizontalLayout_11.addWidget(self.frame_26)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(20, 0))
        self.frame_30.setMaximumSize(QSize(30, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_30)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_27)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 35))
        self.label_30.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.comboBox_dateEnd = QComboBox(self.frame_27)
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.addItem("")
        self.comboBox_dateEnd.setObjectName(u"comboBox_dateEnd")
        self.comboBox_dateEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_dateEnd)

        self.comboBox_monthEnd = QComboBox(self.frame_27)
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.addItem("")
        self.comboBox_monthEnd.setObjectName(u"comboBox_monthEnd")
        self.comboBox_monthEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_monthEnd)

        self.comboBox_yearEnd = QComboBox(self.frame_27)
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.addItem("")
        self.comboBox_yearEnd.setObjectName(u"comboBox_yearEnd")
        self.comboBox_yearEnd.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.comboBox_yearEnd)


        self.horizontalLayout_11.addWidget(self.frame_27)

        self.btn_select = QPushButton(self.frame_25)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setMinimumSize(QSize(140, 40))
        self.btn_select.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_select)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_29)


        self.verticalLayout_19.addWidget(self.frame_25)

        self.tab_NationalStatistics = QTabWidget(self.frame_19)
        self.tab_NationalStatistics.setObjectName(u"tab_NationalStatistics")
        self.tab_NationalStatistics.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"    border: 1px solid gray;\n"
"    color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"    color: rgb(191, 191, 191);\n"
"	font-size: 18px;\n"
"	width: 250px;\n"
"	height: 40px;\n"
"	border: 2px solid gray;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: -9px;\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"	background-color: rgb(41, 44, 94);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(13, 34, 42);\n"
"}\n"
"QTableWidget\n"
"{\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(13, 34, 42);;\n"
"	alternate-background-color: rgb(88, 88, 88);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 17px;\n"
"	gridline-color: gray;\n"
"}\n"
"QHeaderView\n"
"{\n"
"	background-color: rgb(13, 34, 42);\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"	color: rgb(255, 255, 255);\n"
"	f"
                        "ont: bold;\n"
"}\n"
"QTableWidget QTableCornerButton::section \n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"}")
        self.tab_Age = QWidget()
        self.tab_Age.setObjectName(u"tab_Age")
        self.horizontalLayout_43 = QHBoxLayout(self.tab_Age)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_20 = QFrame(self.tab_Age)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.graph1 = QVBoxLayout()
        self.graph1.setObjectName(u"graph1")

        self.verticalLayout_17.addLayout(self.graph1)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_23)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.graph4 = QVBoxLayout()
        self.graph4.setObjectName(u"graph4")

        self.verticalLayout_18.addLayout(self.graph4)


        self.gridLayout.addWidget(self.frame_23, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.graph2 = QVBoxLayout()
        self.graph2.setObjectName(u"graph2")

        self.verticalLayout_16.addLayout(self.graph2)


        self.gridLayout.addWidget(self.frame_22, 0, 1, 1, 1)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.graph3 = QVBoxLayout()
        self.graph3.setObjectName(u"graph3")

        self.horizontalLayout_9.addLayout(self.graph3)


        self.gridLayout.addWidget(self.frame_24, 1, 0, 1, 1)


        self.horizontalLayout_43.addWidget(self.frame_20)

        self.tab_NationalStatistics.addTab(self.tab_Age, "")
        self.tab_Gender = QWidget()
        self.tab_Gender.setObjectName(u"tab_Gender")
        self.horizontalLayout_45 = QHBoxLayout(self.tab_Gender)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_64 = QFrame(self.tab_Gender)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_64)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_65)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.graph1_2 = QVBoxLayout()
        self.graph1_2.setObjectName(u"graph1_2")

        self.verticalLayout_34.addLayout(self.graph1_2)


        self.gridLayout_2.addWidget(self.frame_65, 0, 0, 1, 1)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_66)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.graph4_2 = QVBoxLayout()
        self.graph4_2.setObjectName(u"graph4_2")

        self.verticalLayout_35.addLayout(self.graph4_2)


        self.gridLayout_2.addWidget(self.frame_66, 1, 1, 1, 1)

        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_67)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.graph2_2 = QVBoxLayout()
        self.graph2_2.setObjectName(u"graph2_2")

        self.verticalLayout_36.addLayout(self.graph2_2)


        self.gridLayout_2.addWidget(self.frame_67, 0, 1, 1, 1)

        self.frame_68 = QFrame(self.frame_64)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.graph3_2 = QVBoxLayout()
        self.graph3_2.setObjectName(u"graph3_2")

        self.horizontalLayout_44.addLayout(self.graph3_2)


        self.gridLayout_2.addWidget(self.frame_68, 1, 0, 1, 1)


        self.horizontalLayout_45.addWidget(self.frame_64)

        self.tab_NationalStatistics.addTab(self.tab_Gender, "")
        self.tab_Region = QWidget()
        self.tab_Region.setObjectName(u"tab_Region")
        self.horizontalLayout_47 = QHBoxLayout(self.tab_Region)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.frame_69 = QFrame(self.tab_Region)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_69)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_70)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.graph1_3 = QVBoxLayout()
        self.graph1_3.setObjectName(u"graph1_3")

        self.verticalLayout_37.addLayout(self.graph1_3)


        self.gridLayout_4.addWidget(self.frame_70, 0, 0, 1, 1)

        self.frame_71 = QFrame(self.frame_69)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_71)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.graph4_3 = QVBoxLayout()
        self.graph4_3.setObjectName(u"graph4_3")

        self.verticalLayout_38.addLayout(self.graph4_3)


        self.gridLayout_4.addWidget(self.frame_71, 1, 1, 1, 1)

        self.frame_72 = QFrame(self.frame_69)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_72)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.graph2_3 = QVBoxLayout()
        self.graph2_3.setObjectName(u"graph2_3")

        self.verticalLayout_39.addLayout(self.graph2_3)


        self.gridLayout_4.addWidget(self.frame_72, 0, 1, 1, 1)

        self.frame_73 = QFrame(self.frame_69)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.graph3_3 = QVBoxLayout()
        self.graph3_3.setObjectName(u"graph3_3")

        self.horizontalLayout_46.addLayout(self.graph3_3)


        self.gridLayout_4.addWidget(self.frame_73, 1, 0, 1, 1)


        self.horizontalLayout_47.addWidget(self.frame_69)

        self.tab_NationalStatistics.addTab(self.tab_Region, "")

        self.verticalLayout_19.addWidget(self.tab_NationalStatistics)


        self.verticalLayout.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.national_Statistics)
        self.world_statistics = QWidget()
        self.world_statistics.setObjectName(u"world_statistics")
        self.horizontalLayout_49 = QHBoxLayout(self.world_statistics)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_76 = QFrame(self.world_statistics)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_76)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tab_worldStatistics = QTabWidget(self.frame_76)
        self.tab_worldStatistics.setObjectName(u"tab_worldStatistics")
        self.tab_worldStatistics.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"    border: 1px solid gray;\n"
"    color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"    color: rgb(191, 191, 191);\n"
"	font-size: 18px;\n"
"	width: 150px;\n"
"	height: 40px;\n"
"	border: 2px solid gray;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: -9px;\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"	background-color: rgb(41, 44, 94);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(13, 34, 42);\n"
"}\n"
"QTableWidget\n"
"{\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(13, 34, 42);;\n"
"	alternate-background-color: rgb(88, 88, 88);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 17px;\n"
"	gridline-color: gray;\n"
"}\n"
"QHeaderView\n"
"{\n"
"	background-color: rgb(13, 34, 42);\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"	color: rgb(255, 255, 255);\n"
"	f"
                        "ont: bold;\n"
"}\n"
"QTableWidget QTableCornerButton::section \n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"}")
        self.tab_Asia = QWidget()
        self.tab_Asia.setObjectName(u"tab_Asia")
        self.horizontalLayout_50 = QHBoxLayout(self.tab_Asia)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_77 = QFrame(self.tab_Asia)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_77)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_78)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.graph1_4 = QVBoxLayout()
        self.graph1_4.setObjectName(u"graph1_4")

        self.verticalLayout_40.addLayout(self.graph1_4)


        self.gridLayout_5.addWidget(self.frame_78, 0, 0, 1, 1)

        self.frame_79 = QFrame(self.frame_77)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_79)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.graph4_4 = QVBoxLayout()
        self.graph4_4.setObjectName(u"graph4_4")

        self.verticalLayout_41.addLayout(self.graph4_4)


        self.gridLayout_5.addWidget(self.frame_79, 1, 1, 1, 1)

        self.frame_80 = QFrame(self.frame_77)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_80)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.graph2_4 = QVBoxLayout()
        self.graph2_4.setObjectName(u"graph2_4")

        self.verticalLayout_42.addLayout(self.graph2_4)


        self.gridLayout_5.addWidget(self.frame_80, 0, 1, 1, 1)

        self.frame_81 = QFrame(self.frame_77)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.graph3_4 = QVBoxLayout()
        self.graph3_4.setObjectName(u"graph3_4")

        self.horizontalLayout_51.addLayout(self.graph3_4)


        self.gridLayout_5.addWidget(self.frame_81, 1, 0, 1, 1)


        self.horizontalLayout_50.addWidget(self.frame_77)

        self.tab_worldStatistics.addTab(self.tab_Asia, "")
        self.tab_Africa = QWidget()
        self.tab_Africa.setObjectName(u"tab_Africa")
        self.horizontalLayout_52 = QHBoxLayout(self.tab_Africa)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_82 = QFrame(self.tab_Africa)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_82)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_83)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.graph1_5 = QVBoxLayout()
        self.graph1_5.setObjectName(u"graph1_5")

        self.verticalLayout_43.addLayout(self.graph1_5)


        self.gridLayout_6.addWidget(self.frame_83, 0, 0, 1, 1)

        self.frame_84 = QFrame(self.frame_82)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_84)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.graph4_5 = QVBoxLayout()
        self.graph4_5.setObjectName(u"graph4_5")

        self.verticalLayout_44.addLayout(self.graph4_5)


        self.gridLayout_6.addWidget(self.frame_84, 1, 1, 1, 1)

        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_85)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.graph2_5 = QVBoxLayout()
        self.graph2_5.setObjectName(u"graph2_5")

        self.verticalLayout_45.addLayout(self.graph2_5)


        self.gridLayout_6.addWidget(self.frame_85, 0, 1, 1, 1)

        self.frame_86 = QFrame(self.frame_82)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.graph3_5 = QVBoxLayout()
        self.graph3_5.setObjectName(u"graph3_5")

        self.horizontalLayout_53.addLayout(self.graph3_5)


        self.gridLayout_6.addWidget(self.frame_86, 1, 0, 1, 1)


        self.horizontalLayout_52.addWidget(self.frame_82)

        self.tab_worldStatistics.addTab(self.tab_Africa, "")
        self.tab_Europe = QWidget()
        self.tab_Europe.setObjectName(u"tab_Europe")
        self.horizontalLayout_54 = QHBoxLayout(self.tab_Europe)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.frame_87 = QFrame(self.tab_Europe)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_87)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_88)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.graph1_6 = QVBoxLayout()
        self.graph1_6.setObjectName(u"graph1_6")

        self.verticalLayout_46.addLayout(self.graph1_6)


        self.gridLayout_7.addWidget(self.frame_88, 0, 0, 1, 1)

        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_89)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.graph4_6 = QVBoxLayout()
        self.graph4_6.setObjectName(u"graph4_6")

        self.verticalLayout_47.addLayout(self.graph4_6)


        self.gridLayout_7.addWidget(self.frame_89, 1, 1, 1, 1)

        self.frame_90 = QFrame(self.frame_87)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_90)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.graph2_6 = QVBoxLayout()
        self.graph2_6.setObjectName(u"graph2_6")

        self.verticalLayout_48.addLayout(self.graph2_6)


        self.gridLayout_7.addWidget(self.frame_90, 0, 1, 1, 1)

        self.frame_91 = QFrame(self.frame_87)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.graph3_6 = QVBoxLayout()
        self.graph3_6.setObjectName(u"graph3_6")

        self.horizontalLayout_55.addLayout(self.graph3_6)


        self.gridLayout_7.addWidget(self.frame_91, 1, 0, 1, 1)


        self.horizontalLayout_54.addWidget(self.frame_87)

        self.tab_worldStatistics.addTab(self.tab_Europe, "")
        self.tab_NorthAmerica = QWidget()
        self.tab_NorthAmerica.setObjectName(u"tab_NorthAmerica")
        self.verticalLayout_10 = QVBoxLayout(self.tab_NorthAmerica)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_92 = QFrame(self.tab_NorthAmerica)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_92)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_93)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.graph1_7 = QVBoxLayout()
        self.graph1_7.setObjectName(u"graph1_7")

        self.verticalLayout_49.addLayout(self.graph1_7)


        self.gridLayout_8.addWidget(self.frame_93, 0, 0, 1, 1)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_94)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.graph4_7 = QVBoxLayout()
        self.graph4_7.setObjectName(u"graph4_7")

        self.verticalLayout_50.addLayout(self.graph4_7)


        self.gridLayout_8.addWidget(self.frame_94, 1, 1, 1, 1)

        self.frame_95 = QFrame(self.frame_92)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_95)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.graph2_7 = QVBoxLayout()
        self.graph2_7.setObjectName(u"graph2_7")

        self.verticalLayout_51.addLayout(self.graph2_7)


        self.gridLayout_8.addWidget(self.frame_95, 0, 1, 1, 1)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.graph3_7 = QVBoxLayout()
        self.graph3_7.setObjectName(u"graph3_7")

        self.horizontalLayout_56.addLayout(self.graph3_7)


        self.gridLayout_8.addWidget(self.frame_96, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_92)

        self.tab_worldStatistics.addTab(self.tab_NorthAmerica, "")
        self.tab_southAmerica = QWidget()
        self.tab_southAmerica.setObjectName(u"tab_southAmerica")
        self.verticalLayout_13 = QVBoxLayout(self.tab_southAmerica)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_97 = QFrame(self.tab_southAmerica)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_97)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_98)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.graph1_8 = QVBoxLayout()
        self.graph1_8.setObjectName(u"graph1_8")

        self.verticalLayout_52.addLayout(self.graph1_8)


        self.gridLayout_9.addWidget(self.frame_98, 0, 0, 1, 1)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_99)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.graph4_8 = QVBoxLayout()
        self.graph4_8.setObjectName(u"graph4_8")

        self.verticalLayout_53.addLayout(self.graph4_8)


        self.gridLayout_9.addWidget(self.frame_99, 1, 1, 1, 1)

        self.frame_100 = QFrame(self.frame_97)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_100)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.graph2_8 = QVBoxLayout()
        self.graph2_8.setObjectName(u"graph2_8")

        self.verticalLayout_54.addLayout(self.graph2_8)


        self.gridLayout_9.addWidget(self.frame_100, 0, 1, 1, 1)

        self.frame_101 = QFrame(self.frame_97)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.graph3_8 = QVBoxLayout()
        self.graph3_8.setObjectName(u"graph3_8")

        self.horizontalLayout_57.addLayout(self.graph3_8)


        self.gridLayout_9.addWidget(self.frame_101, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_97)

        self.tab_worldStatistics.addTab(self.tab_southAmerica, "")
        self.tab_Australia = QWidget()
        self.tab_Australia.setObjectName(u"tab_Australia")
        self.verticalLayout_14 = QVBoxLayout(self.tab_Australia)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_102 = QFrame(self.tab_Australia)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_102)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_102)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_103)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.graph1_9 = QVBoxLayout()
        self.graph1_9.setObjectName(u"graph1_9")

        self.verticalLayout_55.addLayout(self.graph1_9)


        self.gridLayout_10.addWidget(self.frame_103, 0, 0, 1, 1)

        self.frame_104 = QFrame(self.frame_102)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_104)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.graph4_9 = QVBoxLayout()
        self.graph4_9.setObjectName(u"graph4_9")

        self.verticalLayout_56.addLayout(self.graph4_9)


        self.gridLayout_10.addWidget(self.frame_104, 1, 1, 1, 1)

        self.frame_105 = QFrame(self.frame_102)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_105)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.graph2_9 = QVBoxLayout()
        self.graph2_9.setObjectName(u"graph2_9")

        self.verticalLayout_57.addLayout(self.graph2_9)


        self.gridLayout_10.addWidget(self.frame_105, 0, 1, 1, 1)

        self.frame_106 = QFrame(self.frame_102)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.graph3_9 = QVBoxLayout()
        self.graph3_9.setObjectName(u"graph3_9")

        self.horizontalLayout_58.addLayout(self.graph3_9)


        self.gridLayout_10.addWidget(self.frame_106, 1, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_102)

        self.tab_worldStatistics.addTab(self.tab_Australia, "")

        self.verticalLayout_8.addWidget(self.tab_worldStatistics)


        self.horizontalLayout_49.addWidget(self.frame_76)

        self.stackedWidget.addWidget(self.world_statistics)
        self.hospitals = QWidget()
        self.hospitals.setObjectName(u"hospitals")
        self.horizontalLayout_18 = QHBoxLayout(self.hospitals)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_11 = QFrame(self.hospitals)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_11)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamily(u"Lato Black")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(10)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"font: 87 20pt \"Lato Black\";")

        self.verticalLayout_33.addWidget(self.label_4)

        self.frame_61 = QFrame(self.frame_11)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tableWidget_hospitals = QTableWidget(self.frame_61)
        if (self.tableWidget_hospitals.columnCount() < 6):
            self.tableWidget_hospitals.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(17, 63, 67));
        self.tableWidget_hospitals.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_hospitals.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_hospitals.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_hospitals.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(17, 67, 70));
        self.tableWidget_hospitals.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_hospitals.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_hospitals.rowCount() < 16):
            self.tableWidget_hospitals.setRowCount(16)
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tableWidget_hospitals.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_hospitals.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_hospitals.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_hospitals.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_hospitals.setItem(0, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_hospitals.setItem(0, 3, __qtablewidgetitem25)
        self.tableWidget_hospitals.setObjectName(u"tableWidget_hospitals")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget_hospitals.sizePolicy().hasHeightForWidth())
        self.tableWidget_hospitals.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(88, 88, 88, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_hospitals.setPalette(palette)
        self.tableWidget_hospitals.setStyleSheet(u"QHeaderView::section { \n"
"	color:white;\n"
"	background-color: rgb(18, 81, 79);\n"
"}")
        self.tableWidget_hospitals.setFrameShape(QFrame.NoFrame)
        self.tableWidget_hospitals.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_hospitals.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_hospitals.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_hospitals.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_hospitals.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_hospitals.setShowGrid(True)
        self.tableWidget_hospitals.setGridStyle(Qt.SolidLine)
        self.tableWidget_hospitals.setSortingEnabled(False)
        self.tableWidget_hospitals.horizontalHeader().setVisible(True)
        self.tableWidget_hospitals.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_hospitals.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_hospitals.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_hospitals.verticalHeader().setVisible(False)
        self.tableWidget_hospitals.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_hospitals.verticalHeader().setHighlightSections(False)
        self.tableWidget_hospitals.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_24.addWidget(self.tableWidget_hospitals)


        self.verticalLayout_33.addWidget(self.frame_61)


        self.horizontalLayout_18.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.hospitals)
        self.infographics = QWidget()
        self.infographics.setObjectName(u"infographics")
        self.verticalLayout_20 = QVBoxLayout(self.infographics)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tabWidget = QTabWidget(self.infographics)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"    border: 1px solid gray;\n"
"    color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"    color: rgb(191, 191, 191);\n"
"	font-size: 18px;\n"
"	width: 100px;\n"
"	height: 40px;\n"
"	border: 2px solid gray;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: -9px;\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"	background-color: rgb(41, 44, 94);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(13, 34, 42);\n"
"}\n"
"QTableWidget\n"
"{\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(13, 34, 42);;\n"
"	alternate-background-color: rgb(88, 88, 88);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 17px;\n"
"	gridline-color: gray;\n"
"}\n"
"QHeaderView\n"
"{\n"
"	background-color: rgb(13, 34, 42);\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"	color: rgb(255, 255, 255);\n"
"	f"
                        "ont: bold;\n"
"}\n"
"QTableWidget QTableCornerButton::section \n"
"{\n"
"	background-color: rgb(52, 52, 52);	\n"
"}")
        self.tab_Symptoms = QWidget()
        self.tab_Symptoms.setObjectName(u"tab_Symptoms")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_Symptoms)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea_2 = QScrollArea(self.tab_Symptoms)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1122, 979))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(27, -1, -1, -1)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 450))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_symptoms = QTableWidget(self.frame_7)
        if (self.tableWidget_symptoms.columnCount() < 5):
            self.tableWidget_symptoms.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setBackground(QColor(17, 63, 67));
        self.tableWidget_symptoms.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_symptoms.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setBackground(QColor(17, 67, 70));
        self.tableWidget_symptoms.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        if (self.tableWidget_symptoms.rowCount() < 16):
            self.tableWidget_symptoms.setRowCount(16)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font5);
        self.tableWidget_symptoms.setVerticalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(7, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(8, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(9, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(10, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(11, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(12, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(13, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(14, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_symptoms.setVerticalHeaderItem(15, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_symptoms.setItem(0, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_symptoms.setItem(0, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_symptoms.setItem(0, 2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_symptoms.setItem(0, 3, __qtablewidgetitem50)
        self.tableWidget_symptoms.setObjectName(u"tableWidget_symptoms")
        sizePolicy3.setHeightForWidth(self.tableWidget_symptoms.sizePolicy().hasHeightForWidth())
        self.tableWidget_symptoms.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(13, 34, 42, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_symptoms.setPalette(palette1)
        self.tableWidget_symptoms.setStyleSheet(u"QHeaderView::section { \n"
"	color:white;\n"
"	background-color: rgb(18, 81, 79);\n"
"}")
        self.tableWidget_symptoms.setFrameShape(QFrame.NoFrame)
        self.tableWidget_symptoms.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_symptoms.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_symptoms.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_symptoms.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_symptoms.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_symptoms.setShowGrid(True)
        self.tableWidget_symptoms.setGridStyle(Qt.SolidLine)
        self.tableWidget_symptoms.setSortingEnabled(False)
        self.tableWidget_symptoms.horizontalHeader().setVisible(False)
        self.tableWidget_symptoms.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_symptoms.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_symptoms.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_symptoms.verticalHeader().setVisible(False)
        self.tableWidget_symptoms.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_symptoms.verticalHeader().setHighlightSections(False)
        self.tableWidget_symptoms.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_10.addWidget(self.tableWidget_symptoms)


        self.horizontalLayout_17.addWidget(self.frame_7)

        self.frame_48 = QFrame(self.frame_8)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(450, 0))
        self.frame_48.setStyleSheet(u"border-image: url(:/images/images/images/symptoms.png);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_48)


        self.verticalLayout_22.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 500))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.graph5 = QHBoxLayout()
        self.graph5.setObjectName(u"graph5")

        self.horizontalLayout_20.addLayout(self.graph5)

        self.graph6 = QHBoxLayout()
        self.graph6.setObjectName(u"graph6")

        self.horizontalLayout_20.addLayout(self.graph6)


        self.verticalLayout_22.addWidget(self.frame_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_7.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_Symptoms, "")
        self.tab_prevention = QWidget()
        self.tab_prevention.setObjectName(u"tab_prevention")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_prevention)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_3 = QScrollArea(self.tab_prevention)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1122, 1409))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"font-size: 30px;\n"
"font: bold;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.label)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 450))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(11, -1, 0, -1)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 300))
        self.frame_3.setMaximumSize(QSize(400, 600))
        self.frame_3.setStyleSheet(u"border-image: url(:/images/images/images/things_you_should_do.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(650, 16777215))
        self.frame.setStyleSheet(u"font: 75 18pt \"Lato\";\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_23.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_23.addWidget(self.label_19)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_23.addWidget(self.label_25)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_23.addWidget(self.label_21)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_23.addWidget(self.label_24)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_23.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_23.addWidget(self.label_23)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_23.addWidget(self.label_20)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_23.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_23.addWidget(self.label_27)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_62 = QFrame(self.frame_4)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_62)


        self.verticalLayout_21.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 450))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(450, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setStyleSheet(u"font-size: 25px;\n"
"font: bold;")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_27.addWidget(self.label_7)

        self.plainTextEdit = QPlainTextEdit(self.frame_9)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font6 = QFont()
        font6.setFamily(u"Lato")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.plainTextEdit.setFont(font6)
        self.plainTextEdit.setStyleSheet(u"font: 20pt \"Lato\";")

        self.verticalLayout_27.addWidget(self.plainTextEdit)


        self.horizontalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(400, 0))
        self.frame_10.setMaximumSize(QSize(400, 151556))
        self.frame_10.setStyleSheet(u"border-image: url(:/images/images/images/get_vaccinated.png);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_10)

        self.frame_63 = QFrame(self.frame_2)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_63)


        self.verticalLayout_21.addWidget(self.frame_2)

        self.frame_60 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 400))
        self.frame_60.setSizeIncrement(QSize(0, 0))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.graph7 = QHBoxLayout()
        self.graph7.setObjectName(u"graph7")

        self.horizontalLayout_19.addLayout(self.graph7)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")

        self.horizontalLayout_19.addLayout(self.horizontalLayout_42)


        self.verticalLayout_21.addWidget(self.frame_60)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"font: 25px;")

        self.verticalLayout_21.addWidget(self.label_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_8.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.tab_prevention, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_48 = QHBoxLayout(self.tab)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_74 = QFrame(self.tab)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_74)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 471, 71))
        self.label_6.setStyleSheet(u"font: 18pt \"Lato\";")
        self.label_5 = QLabel(self.frame_74)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 260, 1091, 71))
        self.label_5.setStyleSheet(u"font: 25pt \"Lato\";")
        self.label_8 = QLabel(self.frame_74)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 110, 651, 71))
        self.label_8.setStyleSheet(u"font: 25pt \"Lato\";")
        self.label_9 = QLabel(self.frame_74)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 180, 651, 71))
        self.label_9.setStyleSheet(u"font:  25pt \"Lato\";")

        self.horizontalLayout_48.addWidget(self.frame_74)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.infographics)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tab_NationalStatistics.setCurrentIndex(1)
        self.tab_worldStatistics.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"COVINFO", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Stay Safe", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_nationalStatistics.setText(QCoreApplication.translate("MainWindow", u"National Statistics", None))
        self.btn_worldStatistics.setText(QCoreApplication.translate("MainWindow", u"World Statistics", None))
        self.btn_hospitals.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        self.btn_infographics.setText(QCoreApplication.translate("MainWindow", u"Infographics", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"COVID-19 Situation Analysis Application", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Last 24 Hours", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Nepal", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Last 24 Hours", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Active Cases:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Recovered:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Start Date: ", None))
        self.comboBox_dateStart.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_dateStart.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_dateStart.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_dateStart.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_dateStart.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dateStart.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dateStart.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dateStart.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_dateStart.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_dateStart.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_dateStart.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_dateStart.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_dateStart.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_dateStart.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_dateStart.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_dateStart.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_dateStart.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_dateStart.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_dateStart.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_dateStart.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_dateStart.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_dateStart.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_dateStart.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_dateStart.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_dateStart.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_dateStart.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_dateStart.setItemText(26, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_dateStart.setItemText(27, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_dateStart.setItemText(28, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_dateStart.setItemText(29, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox_monthStart.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_monthStart.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.comboBox_monthStart.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.comboBox_monthStart.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.comboBox_monthStart.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.comboBox_monthStart.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.comboBox_monthStart.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.comboBox_monthStart.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.comboBox_monthStart.setItemText(8, QCoreApplication.translate("MainWindow", u"September", None))
        self.comboBox_monthStart.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.comboBox_monthStart.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.comboBox_monthStart.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.comboBox_yearStart.setItemText(0, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_yearStart.setItemText(1, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_yearStart.setItemText(2, QCoreApplication.translate("MainWindow", u"2021", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"End Date: ", None))
        self.comboBox_dateEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_dateEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_dateEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_dateEnd.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_dateEnd.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_dateEnd.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_dateEnd.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_dateEnd.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_dateEnd.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_dateEnd.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_dateEnd.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_dateEnd.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_dateEnd.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_dateEnd.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_dateEnd.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_dateEnd.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_dateEnd.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_dateEnd.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_dateEnd.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_dateEnd.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_dateEnd.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_dateEnd.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_dateEnd.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_dateEnd.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_dateEnd.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_dateEnd.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_dateEnd.setItemText(26, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_dateEnd.setItemText(27, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_dateEnd.setItemText(28, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_dateEnd.setItemText(29, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox_monthEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_monthEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.comboBox_monthEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.comboBox_monthEnd.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.comboBox_monthEnd.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.comboBox_monthEnd.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.comboBox_monthEnd.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.comboBox_monthEnd.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.comboBox_monthEnd.setItemText(8, QCoreApplication.translate("MainWindow", u"September", None))
        self.comboBox_monthEnd.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.comboBox_monthEnd.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.comboBox_monthEnd.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.comboBox_yearEnd.setItemText(0, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_yearEnd.setItemText(1, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_yearEnd.setItemText(2, QCoreApplication.translate("MainWindow", u"2021", None))

        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.tab_NationalStatistics.setTabText(self.tab_NationalStatistics.indexOf(self.tab_Age), QCoreApplication.translate("MainWindow", u"Age", None))
        self.tab_NationalStatistics.setTabText(self.tab_NationalStatistics.indexOf(self.tab_Gender), QCoreApplication.translate("MainWindow", u"Gender", None))
        self.tab_NationalStatistics.setTabText(self.tab_NationalStatistics.indexOf(self.tab_Region), QCoreApplication.translate("MainWindow", u"Region", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_Asia), QCoreApplication.translate("MainWindow", u"Asia", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_Africa), QCoreApplication.translate("MainWindow", u"Africa", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_Europe), QCoreApplication.translate("MainWindow", u"Europe", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_NorthAmerica), QCoreApplication.translate("MainWindow", u"North America", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_southAmerica), QCoreApplication.translate("MainWindow", u"South America", None))
        self.tab_worldStatistics.setTabText(self.tab_worldStatistics.indexOf(self.tab_Australia), QCoreApplication.translate("MainWindow", u"Australia", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        ___qtablewidgetitem = self.tableWidget_hospitals.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Hospital Name", None));
        ___qtablewidgetitem1 = self.tableWidget_hospitals.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem2 = self.tableWidget_hospitals.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total Beds", None));
        ___qtablewidgetitem3 = self.tableWidget_hospitals.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ICU Beds", None));
        ___qtablewidgetitem4 = self.tableWidget_hospitals.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ventilators", None));
        ___qtablewidgetitem5 = self.tableWidget_hospitals.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Isolation Beds", None));
        ___qtablewidgetitem6 = self.tableWidget_hospitals.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_hospitals.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_hospitals.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget_hospitals.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget_hospitals.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget_hospitals.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget_hospitals.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget_hospitals.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget_hospitals.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget_hospitals.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_hospitals.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_hospitals.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_hospitals.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_hospitals.verticalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_hospitals.verticalHeaderItem(14)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_hospitals.verticalHeaderItem(15)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_hospitals.isSortingEnabled()
        self.tableWidget_hospitals.setSortingEnabled(False)
        self.tableWidget_hospitals.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem22 = self.tableWidget_symptoms.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Symptoms", None));
        ___qtablewidgetitem23 = self.tableWidget_symptoms.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"COVID-19", None));
        ___qtablewidgetitem24 = self.tableWidget_symptoms.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Common Cold", None));
        ___qtablewidgetitem25 = self.tableWidget_symptoms.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Flu", None));
        ___qtablewidgetitem26 = self.tableWidget_symptoms.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Allergies", None));
        ___qtablewidgetitem27 = self.tableWidget_symptoms.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_symptoms.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_symptoms.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_symptoms.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_symptoms.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_symptoms.verticalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_symptoms.verticalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_symptoms.verticalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_symptoms.verticalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_symptoms.verticalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_symptoms.verticalHeaderItem(10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_symptoms.verticalHeaderItem(11)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_symptoms.verticalHeaderItem(12)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_symptoms.verticalHeaderItem(13)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_symptoms.verticalHeaderItem(14)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget_symptoms.verticalHeaderItem(15)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_symptoms.isSortingEnabled()
        self.tableWidget_symptoms.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.tableWidget_symptoms.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem44 = self.tableWidget_symptoms.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem45 = self.tableWidget_symptoms.item(0, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem46 = self.tableWidget_symptoms.item(0, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget_symptoms.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Symptoms), QCoreApplication.translate("MainWindow", u"Symptoms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Preventions:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u2022 Wear your mask", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2022 Stay socially distant", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep washing your hands", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep holiday gatherings small", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u2022 Dine out carefully", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u2022 Get your flu shot", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2022 Seek routine medical care", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2022 Be mindful of your mental health", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u2022 Watch your weight", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u2022 Keep up the good (safety) work", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Vaccines in Nepal:", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u2022 Covishield\n"
"\u2022 Verocell (Sinopharm)\n"
"\u2022 Johnson & Johnson\n"
"\u2022 AstraZeneca", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Prevention is Better than Cure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prevention), QCoreApplication.translate("MainWindow", u"Prevention", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"COVID-19 Hotline Number(MoHP)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"9851255834 | 9851255837 (08:00 AM - 08:00 PM)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1133 (24 Hours)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1115 (06:00 AM - 10:00 PM)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Helpline", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: DASS", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

