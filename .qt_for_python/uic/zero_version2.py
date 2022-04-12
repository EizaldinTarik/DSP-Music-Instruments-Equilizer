# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zero_version2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sourceGuitar_rc

class Ui_Piano_istrument(object):
    def setupUi(self, Piano_istrument):
        if not Piano_istrument.objectName():
            Piano_istrument.setObjectName(u"Piano_istrument")
        Piano_istrument.resize(1206, 879)
        Piano_istrument.setStyleSheet(u"#Piano_Button_1,#Piano_Button_2,#Piano_Button_3,#Piano_Button_4,#Piano_Button_5,#Piano_Button_6,#Piano_Button_7\n"
"{\n"
"background-color: rgb(250, 250, 250);\n"
"}\n"
"#Piano_Button_1:hover,#Piano_Button_2:hover,#Piano_Button_3:hover,#Piano_Button_4:hover,#Piano_Button_5:hover,#Piano_Button_6:hover,#Piano_Button_7:hover\n"
"{\n"
"background-color: rgb(240, 240, 250);\n"
"}\n"
"\n"
"#Piano_Button_1:pushed,#Piano_Button_2:pushed,#Piano_Button_3:pushed,#Piano_Button_4:pushed,#Piano_Button_5:pushed,#Piano_Button_6:pushed,#Piano_Button_7:pushed\n"
"{\n"
"background-color: rgb(255, 255, 0)\n"
"}\n"
"\n"
"#Piano_Button_above_1,#Piano_Button_above_2,#Piano_Button_above_3,#Piano_Button_above_4,#Piano_Button_above_5\n"
"{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"#Piano_Button_above_1:hover,#Piano_Button_above_2:hover,#Piano_Button_above_3:hover,#Piano_Button_above_4:hover,#Piano_Button_above_5:hover,DrumbButton:hover\n"
"{\n"
"background-color: rgb(75, 75, 75);\n"
"}\n"
"#Piano_Button_above_1:pushed,#P"
                        "iano_Button_above_2:pushed,#Piano_Button_above_3:pushed,#Piano_Button_above_4:pushed,#Piano_Button_above_5:pushed,DrumbButton:pushed\n"
"{\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.verticalLayout = QVBoxLayout(Piano_istrument)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidgets = QTabWidget(Piano_istrument)
        self.tabWidgets.setObjectName(u"tabWidgets")
        self.musicTab = QWidget()
        self.musicTab.setObjectName(u"musicTab")
        self.frameForPiano = QFrame(self.musicTab)
        self.frameForPiano.setObjectName(u"frameForPiano")
        self.frameForPiano.setGeometry(QRect(40, 50, 371, 211))
        self.frameForPiano.setFrameShape(QFrame.StyledPanel)
        self.frameForPiano.setFrameShadow(QFrame.Raised)
        self.backGroundForSubPiano = QLabel(self.frameForPiano)
        self.backGroundForSubPiano.setObjectName(u"backGroundForSubPiano")
        self.backGroundForSubPiano.setGeometry(QRect(10, 10, 351, 61))
        self.backGroundForSubPiano.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.Piano_Button_above_4 = QPushButton(self.frameForPiano)
        self.Piano_Button_above_4.setObjectName(u"Piano_Button_above_4")
        self.Piano_Button_above_4.setGeometry(QRect(240, 30, 40, 130))
        self.Piano_Button_6 = QPushButton(self.frameForPiano)
        self.Piano_Button_6.setObjectName(u"Piano_Button_6")
        self.Piano_Button_6.setGeometry(QRect(260, 70, 50, 130))
        self.Piano_Button_above_5 = QPushButton(self.frameForPiano)
        self.Piano_Button_above_5.setObjectName(u"Piano_Button_above_5")
        self.Piano_Button_above_5.setGeometry(QRect(290, 30, 40, 130))
        self.Piano_Button_4 = QPushButton(self.frameForPiano)
        self.Piano_Button_4.setObjectName(u"Piano_Button_4")
        self.Piano_Button_4.setGeometry(QRect(160, 70, 50, 130))
        self.Piano_Button_7 = QPushButton(self.frameForPiano)
        self.Piano_Button_7.setObjectName(u"Piano_Button_7")
        self.Piano_Button_7.setGeometry(QRect(310, 70, 50, 130))
        self.Piano_Button_above_1 = QPushButton(self.frameForPiano)
        self.Piano_Button_above_1.setObjectName(u"Piano_Button_above_1")
        self.Piano_Button_above_1.setGeometry(QRect(40, 30, 40, 130))
        self.Piano_Button_above_3 = QPushButton(self.frameForPiano)
        self.Piano_Button_above_3.setObjectName(u"Piano_Button_above_3")
        self.Piano_Button_above_3.setGeometry(QRect(190, 30, 40, 130))
        self.Piano_Button_1 = QPushButton(self.frameForPiano)
        self.Piano_Button_1.setObjectName(u"Piano_Button_1")
        self.Piano_Button_1.setGeometry(QRect(10, 70, 50, 130))
        self.Piano_Button_2 = QPushButton(self.frameForPiano)
        self.Piano_Button_2.setObjectName(u"Piano_Button_2")
        self.Piano_Button_2.setGeometry(QRect(60, 70, 50, 130))
        self.Piano_Button_3 = QPushButton(self.frameForPiano)
        self.Piano_Button_3.setObjectName(u"Piano_Button_3")
        self.Piano_Button_3.setGeometry(QRect(110, 70, 50, 130))
        self.Piano_Button_5 = QPushButton(self.frameForPiano)
        self.Piano_Button_5.setObjectName(u"Piano_Button_5")
        self.Piano_Button_5.setGeometry(QRect(210, 70, 50, 130))
        self.Piano_Button_above_2 = QPushButton(self.frameForPiano)
        self.Piano_Button_above_2.setObjectName(u"Piano_Button_above_2")
        self.Piano_Button_above_2.setGeometry(QRect(90, 30, 40, 130))
        self.gridLayout = QGridLayout(self.frameForPiano)
        self.gridLayout.setObjectName(u"gridLayout")
        self.backGroundForPiano = QLabel(self.frameForPiano)
        self.backGroundForPiano.setObjectName(u"backGroundForPiano")
        self.backGroundForPiano.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(148, 118, 254, 255), stop:1 rgba(71, 255, 243, 255))")

        self.gridLayout.addWidget(self.backGroundForPiano, 0, 0, 1, 1)

        self.backGroundForPiano.raise_()
        self.Piano_Button_6.raise_()
        self.Piano_Button_4.raise_()
        self.Piano_Button_7.raise_()
        self.Piano_Button_1.raise_()
        self.Piano_Button_2.raise_()
        self.Piano_Button_3.raise_()
        self.Piano_Button_5.raise_()
        self.Piano_Button_above_4.raise_()
        self.Piano_Button_above_5.raise_()
        self.Piano_Button_above_1.raise_()
        self.Piano_Button_above_2.raise_()
        self.Piano_Button_above_3.raise_()
        self.backGroundForSubPiano.raise_()
        self.Guitar_widget = QWidget(self.musicTab)
        self.Guitar_widget.setObjectName(u"Guitar_widget")
        self.Guitar_widget.setGeometry(QRect(50, 300, 951, 501))
        self.Guitar_button_4 = QPushButton(self.Guitar_widget)
        self.Guitar_button_4.setObjectName(u"Guitar_button_4")
        self.Guitar_button_4.setGeometry(QRect(240, 280, 16, 16))
        self.Guitar_button_1 = QPushButton(self.Guitar_widget)
        self.Guitar_button_1.setObjectName(u"Guitar_button_1")
        self.Guitar_button_1.setGeometry(QRect(180, 250, 16, 16))
        self.Guitar_button_2 = QPushButton(self.Guitar_widget)
        self.Guitar_button_2.setObjectName(u"Guitar_button_2")
        self.Guitar_button_2.setGeometry(QRect(200, 260, 16, 16))
        self.Guitar_button_3 = QPushButton(self.Guitar_widget)
        self.Guitar_button_3.setObjectName(u"Guitar_button_3")
        self.Guitar_button_3.setGeometry(QRect(220, 270, 16, 16))
        self.Guitar_button_5 = QPushButton(self.Guitar_widget)
        self.Guitar_button_5.setObjectName(u"Guitar_button_5")
        self.Guitar_button_5.setGeometry(QRect(260, 290, 16, 16))
        self.gridLayout_4 = QGridLayout(self.Guitar_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Guitar_Picture = QLabel(self.Guitar_widget)
        self.Guitar_Picture.setObjectName(u"Guitar_Picture")
        self.Guitar_Picture.setStyleSheet(u"image: url(:/newPrefix/Guitar.png);")

        self.gridLayout_4.addWidget(self.Guitar_Picture, 0, 0, 1, 1)

        self.Guitar_button_5.raise_()
        self.Guitar_Picture.raise_()
        self.Guitar_button_4.raise_()
        self.Guitar_button_1.raise_()
        self.Guitar_button_2.raise_()
        self.Guitar_button_3.raise_()
        self.widget = QWidget(self.musicTab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(580, 40, 401, 261))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_14 = QPushButton(self.widget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_5.addWidget(self.pushButton_14, 1, 3, 1, 1)

        self.horizontalSlider_For_piano = QSlider(self.widget)
        self.horizontalSlider_For_piano.setObjectName(u"horizontalSlider_For_piano")
        self.horizontalSlider_For_piano.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_For_piano, 4, 0, 1, 3)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_5.addWidget(self.pushButton_10, 0, 1, 1, 2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_5.addWidget(self.pushButton_12, 1, 0, 1, 2)

        self.horizontalSlider_For_Drumb = QSlider(self.widget)
        self.horizontalSlider_For_Drumb.setObjectName(u"horizontalSlider_For_Drumb")
        self.horizontalSlider_For_Drumb.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_For_Drumb, 2, 0, 1, 3)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_5.addWidget(self.pushButton_11, 0, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_5.addWidget(self.pushButton_13, 1, 2, 1, 1)

        self.horizontalSlider_For_Guitar = QSlider(self.widget)
        self.horizontalSlider_For_Guitar.setObjectName(u"horizontalSlider_For_Guitar")
        self.horizontalSlider_For_Guitar.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_For_Guitar, 3, 0, 1, 3)

        self.comboBox_for_tunes = QComboBox(self.widget)
        self.comboBox_for_tunes.addItem("")
        self.comboBox_for_tunes.addItem("")
        self.comboBox_for_tunes.addItem("")
        self.comboBox_for_tunes.setObjectName(u"comboBox_for_tunes")

        self.gridLayout_5.addWidget(self.comboBox_for_tunes, 2, 3, 1, 1)

        self.DrumbButton = QPushButton(self.musicTab)
        self.DrumbButton.setObjectName(u"DrumbButton")
        self.DrumbButton.setGeometry(QRect(440, 90, 111, 111))
        self.DrumbButton.setStyleSheet(u"#DrumbButton {\n"
"	\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 50px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"#DrumbButton:hover {\n"
"background:qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"#DrumbButton:pushed\n"
"{\n"
"background:qradialgradient(\n"
"cx: 0.8, cy: -0.9, fx: 0.3, fy: -0.5,\n"
"radius: 1.5, stop: 1 #000, stop: 2 #aaa\n"
");\n"
"}\n"
"")
        self.tabWidgets.addTab(self.musicTab, "")
        self.equilizerTab = QWidget()
        self.equilizerTab.setObjectName(u"equilizerTab")
        self.gridLayout_3 = QGridLayout(self.equilizerTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_8 = QPushButton(self.equilizerTab)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 9, 0, 1, 1)

        self.horizontalSlider_5 = QSlider(self.equilizerTab)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setMaximum(10)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_3.addWidget(self.horizontalSlider_5, 9, 2, 1, 1)

        self.pushButton_Play = QPushButton(self.equilizerTab)
        self.pushButton_Play.setObjectName(u"pushButton_Play")

        self.gridLayout_3.addWidget(self.pushButton_Play, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.equilizerTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 5, 0, 2, 1)

        self.verticalSlider_3 = QSlider(self.equilizerTab)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(10)
        self.verticalSlider_3.setPageStep(1)
        self.verticalSlider_3.setOrientation(Qt.Vertical)
        self.verticalSlider_3.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_3.addWidget(self.verticalSlider_3, 0, 4, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.Guitar_Picture_2 = QLabel(self.equilizerTab)
        self.Guitar_Picture_2.setObjectName(u"Guitar_Picture_2")
        self.Guitar_Picture_2.setStyleSheet(u"image: url(:/newPrefix/Guitar.png);")

        self.gridLayout_3.addWidget(self.Guitar_Picture_2, 3, 3, 4, 1)

        self.horizontalSlider_6 = QSlider(self.equilizerTab)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setMaximum(10)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_3.addWidget(self.horizontalSlider_6, 9, 3, 1, 1)

        self.pushButton_Open = QPushButton(self.equilizerTab)
        self.pushButton_Open.setObjectName(u"pushButton_Open")

        self.gridLayout_3.addWidget(self.pushButton_Open, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.equilizerTab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 7, 0, 2, 1)

        self.horizontalSlider_For_Drumb_2 = QSlider(self.equilizerTab)
        self.horizontalSlider_For_Drumb_2.setObjectName(u"horizontalSlider_For_Drumb_2")
        self.horizontalSlider_For_Drumb_2.setMaximum(10)
        self.horizontalSlider_For_Drumb_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_For_Drumb_2.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_3.addWidget(self.horizontalSlider_For_Drumb_2, 8, 1, 2, 1)

        self.Guitar_Picture_4 = QLabel(self.equilizerTab)
        self.Guitar_Picture_4.setObjectName(u"Guitar_Picture_4")
        self.Guitar_Picture_4.setStyleSheet(u"\n"
"image: url(:/newPrefix/piano2.png);")

        self.gridLayout_3.addWidget(self.Guitar_Picture_4, 3, 2, 4, 1)

        self.Guitar_Picture_5 = QLabel(self.equilizerTab)
        self.Guitar_Picture_5.setObjectName(u"Guitar_Picture_5")
        self.Guitar_Picture_5.setStyleSheet(u"image: url(:/newPrefix/drumb.png);\n"
"")

        self.gridLayout_3.addWidget(self.Guitar_Picture_5, 2, 1, 4, 1)

        self.pushButton_pause = QPushButton(self.equilizerTab)
        self.pushButton_pause.setObjectName(u"pushButton_pause")

        self.gridLayout_3.addWidget(self.pushButton_pause, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.widget_2 = QWidget(self.equilizerTab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 3)

        self.tabWidgets.addTab(self.equilizerTab, "")

        self.verticalLayout.addWidget(self.tabWidgets)


        self.retranslateUi(Piano_istrument)

        self.tabWidgets.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Piano_istrument)
    # setupUi

    def retranslateUi(self, Piano_istrument):
        Piano_istrument.setWindowTitle(QCoreApplication.translate("Piano_istrument", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.tabWidgets.setWhatsThis(QCoreApplication.translate("Piano_istrument", u"<html><head/><body><p>musicTab</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.musicTab.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.backGroundForSubPiano.setText("")
        self.Piano_Button_above_4.setText("")
        self.Piano_Button_6.setText("")
        self.Piano_Button_above_5.setText("")
        self.Piano_Button_4.setText("")
        self.Piano_Button_7.setText("")
        self.Piano_Button_above_1.setText("")
        self.Piano_Button_above_3.setText("")
        self.Piano_Button_1.setText("")
        self.Piano_Button_2.setText("")
        self.Piano_Button_3.setText("")
        self.Piano_Button_5.setText("")
        self.Piano_Button_above_2.setText("")
        self.backGroundForPiano.setText("")
        self.Guitar_button_4.setText("")
        self.Guitar_button_1.setText("")
        self.Guitar_button_2.setText("")
        self.Guitar_button_3.setText("")
        self.Guitar_button_5.setText("")
        self.Guitar_Picture.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.comboBox_for_tunes.setItemText(0, QCoreApplication.translate("Piano_istrument", u"octave", None))
        self.comboBox_for_tunes.setItemText(1, QCoreApplication.translate("Piano_istrument", u"solo", None))
        self.comboBox_for_tunes.setItemText(2, QCoreApplication.translate("Piano_istrument", u"spare", None))

        self.DrumbButton.setText("")
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.musicTab), QCoreApplication.translate("Piano_istrument", u"musicTab", None))
        self.pushButton_8.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.pushButton_Play.setText(QCoreApplication.translate("Piano_istrument", u"Play", None))
        self.pushButton_2.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.Guitar_Picture_2.setText("")
        self.pushButton_Open.setText(QCoreApplication.translate("Piano_istrument", u"Open", None))
        self.pushButton_3.setText(QCoreApplication.translate("Piano_istrument", u"PushButton", None))
        self.Guitar_Picture_4.setText("")
        self.Guitar_Picture_5.setText("")
        self.pushButton_pause.setText(QCoreApplication.translate("Piano_istrument", u"Pause", None))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.equilizerTab), QCoreApplication.translate("Piano_istrument", u"equilizerTab", None))
    # retranslateUi

